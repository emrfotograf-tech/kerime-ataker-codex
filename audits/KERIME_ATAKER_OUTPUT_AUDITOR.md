# KERIME_ATAKER_OUTPUT_AUDITOR

## MODÜL AMACI

Bu modül, Kerime Ataker operatör çıktılarının **nihai teslimden önce zorunlu simülasyon ve doğrulama katmanından** geçmesini sağlar.

Hedef:
- tüm çıktı tiplerini senaryo bazlı simüle etmek,
- format, ton, dil, hiyerarşi ve doğruluk ihlallerini yakalamak,
- otomasyon dostu PASS/FAIL denetim çıktısı üretmek.

Bu denetim katmanı geçilmeden içerik yayınlanamaz.

---

## KAPSAM (ZORUNLU SİMÜLASYON TİPLERİ)

Auditor aşağıdaki çıktı türlerinin tamamını simüle eder ve doğrular:

1. Instagram Post Output
2. Instagram Story Output
3. Reels Output
4. Meta Ad Output
5. Boutique Output
6. Campaign Output
7. Product Analysis Output

---

## GİRDİ SÖZLEŞMESİ

Auditor, operatörden gelen tekil veya birleşik çıktıyı aşağıdaki alanlarla alır:

- `output_type`
- `operator_heading`
- `brand_copy`
- `cta_or_cti`
- `hashtags`
- `timing`
- `season`
- `occasion`
- `boutique_fit`
- `meta_objective`
- `evidence_tags`
- `final_qa_block`

Not:
- `brand_copy` yalnızca marka-facing metni ifade eder.
- `operator_heading` operasyonel yönlendirme başlığıdır.

---

## DOĞRULAMA MOTORU (KURAL KÜMELERİ)

Her çıktı aşağıdaki kontrol kümelerine girer:

### 1) Luxury Tone Consistency
Kontrol eder:
- premium, kontrollü, rafine, editoryal hissin korunması,
- ucuz/satışçı/bağıran tonun olmaması,
- “aura first, product second” kurgusunun korunması.

Fail tetikleyicileri (örnek):
- “kaçırma”, “şimdi al”, “stok bitiyor”, “çok uygun fiyat” gibi agresif satış dili.

### 2) Forbidden Wording Violations
Kontrol eder:
- brand evreniyle uyumsuz kelime setleri,
- cheap luxury veya spam-commercial çağrışımlar.

### 3) CTA / CTI Discipline
Kontrol eder:
- yönlendirmenin soft olması,
- açık satış baskısı içermemesi,
- CTA yerine mümkünse CTI (consider / discover / explore tone) kullanılması.

### 4) Banned GTA Terminology
GTA (Generic Trendy Ad-speak) blacklist kontrolü:
- “must-have”, “it-girl essential”, “viral pick”, “best seller guaranteed” vb.
- aşırı trend ve influencer-fast-fashion söylemi.

### 5) Fake Data Detection
Kontrol eder:
- uydurma metrik, sahte performans iddiası, doğrulanmamış sayı.
- örnek fail: “%300 etkileşim artışı”, “1M views aldı” (kanıtsızsa).

### 6) Evidence Tagging Presence
Kontrol eder:
- kritik iddia, ürün bilgisi, sezon/occasion ve hedefleme notlarının evidence tag ile işaretlenmesi.
- örnek tag yapısı: `[EVIDENCE:PRODUCT_PAGE]`, `[EVIDENCE:CRM_NOTE]`.

### 7) Turkish Operator Heading Compliance
Kontrol eder:
- operasyonel başlıkların Türkçe olması.
- örnek doğru: `## Operasyonel Çıktı Özeti`

### 8) English-only Brand-facing Copy Compliance
Kontrol eder:
- tüketiciye dönük/caption/campaign copy alanlarında yalnızca İngilizce kullanım.
- Türkçe ifade brand_copy içinde fail üretir.

### 9) Hashtag Placement Logic
Kontrol eder:
- hashtag’in ana metni boğmaması,
- spam yığını olmaması,
- lüks pozisyonlamaya uygun sınırlı ve seçici kullanım.

