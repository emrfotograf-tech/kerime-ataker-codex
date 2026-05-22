# KERIME ATAKER OPERATOR OUTPUT SCHEMA (KAOOS)

Version: 1.0.0  
Status: Canonical / Production  
Scope: All operator outputs in this repository and future automation pipelines.

---

## 1) AMAÇ VE KAPSAM

Bu şema, Kerime Ataker için üretilen **tüm operatör çıktılarını** tek bir kanonik yapıda standardize eder.

Kapsanan çıktı tipleri:
- Single product outputs
- Campaign outputs
- Story outputs
- Reels outputs
- Meta ad outputs
- Boutique outputs
- U.S. city fit outputs
- Competitor intelligence outputs
- Fashion media intelligence outputs
- Product analysis outputs
- Special day campaign outputs

Bu doküman:
- mimari seviye (architecture-level)
- ölçeklenebilir (scalable)
- üretim kalitesi (production-grade)
- otomasyon uyumlu (pipeline-compatible)
olarak tasarlanmıştır.

---

## 2) TEMEL PRENSİPLER

1. **Operasyon dili Türkçe, marka-facing metin İngilizce.**
2. **Doğrulanmamış veri yok.** Varsayım yapıldığında açıkça etiketlenir.
3. **Aura first, product second.** Satış baskısı yasaktır.
4. **Luxury restraint zorunlu.** Spam, agresif CTA, ucuz ton yasak.
5. **Her çıktı final QA kapısından geçer.**

---

## 3) ZORUNLU ÇIKTI HİYERARŞİSİ (GLOBAL ORDER)

Her çıktı aşağıdaki üst akış sırasını korumalıdır:

1. `ÇIKTI_KİMLİĞİ`
2. `GİRDİ_DOĞRULAMA_DURUMU`
3. `OPERATÖR_ÖZETİ`
4. `ANA_MODÜL` (çıktı tipine göre değişen ana gövde)
5. `MARKA_METNİ_İNGİLİZCE`
6. `META_NOTU`
7. `KANIT_ETİKETLERİ`
8. `FINAL_QA_KAPISI`

Sıra değiştirilemez.

---

## 4) ZORUNLU TÜRKÇE OPERATÖR BAŞLIKLARI

Aşağıdaki başlık adları **exact-match** olmalıdır:

- `ÇIKTI_KİMLİĞİ`
- `GİRDİ_DOĞRULAMA_DURUMU`
- `OPERATÖR_ÖZETİ`
- `ÜRÜN_ANALİZİ`
- `KAMPANYA_İSKELETİ`
- `STORY_AKIŞI`
- `REELS_ZAMAN_AKISI`
- `META_REKLAM_NOTU`
- `BOUTIQUE_UYUMU`
- `ABD_ŞEHİR_UYUMU`
- `RAKİP_ZEKASI`
- `MODA_MEDYA_ZEKASI`
- `CTA_CTI_YERLEŞİMİ`
- `ZAMANLAMA_PLANI`
- `ETİKET_SİSTEMİ`
- `SEZON_UYUM_KONTROLÜ`
- `OCCASION_UYUM_KONTROLÜ`
- `LÜKS_TON_KORUMA_KONTROLÜ`
- `ANTI_SPAM_DİL_KONTROLÜ`
- `FINAL_QA_KAPISI`

Not: Tüm çıktılarda tüm başlıklar zorunlu değildir; fakat kullanılan başlık adı bu listedeki canonical isimlerden seçilmelidir.

---

## 5) İNGİLİZCE MARKA-FACING COPY ZONELARI

Aşağıdaki alanlarda **yalnızca İngilizce** kullanılabilir:

- `BRAND_COPY.CAPTION`
- `BRAND_COPY.STORY_TEXT`
- `BRAND_COPY.REELS_ONSCREEN_TEXT`
- `BRAND_COPY.REELS_VOICEOVER`
- `BRAND_COPY.CTA`
- `BRAND_COPY.CTI`
- `BRAND_COPY.HASHTAGS`

Operatör açıklaması, analiz, doğrulama ve QA katmanları Türkçe kalır.

---

## 6) YASAK FORMATLAR

Aşağıdakiler yasaktır:

1. Başlıksız serbest metin blokları.
2. Operatör katmanında emoji yoğunluğu (maksimum 1 uyarı emojisi).
3. Tamamı büyük harf satış metni (`BUY NOW`, `LIMITED!!!` vb.).
4. 3’ten fazla ünlem (`!!!`) veya hype kalıpları.
5. Spam hashtag yığını (tek satırda 20+ hashtag).
6. Doğrulanmamış metrik/claim (`best seller`, `viral`, `top-converting`) etiketsiz kullanımı.
7. Rakip metninin birebir kopyası.

