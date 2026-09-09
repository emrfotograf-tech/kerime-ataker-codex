#!/usr/bin/env python3
import json
import os
import time
from datetime import datetime
from pathlib import Path
from urllib.parse import quote
from zoneinfo import ZoneInfo

import requests

GRAPH_VERSION = os.getenv("META_GRAPH_VERSION", "v23.0")
GRAPH = f"https://graph.facebook.com/{GRAPH_VERSION}"
SYSTEM_TOKEN = os.environ["META_SYSTEM_USER_TOKEN"]
PAGE_ID = os.getenv("FB_PAGE_ID", "883182878201071")
IG_USER_ID = os.getenv("IG_USER_ID", "17841476687386286")
REPO = os.getenv("GITHUB_REPOSITORY", "emrfotograf-tech/kerime-ataker-codex")
REF = os.getenv("GITHUB_REF_NAME", "main")
TZ = ZoneInfo("Europe/Istanbul")
QUEUE_DIR = Path("publish_queue")


def call(method, url, *, params=None, data=None, headers=None, timeout=120):
    r = requests.request(method, url, params=params, data=data, headers=headers, timeout=timeout)
    try:
        payload = r.json()
    except Exception:
        payload = {"raw": r.text}
    if not r.ok or (isinstance(payload, dict) and payload.get("error")):
        raise RuntimeError(f"Meta API error {r.status_code}: {payload}")
    return payload


def raw_url(path):
    path = path.lstrip("/")
    return f"https://raw.githubusercontent.com/{REPO}/{quote(REF)}/{quote(path, safe='/')}"


def page_token():
    payload = call("GET", f"{GRAPH}/me/accounts", params={
        "fields": "id,name,access_token,instagram_business_account",
        "access_token": SYSTEM_TOKEN,
    })
    for row in payload.get("data", []):
        if str(row.get("id")) == str(PAGE_ID):
            return row.get("access_token") or SYSTEM_TOKEN
    return SYSTEM_TOKEN


def wait_container(container_id, token, timeout=600):
    deadline = time.time() + timeout
    while time.time() < deadline:
        p = call("GET", f"{GRAPH}/{container_id}", params={
            "fields": "status_code,status",
            "access_token": token,
        })
        if p.get("status_code") == "FINISHED":
            return
        if p.get("status_code") in {"ERROR", "EXPIRED"}:
            raise RuntimeError(f"Instagram container failed: {p}")
        time.sleep(10)
    raise TimeoutError(f"Container timeout: {container_id}")


def ig_publish_container(container_id, token):
    return call("POST", f"{GRAPH}/{IG_USER_ID}/media_publish", data={
        "creation_id": container_id,
        "access_token": token,
    })


def publish_instagram(item, token):
    kind = item["type"].upper()
    media = item["media"]
    caption = item.get("caption", "")

    if kind == "POST":
        if len(media) == 1:
            m = media[0]
            data = {"caption": caption, "access_token": token}
            if m.get("kind", "image") == "video":
                data.update({"media_type": "VIDEO", "video_url": raw_url(m["path"])})
            else:
                data["image_url"] = raw_url(m["path"])
            c = call("POST", f"{GRAPH}/{IG_USER_ID}/media", data=data)
            if m.get("kind", "image") == "video":
                wait_container(c["id"], token)
            return ig_publish_container(c["id"], token)

        children = []
        for m in media:
            data = {"is_carousel_item": "true", "access_token": token}
            if m.get("kind", "image") == "video":
                data.update({"media_type": "VIDEO", "video_url": raw_url(m["path"])})
            else:
                data["image_url"] = raw_url(m["path"])
            c = call("POST", f"{GRAPH}/{IG_USER_ID}/media", data=data)
            if m.get("kind", "image") == "video":
                wait_container(c["id"], token)
            children.append(c["id"])
        parent = call("POST", f"{GRAPH}/{IG_USER_ID}/media", data={
            "media_type": "CAROUSEL",
            "children": ",".join(children),
            "caption": caption,
            "access_token": token,
        })
        return ig_publish_container(parent["id"], token)

    if kind == "STORY":
        m = media[0]
        data = {"media_type": "STORIES", "access_token": token}
        if m.get("kind", "image") == "video":
            data["video_url"] = raw_url(m["path"])
        else:
            data["image_url"] = raw_url(m["path"])
        c = call("POST", f"{GRAPH}/{IG_USER_ID}/media", data=data)
        if m.get("kind", "image") == "video":
            wait_container(c["id"], token)
        return ig_publish_container(c["id"], token)

    if kind == "REEL":
        m = media[0]
        c = call("POST", f"{GRAPH}/{IG_USER_ID}/media", data={
            "media_type": "REELS",
            "video_url": raw_url(m["path"]),
            "caption": caption,
            "share_to_feed": str(item.get("share_to_feed", True)).lower(),
            "access_token": token,
        })
        wait_container(c["id"], token)
        return ig_publish_container(c["id"], token)

    raise RuntimeError(f"Unsupported Instagram type: {kind}")


