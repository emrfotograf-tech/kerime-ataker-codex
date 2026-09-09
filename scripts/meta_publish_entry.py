#!/usr/bin/env python3
from scripts import meta_publish

_original_raw_url = meta_publish.raw_url


def media_url(value):
    if isinstance(value, str) and value.startswith(("https://", "http://")):
        return value
    return _original_raw_url(value)


meta_publish.raw_url = media_url

if __name__ == "__main__":
    raise SystemExit(meta_publish.main())