---

## 7) HASHTAG YERLEŞİM KURALI

- Hashtag sadece `BRAND_COPY.HASHTAGS` alanında verilir.
- Caption gövdesine gömülmez.
- Önerilen aralık: 3–8 adet.
- Spam veya jenerik kitle çağrısı etiketleri yasak (`#followforfollow`, `#instagood` tipi).
- Hashtag seti ürün/malzeme/siluet/şehir bağlamına bağlı olmalıdır.

---

## 8) STORY YAPISI KURALI

`STORY_AKIŞI` aşağıdaki sırayı izler:

1. `Frame_01_Aura`
2. `Frame_02_Material`
3. `Frame_03_Silhouette`
4. `Frame_04_Direction` (soft CTA/CTI)

Her frame için zorunlu alanlar:
- `Amaç` (TR)
- `OnScreenText` (EN)
- `VisualCue` (TR)
- `Interaction` (EN, optional: poll/slider/question)

---

## 9) REELS ZAMAN AKIŞI KURALI

`REELS_ZAMAN_AKISI` timecode formatı:

- `00:00-00:02 Hook Aura`
- `00:02-00:05 Material Detail`
- `00:05-00:08 Silhouette Motion`
- `00:08-00:12 Direction Close`

Her segment için:
- `Amaç` (TR)
- `VisualAction` (TR)
- `OnScreenText` (EN)
- `Voiceover` (EN, optional)
- `EditNote` (TR)

---

## 10) META NOTU FORMATI

Meta önerileri yalnızca `META_REKLAM_NOTU` içinde ve üçe ayrılmış şekilde yazılır:

1. `SearchableInterests`  
2. `LuxuryBehaviorSignals`  
3. `StrategicAudienceSignals`

Kurallar:
- Platformda varlığı doğrulanmamış hedefleme ifadesi yazılamaz.
- Tahmin alanı gerekiyorsa `AssumptionFlag: true` ile işaretlenir.
- Delivery/ROAS iddiası verilmez.

---

## 11) CTA / CTI GÖMME KURALI

`CTA_CTI_YERLEŞİMİ` şunu zorunlu kılar:

- `CTA` = eylem çağrısı (soft, low-pressure)
- `CTI` = interaction çağrısı (save/share/reply/poll)

Yerleşim:
- Caption sonunda en fazla 1 CTA.
- Story’de en fazla 1 CTI öğesi/frame.
- Reels’te son 3 saniyede tek CTA veya tek CTI.

Yasak CTA örnekleri:
- “BUY NOW!!!”
- “LAST CHANCE HURRY”
- “DON’T MISS OUT” (agresif kullanım)

---

## 12) YASAK GTA TERMINOLOJİSİ

Aşağıdaki “growth-hack / cheap urgency” terminolojisi yasaktır:

- hack, growth hack, conversion trick
- funnel crush, force conversion
- cheap win, quick flip
- mass blast, spam drop
- hard sell push

---

## 13) KAMPANYA ZAMANLAMA YAPISI

`ZAMANLAMA_PLANI` formatı:

- `T-14 / T-10 / T-7`: tease and material world
- `T-5 / T-3`: silhouette and occasion framing
- `T-2 / T-1`: editorial proximity and reminder
- `T0`: release post
- `T+1 / T+3`: continuation + social proof (verified only)

Her satır alanları:
- `Phase`
- `Objective`
- `PrimaryChannel`
- `AssetType`
- `CopyAngle`
- `VerificationNeed`

---

## 14) ÜRÜN DOĞRULAMA GEREKSİNİMLERİ

`GİRDİ_DOĞRULAMA_DURUMU` zorunlu alanları:

- `ProductNameVerified` (bool)
- `MaterialVerified` (bool)
- `PriceVerified` (bool/na)
- `AvailabilityVerified` (bool/na)
- `SourceList` (URL or internal ref)

---

## 14.1) COMPLETE SOCIAL EXECUTION FORMAT ZORUNLULUĞU

Sosyal üretim çıktılarında aşağıdaki yürütme bloklarının **tamamı zorunludur**:

1. `POST`
   - `posting_time`
   - `caption`
   - `hashtags`
2. `STORY`
   - `story_1_text`
   - `story_2_text`
   - `link_sticker_text`
   - `story_timing`
3. `REELS`
   - `reels_15s_structure`
   - `reels_overlay_texts`
   - `reels_caption`
   - `reels_hashtags`
   - `reels_timing`
