# KERIME ATAKER OUTPUT ENFORCEMENT ENGINE (KOEE)

## 0) PURPOSE AND POSITION IN SYSTEM HIERARCHY

KOEE, Kerime Ataker Operating System (KA-OS) içinde **zorunlu uyum (compliance) katmanı** olarak çalışır.
Bu modülün amacı, üretilen tüm metinlerin:

- premium/luxury tonunu koruması,
- marka dışı dil, ucuz satış dili ve yapay iddialardan arındırılması,
- çıktı formatlarının tutarlı, ölçeklenebilir ve doğrulanabilir olmasını sağlamasıdır.

KOEE; marka sistemi, ürün kuralları, Instagram sistemi, Meta Ads sistemi ve Final QA sistemi ile **kanonik olarak uyumlu** olmalıdır.

---

## 1) ENFORCEMENT ARCHITECTURE

KOEE enforcement akışı:

1. **Input Intake Layer**
   - Görev tipi algılama (caption, campaign, product analysis, ads note, operator answer).
   - Dil kontrolü (operasyonel açıklama: TR, brand-facing text: EN).

2. **Structural Validation Layer**
   - Zorunlu bölüm/başlık varlığı kontrolü.
   - Output hierarchy sırası kontrolü.

3. **Tone & Lexicon Enforcement Layer**
   - Forbidden wording taraması.
   - Luxury-breaking phrase tespiti.
   - CTA/CTI güvenlik kontrolü.

4. **Context & Logic Validation Layer**
   - Seasonal mismatch detection.
   - Campaign structure validation.
   - Boutique/U.S. city fit tutarlılık kontrolü.

5. **Evidence & Data Integrity Layer**
   - Fake data detection.
   - Unverified claim blocking.
   - Evidence tag doğrulaması.

6. **Output Sanitization & Schema Layer**
   - Hashtag policy enforcement.
   - JSON schema uyumluluk hazırlığı.

7. **Final QA Gate**
   - Release/no-release kararı.
   - Hata kodu + düzeltme önerisi üretimi.

---

## 2) FORBIDDEN WORDING SYSTEM

### 2.1 Wording Severity Model

- **FATAL**: Yayın engellenir.
- **MAJOR**: Revizyon zorunlu.
- **MINOR**: Stil revizyonu önerilir.

### 2.2 Forbidden Categories

1. **Mass-market / cheap urgency language** (FATAL)
   - Örn: “cheap”, “budget luxury”, “discount queen”, “must-buy now”.

2. **Spam conversion language** (FATAL)
   - Örn: “buy now!!!”, “limited stock hurry”, “don’t miss out girls”.

3. **Overt lingerie-first framing** (MAJOR/FATAL bağlama göre)
   - Ürünü yalnızca provokatif iç giyim diliyle sunma.

4. **Trend-chasing low authority wording** (MAJOR)
   - Örn: “viral look”, “TikTok made me buy it”, “it-girl dupe”.

5. **Fabrication-trigger wording** (FATAL)
   - Örn: “best seller of the year” (kanıtsız), “highest conversion product” (kanıtsız).

### 2.3 Enforcement Rule

- Forbidden phrase sözlüğü regex + phrase-list ile taranır.
- FATAL eşleşme varsa output **reject** edilir.
- MAJOR eşleşmede otomatik rewrite önerisi üretilir.

---

## 3) BANNED LUXURY-BREAKING PHRASES

Aşağıdaki kalıplar luxury positioning’i düşürdüğü için yasaktır:

- “affordable luxury”
- “cheap chic”
- “dupe”
- “budget alternative”
- “must-have deal”
- “flash sale vibe”
- “hot girl fit” (brand tone dışı kullanımda)
- “sexy for less”
- “mass favorite”
- “everyday basic everyone needs”

**Rule:** Bu ifadeler doğrudan veya yakın varyantlarla geçtiğinde FATAL/MAJOR flag üret.

---

## 4) CTA / CTI VALIDATION RULES

### 4.1 CTA Policy

Yalnızca “soft direction” kabul edilir.

**Allowed CTA patterns (EN):**
- “Discover the silhouette.”
- “Explore the piece.”
- “View details.”
- “Experience the texture in motion.”

**Blocked CTA patterns:**
- “Buy now”
- “Shop now before it’s gone”
- “Order today”
- “Click fast”

### 4.2 CTI (Call-to-Intent) Policy

CTI, agresif satış değil; estetik niyete yönlendirme olmalıdır.

**Allowed CTI intents:**
- material appreciation
- silhouette attention
- evening context framing
- editorial aura building

**Validation:**
- Maksimum 1 CTA/CTI bloğu.
- Ünlem yoğunluğu >1 ise MAJOR.
- Caps-lock satış dili varsa FATAL.

---

