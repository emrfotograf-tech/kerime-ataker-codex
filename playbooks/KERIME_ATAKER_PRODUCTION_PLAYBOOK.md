# KERIME ATAKER PRODUCTION PLAYBOOK

Version: 1.0.0  
Status: Official / Production  
Owner: Kerime Ataker Production OS

---

## 1) Amaç ve Kapsam

Bu playbook, Kerime Ataker Production OS içinde tüm içerik ve kampanya üretimlerinin **deterministic**, **audit edilebilir**, **automation-ready** ve **production-safe** şekilde yürütülmesi için resmi işletim prosedürüdür.

Kapsam:
- Single Product Workflow
- Campaign Workflow
- Story Workflow
- Reels Workflow
- Meta Ad Workflow
- Boutique Workflow
- Product Analysis Workflow
- Seasonal Campaign Workflow
- Bridal Campaign Workflow
- Holiday Campaign Workflow
- Competitor Intelligence Workflow
- Fashion Media Intelligence Workflow

Bu doküman, routing/validation/enforcement/simulation/QA/release adımlarını tek bir üretim disiplini altında birleştirir.

---

## 2) Sistem Prensipleri

1. **Aura First, Product Second**: Çıktı önce marka aurasını kurar, sonra ürüne iner.  
2. **No Fabrication**: Ürün, medya, reklam veya performans metriklerinde uydurma yok.  
3. **Deterministic Flow**: Aynı input + aynı kurallar = aynı route ve aynı kalite davranışı.  
4. **Strict Gates**: PASS almayan output production’a çıkamaz.  
5. **Traceability**: Her adımda karar izi (decision log) tutulur.  
6. **Luxury Consistency**: Ton, materyal, silüet ve premium positioning sapması kritik risk sayılır.

---

## 3) Operatör Rolleri

- **Operator**: Input hazırlama, brief netleştirme, ilk route tetikleme.
- **Router**: İşi doğru workflow’a dağıtma.
- **Validator**: Şema, içerik bütünlüğü ve gerçeklik kontrolü.
- **Enforcement Controller**: Marka kuralları ihlal taraması.
- **Simulation Controller**: Stress-test, edge-case, fallback simülasyonu.
- **QA Gatekeeper**: Final PASS/FAIL ve release onayı.
- **Release Manager**: Production yayın ve post-release izleme.

Not: Roller insan veya otomasyon ajanı olabilir; protokol aynıdır.

---

## 4) Global İşletim Sırası (Execution Order)

Her output tipi aşağıdaki sabit sırayı kullanır:

1. **Input Intake**
2. **Intent Classification**
3. **Workflow Routing**
4. **Product/Context Analysis**
5. **Draft Generation**
6. **Validation Layer**
7. **Enforcement Layer**
8. **Simulation Layer**
9. **QA Gate Layer**
10. **Release Decision**
11. **Post-Release Audit**

Bu sıra değiştirilemez; yalnızca fail-safe akışlarıyla geri dönüş yapılabilir.

---

## 5) Routing Order (Yönlendirme Sırası)

### 5.1 Birincil Route Kararı

1. Input türü belirlenir: Product / Campaign / Story / Reels / Meta Ad / Boutique / Intelligence.
2. Zaman bağlamı belirlenir: Seasonal / Bridal / Holiday / Evergreen.
3. Kanal bağlamı belirlenir: Instagram Feed / Story / Reels / Meta Ads / Boutique kit.
4. Risk seviyesi belirlenir: Low / Medium / High / Critical.
5. Uygun workflow pipeline atanır.

### 5.2 İkincil Route Kararı

- Ürün varsa Product Analysis pipeline önce çalışır.
- Kampanya ise Campaign core pipeline + ilgili alt pipeline (Seasonal/Bridal/Holiday).
- Intelligence talepleri (competitor/media) yayın pipeline’ına doğrudan çıkmaz; önce insight-only modda işlenir.

