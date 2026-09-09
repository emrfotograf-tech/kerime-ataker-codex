# KERIME ATAKER — META PUBLISH BRIDGE

## Purpose

This bridge turns user-selected media into scheduled Instagram/Facebook publishing through Meta Graph API.

The user remains the visual authority. Codex must never replace, reinterpret, crop, regenerate, or substitute an uploaded publishing asset unless the user explicitly asks.

## Required user input

For one product/campaign the user may provide, in one conversation:

- product link or product name
- POST image(s)
- STORY image/video
- REELS video
- publishing date/time in Europe/Istanbul

The product link does not need to be repeated for Post, Story, and Reels when they belong to the same product package.

## Codex execution rule

When the user says an asset is for publishing and gives a time:

1. Run the normal Kerime Ataker product/content system.
2. Preserve the exact uploaded media selected by the user.
3. Save publishing media under `media/YYYY-MM-DD/<product-slug>/`.
4. Create one queue JSON per publishing event under `publish_queue/`.
5. Set `status` to `scheduled` only when the requested copy and media are complete.
6. Commit and push the media + queue JSON to `main`.
7. Report the exact scheduled items back to the user.

Do not require the user to separately upload files anywhere else.

## Queue schema

Example Post item:

```json
{
  "id": "2026-09-09-luna-post-2200",
  "product": "LUNA",
  "product_url": "https://kerimeataker.com/products/luna",
  "type": "POST",
  "platforms": ["instagram", "facebook"],
  "publish_at": "2026-09-09T22:00:00+03:00",
  "caption": "Brand-facing English caption and hashtags here.",
  "media": [
    {"kind": "image", "path": "media/2026-09-09/luna/post-01.jpg"}
  ],
  "status": "scheduled",
  "results": {}
}
```

Example Story item:

```json
{
  "id": "2026-09-09-luna-story-1900",
  "product": "LUNA",
  "type": "STORY",
  "platforms": ["instagram", "facebook"],
  "publish_at": "2026-09-09T19:00:00+03:00",
  "caption": "",
  "media": [
    {"kind": "image", "path": "media/2026-09-09/luna/story.jpg"}
  ],
  "status": "scheduled",
  "results": {}
}
```

Example Reel item:

```json
{
  "id": "2026-09-10-luna-reel-0100",
  "product": "LUNA",
  "type": "REEL",
  "platforms": ["instagram", "facebook"],
  "publish_at": "2026-09-10T01:00:00+03:00",
  "caption": "Brand-facing English Reels caption with required premium hashtags.",
  "media": [
    {"kind": "video", "path": "media/2026-09-09/luna/reel.mp4"}
  ],
  "share_to_feed": true,
  "status": "scheduled",
  "results": {}
}
```

## Publisher

GitHub Actions runs `.github/workflows/meta-publish.yml` every five minutes.

It executes `scripts/meta_publish.py`, which:

- checks due queue items in Europe/Istanbul time
- publishes them through Meta Graph API
- records per-platform success/failure in the queue JSON
- commits queue status back to the repository

## Secrets

The System User token must never be committed to the repository.

GitHub Actions requires this repository secret:

`META_SYSTEM_USER_TOKEN`

The configured assets are:

- Facebook Page ID: `883182878201071`
- Instagram Professional Account ID: `17841476687386286`

## Media visibility caveat

This repository is currently public. Media committed here can be reachable via public raw GitHub URLs before the scheduled publish time. For unreleased/private campaign assets, move media hosting to a private-to-public-on-demand media host or another controlled CDN before using this workflow for embargoed content.
