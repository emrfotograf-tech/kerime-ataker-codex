# KERIME ATAKER — CODEX OPERATION GUIDE

## PURPOSE

This project is the operational rule system for Kerime Ataker outputs inside Codex.

Codex must read:

- AGENTS.md
- skills/kerime-ataker-luxury-operator/SKILL.md
- resources/*.md
- enforcement/KERIME_ATAKER_OUTPUT_ENFORCEMENT_ENGINE.md

before producing Kerime Ataker content.

## HOW TO USE

When a new product, campaign or visual request is given, Codex must:

1. Read AGENTS.md
2. Read the luxury operator skill
3. Read all resource files
4. Read enforcement engine
5. Check product-index.md if product exists
6. Produce output according to Kerime Ataker rules
7. Run final QA mentally before final answer

## UPDATE METHOD

New products must be added to:

skills/kerime-ataker-luxury-operator/resources/product-index.md

Do not invent product details.
If product data is missing, mark as:
requires verification.

## STANDARD CODEX COMMAND

Run this product through the Kerime Ataker Luxury Operator System:
[PRODUCT LINK / PRODUCT NAME / CAMPAIGN REQUEST]

Return:
- product character
- Instagram caption
- story text
- reels structure
- hashtags
- boutique fit
- U.S. city fit
- Meta ads note
- final QA note

## REPOSITORY ARCHITECTURE

Detailed operating-system repository map and standards:

- docs/OPERATING_SYSTEM_ARCHITECTURE.md


## CANONICAL OUTPUT SCHEMA

Canonical operator output schema for all output types:

- schemas/KERIME_ATAKER_OPERATOR_OUTPUT_SCHEMA.md


## AUDIT MODULE

Production-grade pre-delivery simulation and validation module:

- audits/KERIME_ATAKER_OUTPUT_AUDITOR.md

## DECISION ENGINE

Production-grade orchestration and routing engine (pre-output logic layer):

- decision-engine/KERIME_ATAKER_DECISION_ENGINE.md

## SIMULATION ENGINE

Production-grade deterministic simulation and stress-test engine:

- simulation-engine/KERIME_ATAKER_SIMULATION_ENGINE.md

