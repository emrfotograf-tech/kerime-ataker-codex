# KERIME ATAKER — PRODUCTION ORCHESTRATION ROUTER

## 1) AMAÇ

Bu modül, Kerime Ataker üretim çıktılarının tamamını doğru yürütme hatlarına (execution pipelines) deterministik şekilde yönlendiren ana orkestrasyon katmanıdır.

Kapsam:
- single product outputs
- campaign outputs
- story outputs
- reels outputs
- Meta ad outputs
- boutique outputs
- product analysis outputs
- seasonal campaign outputs
- bridal campaign outputs
- holiday campaign outputs
- fashion media intelligence outputs
- competitor intelligence outputs

Router çıktısı yalnızca “iç operasyon” içindir; marka dili üretimi, ilgili hedef pipeline’da yapılır.

---

## 2) BAĞIMLILIKLAR / ENTEGRASYON NOKTALARI

Router aşağıdaki çekirdek modüllerle entegredir:

1. Enforcement Engine  
   `enforcement/KERIME_ATAKER_OUTPUT_ENFORCEMENT_ENGINE.md`
2. Canonical Schema System  
   `schemas/KERIME_ATAKER_OPERATOR_OUTPUT_SCHEMA.md`
3. Output Auditor  
   `audits/KERIME_ATAKER_OUTPUT_AUDITOR.md`
4. Decision Engine  
   `decision-engine/KERIME_ATAKER_DECISION_ENGINE.md`
5. Simulation Engine  
   `simulation-engine/KERIME_ATAKER_SIMULATION_ENGINE.md`

Tüm üretimler şu sırayı izler:
`INTAKE -> CLASSIFY -> ROUTE -> ENFORCE -> DECIDE -> SIMULATE -> AUDIT -> QA GATES -> RELEASE/ESCALATE`

---

## 3) GİRDİ KONTRATI (ROUTER INTAKE CONTRACT)

Router’a gelen minimum input:

```yaml
request_id: string
timestamp_utc: ISO-8601
request_source: [manual, api, batch, scheduled]
requested_output: string
product_context:
  product_name: string | null
  category: string | null
  materials: [string]
campaign_context:
  campaign_type: string | null
  season: string | null
  market: [string]
risk_context:
  claims_risk: [low, medium, high]
  legal_sensitivity: [low, medium, high]
  brand_sensitivity: [low, medium, high]
automation_mode: [full_auto, human_in_loop, manual_only]
```

Eksik zorunlu alan varsa router `FAIL_INTAKE_SCHEMA` döndürür ve escalation başlatır.

---

## 4) DESTİNASYON MATRİSİ (OUTPUT TYPE -> ROUTING DESTINATION)

| Output Type | Primary Destination | Secondary Destination | Notes |
|---|---|---|---|
| single_product | Product Pipeline | Story/Reels Pipeline | SKU odaklı üretim |
| campaign | Campaign Pipeline | Meta Ads Pipeline | Çoklu varlık yönetimi |
| story | Story Pipeline | Enforcement Engine | Kısa form aura-first kontrol |
| reels | Reels Pipeline | Simulation Engine | Hook-flow-retention simülasyonu |
| meta_ads | Meta Ads Pipeline | Auditor | Targeting doğrulama zorunlu |
| boutique | Boutique Pipeline | Decision Engine | Mağaza/şehir uyumu |
| product_analysis | Analysis Pipeline | Auditor | 9 katmanlı analiz zorunlu |
| seasonal_campaign | Seasonal Campaign Pipeline | Simulation Engine | Sezonal tutarlılık stresi |
| bridal_campaign | Bridal Pipeline | Enforcement Engine | Hassas marka tonu kontrolü |
| holiday_campaign | Holiday Pipeline | Decision Engine | Ticari agresyon riski yüksek |
| fashion_media_intelligence | Media Intel Pipeline | Auditor | Kaynak güvenilirlik denetimi |
| competitor_intelligence | Competitor Intel Pipeline | Enforcement Engine | Kopya-dil ihlali denetimi |

---

## 5) DETERMİNİSTİK ROUTING KURALLARI

### 5.1 Rule Priority (katı sıra)
1. Intake schema validity
2. Output type classification certainty
3. Brand safety hard blocks
4. Legal/compliance hard blocks
5. Pipeline availability
6. Automation compatibility
7. Weighted execution score

### 5.2 Deterministic Classifier

`requested_output` ve context alanları ile kesin sınıflandırma yapılır:

```text
if requested_output in ["single product", "product", "sku"] => single_product
if requested_output in ["campaign", "launch campaign"] => campaign
if requested_output in ["story", "ig story"] => story
if requested_output in ["reels", "video short"] => reels
if requested_output in ["meta", "ads", "paid"] => meta_ads
if requested_output in ["boutique", "wholesale", "store fit"] => boutique
if requested_output in ["analysis", "product analysis"] => product_analysis
if campaign_type == "seasonal" => seasonal_campaign
if campaign_type == "bridal" => bridal_campaign
if campaign_type == "holiday" => holiday_campaign
if requested_output contains "media intelligence" => fashion_media_intelligence
if requested_output contains "competitor" => competitor_intelligence
else => UNRESOLVED_TYPE
```

`UNRESOLVED_TYPE` durumunda otomatik release yasaktır.

---

## 6) WEIGHTED EXECUTION LOGIC

Deterministik route belirlendikten sonra aynı type içindeki execution profile weighted scoring ile seçilir.

### 6.1 Skor Formülü

```text
ExecutionScore =
  (0.30 * BrandSafetyScore)
+ (0.20 * DataCompletenessScore)
+ (0.15 * SchemaCompatibilityScore)
+ (0.15 * AutomationReadinessScore)
+ (0.10 * TimeCriticalityScore)
+ (0.10 * HistoricalPassRateScore)
```

Skor aralıkları:
- `>= 85`: Auto-route profile A
- `70-84`: Controlled-route profile B (human checkpoint)
- `< 70`: Escalation profile C (manual adjudication)

---

## 7) ZORUNLU VALIDATION LAYERS

Her output type için validation minimumları:

1. **Schema Validation** (canonical schema)
2. **Brand Tone Validation** (premium/refined/editorial)
3. **Claims Validation** (fake data / unverifiable claim blok)
4. **Material & Silhouette Validation** (ürün gerçeklik katmanı)
5. **Channel Fit Validation** (IG / Meta / Boutique uyumu)
6. **Context Validation** (season, campaign, market)

`product_analysis` tipinde ek zorunluluk:
- 9 katmanlı Product Analysis Layer tam geçiş.

---

## 8) ENFORCEMENT LAYERS

Hard enforcement (PASS zorunlu):
- no fake metrics
- no fabricated targeting
- no copied competitor language
- no spam-luxury tone
- no aggressive sales CTA
- no realism-breaking visual directives

Soft enforcement (warning üretebilir):
- excessive adjective density
- repeated phrase patterns
- seasonal mismatch suggestion

Hard fail durumları doğrudan `ESCALATE_SEV2+` üretir.

---

## 9) AUDIT LAYERS

Output Auditor ile minimum audit seti:
- Structural audit (schema integrity)
- Linguistic audit (tone, duplication, oversell)
- Strategic audit (market/channel fit)
- Compliance audit (claim and targeting verifiability)
- Trace audit (decision log completeness)

Audit sonucu:
- `AUDIT_PASS`
- `AUDIT_PASS_WITH_WARNINGS`
- `AUDIT_FAIL`

---

## 10) SIMULATION LAYERS

Simulation Engine aşağıdaki testleri çalıştırır:
- Best-case scenario simulation
- Baseline scenario simulation
- Adverse scenario simulation
- Edge-case prompt mutation simulation
- Channel drift simulation

Simulation sonucu risk haritasına işlenir ve routing confidence skorunu günceller.

---

## 11) QA GATES (PRE-RELEASE)

Release öncesi gate sırası:
1. Gate-QA-01: Schema PASS
2. Gate-QA-02: Enforcement PASS
3. Gate-QA-03: Audit PASS/PASS_WITH_WARNINGS
4. Gate-QA-04: Simulation complete
5. Gate-QA-05: Risk level accepted by policy
6. Gate-QA-06: Automation mode policy uyumu

Herhangi bir gate FAIL => release blok + fail-safe escalation.

---

## 12) RISK SEVERITY MODEL

Seviye tanımları:
- **SEV0 (Info):** düşük operasyon riski
- **SEV1 (Low):** kontrol edilebilir küçük sapma
- **SEV2 (Medium):** marka tutarlılığı riski
- **SEV3 (High):** compliance/brand damage riski
- **SEV4 (Critical):** yayın bloklayıcı kritik ihlal

Severity hesap girdi faktörleri:
- claims_risk
- legal_sensitivity
- brand_sensitivity
- audit fail count
- enforcement hard fail count

---

## 13) AUTOMATION COMPATIBILITY MATRİSİ