4. `META_DEPLOYMENT`
   - `meta_objective`
   - `campaign_type`
   - `deployment_logic`
   - `warm_cold_retargeting_logic`
5. `TARGETING`
   - `primary_us_cities`
   - `state_targeting`
   - `luxury_radius_strategy`
   - `interests`
   - `behaviors`
   - `strategic_audience_signals`
6. `POSITIONING`
   - `boutique_fit`
   - `seasonal_fit`
   - `occasion_fit`
   - `luxury_positioning_logic`
7. `QA`
   - `spam_control`
   - `aggressive_cta_control`
   - `luxury_tone_validation`
   - `competitor_copy_prevention`
   - `meta_safety_validation`

### 14.1.1 Erken Bitirme Yasağı

Aşağıdaki outputlar geçersizdir:
- sadece caption ile biten output
- sadece product analysis ile biten output
- sadece operatör özeti ile biten output

Kural: Bu kısmi formatlar `INVALID_SOCIAL_OUTPUT_FORMAT` olarak işaretlenir ve yayın hattına alınamaz.
- `MissingData` (array)

Eksik veri varsa:
- Çıktı devam edebilir, ancak ilgili claim alanları `requires_verification` etiketlenmelidir.

---

## 15) KANIT ETİKETLEME SİSTEMİ

`ETİKET_SİSTEMİ` canonical evidence tags:

- `[VERIFIED_SOURCE]`
- `[INTERNAL_ARCHIVE]`
- `[OBSERVATIONAL_INFERENCE]`
- `[REQUIRES_VERIFICATION]`
- `[NO_PUBLIC_DATA]`

Kural:
- Her kritik iddia en az bir etiket taşır.
- Etiketsiz kritik claim üretilemez.

---

## 16) LÜKS TON KORUMA KURALI

`LÜKS_TON_KORUMA_KONTROLÜ` aşağıyı doğrular:

1. Premium, kontrollü, rafine dil var mı?
2. Aşırı iddia/satış baskısı var mı?
3. Editorial atmosfer korunuyor mu?
4. Malzeme ve yapı odağı korunuyor mu?
5. Fast-fashion tınısı engellendi mi?

Sonuç formatı:
- `Status: pass|revise`
- `Violations: []`
- `RevisionNote`

---

## 17) ANTI-SPAM DİL ZORLAMASI

`ANTI_SPAM_DİL_KONTROLÜ` yasak dil örüntüleri:

- “must have now”, “crazy deal”, “insane drop”
- clickbait soru dizileri
- manipülatif scarcity (doğrulamasız)
- aşırı tekrar eden satış fiilleri

Çıktı bu kalıpları içeriyorsa otomatik `revise`.

---

## 18) SEZON VE OCCASION UYUM DOĞRULAMASI

### `SEZON_UYUM_KONTROLÜ`
- `SeasonClaim`
- `ClimateLogic`
- `MaterialLogic`
- `Status`

### `OCCASION_UYUM_KONTROLÜ`
- `OccasionType` (evening, bridal-intimate, event dinner, etc.)
- `FormalityLevel`
- `StylingLogic`
- `Status`

---

## 19) BOUTIQUE VE ABD LÜKS ŞEHİR FORMATI

### `BOUTIQUE_UYUMU`
Zorunlu alanlar:
- `BoutiqueProfile`
- `MerchandisingFit`
- `ClientType`
- `PriceSensitivityNote` (no fabricated data)
- `Status`

### `ABD_ŞEHİR_UYUMU`
Zorunlu alanlar:
- `City`
- `LuxuryContext`
- `ClimateOccasionLink`
- `ConsumerSignal` (verified/inference-tagged)
- `Status`

---

## 20) MODÜL BAZLI ZORUNLU ALAN MATRİSİ