def publish_facebook(item, token):
    kind = item["type"].upper()
    media = item["media"]
    caption = item.get("caption", "")

    if kind == "POST":
        if len(media) == 1 and media[0].get("kind", "image") == "image":
            return call("POST", f"{GRAPH}/{PAGE_ID}/photos", data={
                "url": raw_url(media[0]["path"]),
                "caption": caption,
                "published": "true",
                "access_token": token,
            })
        if len(media) == 1 and media[0].get("kind") == "video":
            return call("POST", f"{GRAPH}/{PAGE_ID}/videos", data={
                "file_url": raw_url(media[0]["path"]),
                "description": caption,
                "access_token": token,
            })
        photo_ids = []
        for m in media:
            if m.get("kind", "image") != "image":
                raise RuntimeError("Facebook carousel currently accepts images only")
            p = call("POST", f"{GRAPH}/{PAGE_ID}/photos", data={
                "url": raw_url(m["path"]),
                "published": "false",
                "access_token": token,
            })
            photo_ids.append(p["id"])
        data = {"message": caption, "access_token": token}
        for i, pid in enumerate(photo_ids):
            data[f"attached_media[{i}]"] = json.dumps({"media_fbid": pid})
        return call("POST", f"{GRAPH}/{PAGE_ID}/feed", data=data)

    if kind == "STORY":
        m = media[0]
        if m.get("kind", "image") != "image":
            raise RuntimeError("Facebook video Story not enabled yet")
        p = call("POST", f"{GRAPH}/{PAGE_ID}/photos", data={
            "url": raw_url(m["path"]),
            "published": "false",
            "access_token": token,
        })
        return call("POST", f"{GRAPH}/{PAGE_ID}/photo_stories", data={
            "photo_id": p["id"],
            "access_token": token,
        })

    if kind == "REEL":
        m = media[0]
        start = call("POST", f"{GRAPH}/{PAGE_ID}/video_reels", data={
            "upload_phase": "start",
            "access_token": token,
        })
        video_id = start["video_id"]
        upload_url = start.get("upload_url") or f"https://rupload.facebook.com/video-upload/{GRAPH_VERSION}/{video_id}"
        call("POST", upload_url, headers={
            "Authorization": f"OAuth {token}",
            "file_url": raw_url(m["path"]),
        })
        return call("POST", f"{GRAPH}/{PAGE_ID}/video_reels", data={
            "upload_phase": "finish",
            "video_id": video_id,
            "video_state": "PUBLISHED",
            "description": caption,
            "access_token": token,
        })

    raise RuntimeError(f"Unsupported Facebook type: {kind}")


def due(item):
    dt = datetime.fromisoformat(item["publish_at"])
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=TZ)
    return datetime.now(TZ) >= dt.astimezone(TZ)


def main():
    if not QUEUE_DIR.exists():
        return 0
    token = page_token()
    for path in sorted(QUEUE_DIR.glob("*.json")):
        item = json.loads(path.read_text(encoding="utf-8"))
        if item.get("status") not in {"scheduled", "partial_failed"} or not due(item):
            continue
        results = item.setdefault("results", {})
        for platform in item.get("platforms", ["instagram"]):
            if results.get(platform, {}).get("status") == "published":
                continue
            try:
                response = publish_instagram(item, token) if platform == "instagram" else publish_facebook(item, token)
                results[platform] = {
                    "status": "published",
                    "published_at": datetime.now(TZ).isoformat(),
                    "response": response,
                }
            except Exception as exc:
                results[platform] = {
                    "status": "failed",
                    "failed_at": datetime.now(TZ).isoformat(),
                    "error": str(exc),
                }
        item["status"] = "published" if all(results.get(p, {}).get("status") == "published" for p in item.get("platforms", ["instagram"])) else "partial_failed"
        item["updated_at"] = datetime.now(TZ).isoformat()
        path.write_text(json.dumps(item, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