| Condition | Mode |
|---|---|
| score >= 85 and no hard fail and sev <= 1 | full_auto |
| score 70-84 or sev == 2 | human_in_loop |
| score < 70 or sev >= 3 | manual_only |

Router, öneri modu ile istenen `automation_mode` çakışırsa daha güvenli moda düşürür (downshift).

---

## 14) FAIL-SAFE ESCALATION PATHS

Escalation zinciri:
1. `ESC_L1_ROUTER_RETRY` (yalnızca geçici teknik hata)
2. `ESC_L2_HUMAN_REVIEW` (classification/validation belirsizliği)
3. `ESC_L3_BRAND_GUARDIAN` (tone/luxury positioning riski)
4. `ESC_L4_COMPLIANCE_OWNER` (claim/legal/targeting ihlali)
5. `ESC_L5_RELEASE_BLOCK` (kritik, yayın yasağı)

SEV3+ durumunda minimum L3 zorunludur. SEV4 doğrudan L5.

---

## 15) ROUTING CONFIDENCE SCORING

```text
RoutingConfidence =
  (0.35 * ClassificationConfidence)
+ (0.25 * DataCompletenessScore)
+ (0.20 * ValidationPassDensity)
+ (0.20 * HistoricalRouteStability)
```

Eşikler:
- `>= 0.90`: high confidence
- `0.75 - 0.89`: moderate confidence
- `< 0.75`: low confidence (auto release yok)

---

## 16) ÜRETİLEN ARTEFAKTLAR (MANDATORY OUTPUTS)

Her router çalışmasında aşağıdaki artefaktlar üretilir:

1. **Routing Report**
2. **Execution Map**
3. **Orchestration Summary**
4. **PASS/FAIL Routing Validation**
5. **Severity Scorecard**
6. **Fail-state Recommendations**

### 16.1 Routing Report Şablonu

```yaml
request_id: string
resolved_output_type: string
primary_destination: string
secondary_destination: string
automation_mode_selected: string
routing_confidence: float
execution_score: int
severity_level: string
qa_gate_results:
  gate_01_schema: [PASS|FAIL]
  gate_02_enforcement: [PASS|FAIL]
  gate_03_audit: [PASS|FAIL|PASS_WITH_WARNINGS]
  gate_04_simulation: [PASS|FAIL]
  gate_05_risk_policy: [PASS|FAIL]
  gate_06_automation_policy: [PASS|FAIL]
final_routing_validation: [PASS|FAIL]
escalation_path: string | null
recommendations:
  - string
```

---

## 17) PRODUCTION-SAFE ORCHESTRATION (STATE MACHINE)

```text
STATE_RECEIVED
  -> STATE_CLASSIFIED
  -> STATE_VALIDATED
  -> STATE_ENFORCED
  -> STATE_SIMULATED
  -> STATE_AUDITED
  -> STATE_QA_GATED
  -> [STATE_RELEASED | STATE_ESCALATED | STATE_BLOCKED]
```

Geçiş kuralı: Her state bir önceki state `PASS` olmadan ilerleyemez.

---

## 18) API / PIPELINE READY EXTENSION CONTRACT

Gelecek entegrasyonlar için önerilen endpoint yapısı:

- `POST /router/resolve`
- `POST /router/validate`
- `POST /router/simulate`
- `POST /router/finalize`
- `GET /router/report/{request_id}`

Önerilen event bus topic’leri:
- `ka.router.received`
- `ka.router.routed`
- `ka.router.failed`
- `ka.router.escalated`
- `ka.router.released`

Bu tanımlar ileriye dönük entegrasyon içindir; mevcut doküman seviyesinde vendor bağımsız kalınır.

---

## 19) PASS / FAIL GLOBAL KURALI

Global PASS için zorunlu koşullar:
- output type resolved
- tüm hard enforcement kuralları PASS
- schema PASS
- audit FAIL değil
- simulation tamamlandı
- sev <= policy threshold
- QA gates tamamlama PASS

Aksi durumda global sonuç `FAIL` ve escalation path zorunlu.

---

## 20) KISA OPERASYON ÖZETİ

Bu router, Kerime Ataker üretim sisteminde:
- doğru output’u doğru pipeline’a deterministik taşır,
- weighted logic ile execution profilini seçer,
- enforcement + audit + simulation + QA katmanlarıyla üretimi güvene alır,
- severity tabanlı escalation ile riskli çıktıları bloklar,
- otomasyon uyumunu policy bazlı yönetir,
- ve her çalışmada izlenebilir artefaktlar üretir.

