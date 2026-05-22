# KERIME ATAKER — SIMULATION ENGINE (Production Deterministic Test Layer)

## 1) Purpose

Bu modül, Kerime Ataker üretim çıktılarının canlıya alınmadan önce deterministik senaryo simülasyonu ile test edilmesini sağlar. Amaç; lüks ton korunumu, kural uyumu, rota doğruluğu ve QA gate davranışını ölçmek, ölçülebilir PASS/FAIL raporu üretmek ve otomasyon pipeline’larına makine-okunur çıktı vermektir.

Bu engine aşağıdaki çıktı türlerini kapsar:

- Instagram post outputs
- Story outputs
- Reels outputs
- Campaign outputs
- Meta ad outputs
- Boutique outputs
- Product analysis outputs
- Seasonal campaign outputs
- Bridal campaign outputs
- Holiday campaign outputs

---

## 2) Scope

Simulation Engine aşağıdaki üretim katmanları ile entegre düşünülür:

- `AGENTS.md` (global policy)
- `schemas/KERIME_ATAKER_OPERATOR_OUTPUT_SCHEMA.md` (çıktı şeması)
- `enforcement/KERIME_ATAKER_OUTPUT_ENFORCEMENT_ENGINE.md` (zorunlu kural katmanı)
- `audits/KERIME_ATAKER_OUTPUT_AUDITOR.md` (denetim katmanı)
- `decision-engine/KERIME_ATAKER_DECISION_ENGINE.md` (yönlendirme/routing katmanı)

Simulation Engine üretim motorunun yerine geçmez; üretim motoruna “release gate” ve “stress harness” sağlar.

---

## 3) Core Architecture

### 3.1 Deterministic Test Philosophy

Deterministik test için aşağıdaki prensipler zorunludur:

1. Aynı input seti + aynı policy sürümü + aynı test seed => aynı skor ve aynı karar.
2. Tüm kural ihlalleri rule-id ile loglanır.
3. Her test adımı timestamped ama karar mantığı zaman-bağımsızdır.
4. “Soft suggestion” ve “hard fail” ayrımı net tutulur.

### 3.2 Module Graph

1. **Scenario Loader**
   - Senaryo tanımı yükler.
2. **Normalizer**
   - Input’u kanonik şemaya çevirir.
3. **Routing Probe**
   - Decision engine rota davranışını simüle eder.
4. **Policy Validator**
   - Global policy ve output rule kontrolleri.
5. **Enforcement Emulator**
   - Hard gate kurallarını uygular.
6. **Auditor Emulator**
   - Audit katmanı ile skor ve bulgu üretir.
7. **QA Gate Simulator**
   - Final QA lock davranışını test eder.
8. **Scoring Engine**
   - Severity skorları ve PASS/FAIL hesaplar.
9. **Correction Recommender**
   - Kural bazlı düzeltme aksiyonları üretir.
10. **Report Builder**
   - Human-readable + automation-ready rapor üretir.

### 3.3 Execution Modes

- **Mode A — Preflight Smoke**: kritik alanları hızlı kontrol.
- **Mode B — Full Validation**: tüm kural setini kapsayan derin test.
- **Mode C — Stress Test**: çelişkili, eksik, noisy input ile dayanıklılık testi.
- **Mode D — Regression Lock**: önceki release baseline ile fark analizi.

---

## 4) Simulation Input Contract

Her senaryo aşağıdaki alanlarla tanımlanır:

- `scenario_id`
- `scenario_type` (instagram_post | story | reels | campaign | meta_ad | boutique | product_analysis | seasonal_campaign | bridal_campaign | holiday_campaign)
- `locale_policy`
- `operator_zone_content`
- `brand_facing_content`
- `product_context`
- `season_context`
- `occasion_context`
- `boutique_context`
- `meta_objective`
- `timing_block`
- `expected_route`
- `evidence_tags`
- `test_seed`

Not: Brand-facing alanlar yalnız İngilizce, operasyonel başlıklar Türkçe olmak zorundadır.

---

## 5) Validation Matrix (Mandatory)

Engine aşağıdaki kontrolleri zorunlu uygular:

1. luxury tone consistency
2. CTA/CTI discipline
3. banned GTA terminology
4. evidence tagging
5. fake data detection
6. hashtag structure
7. Turkish operator heading compliance
8. English-only brand-facing copy zones
9. seasonal mismatch detection
10. occasion mismatch detection
11. boutique mismatch detection
12. Meta objective mismatch detection
13. anti-spam discipline
14. output hierarchy validation
15. timing structure validation
16. QA gate behavior
17. routing logic behavior
18. enforcement engine behavior
19. auditor behavior
20. decision engine behavior

Her kontrol için minimum alanlar:

- `control_id`
- `severity` (critical | high | medium | low)
- `result` (PASS | FAIL | WARN)
- `evidence`
- `correction_action`

---

## 6) Rule Severity Model

### 6.1 Severity Definitions

- **Critical**: marka güvenliği veya policy ihlali; otomatik FAIL.
- **High**: positioning bozan ciddi uygunsuzluk; güçlü düzeltme gerekir.
- **Medium**: kalite düşüren ama düzeltilebilir sapma.
- **Low**: stil/tutarlılık iyileştirme alanı.

### 6.2 Auto-Fail Triggers

Aşağıdakilerden herhangi biri “FAIL_RELEASE” üretir:

- fake data tespiti
- brand-facing zone’da İngilizce dışı kopya
- yasaklı GTA terminolojisi
- spam CTA yapısı
- seasonal/occasion/boutique kritik çakışması
- Meta objective ile output niyetinin çelişmesi

---

