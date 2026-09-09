# KERIME ATAKER — SEO REMEDIATION STATE

Status: ACTIVE / CANONICAL
Last updated: 2026-09-09

Purpose: track verified Google/Search Console SEO issues without redoing completed product SEO or inventing structured-data values.

## Verified Google / Search Console Baseline

1. Page Indexing — PARTIAL / OPEN
   - Official Search Console notices report some validation attempts failed.
   - Some separate Page Indexing fixes were also verified successfully.

2. Soft 404 — OPEN / REQUIRES AFFECTED URL LIST
   - Official Search Console notice dated 2026-09-06 identifies Soft 404 as a new indexing exclusion reason.
   - A second Search Console notice explicitly says Soft 404 affects pages listed in the sitemap.
   - Gmail notices do not expose the affected URL list; do not claim a specific URL is affected without Search Console detail/export evidence.

3. Video Indexing — PARTIAL / OPEN
   - Official Search Console notice reports failed Video Indexing fix validation.
   - Exact affected URLs/pages require Search Console detail access.

4. Merchant Listings structured data — NON-CRITICAL / DIAGNOSED
   Google reports missing fields inside offers:
   - shippingDetails
   - validFrom
   - hasMerchantReturnPolicy
   These are improvement recommendations and were explicitly described by Google as non-critical.

5. Product Snippets structured data — NON-CRITICAL / DIAGNOSED
   Google reports missing:
   - aggregateRating
   - review
   Do not fabricate ratings or reviews. Only add these fields when verified real review/rating data exists.

## Live Shopify Policy / Commerce Findings

1. Shipping market support — VERIFIED
   - Shopify live shop has shipping countries configured, including US and multiple international markets.
   - This does not by itself prove that Google Merchant structured data currently emits shippingDetails.

2. Contact policy — VERIFIED
   - info@kerimeataker.com
   - 607 Ardross Avenue, Ambler PA 19002, United States
   - 9177949300

3. Refund policy — PARTIAL / DATA QUALITY ISSUE
   - Live policy states a 30-day return policy.
   - Live policy still contains placeholder: [INSERT RETURN ADDRESS].
   - Do not replace this with the contact address unless the merchant confirms that it is the actual return address.

4. Terms of Service — PARTIAL / DATA QUALITY ISSUE
   - Live policy still contains placeholders including [LINK], [INSERT TRADING NAME], [INSERT BUSINESS ADDRESS], [INSERT BUSINESS PHONE NUMBER], [INSERT BUSINESS REGISTRATION NUMBER], and [INSERT VAT NUMBER].
   - Do not invent missing legal/business values.

## Live Shopify Soft-404 Candidate Inventory Audit — VERIFIED 2026-09-09

This section is a first-party Shopify inventory audit, NOT a claim that these URLs are the Search Console Soft 404 examples.

1. Current ACTIVE catalog — healthy baseline
   - Current active products inspected have live onlineStoreUrl values, substantive descriptions, and completed SEO title/meta description fields.
   - Newly added active products also have live URLs and substantive descriptions.
   - Completed active-product SEO must not be rewritten without a verified delta.

2. Legacy / non-current product records requiring crawl/index review
   - `01` — handle `/products/01` — UNLISTED, no onlineStoreUrl, empty description, no SEO title/meta.
   - Old `ELLY` — handle `/products/elly` — UNLISTED, still has onlineStoreUrl, legacy duplicate content and no SEO fields. Current canonical product is `/products/elly-leather-mini-dress`.
   - `GRACE` — handle `/products/grace` — UNLISTED, still has onlineStoreUrl, legacy SEO-style copy and no SEO fields.
   - `KA-FUR 1` — `/products/ka-fur-1` — UNLISTED, still has onlineStoreUrl, legacy repetitive copy and no SEO fields.
   - `KA-F2` — `/products/ka-f2` — UNLISTED, still has onlineStoreUrl, legacy repetitive copy and no SEO fields.
   - `KA-F3` — `/products/ka-f3` — UNLISTED, still has onlineStoreUrl, legacy repetitive copy and no SEO fields.
   - `KA-F4` — `/products/ka-f4` — UNLISTED, still has onlineStoreUrl, legacy repetitive copy and no SEO fields.
   - Old imported lingerie records (`blue-leavers-lace-non-wired-bra`, `coral-balconette-bra-in-leavers-lace-and-stretch-tulle`, `cranberry-leavers-lace-non-wired-bra`, `dark-gray-lace-underwired-bra`, `gabrielle`, `gabrielle-2`, `gabrielle-3`, `gabrielle-4`) are UNLISTED with no onlineStoreUrl and no SEO metadata.
   - Draft-only records (`rabbit-fur-bolero`, `white-lamb-leather-strapless-maxi-dress-with-seam-paneling`, `__noop__`) have no live onlineStoreUrl and must not be treated as current indexed product pages.

3. Pages
   - `Contact` is published; Shopify page bodySummary is empty, but live storefront rendering contains the contact form and contact navigation. Do not classify it as Soft 404 from bodySummary alone.
   - `Catalog` (`/pages/lookbook`) and `Lookbook` (`/pages/gallery`) are unpublished and both already redirect to `/collections/all`.
   - `About Kerimè Ataker` is published.

4. Redirect hygiene — VERIFIED
   - Existing redirects cover renamed products, old collection handles, old page handles, and several old blog URLs.
   - `/products/elly-1` redirects to `/products/elly-leather-mini-dress`.
   - `/products/nergis` currently redirects to `/products/elly-1`, creating a redirect chain. This is not proven as a Search Console Soft 404, but should be flattened to point directly to the final canonical product when safe.
   - Old `/pages/lookbook` and `/pages/gallery` redirect to `/collections/all`.

## Safe Remediation Rules

- Completed product SEO remains DONE unless a verified delta exists.
- Never create fake aggregateRating/review structured data.
- Do not guess return address, registration number, VAT number, shipping timing, or shipping costs.
- Theme/schema changes require an unpublished-theme or safe staging path; do not blindly write to the live MAIN theme.
- Search Console affected URLs must come from direct Search Console detail access or another first-party export, not inference.
- Legacy UNLISTED products with live storefront URLs may be crawl/index candidates, but do not redirect/archive/delete them solely because they look suspicious; first verify whether they are referenced by sitemap, Search Console, backlinks, menus, collections, or internal links.
- Redirect chains should be flattened only when the final canonical target is already verified and the intermediate URL has no independent business purpose.

## Current Next Actions

1. Obtain affected URL list for Soft 404 / failed indexing validation — REQUIRES SEARCH CONSOLE DETAIL ACCESS.
2. Cross-check the verified legacy candidate URLs above against first-party sitemap/Search Console examples before any destructive change.
3. Flatten `/products/nergis` → `/products/elly-leather-mini-dress` after a final live redirect verification — SAFE DELTA CANDIDATE.
4. Clean legal-policy placeholders after merchant confirms missing legal/return details — REQUIRES USER CONFIGURATION.
5. Map verified shipping/return settings into Google Merchant structured data only after source values are complete — PARTIAL.
6. Keep daily SEO Health monitoring active and notify only on status changes — ACTIVE.
