# KERIME ATAKER — STRUCTURED DATA ROOT-CAUSE AUDIT

Status: VERIFIED / READ-ONLY
Date: 2026-09-09
Source: live Shopify MAIN theme `snippets/structured-data.liquid`

## Product schema currently emitted by theme

The live theme explicitly builds a `Product` JSON-LD object and an `Offer` object for every variant.

Current Offer fields are:
- `@type: Offer`
- `price`
- `priceCurrency`
- `availability`
- `priceValidUntil`
- `url`

## Verified causes of current Google recommendations

The live Offer markup does NOT emit:
- `shippingDetails`
- `hasMerchantReturnPolicy`
- `validFrom`

This directly explains the current Merchant Listings recommendations already reported by Google for those fields.

The Product markup also does NOT emit:
- `aggregateRating`
- `review`

This directly explains the Product Snippets recommendations. These fields must remain absent until verified real review/rating data exists. No fabricated review data is permitted.

## Additional schema-quality issue found

The live theme currently hard-codes every variant offer as:
- `"availability": "http://schema.org/InStock"`

It does not branch on `variant.available` in this JSON-LD snippet. Therefore unavailable variants could be represented as InStock in theme-generated structured data. This is a verified code-level quality issue and should be corrected in a safe staging theme before any live deployment.

### Current live impact check — VERIFIED 2026-09-09

The current ACTIVE online-store catalog was separately re-read after identifying this code pattern. All inspected active published variants currently report `availableForSale: true`, and no inspected active product reports out-of-stock variants. Therefore the hard-coded `InStock` value does not currently create a verified live availability contradiction for the present catalog snapshot.

Classification:
- current catalog mismatch: NOT OBSERVED
- future correctness risk if inventory changes: VERIFIED
- safe staging fix still recommended before a real out-of-stock state occurs

The theme also hard-codes:
- `"priceValidUntil": "2030-01-01"`

Google's current recommendation concerns `validFrom`, which is a different property. The fixed `priceValidUntil` value does not satisfy the missing `validFrom` recommendation and should not be treated as a fix.

## Safe remediation boundary

Do not add `shippingDetails` or `hasMerchantReturnPolicy` until the underlying shipping and return facts are complete and verified. Current refund policy still has an unresolved return-address placeholder.

Do not add `aggregateRating` or `review` without real source data.

Do not write directly to the live MAIN theme. Preferred path:
1. duplicate/create unpublished staging theme,
2. patch structured data there,
3. validate rendered JSON-LD against actual product states,
4. compare with Google's rich-result/merchant requirements,
5. publish only after verification.

## Status

- Merchant Listings root cause — DONE / VERIFIED
- Product Snippets root cause — DONE / VERIFIED
- Hard-coded availability code risk — DONE / VERIFIED
- Current active-catalog availability impact audit — DONE / NO MISMATCH OBSERVED
- Live remediation — PARTIAL / BLOCKED by missing return/shipping facts + staging deployment requirement
