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
21. Main-branch ruleset — ACTIVE; ChatGPT Codex Connector bypass is still present and should be removed after GitHub maintenance is finished
22. Kerime Ataker brand mailbox `info@kerimeataker.com` integration — REQUIRES USER CONFIGURATION / not verified in connected Gmail
23. U.S. buyer / wholesale outreach — PAUSED until brand mailbox is verified
24. Editorial / PR outreach — PAUSED until brand mailbox is verified
25. Organic backlink / link-earning outreach — PAUSED until brand mailbox is verified; spam/bulk backlink acquisition prohibited
26. Old blog gray-background image cleanup — PARTIAL / requires visual final QA if any legacy page still shows gray media
27. Search Console baseline known issues — ACTIVE: Soft 404 plus previously failed Page Indexing / Video Indexing fix validations; report only changes, not the same baseline repeatedly

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

## Current Priority Queue
1. Finish GitHub maintenance, then remove unnecessary Codex ruleset bypass.
2. Verify / configure `info@kerimeataker.com` so brand mail can send and replies can be read safely.
3. Reactivate buyer / editorial / backlink outreach only after mailbox verification.
4. Keep Meta Publisher paused until a separate explicit safe test is approved.
5. Continue SEO Delta + Search/Index monitoring + Daily Blog health checks.