### 10) Timing Structure Compliance
Kontrol eder:
- story/reels/post zaman akışının açık olması,
- adım/sahne/zaman bloklarının formatlı yazılması.

### 11) Seasonal Mismatch Detection
Kontrol eder:
- materyal/siluet/occasion ile season alanının uyumu.
- örnek fail: ağır fur look + high summer beach occasion.

### 12) Occasion Fit Mismatch Detection
Kontrol eder:
- ürün dili ile kullanım anı uyumu.
- örnek fail: formal sculptural eveningwear için “daily gym errand” çerçevesi.

### 13) Boutique Fit Formatting
Kontrol eder:
- boutique önerisinin segmentlenmiş ve okunabilir formatta verilmesi.
- zorunlu alt alanlar: müşteri profili, fiyat algısı, sunum dili, stok/assortment notu.

### 14) Meta Objective Formatting
Kontrol eder:
- Meta hedefinin standart formatta yazılması,
- interest/behavior/strategic signal ayrımının net verilmesi,
- doğrulanmamış targeting claim üretilmemesi.

### 15) Anti-spam Language Discipline
Kontrol eder:
- tekrar eden ünlem, abartılı emoji, kampanya-bağıran dil, clickbait kalıbı.

### 16) Output Hierarchy Correctness
Kontrol eder:
- çıktı bölümlerinin beklenen sırayla sunulması,
- başlık-seviye düzeni ve tip bazlı alt blok bütünlüğü.

### 17) Final QA Gate Completeness
Kontrol eder:
- final QA bloğunda aşağıdakilerin tamamının bulunması:
  - tone
  - realism
  - luxury consistency
  - seasonal logic
  - boutique compatibility
  - duplicated language
  - over-selling
  - fake claims

---

## ÇIKTI TİPİNE GÖRE SİMÜLASYON PROFİLLERİ

### A) Instagram Post Simulation
Doğrular:
- aura-first caption akışı,
- ürün odağı ikinci katmanda,
- hashtag’in dip blokta ve sınırlı olması,
- soft CTI.

### B) Story Simulation
Doğrular:
- frame bazlı akış (F1/F2/F3...),
- kısa ve rafine mikro-kopya,
- temporal sequencing ve görsel not senkronu.

### C) Reels Simulation
Doğrular:
- hook/body/close yapısı,
- shot timing,
- ses-görüntü-metnin aşırı satışa kaymaması.

### D) Meta Ad Simulation
Doğrular:
- objective formatı,
- audience ayrımı (searchable interests / luxury behavioral signals / strategic audience signals),
- kanıtsız iddia ve platformda olmayan targeting uydurmasının engellenmesi.

### E) Boutique Simulation
Doğrular:
- butik persona uyumu,
- şehir/mağaza bağlamı,
- premium danışmanlık tonu.

### F) Campaign Simulation
Doğrular:
- kampanya anlatı omurgası,
- kanal bazlı varyasyon disiplini,
- sezon ve occasion mantığı.

### G) Product Analysis Simulation
Doğrular (zorunlu 9 blok):
1. Product Character
2. Material Reading
3. Silhouette Reading
4. Seasonal Fit
5. Boutique Fit
6. U.S. City Fit
7. Meta Ads Logic
8. Instagram Positioning
9. Final QA Check

---

## ŞİDDET SKORLAMA MODELİ

Her ihlal severity puanı alır:

- `S1-CRITICAL` (9-10): yayın engelleyici risk
- `S2-HIGH` (7-8): güçlü kalite/marka riski
- `S3-MEDIUM` (4-6): düzeltilebilir uyum sorunu
- `S4-LOW` (1-3): kozmetik/biçimsel sorun

Toplam kalite skoru:

`quality_score = 100 - Σ(weighted_violations)`

Önerilen ağırlıklar:
- Critical: -20
- High: -12
- Medium: -7
- Low: -3

Karar eşiği:
- `PASS`: kritik ihlal yok VE score >= 85
- `FAIL`: kritik ihlal var VEYA score < 85

---