---

## 6) Validation Order (Doğrulama Sırası)

1. **Schema Validation**: Zorunlu alanlar dolu mu?
2. **Data Integrity Validation**: Kaynak/doğrulanabilirlik var mı?
3. **Tone Validation**: Premium, restrained, editorial çizgi korunuyor mu?
4. **Material & Silhouette Validation**: Teknik moda okumaları tutarlı mı?
5. **Channel Validation**: Feed/Story/Reels/Ads formatına uyum var mı?
6. **Compliance Validation**: Fake claim, spam CTA, kopya dil var mı?

Validation sonucu `VAL_PASS` veya `VAL_FAIL` olarak kaydedilir.

---

## 7) Enforcement Order (Kural Uygulama Sırası)

1. **Brand Positioning Lock**
2. **Language Discipline Lock**
3. **No-Fabrication Lock**
4. **Luxury Tone Lock**
5. **Visual Realism Lock**
6. **Channel Policy Lock**

Her lock için outcome:
- `PASS`
- `SOFT_FAIL` (düzeltilebilir)
- `HARD_FAIL` (bloklayıcı)

`HARD_FAIL` durumunda otomatik production block tetiklenir.

---

## 8) Audit Order (Denetim Sırası)

1. Decision log bütünlüğü
2. Route doğruluğu
3. Validation kayıtları
4. Enforcement ihlal kayıtları
5. Simulation senaryoları + sonuçları
6. QA gate kararı
7. Release/not-release gerekçesi

Audit çıktısı: `AUDIT_CLEAR` veya `AUDIT_HOLD`.

---

## 9) Simulation Order (Simülasyon Sırası)

Simülasyon, release öncesi aşağıdaki sıra ile çalışır:

1. **Baseline Simulation**: Normal kullanım senaryosu
2. **Stress Simulation**: Yoğun/karma input
3. **Ambiguity Simulation**: Eksik veya belirsiz brief
4. **Policy Collision Simulation**: Kanal ve brand kural çakışmaları
5. **Fallback Simulation**: Veri eksikliği ve fail-safe yolları

Simulation sonucu:
- `SIM_PASS`
- `SIM_FAIL_RETRY`
- `SIM_FAIL_BLOCK`

---

## 10) QA Gate Order

Final QA gate aşağıdaki sırayla zorunlu kontrol yapar:

1. Tone
2. Realism
3. Luxury consistency
4. Seasonal logic
5. Boutique compatibility
6. Duplicated language
7. Over-selling risk
8. Fake claim risk

Skorlama ve eşikler:
- Her madde: 0 (pass) / 1 (minor issue) / 2 (major issue)
- Toplam skor 0–16

Gate mantığı:
- **0–2**: `QA_PASS`
- **3–5**: `QA_CONDITIONAL_PASS` (zorunlu düzeltme sonrası yeniden gate)
- **6+**: `QA_FAIL_BLOCK`

---

## 11) Severity Scoring ve PASS/FAIL Mantığı

### 11.1 Severity Seviyeleri
- **S0 (Info)**: operasyonel not, bloklama yok.
- **S1 (Minor)**: kalite iyileştirmesi, release öncesi düzeltilebilir.
- **S2 (Major)**: yüksek kalite riski, zorunlu düzeltme gerekir.
- **S3 (Critical)**: marka/gerçeklik/policy ihlali, anında block.

### 11.2 PASS/FAIL Motoru

- `PASS`: Validation + Enforcement + Simulation + QA tamamı geçer.
- `FAIL_SOFT`: En az bir S1/S2 bulgu var, remediation sonrası tekrar test gerekir.
- `FAIL_HARD`: En az bir S3 bulgu var; production release yasak.

---

## 12) Production Blocking Kuralları

