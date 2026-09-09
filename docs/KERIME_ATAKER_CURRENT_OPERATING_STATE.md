# KERIME ATAKER — CURRENT OPERATING STATE

Status: ACTIVE / CANONICAL
Last updated: 2026-09-09

Purpose: prevent repeated work, forgotten project state, and unsafe overwrites. Before any Kerime Ataker task, read this state first, then live systems, then act only on the delta.

## Status Vocabulary
- DONE
- ACTIVE
- PARTIAL
- PAUSED
- FAILED
- NEW
- REQUIRES USER CONFIGURATION

## Canonical Rule
DONE work must not be rebuilt unless live evidence shows a verified regression or the user explicitly requests a redesign. Live Shopify / Search Console / Meta / Gmail state overrides stale snapshots.

## Current State

1. Brand positioning / tone / U.S. luxury logic — DONE / ACTIVE
2. CTI + CTA terminology; GTA prohibited — DONE / ACTIVE
3. Standard product/social output format — DONE / ACTIVE
4. Evidence / anti-hallucination / final QA system — DONE / ACTIVE
5. Seasonal content + seasonal product-fit logic — DONE / ACTIVE
6. Meta radius / city-fit logic — DONE / ACTIVE
7. Product discovery full social-output logic — DONE / ACTIVE
8. Shopify product visual-edit rules (#EEDEC4, natural grounding shadow, color preservation, video last) — DONE / ACTIVE
9. Existing product SEO baseline — DONE; do not rewrite completed products without a verified delta
10. SEO Delta Operator protocol — DONE / ACTIVE
11. Search / Index monitoring protocol — DONE / ACTIVE
12. Kerimé Ataker Daily Blog automation — ACTIVE
13. Daily Blog post-publish verification / health check — ACTIVE
14. Competitor intelligence historical dataset — ACTIVE BACKGROUND; refresh live for current claims
15. Fashion media intelligence historical dataset — ACTIVE BACKGROUND; refresh live for current claims
16. Verified Product Index historical snapshot — ACTIVE FALLBACK; live Shopify ACTIVE catalog is source of truth
17. Meta direct publishing API credentials / manual IG publish proof — DONE
18. Meta Publisher GitHub workflow — PAUSED; runtime state architecture repaired on 2026-09-09, but live publisher must not be reactivated without an explicit safe test
19. Meta runtime state branch `meta-publish-state` — DONE / ACTIVE; mutable queue status belongs here, not protected main
20. Legacy Meta test queue item — CANCELLED in state branch
21. Main-branch ruleset — DONE / ACTIVE; ChatGPT Codex Connector bypass removed and verified (`bypass_actors: []`)
22. Kerime Ataker brand mailbox `info@kerimeataker.com` integration — PAUSED by user; complete later
23. U.S. buyer / wholesale outreach — PAUSED until brand mailbox is verified
24. Editorial / PR outreach — PAUSED until brand mailbox is verified
25. Organic backlink / link-earning outreach — PAUSED until brand mailbox is verified; spam/bulk backlink acquisition prohibited
26. Old blog gray-background image technical source audit — DONE; current published article featured images resolve through Shopify CDN and carry ALT text. Visual pixel/background QA remains only if a legacy page still visibly shows gray media.
27. Search Console baseline known issues — ACTIVE: Soft 404, failed Page Indexing validation, failed Video Indexing validation. Some other Page Indexing fixes have succeeded. Report only status changes, not the same baseline repeatedly.
28. Merchant Listings structured data — PARTIAL / DIAGNOSED: Google reports missing `shippingDetails`, `validFrom`, and `hasMerchantReturnPolicy` inside offers; currently non-critical recommendations.
29. Product Snippets structured data — DIAGNOSED / NO FABRICATION: Google reports missing `aggregateRating` and `review`; do not create these unless verified real review/rating data exists.
30. Shopify legal/policy data quality — PARTIAL: Refund Policy contains `[INSERT RETURN ADDRESS]`; Terms of Service contains unresolved template placeholders. Missing legal/return values must be confirmed before edits.
31. Canonical SEO remediation state — ACTIVE in `docs/KERIME_ATAKER_SEO_REMEDIATION_STATE.md`.

## Required Preflight Before Any New Work
1. Check this state.
2. Read the live target system.
3. Classify the requested area as DONE / ACTIVE / PARTIAL / PAUSED / FAILED / NEW.
4. If DONE, do not rebuild.
5. If PARTIAL / NEW / FAILED, change only the verified delta.
6. Re-read the live result after any write.
7. Log the new state here or in the relevant execution record.

## High-Risk Write Protection
Never blindly overwrite:
- Shopify product title
- product handle / URL
- completed product description
- valid SEO title / meta description
- valid ALT text
- canonical/index directives
- Meta publishing state
- outreach history / sent-domain dedupe state
- legal/policy placeholders with guessed values
- structured review/rating data without real reviews

## Current Priority Queue
1. Keep `info@kerimeataker.com` mailbox setup PAUSED until the user resumes it.
2. Keep buyer / editorial / backlink outreach PAUSED until mailbox verification.
3. Keep Meta Publisher PAUSED until a separate explicit safe test is approved.
4. Resolve Search Console issues by verified delta: affected Soft 404/indexing URLs first, then merchant structured-data improvements where source facts are complete.
5. Obtain/confirm missing return/legal details before editing live policies.
6. Continue SEO Delta + Search/Index monitoring + Daily Blog health checks.
