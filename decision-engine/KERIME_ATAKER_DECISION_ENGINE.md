# KERIME ATAKER — DECISION ENGINE (PRODUCTION GRADE)

## 0) AMAÇ VE KAPSAM

Bu motor, **çıktı üretiminden önce** tüm operatör mantığını deterministik biçimde çalıştırır ve hangi çıktı modülünün hangi disiplinle üretileceğini belirler.

Bu dosya aşağıdaki kullanım tiplerini destekler:

- single product outputs
- campaign outputs
- reels outputs
- story outputs
- Meta outputs
- boutique outputs
- product analysis outputs
- seasonal campaigns
- bridal campaigns
- holiday campaigns

Bu motorun temel hedefleri:

1. Lüks pozisyonu korumak
2. Lingerie-first riski engellemek
3. Ürün/kanal/hedef kitle uyumunu doğrulamak
4. Tekrarlı ve düşük kalite dili önlemek
5. Operatörü doğru üretim rotasına yönlendirmek

---

## 1) GİRDİ ŞEMASI (AUTOMATION-READY)

Zorunlu giriş alanları:

- `request_type` ∈ {single_product, campaign, reels, story, meta_ads, boutique, product_analysis, seasonal_campaign, bridal_campaign, holiday_campaign}
- `product_data`:
  - `name`
  - `category`
  - `materials[]`
  - `silhouette`
  - `colorways[]`
  - `price_band` (if available)
  - `verified_fields[]`
- `season_context`:
  - `market_season` (SS/FW/Transitional)
  - `climate_notes`
  - `holiday_window` (if exists)
- `occasion_context[]`
- `market_context`:
  - `target_us_cities[]`
  - `boutique_type[]`
  - `channel` ∈ {instagram_feed, instagram_story, reels, paid_meta, boutique_pitch}
- `brand_constraints`:
  - `tone_lock = premium_controlled_feminine`
  - `no_mass_market = true`
  - `no_spam_luxury = true`
- `evidence_pack`:
  - `internal_product_docs`
  - `approved_media_references`
  - `competitor_observations`
  - `confidence_inputs`

Opsiyonel alanlar:

- `campaign_stage` ∈ {awareness, consideration, intent, conversion, retention}
- `meta_budget_tier`
- `inventory_signal`
- `editorial_priority_hint`

---

## 2) ZORUNLU KARAR KATMANLARI

Her istekte aşağıdaki kararlar **sırasıyla** çalışır:

1. Product world classification
2. Luxury positioning fit
3. Lingerie-first risk detection
4. Seasonal fit validation
5. Occasion fit validation
6. Boutique compatibility
7. U.S. city compatibility
8. Meta objective selection
9. Audience quality logic
10. Campaign sequencing logic
11. Product hierarchy logic
12. Editorial priority logic
13. Caption rhythm variation
14. Anti-repetition protection
15. Fashion media intelligence usage
16. Competitor intelligence weighting
17. Evidence confidence scoring
18. CTA/CTI soft-discipline enforcement
19. Forbidden wording escalation
20. Luxury tone preservation
21. Final operator routing

---

## 3) DETERMİNİSTİK KARAR AĞACI (DECISION TREE)

## AŞAMA A — UYGUNLUK GATE

### A1: Veri doğrulama
- Eğer `verified_fields` kritik alanları kapsamıyorsa:
  - `status = HOLD_REQUIRES_VERIFICATION`
  - üretim sınırlı taslak moduna düşer.

### A2: Ürün dünya sınıflaması
- Kategorilerden biri atanır:
  - `LEATHER_SCULPT`
  - `FUR_ELEVATED`
  - `SILK_SATIN_EVENING`
  - `REFINED_BRIDAL`
  - `TAILORED_FEMININE`
  - `HYBRID_LUXE`
- Kural: birincil + ikincil dünya atanır (tek sınıf zorlaması yok).

### A3: Lingerie-first risk dedektörü
- Risk tetikleyicileri:
  - aşırı iç giyim kelime yoğunluğu
  - dış giyim/terzilik değerinin gölgelenmesi
  - ürünün “lingerie” olarak yanlış konumlanması
- Sonuç:
  - `risk_level ∈ {low, medium, high}`
  - `high` ise içerik otomatik `EDITORIAL_REFRAME_REQUIRED`.

### A4: Luxury positioning fit gate
- Aşağıdakilerden biri ihlal edilirse red:
  - mass-market tonu
  - agresif satış dili
  - hype/trend-chasing copy
- Sonuç:
  - `positioning_fit_score < 70` ise `REWRITE_REQUIRED`.

---

## AŞAMA B — PAZAR VE KULLANIM UYUMU