## 5) OUTPUT HIERARCHY ENFORCEMENT

KOEE, aşağıdaki sıralamanın bozulmasına izin vermez:

1. Product Character
2. Material Reading
3. Silhouette Reading
4. Seasonal Fit
5. Boutique Fit
6. U.S. City Fit
7. Meta Ads Logic
8. Instagram Positioning
9. Final QA Check

**Rule:**
- Product analysis çıktısında 9 bölümün tamamı zorunludur.
- Eksik bölüm varsa `STRUCTURE_MISSING_SECTION` hatası döndürülür.

---

## 6) CAMPAIGN STRUCTURE VALIDATION

Her campaign output minimum şu bileşenleri içermelidir:

- Campaign objective (positioning/consideration/conversion)
- Channel mapping (IG feed/story/reels + web intent)
- Creative angle (material / silhouette / mood)
- Audience logic (searchable interests + behavioral + strategic signals)
- Measurement note (yalnızca doğrulanabilir metrik dili)

**Invalid cases:**
- Objective yok
- Kanal eşleşmesi yok
- Meta audience kategorileri ayrıştırılmamış
- Abartılı performans iddiaları var

---

## 7) SEASONAL MISMATCH DETECTION

### 7.1 Detection Inputs

- Ürün materyali (leather/fur/silk/satin)
- Silhouette yoğunluğu
- Kampanya tarihi/sezonu
- U.S. city iklim bağlamı

### 7.2 Flags

- `SEASONAL_MISMATCH_MINOR`: Geçiş sezonunda şartlı kullanılabilir.
- `SEASONAL_MISMATCH_MAJOR`: Sezon ve materyal ciddi uyumsuz.

### 7.3 Examples

- Ağır fur outerwear + peak summer Miami daytime push => MAJOR
- Satin evening silhouette + spring gala context => PASS

---

## 8) EVIDENCE VALIDATION LAYER

Her iddia aşağıdaki etiketlerden biriyle gelmelidir:

- `VERIFIED_SOURCE`
- `INTERNAL_RULE`
- `REQUIRES_VERIFICATION`

**Rule-set:**
- Kaynaksız performans iddiası yasak.
- “Best performing”, “top city”, “highest CTR” gibi cümleler evidence etiketi olmadan kullanılamaz.
- Belirsizse otomatik olarak `REQUIRES_VERIFICATION` atanır.

---

## 9) PROHIBITED FAKE-DATA DETECTION

### 9.1 Hard Ban

Aşağıdakiler kanıtsızsa FATAL:
- sahte Instagram growth yüzdeleri
- uydurma ROAS/CTR/CVR değerleri
- doğrulanmamış satış adetleri
- “viral reach” gibi metrik benzeri ama kaynaksız iddialar

### 9.2 Detection Signals

- Sayısal claim + source yok
- “industry average” referansı + kaynak yok
- “customer data shows” + dataset yok

### 9.3 Enforcement

- Output redline edilir.
- İddia kaldırılır veya `requires verification` ile yeniden yazılır.

---

## 10) HASHTAG VALIDATION RULES

### 10.1 Core Constraints