Aşağıdaki koşullarda otomatik blok uygulanır:
- Fake data/fake metric tespiti
- Rakip metninin kopya/çok benzer kullanımı
- Premium tonun bozulması (cheap/commercial dil)
- Uydurma Meta targeting claim
- Visual realism lock ihlali
- QA score >= 6
- Herhangi bir `HARD_FAIL`

Block kodu örnekleri:
- `PB-FAKE-001`
- `PB-TONE-002`
- `PB-META-003`
- `PB-VISUAL-004`

---

## 13) Fail-Safe Procedures

1. **Data Missing Fail-Safe**: Bilinmeyen ürün verisi `requires verification` olarak işaretlenir.
2. **Channel Degrade Mode**: Reels başarısızsa önce Story-safe output’a degrade edilir.
3. **Language Safety Fallback**: Aşırı satış tonu tespitinde editorial kısa forma dönülür.
4. **Release Hold Mode**: Kritik belirsizlikte otomatik hold + insan onayı zorunlu.
5. **Rollback Package**: Yayına alınmış içerikte kritik risk bulunursa son güvenli versiyona dönülür.

---

## 14) Escalation Procedures

Escalation matrix:

- **Level 1 (Operator Fix)**: S1 sorunlar
- **Level 2 (Controller Review)**: S2 sorunlar
- **Level 3 (Production Council)**: S3 sorunlar

Escalation tetikleyicileri:
- 2 ardışık `FAIL_SOFT`
- 1 adet `FAIL_HARD`
- Kampanya takvimine 72 saatten az kalmış kritik issue

Escalation çıktısı:
- Go / No-Go kararı
- Düzeltme owner ataması
- Yeniden test takvimi

---

## 15) Production Release Logic

Release kararı yalnızca şu durumda verilir:

`VAL_PASS` + `ENF_PASS` + `SIM_PASS` + `QA_PASS` + `AUDIT_CLEAR`

Release tipleri:
- **Full Release**: Tüm kanallara yayın
- **Staged Release**: Önce düşük riskli kanallarda yayın
- **Shadow Release**: Görünmez test/log-only

Post-release zorunlu:
- 24 saat kalite izlemesi
- anomaly log taraması
- gerekiyorsa hotfix route

---

## 16) Workflow SOP’ları

## 16.1 Single Product Workflow

1. Product intake
2. Product analysis (9-lens zorunlu)
3. Caption/Story/Reels taslakları
4. Boutique + U.S. city fit eşlemesi
5. Meta ad note üretimi
6. Validation/Enforcement/Simulation/QA
7. Release

Çıktı paketleri:
- Instagram caption
- Story copy
- Reels structure
- Hashtag discipline set
- Boutique fit note
- City fit note
- Meta ads logic
- Final QA note

## 16.2 Campaign Workflow

1. Campaign brief intake
2. Theme + objective netleştirme
3. Asset matrix planlama
4. Channel split (Feed/Story/Reels/Ads)
5. Message hierarchy
6. Quality gates
7. Release calendar

## 16.3 Story Workflow

1. Narrative arc (3–5 frame)
2. Minimal copy crafting
3. Soft direction CTA check
4. Tone enforcement
5. QA mini-gate
6. Publish

## 16.4 Reels Workflow

1. Hook type selection
2. Scene sequencing
3. Material movement emphasis
4. Music mood alignment (hak yönetimine dikkat)
5. On-screen text restraint
6. QA + simulation
7. Publish

## 16.5 Meta Ad Workflow

1. Offer/context tanımı
2. Audience segmentation:
   - searchable interests
   - luxury behavioral signals
   - strategic audience signals
3. Creative angle map
4. Compliance check (no fake targeting claims)
5. A/B logic
6. Pre-launch QA
7. Controlled launch

## 16.6 Boutique Workflow

1. Boutique archetype seçimi
2. Product-boutique fit scoring
3. Climate & city relevance
4. Assortment recommendation
5. Communication style alignment
6. QA
7. Distribution note release

## 16.7 Product Analysis Workflow