## PASS / FAIL KARAR MANTIĞI

Fail koşulları:
- fake data tespiti,
- English-only kural ihlali (brand-facing kopyada),
- final QA gate eksikliği,
- output hierarchy bozulması,
- banned GTA terminology yoğun kullanımı,
- Meta objective formatının olmaması (Meta output’ta).

Pass koşulları:
- tüm zorunlu bloklar tam,
- ton/format/dil uygun,
- ciddi ihlal yok,
- minimum kalite skoru karşılanmış.

---

## OTOMASYON-HAZIR VALIDATION ŞEMASI

```yaml
audit_result:
  module: KERIME_ATAKER_OUTPUT_AUDITOR
  timestamp_utc: "{{ISO8601}}"
  output_type: "instagram_post|story|reels|meta_ad|boutique|campaign|product_analysis"
  verdict: "PASS|FAIL"
  quality_score: 0-100
  severity_summary:
    critical: 0
    high: 0
    medium: 0
    low: 0
  violations:
    - id: "V-001"
      rule: "English-only Brand-facing Copy"
      severity: "S1-CRITICAL"
      location: "brand_copy.paragraph_2"
      evidence: "Turkish phrase detected in brand-facing line."
      suggestion: "Rewrite this line in refined English tone."
  corrections:
    - priority: "P1"
      action: "Remove unverified performance metric from caption."
      owner: "operator"
  compliance_flags:
    luxury_tone_consistent: true
    forbidden_wording_clear: true
    cta_cti_disciplined: true
    gta_terminology_clear: true
    fake_data_clear: true
    evidence_tags_present: true
    tr_operator_heading_ok: true
    en_brand_copy_only: true
    hashtag_logic_ok: true
    timing_structure_ok: true
    seasonal_fit_ok: true
    occasion_fit_ok: true
    boutique_format_ok: true
    meta_objective_ok: true
    anti_spam_language_ok: true
    hierarchy_ok: true
    final_qa_complete: true
```

---

## VİOLATION LİSTESİ — STANDART ID KÜTÜĞÜ

- `V-001` English-only brand copy ihlali
- `V-002` Turkish operator heading eksik/uyumsuz
- `V-003` Fake data veya fabricated metric
- `V-004` Forbidden wording kullanımı
- `V-005` GTA terminology kullanımı
- `V-006` Aggressive CTA ihlali
- `V-007` Hashtag spam/placement ihlali
- `V-008` Timing structure eksikliği
- `V-009` Seasonal mismatch
- `V-010` Occasion mismatch
- `V-011` Boutique fit format eksikliği
- `V-012` Meta objective format eksikliği
- `V-013` Output hierarchy bozukluğu
- `V-014` Evidence tagging eksikliği
- `V-015` Final QA gate eksikliği
- `V-016` Anti-spam language ihlali

---

## DÜZELTME ÖNERİ MOTORU (CORRECTION SUGGESTIONS)

Auditor her ihlal için şunları üretir:
- kısa teşhis,
- doğrudan düzeltme aksiyonu,
- hedef ton notu,
- gerekirse örnek yeniden yazım yönü.

Örnek:
- İhlal: `V-006 Aggressive CTA`
- Öneri: “Shop now” yerine “Discover the silhouette in detail.”
- Ton notu: editorial, restrained, premium.

---

## ÇIKTI HİYERARŞİSİ (ZORUNLU RAPOR SIRASI)

Auditor raporu şu sırada döner:

1. Audit Verdict (PASS/FAIL)
2. Quality Score
3. Severity Summary
4. Violation List
5. Correction Suggestions
6. Compliance Flags
7. Final QA Gate Status

---

## UYGULAMA NOTLARI

- Bu modül, enforcement katmanından önce değil sonra; final teslimden hemen önce çalıştırılmalıdır.
- FAIL durumunda yayınlanabilir marka-facing çıktı üretilmiş sayılamaz.
- PASS sonrası yalnızca küçük stil düzeltmeleri yapılabilir; içerik anlamını değiştiren revizyon gerekiyorsa audit yeniden koşulmalıdır.