- Spam hashtag blokları yasak.
- Genel pop hashtag (“#love #fashion #instagood”) yoğunluğu yasak.
- Marka tonu ile uyumsuz pop kültür hashtagleri yasak.

### 10.2 Quality Policy

- Hashtag seti niş + premium bağlamsal olmalı.
- Önerilen bant: 3–8 adet.
- Aynı hashtag tekrar edemez.
- Caption’ın aura yapısını bozacak yoğunlukta olmamalı.

### 10.3 Fail Conditions

- >10 hashtag => MAJOR
- spam/jenerik set => MAJOR/FATAL bağlama göre
- agresif satış etiketi => FATAL

---

## 11) OPERATOR OUTPUT DISCIPLINE

## 11.1) SOCIAL OUTPUT EXPANSION LOCK (SOEL)

KOEE, sosyal üretim çıktılarında **COMPLETE SOCIAL EXECUTION FORMAT** zorunluluğunu uygular.

### 11.1.1 Mandatory Completion Rule

Bir sosyal üretim çıktısı aşağıdaki bölümlerin tamamını içermiyorsa output `INVALID_SOCIAL_INCOMPLETE` olarak reddedilir:

1. `POST`
   - posting time
   - caption
   - hashtags
2. `STORY`
   - story 1 text
   - story 2 text
   - link sticker text
   - story timing
3. `REELS`
   - 15-second reels structure
   - reels overlay texts
   - reels caption
   - reels hashtags
   - reels timing
4. `META_DEPLOYMENT`
   - Meta objective
   - campaign type
   - deployment logic
   - warm/cold/retargeting logic
5. `TARGETING`
   - primary U.S. cities
   - state targeting
   - luxury radius strategy
   - interests
   - behaviors
   - strategic audience signals
6. `POSITIONING`
   - boutique fit
   - seasonal fit
   - occasion fit
   - luxury positioning logic
7. `QA`
   - spam control
   - aggressive CTA control
   - luxury tone validation
   - competitor-copy prevention
   - Meta safety validation

### 11.1.2 Early Stop Prohibition

KOEE aşağıdaki durumda hard fail üretir:

- Output yalnızca caption ile biter.
- Output yalnızca product analysis ile biter.
- Output yalnızca operator summary ile biter.

Bu durumda sistem `FORCE_CONTINUE_SOCIAL_SECTIONS` sinyali ile üretimi zorunlu olarak devam ettirir.

### 11.1.3 Validation Error Codes

- `INVALID_SOCIAL_INCOMPLETE`
- `MISSING_POST_BLOCK`
- `MISSING_STORY_BLOCK`
- `MISSING_REELS_BLOCK`
- `MISSING_META_DEPLOYMENT_BLOCK`
- `MISSING_TARGETING_BLOCK`
- `MISSING_POSITIONING_BLOCK`
- `MISSING_QA_BLOCK`
- `EARLY_STOP_DETECTED`

- Operasyonel anlatım dili: **Türkçe**.
- Brand-facing text: **İngilizce**.
- Gereksiz uzunluk, tekrar, belirsiz jargon yasak.
- Her karar cümlesi rule-grounded olmalı.
- “Tahmin” ile “doğrulanmış bilgi” açık biçimde ayrılmalı.

---

## 12) LUXURY TONE ENFORCEMENT

### 12.1 Tone Anchors

- premium
- controlled
- feminine
- refined
- cinematic
- editorial
- emotionally restrained
- material-focused

### 12.2 Tone Violations

- bağıran satış dili
- emoji aşırılığı
- sokak dili / ucuz hype dili
- aşırı flörtöz ya da kaba çağrı dili

### 12.3 Rewrite Policy

Tone ihlallerinde sistem:
1. düşük kalite ifadeyi işaretler,
2. editorial ve materyal odaklı alternatif üretir,
3. aura-first, product-second düzenini korur.

---

## 13) JSON SCHEMA PREPARATION LAYER

KOEE, gelecekte otomasyon için aşağıdaki şemayı hazırlar:

```json
{
  "output_type": "product_analysis | caption | campaign | ads_note",
  "language": {
    "operational": "tr",
    "brand_facing": "en"
  },
  "structure": {
    "required_sections": [],
    "missing_sections": []
  },
  "tone_validation": {
    "status": "pass | fail",
    "violations": []
  },
  "forbidden_wording": {
    "fatal_hits": [],
    "major_hits": []
  },
  "cta_cti": {
    "status": "pass | fail",
    "notes": []
  },
  "seasonal_check": {
    "status": "pass | minor | major",
    "reason": ""
  },
  "evidence": {
    "unsupported_claims": [],
    "requires_verification": []
  },
  "hashtags": {
    "count": 0,
    "status": "pass | fail",
    "issues": []
  },
  "final_decision": "release | revise | reject"
}
```

Not: Bu şema, API veya workflow engine entegrasyonu için canonical contract olarak kullanılmalıdır.

---

## 14) FINAL QA CHECKLIST (RELEASE GATE)

Çıkış öncesi zorunlu checklist:

1. Tone premium ve restrained mi?
2. Forbidden wording var mı?
3. CTA/CTI soft-direction sınırında mı?
4. 9 katman product analysis hiyerarşisi tam mı?
5. Seasonal fit mantıklı mı?
6. Boutique ve U.S. city fit uyumlu mu?
7. Evidence etiketsiz claim var mı?
8. Fake data veya uydurma metrik var mı?
9. Hashtag seti premium ve spam-dışı mı?
10. Final karar doğru mu? (release / revise / reject)

**Gate policy:**
- Herhangi bir FATAL => `reject`
- MAJOR sayısı ≥2 => `revise`
- FATAL yok, MAJOR ≤1 ve yapı tam => `release`

---

## 15) ERROR CODE MAP (CANONICAL)

- `STRUCTURE_MISSING_SECTION`
- `FORBIDDEN_WORDING_FATAL`
- `LUXURY_TONE_BREAK`
- `CTA_AGGRESSIVE_SALES`
- `CAMPAIGN_LOGIC_INCOMPLETE`
- `SEASONAL_MISMATCH_MAJOR`
- `EVIDENCE_MISSING`
- `FAKE_DATA_DETECTED`
- `HASHTAG_SPAM_PATTERN`
- `LANGUAGE_POLICY_VIOLATION`

Bu hata kodları, KA-OS içinde standart enforcement telemetry olarak kullanılmalıdır.
