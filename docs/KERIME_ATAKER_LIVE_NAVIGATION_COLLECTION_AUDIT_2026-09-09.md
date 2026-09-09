# KERIME ATAKER — LIVE NAVIGATION + COLLECTION AUDIT

Status: VERIFIED / READ-ONLY AUDIT
Date: 2026-09-09
Source of truth: live connected Shopify Admin GraphQL + live MAIN theme configuration

## 1. Active navigation configuration — VERIFIED

The live MAIN theme is `Kerime Ataker`.

Both the current header group and the mobile-navigation settings select:
- `main-menu-2`

The current footer uses:
- `footer` for Info
- `main-menu-2` for Shop

Therefore `main-menu-2` is the active primary commerce navigation. The older `main-menu` and `accessory-menu` are not selected as the current header/mobile/footer navigation in the inspected live MAIN theme configuration.

## 2. Active menu link health — VERIFIED

`main-menu-2` currently points directly to live collection resources:
- `/collections/all`
- `/collections/fur`
- `/collections/jacket`
- `/collections/coat`
- `/collections/vest`
- `/collections/other`
- `/collections/leather`
- `/collections/top`
- `/collections/skirt`
- `/collections/pants`
- `/collections/leather-jacket`
- `/collections/leather-others`
- `/collections/lingerie`
- `/collections/sets`

No redirect-source path was found in the active `main-menu-2` link structure.

## 3. Legacy menu records — VERIFIED / NON-DESTRUCTIVE

Legacy menu records still exist:
- `main-menu` contains `Lookbook` → `/pages/gallery`; that URL currently redirects to `/collections/all`.
- `accessory-menu` contains `Bag` → `/collections/bag` and `Jewelry` → `/collections/jewelry`; both currently redirect to `/collections/all`.

Because these menus are not selected as current primary header/mobile/footer navigation in the inspected MAIN-theme configuration, they are retained and not edited or deleted. This is consistent with the no-destructive-cleanup rule.

## 4. MAIN-theme mega-menu configuration — VERIFIED ISSUE

The live `sections/header-group.json` contains five `linklist_with_images` blocks named for:
- Fur
- Leather
- Lingerie
- Accessory
- New

Each block currently has three image links whose `image_url_1`, `image_url_2`, and `image_url_3` are all set to:
- `shopify://collections/bra`

The store has an existing redirect:
- `/collections/bra` → `/collections/lingerie`

This means the configured mega-menu promotional image links use a legacy collection target rather than a direct current target. This is an internal-link hygiene issue, not evidence of a Google Soft 404 by itself.

No live MAIN-theme file write was attempted. MAIN-theme writes are treated as high-risk and require a safe staging/unpublished-theme path.

## 5. Published collection content audit — VERIFIED

Current published collections were checked for product count, description, and SEO metadata.

Healthy collection baseline:
- Fur — 18 products; description + SEO present
- Fur Jacket — 10; description + SEO present
- Coat — 3; description + SEO present
- Vest — 5; description + SEO present
- Fur Others — 3; description + SEO present
- Leather — 14; description + SEO present
- Top — 2; description + SEO present
- Skirt — 1; description + SEO present
- Pants — 2; description + SEO present
- Leather Jacket — 3; description + SEO present
- Leather Others — 5; description + SEO present
- Lingerie — 3; description + SEO present
- Sets — 3; description + SEO present
- All — 36; description + SEO present

Thin-content candidates requiring evidence before destructive change:

### `/collections/frontpage`
- title: `Home page`
- published
- 0 products
- empty description
- SEO title: null
- SEO description: null
- no direct link found in the inspected active navigation

Classification: `VERIFIED LIVE THIN PUBLISHED CANDIDATE / REQUIRES GSC URL CONFIRMATION`.
Do not call it a confirmed Soft 404 without first-party Search Console affected-URL evidence. Do not delete/unpublish solely from inference.

### `/collections/leather-dress`
- published
- 1 product
- empty collection description
- SEO title and SEO description are present

Classification: `THIN BUT SEO-COMPLETE / MONITOR`.
No rewrite or destructive change is justified from this audit alone.

## 6. Safe next actions

1. Keep completed active collection SEO stable.
2. Obtain the Search Console affected URL list before classifying `/collections/frontpage` as a real Soft 404.
3. Treat the live mega-menu `/collections/bra` image links as a verified internal-link hygiene delta; repair only through safe theme staging or Shopify theme editor review, not a blind MAIN-theme write.
4. Do not delete legacy menus or collections without verified business/reference evidence.