## 7) PASS/FAIL Decision Protocol

### 7.1 Decision States

- `PASS_RELEASE`
- `PASS_WITH_WARNINGS`
- `FAIL_REQUIRES_CORRECTION`
- `FAIL_HARD_POLICY_BLOCK`

### 7.2 Deterministic Decision Function

Önerilen karar fonksiyonu:

- any critical fail => `FAIL_HARD_POLICY_BLOCK`
- high fail count >= 2 => `FAIL_REQUIRES_CORRECTION`
- high fail count = 1 ve medium fail <= 1 => `PASS_WITH_WARNINGS`
- fail yok, warn kontrollü => `PASS_RELEASE`

---

## 8) Stress-Test Scenario Library

Zorunlu stres senaryo aileleri:

1. **Language Boundary Stress**
   - Türkçe/İngilizce zoneların kasıtlı karıştırılması.
2. **Luxury Tone Erosion Stress**
   - ucuz/promosyonel dil enjeksiyonu.
3. **Meta Objective Conflict Stress**
   - traffic objective ile high-luxury intent copy çelişkisi.
4. **Seasonal Conflict Stress**
   - kış ürünü + yaz anlatısı.
5. **Occasion Conflict Stress**
   - bridal ürünün holiday casual framing ile sunulması.
6. **Boutique Persona Stress**
   - yanlış butik karakterine yanlış ürün dili.
7. **Hashtag Spam Stress**
   - aşırı hashtag ve düşük kalite etiket kümeleri.
8. **Evidence Null Stress**
   - kanıt etiketi olmadan kesin iddia üretimi.

---

## 9) Correction Recommendation Engine

Düzeltme önerileri kural-id bazlı ve otomasyona uygun üretilir:

- `rule_id`
- `issue_summary`
- `recommended_fix`
- `priority`
- `owner` (operator | qa | strategy)
- `retest_required` (true|false)

Örnek öneri tipi:

- “brand_facing_copy_language_rule” ihlali -> İngilizceye normalize et, Türkçe başlığı sadece operator zone’da bırak.

---

## 10) Automation-Ready Output Schema

```json
{
  "simulation_run_id": "SIM-2026-0001",
  "engine_version": "1.0.0",
  "scenario_id": "SCN-IG-POST-014",
  "scenario_type": "instagram_post",
  "decision": "FAIL_REQUIRES_CORRECTION",
  "severity_score": 78,
  "status_breakdown": {
    "pass": 11,
    "warn": 3,
    "fail": 6,
    "critical_fail": 0
  },
  "control_results": [
    {
      "control_id": "LANG-002",
      "result": "FAIL",
      "severity": "high",
      "evidence": ["brand_facing_copy contains Turkish sentence"],
      "correction_action": "Rewrite brand-facing copy in English only"
    }
  ],
  "routing_probe": {
    "expected_route": "campaign>enforcement>auditor",
    "observed_route": "campaign>auditor",
    "route_match": false
  },
  "qa_gate": {
    "executed": true,
    "blocked": true,
    "block_reason": "LANG-002"
  },
  "recommendations": [
    {
      "rule_id": "LANG-002",
      "priority": "P1",
      "owner": "operator",
      "recommended_fix": "Replace Turkish brand-facing sentence with premium English editorial copy",
      "retest_required": true
    }
  ],
  "deterministic_hash": "sha256:..."
}
```

---

## 11) Reporting Layer

### 11.1 Human-Readable Report Sections

1. Run Metadata
2. Scenario Summary
3. Control-by-Control Findings
4. Severity Heatmap
5. Routing + Enforcement + Auditor behavior
6. QA Gate Outcome
7. PASS/FAIL Decision
8. Correction Plan
9. Retest Checklist

### 11.2 Machine Output Channels

- JSON artifact (CI/CD tüketimi)
- Markdown audit log (insan okuması)
- Diff-friendly flat summary (`key=value`)

---

## 12) Output Hierarchy & Timing Validation Rules

### 12.1 Output Hierarchy

Kontrol edilen sıra:

1. Context
2. Strategy
3. Brand-facing copy
4. CTA/CTI
5. Hashtags
6. QA footer

Bu sıralama dışına çıkan çıktılar hierarchy fail alır.

### 12.2 Timing Structure

Aşağıdaki yapı doğrulanır:

- campaign start window
- content drop cadence
- reminder cadence
- closing cadence

Eksik veya çelişkili timing bloğu timing fail üretir.

---

## 13) Integration Contract (Future Pipeline)

Engine aşağıdaki pipeline adımlarına bağlanacak şekilde tasarlanır:

1. `generate_output`
2. `simulate_output`
3. `enforce_policy`
4. `audit_output`
5. `decision_gate`
6. `publish_or_return_for_fix`

CI entegrasyonu için minimum gereklilik:

- deterministik seed
- sabit rule versioning
- artifact retention
- release-block webhook

---

## 14) Governance & Versioning

- Semantic versioning: `MAJOR.MINOR.PATCH`
- Her rule değişikliğinde `rule_changelog` güncellenir.
- Eski raporlar backward-audit için saklanır.
- “Unknown behavior” durumları `WARN` değil `FAIL_REQUIRES_CORRECTION` olarak işaretlenir.

---

## 15) Final QA Lock for Simulation Engine

Run kapatmadan önce zorunlu checklist:

- tone check tamam mı?
- realism check tamam mı?
- luxury consistency check tamam mı?
- seasonal logic check tamam mı?
- boutique compatibility check tamam mı?
- duplicated language check tamam mı?
- over-selling check tamam mı?
- fake claims check tamam mı?

Bu checklist tamamlanmadan rapor “final” statüsü alamaz.