### B1: Seasonal fit validation
- Ürün materyali + silüet + sezon penceresi eşleştirilir.
- Çıktı:
  - `seasonal_fit = pass / caution / fail`
  - `fail` ise yalnızca alternatif sezon çerçevesi önerilir.

### B2: Occasion fit validation
- Occasion matrisi:
  - evening, cocktail, gallery, destination dinner, bridal civil, bridal after-party, holiday hosting
- `occasion_fit_score` hesaplanır.

### B3: Boutique compatibility
- Boutique profilleri:
  - avant-garde luxury
  - polished minimal luxury
  - feminine couture leaning
- `boutique_compatibility_score` + taşıma notu üretilir.

### B4: U.S. city compatibility
- Şehir kümeleri:
  - `NYC`, `LA`, `Miami`, `Dallas`, `Chicago`, `SF`
- Değerlendirme boyutları:
  - iklim uygunluğu
  - sosyal kullanım yoğunluğu
  - lüks tüketim davranışı
- Sonuç: `city_fit_map`.

---

## AŞAMA C — BÜYÜME VE MEDYA ORKESTRASYONU

### C1: Meta objective selection
Kurallar:
- Yeni dünya tanıtımı + düşük sinyal => `Awareness/Engagement`
- Ürün ilgisi oluşmuş + site trafiği hedefi => `Traffic`
- Güçlü niyet + stok uygun => `Conversions`
- Yeniden kazanım => `Retargeting`

### C2: Audience quality logic
Ayrı bloklarda çalışır:
1. searchable interests
2. luxury behavioral signals
3. strategic audience signals

Not: Doğrulanmamış hedefleme iddiaları yasaktır.

### C3: Campaign sequencing logic
Standart sıra:
1. Editorial aura seeding
2. Material/silhouette education
3. Occasion anchoring
4. Soft intent nudge
5. Controlled conversion ask

### C4: Product hierarchy logic
SKU veya look düzeyinde öncelik:
- Hero
- Support
- Entry-to-world
- Editorial-only

### C5: Editorial priority logic
Öncelik formülü:
- materyal özgünlüğü
- silüet ayırt ediciliği
- marka dünyası uyumu
- sezon uygunluğu

---

## AŞAMA D — METİN KALİTESİ VE KORUMA

### D1: Caption rhythm variation
Ritim şablonları dönüşümlü kullanılır:
- poetic-minimal
- material-cinematic
- silhouette-structured
- occasion-whisper

Aynı ritim arka arkaya 2’den fazla kullanılamaz.

### D2: Anti-repetition protection
- Son N çıktıda n-gram tekrar taraması
- Eşik üstü tekrar varsa otomatik yeniden yazım
- Yasak: aynı açılış cümlesi, aynı CTA kalıbı, aynı kapanış tınısı

### D3: Fashion media intelligence usage
- Yalnızca onaylı kaynak paketinden içgörü çekilir
- Her içgörü `insight_relevance_score` ile işaretlenir

### D4: Competitor intelligence weighting
Referans evreni (kopya yasak):
- Khaite, Nour Hammour, The Row, Saint Laurent, Alaïa, Fleur du Mal, Kiki de Montparnasse, LaPointe, Gabriela Hearst

Ağırlıklandırma:
- silhouette relevance: 35%
- material relevance: 35%
- market posture relevance: 30%

---

## AŞAMA E — GÜVEN, DİL DİSİPLİNİ VE ESCALATION

### E1: Evidence confidence scoring
Bileşik güven skoru:
- product evidence quality: 40%
- market evidence quality: 30%
- media/competitor support: 20%
- recency/verification state: 10%

Bandlar:
- `85-100`: publish-ready
- `70-84`: publish-with-caution
- `<70`: operator escalation required

### E2: CTA/CTI soft-discipline enforcement
Zorunlu kurallar:
- hard sell yasak
- “buy now” tarzı agresif çağrı yasak
- soft-direction izinli (discover, explore, inquire)

### E3: Forbidden wording escalation
Kelime/fraze sınıfları:
- cheap luxury tonları
- spam promosyon dili
- sahte kıtlık iddiaları
- doğrulanmamış performans iddiaları

Tetiklenirse:
- `FORBIDDEN_WORDING_BLOCK`
- otomatik redraft + audit flag

### E4: Luxury tone preservation
Final ton filtresi:
- premium
- controlled
- feminine
- refined
- cinematic
- editorial
- emotionally restrained
- material-focused

Skor < 80 ise final çıkışa izin verilmez.

---

## 4) WEIGHTED VALIDATION MODEL

Toplam skor: `DecisionScore = Σ(weight_i * score_i)`

Önerilen ağırlıklar:

- Product world precision: 8
- Luxury positioning fit: 12
- Lingerie-first safety: 10
- Seasonal fit: 8
- Occasion fit: 6
- Boutique compatibility: 8
- U.S. city compatibility: 6
- Meta objective correctness: 6
- Audience quality integrity: 6
- Campaign sequencing integrity: 5
- Product hierarchy clarity: 4
- Editorial priority clarity: 4
- Caption rhythm quality: 4
- Anti-repetition robustness: 4
- Fashion media intelligence relevance: 3
- Competitor weighting quality: 3
- Evidence confidence: 6
- CTA/CTI discipline: 3
- Forbidden wording safety: 2
- Luxury tone preservation: 10

Toplam = 118 normalize edilerek 100’e çevrilir.

Routing eşikleri:
- `>= 85` → `ROUTE_PRODUCTION`
- `70-84` → `ROUTE_SENIOR_REVIEW`
- `<70` → `ROUTE_HOLD_AND_REBUILD`

Kritik fail-safe kuralları (override):
- Forbidden wording block varsa doğrudan HOLD
- Lingerie-first high risk + low luxury fit varsa HOLD
- Evidence confidence <70 ise REVIEW altına düşemez, HOLD olur

---

## 5) OUTPUT TYPE ROUTING MATRİSİ

| Request Type | Primary Route | Secondary Modules | Final Gate |
|---|---|---|---|
| single_product | Product Analysis Core | Caption + Story + Meta Note | Tone + Evidence |
| campaign | Campaign Orchestrator | Sequencing + Hierarchy + City Fit | Anti-Repetition |
| reels | Reels Narrative Engine | Rhythm + Occasion + CTA Soft | Lingerie Risk |
| story | Story Microcopy Engine | Editorial Priority + Soft CTI | Forbidden Wording |
| meta_ads | Meta Strategy Engine | Objective + Audience + Sequencing | Evidence + Claim Safety |
| boutique | Boutique Placement Engine | Boutique Fit + Seasonal + Material | Luxury Positioning |
| product_analysis | Deep Analysis Engine | All 9 analysis layers | Confidence Score |
| seasonal_campaign | Seasonal Orchestrator | Climate + Occasion + City Clusters | Tone Lock |
| bridal_campaign | Bridal Refinement Engine | Bridal Occasion Matrix + Editorial | Lingerie Risk + Tone |
| holiday_campaign | Holiday Prestige Engine | Gifting/Hosting Context + Sequencing | No Mass-Market Drift |

---

## 6) OTOMASYON İÇİN DURUM KODLARI

- `OK_PROCEED`
- `OK_PROCEED_WITH_CAUTION`
- `REWRITE_REQUIRED`
- `EDITORIAL_REFRAME_REQUIRED`
- `HOLD_REQUIRES_VERIFICATION`
- `FORBIDDEN_WORDING_BLOCK`
- `ROUTE_SENIOR_REVIEW`
- `ROUTE_HOLD_AND_REBUILD`

Makine-okunur öneri çıktısı:

```json
{
  "status": "OK_PROCEED",
  "route": "ROUTE_PRODUCTION",
  "decision_score": 89,
  "risk_flags": ["none"],
  "required_actions": ["maintain_soft_cta", "preserve_material_focus"],
  "modules": ["campaign_orchestrator", "caption_rhythm_engine"]
}
```

---

## 7) FİNAL OPERATOR ROUTING PROTOKOLÜ

Final routing kuralları:

1. Önce güvenlik (forbidden wording, fake claim, lingerie-first high risk)
2. Sonra konumlandırma (luxury fit, tone preservation)
3. Sonra pazar uyumu (season, occasion, boutique, city)
4. Sonra büyüme orkestrasyonu (Meta objective, audience, sequencing)
5. En son metin varyasyonu (rhythm, anti-repetition)

Bu sıra bozulamaz. Bu sayede kalite her zaman büyümeden önce kilitlenir.

---

## 8) QA KİLİDİ (PRE-OUTPUT MANDATORY)

Yayın öncesi zorunlu checklist:

- tone check
- realism check
- luxury consistency check
- seasonal logic check
- boutique compatibility check
- duplicated language check
- over-selling check
- fake claims check

Her madde `pass/fail` döner. Herhangi bir `fail` varsa üretim çıkışı bloke edilir.

---

## 9) ENTEGRASYON NOTU

Bu motor aşağıdaki dosyalarla birlikte çalışır:

- `skills/kerime-ataker-luxury-operator/resources/*.md`
- `enforcement/KERIME_ATAKER_OUTPUT_ENFORCEMENT_ENGINE.md`
- `audits/KERIME_ATAKER_OUTPUT_AUDITOR.md`
- `schemas/KERIME_ATAKER_OPERATOR_OUTPUT_SCHEMA.md`

Bu dosya, orkestrasyon katmanıdır; içerik üretim katmanını yönetir, onun yerine geçmez.