Zorunlu 9 katman:
1. Product Character
2. Material Reading
3. Silhouette Reading
4. Seasonal Fit
5. Boutique Fit
6. U.S. City Fit
7. Meta Ads Logic
8. Instagram Positioning
9. Final QA Check

## 16.8 Seasonal Campaign Workflow

1. Sezon stratejisi (SS/FW)
2. Material priority plan
3. Visual world board
4. Channel roll-out order
5. Risk simulation (weather, timing, demand)
6. QA + staged release

## 16.9 Bridal Campaign Workflow

1. Bridal capsule narrative
2. Femininity restraint check
3. Occasion matrix (engagement, after-party, reception)
4. Boutique bridal fit
5. Tone lock (no mass bridal language)
6. QA + release

## 16.10 Holiday Campaign Workflow

1. Holiday context definition
2. Gifting vs eveningwear split
3. Luxury restraint enforcement
4. CTA softness calibration
5. Risk check (over-commercialization)
6. QA + release

## 16.11 Competitor Intelligence Workflow

1. Reference house selection
2. Signal extraction (silhouette/material/tone)
3. Copy-risk filtering
4. Differentiation synthesis
5. Strategic insight note
6. Non-copy compliance gate

## 16.12 Fashion Media Intelligence Workflow

1. Media source qualification
2. Trend signal scoring
3. Brand-fit relevance mapping
4. Noise elimination
5. Insight-to-campaign translation
6. Release eligibility check (insight only / actionable)

---

## 17) Operatör Kullanım Protokolü

Operatör her görevde:
1. Brief’i normalize eder.
2. Eksik veri varsa `requires verification` etiketi koyar.
3. İlgili workflow’u tetikler.
4. Pipeline durumlarını takip eder.
5. FAIL durumunda remediation döngüsünü yönetir.
6. PASS durumunda release talebi açar.

Zorunlu log alanları:
- Request ID
- Workflow ID
- Route decision
- Severity summary
- QA score
- Release decision

---

## 18) Pipeline Hareketi (Output Flow)

`Input -> Router -> Generator -> Validator -> Enforcement -> Simulation -> QA Gate -> Release Manager -> Audit Archive`

Her geçişte paket yapısı:
- payload
- metadata
- decision flags
- severity map
- trace timestamp

Bu yapı gelecekte API orkestrasyonuna doğrudan uygundur.

---

## 19) Routing Decision Mantığı

Routing kararında kullanılan öncelik sırası:
1. İş türü
2. Kanal
3. Zaman bağlamı
4. Risk düzeyi
5. Veri güven skoru

Karar modeli deterministic rule-set’tir; black-box karar yasaktır.

---

## 20) Simulation Trigger Kuralları

Simulation şu durumlarda otomatik tetiklenir:
- Yeni campaign tipi
- Bridal/Holiday kritik dönem yayını
- S2 veya üzeri issue geçmişi
- Multi-channel release
- Yeni otomasyon entegrasyonu

Manual trigger:
- QA gatekeeper veya release manager talebi

---

## 21) Automation Compatibility Standard

Otomasyon uyumluluğu için zorunlu:
- Sabit stage isimleri
- Makine okunabilir PASS/FAIL kodları
- Severity enum standardı (S0–S3)
- Deterministic routing rules
- Idempotent retry davranışı
- Audit log schema uyumu

API-ready prensipler:
- Stateless task invocation
- Versioned schema
- Explicit error contracts
- Reproducible simulation runs

---

## 22) Değişiklik Yönetimi

Bu playbook’taki her revizyon:
1. Version increment alır.
2. Changelog’a işlenir.
3. Simulation regression testi görür.
4. QA council onayı olmadan production’a alınmaz.

---

## 23) Kapanış Kuralı

Bu playbook Kerime Ataker Production OS için **resmi işletim standardıdır**.  
PASS disiplini, luxury positioning korunumu ve no-fabrication ilkesi non-negotiable’dır.