| Output Type | Required Modules |
|---|---|
| Single Product | ÜRÜN_ANALİZİ, BRAND_COPY, BOUTIQUE_UYUMU, ABD_ŞEHİR_UYUMU, FINAL_QA_KAPISI |
| Campaign | KAMPANYA_İSKELETİ, ZAMANLAMA_PLANI, BRAND_COPY, META_REKLAM_NOTU, FINAL_QA_KAPISI |
| Story | STORY_AKIŞI, BRAND_COPY.STORY_TEXT, CTA_CTI_YERLEŞİMİ, FINAL_QA_KAPISI |
| Reels | REELS_ZAMAN_AKISI, BRAND_COPY.REELS_ONSCREEN_TEXT, CTA_CTI_YERLEŞİMİ, FINAL_QA_KAPISI |
| Meta Ad | META_REKLAM_NOTU, BRAND_COPY, ETİKET_SİSTEMİ, FINAL_QA_KAPISI |
| Boutique | BOUTIQUE_UYUMU, ETİKET_SİSTEMİ, FINAL_QA_KAPISI |
| U.S. City Fit | ABD_ŞEHİR_UYUMU, SEZON_UYUM_KONTROLÜ, FINAL_QA_KAPISI |
| Competitor Intelligence | RAKİP_ZEKASI, ETİKET_SİSTEMİ, LÜKS_TON_KORUMA_KONTROLÜ, FINAL_QA_KAPISI |
| Fashion Media Intelligence | MODA_MEDYA_ZEKASI, ETİKET_SİSTEMİ, FINAL_QA_KAPISI |
| Product Analysis | ÜRÜN_ANALİZİ (9-layer), SEZON_UYUM_KONTROLÜ, OCCASION_UYUM_KONTROLÜ, FINAL_QA_KAPISI |
| Special Day Campaign | KAMPANYA_İSKELETİ, ZAMANLAMA_PLANI, STORY_AKIŞI/REELS_ZAMAN_AKISI, FINAL_QA_KAPISI |

---

## 21) ÜRÜN ANALİZİ — 9 KATMAN ZORUNLULUĞU

`ÜRÜN_ANALİZİ` aşağıdaki sırada olmalıdır:

1. `ProductCharacter`
2. `MaterialReading`
3. `SilhouetteReading`
4. `SeasonalFit`
5. `BoutiqueFit`
6. `USCityFit`
7. `MetaAdsLogic`
8. `InstagramPositioning`
9. `FinalQACheck`

---

## 22) FINAL QA KAPISI (RELEASE GATE)

`FINAL_QA_KAPISI` geçiş checklist’i:

- `ToneCheck`
- `RealismCheck`
- `LuxuryConsistencyCheck`
- `SeasonalLogicCheck`
- `BoutiqueCompatibilityCheck`
- `DuplicationCheck`
- `OverSellingCheck`
- `FakeClaimCheck`

Çıkış:
- `GateStatus: pass|revise|block`
- `BlockingIssues`
- `RequiredEdits`

`GateStatus != pass` ise brand-facing final metin yayınlanamaz.

---

## 23) OTOMASYON UYUMLULUĞU (PIPELINE CONTRACT)

Bu doküman aşağıdaki otomasyon ihtiyaçlarına uyumludur:

- deterministic heading parsing
- module-level validation
- evidence-tag linting
- language-zone enforcement (TR vs EN)
- CTA/CTI policy lint
- anti-spam lexicon scanning
- QA gate blocking logic

Önerilen entegrasyon:
- JSON dönüştürücü katmanında heading-to-key mapping
- preflight validator
- post-generation QA validator

---

## 24) MINIMUM CANONICAL SKELETON (TEMPLATE)

```md
ÇIKTI_KİMLİĞİ
- OutputType:
- Version: KAOOS-1.0.0
- TimestampUTC:

GİRDİ_DOĞRULAMA_DURUMU
- ProductNameVerified:
- MaterialVerified:
- PriceVerified:
- AvailabilityVerified:
- SourceList:
- MissingData:

OPERATÖR_ÖZETİ
- Amaç:
- Kapsam:
- RiskNotu:

ANA_MODÜL
- (Output type-specific canonical module blocks)

MARKA_METNİ_İNGİLİZCE
- BRAND_COPY.CAPTION:
- BRAND_COPY.STORY_TEXT:
- BRAND_COPY.REELS_ONSCREEN_TEXT:
- BRAND_COPY.REELS_VOICEOVER:
- BRAND_COPY.CTA:
- BRAND_COPY.CTI:
- BRAND_COPY.HASHTAGS:

META_NOTU
- (if applicable)

KANIT_ETİKETLERİ
- Claim_01: [VERIFIED_SOURCE]
- Claim_02: [OBSERVATIONAL_INFERENCE]

FINAL_QA_KAPISI
- GateStatus:
- BlockingIssues:
- RequiredEdits:
```

---

## 25) SÜRÜMLEME VE GERİYE DÖNÜK UYUMLULUK

- Şema etiketi: `KAOOS-{major}.{minor}.{patch}`
- `major`: kırıcı değişiklik
- `minor`: yeni modül/alan ekleme
- `patch`: dil/format düzeltmesi

Pipeline tarafında en az son iki minor sürüm desteklenmelidir.
