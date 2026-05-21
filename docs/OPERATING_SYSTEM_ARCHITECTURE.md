# Kerime Ataker Operating System — Repository Haritası ve Standart Mimari

Bu doküman, Kerime Ataker operasyon sisteminin **tekil kaynak mimarisini** tanımlar: mevcut depo haritası, standart modül düzeni, isimlendirme kuralları, klasör hiyerarşisi, enforcement (zorunlu kontrol) katmanları ve ölçeklenebilir genişleme stratejisi.

---

## 1) Tam Repository Structure Map (Mevcut Durum)

```text
kerime-ataker-codex/
├── AGENTS.md
├── README.md
├── docs/
│   └── OPERATING_SYSTEM_ARCHITECTURE.md
└── skills/
    └── kerime-ataker-luxury-operator/
        ├── SKILL.md
        └── resources/
            ├── boutique-system.md
            ├── brand-system.md
            ├── competitor-system.md
            ├── final-qa-system.md
            ├── instagram-output-system.md
            ├── meta-ads-system.md
            ├── product-index.md
            ├── product-rules.md
            └── visual-generation-lock.md
```

---

## 2) Standart Modül Mimarisi (Canonical Module Architecture)

Sistem, tek bir “execution skill” + kuralları bölen kaynak modüller üzerine kurulu olmalıdır.

### 2.1 Katmanlı Mimari

1. **Policy Layer (Üst Kurallar)**
   - `AGENTS.md`
   - Marka tonu, yasaklı diller, QA zorunlulukları, çıktı dili gibi global governance kuralları.

2. **Orchestration Layer (Akış Yönetimi)**
   - `skills/kerime-ataker-luxury-operator/SKILL.md`
   - Hangi sırayla hangi kaynakların okunacağı, nasıl cevap üretileceği.

3. **Domain Knowledge Layer (Alan Modülleri)**
   - `skills/.../resources/*.md`
   - Her işlevin kendi modülünde yönetilmesi:
     - marka
     - ürün kuralları
     - butik/şehir uyumu
     - Meta ads mantığı
     - Instagram metin sistemi
     - görsel kalite kilidi
     - final QA

4. **Operational Data Layer (Canlı Veri Referansı)**
   - `product-index.md`
   - Ürün gerçekliği ve doğrulama durumu (ör. `requires verification`) için tek kaynak.

5. **Architecture & Governance Layer (Bu Doküman)**
   - `docs/OPERATING_SYSTEM_ARCHITECTURE.md`
   - Ekip büyüdükçe standardın bozulmaması için tasarım anayasası.

---

## 3) İsimlendirme Konvansiyonları (Naming Conventions)

### 3.1 Dosya/Klasör Adlandırma

- Tüm dosya adları: **kebab-case**
  - Doğru: `meta-ads-system.md`
  - Yanlış: `MetaAdsSystem.md`, `meta_ads_system.md`
- Sistem seviyesinde sabit dosyalar:
  - `AGENTS.md`
  - `SKILL.md`
  - `README.md`

### 3.2 Modül Sonekleri (Suffix Standards)

- Kural ve çerçeve modülleri: `*-system.md`
- Ürün veri indeksi: `product-index.md`
- Kural seti: `*-rules.md`
- Kilit/guardrail dosyaları: `*-lock.md`

### 3.3 İç Başlık Standardı

Her resource dosyası aşağıdaki blokları içermelidir (uygun olanlar):

- `## Purpose`
- `## Scope`
- `## Inputs`
- `## Rules`
- `## Output Format`
- `## QA Checks`
- `## Failure / Requires Verification Conditions`

---

## 4) Klasör Hiyerarşisi Standardı (Hedef Durum)

Büyümeye uygun hedef hiyerarşi:

```text
kerime-ataker-codex/
├── AGENTS.md
├── README.md
├── docs/
│   ├── OPERATING_SYSTEM_ARCHITECTURE.md
│   ├── CHANGELOG.md
│   └── DECISIONS/
│       ├── 0001-module-boundaries.md
│       └── 0002-output-language-policy.md
├── skills/
│   └── kerime-ataker-luxury-operator/
│       ├── SKILL.md
│       ├── resources/
│       │   ├── brand-system.md
│       │   ├── product-rules.md
│       │   ├── product-index.md
│       │   ├── boutique-system.md
│       │   ├── meta-ads-system.md
│       │   ├── instagram-output-system.md
│       │   ├── visual-generation-lock.md
│       │   ├── final-qa-system.md
│       │   └── competitor-system.md
│       ├── templates/
│       │   ├── product-analysis-template.md
│       │   ├── instagram-caption-template.md
│       │   └── meta-ads-template.md
│       └── validators/
│           ├── qa-checklist.md
│           └── banned-phrases-tr.md
└── tests/
    ├── policy/
    ├── outputs/
    └── fixtures/
```

Not: Bu hedef yapı, mevcut depoyu bozmaz; kontrollü genişleme için referans modeldir.

---

## 5) Enforcement Layers (Uyum/Zorunlu Kontrol Katmanları)

### 5.1 L0 — Structural Enforcement

- Zorunlu dosyaların varlığı:
  - `AGENTS.md`
  - `skills/.../SKILL.md`
  - temel `resources` modülleri
- Fail koşulu: kritik modül eksikse “production response” üretilmez.

### 5.2 L1 — Policy Enforcement

- Yasaklı ton kontrolü (cheap, mass, spam luxury).
- “Fake data” ve uydurma metrik yasağı.
- Output language enforcement:
  - Operasyonel açıklama: Türkçe
  - Brand-facing metin: İngilizce

### 5.3 L2 — Module Enforcement

- Product task ise 9 katmanlı analiz zorunlu:
  1. Product Character
  2. Material Reading
  3. Silhouette Reading
  4. Seasonal Fit
  5. Boutique Fit
  6. U.S. City Fit
  7. Meta Ads Logic
  8. Instagram Positioning
  9. Final QA Check

- Meta ads çıktısında zorunlu ayrım:
  - searchable interests
  - luxury behavioral signals
  - strategic audience signals

### 5.4 L3 — Output QA Enforcement

- Final QA lock adımları zorunlu doğrulama listesi olarak çalışır:
  - tone
  - realism
  - luxury consistency
  - seasonal logic
  - boutique compatibility
  - duplicate language
  - over-selling
  - fake claims

### 5.5 L4 — Change Enforcement (Repo Değişiklik Disiplini)

- Her kural değişikliği için:
  - hangi modül değişti
  - neden değişti
  - hangi çıktıları etkiler
  - geriye dönük risk
  kısa notu `docs/CHANGELOG.md` veya `docs/DECISIONS/*` içine eklenir.

---

## 6) Gelecek Genişleme Stratejisi (Future Expansion Strategy)

### 6.1 Domain Expansion

Yeni domain modülleri ayrı dosya olarak eklenmeli:

- `wholesale-system.md`
- `bridal-system.md`
- `crm-voice-system.md`
- `email-editorial-system.md`

Kural: yeni domain, mevcut modülleri şişirmek yerine **ayrı kaynak dosyası** olarak açılır.

### 6.2 Geographic Expansion

- `us-city-fit` modeli korunur.
- Yeni bölge geldiğinde ayrı modül:
  - `eu-city-fit-system.md`
  - `gulf-client-system.md`

### 6.3 Channel Expansion

Instagram-first korunur; yeni kanallar için ayrı modüller:

- `pinterest-editorial-system.md`
- `tiktok-direction-system.md` (tone guardrail ile)

### 6.4 Data Reliability Expansion

`product-index.md` yapısı zamanla alanlandırılmalı:

- `product_id`
- `name`
- `category`
- `materials_verified`
- `silhouette_notes`
- `season`
- `status` (`verified` | `requires verification`)
- `last_updated`

### 6.5 Automation Expansion

Orta vadede `tests/` altında metin kontrol testi:

- banned phrase taraması
- required section varlığı
- Meta ads üçlü ayrım kontrolü
- QA lock checklist doğrulaması

---

## 7) Standardized Module Contract (Kısa Sözleşme)

Her yeni modül aşağıdaki sözleşmeyi karşılamalıdır:

1. Tek bir sorumluluğa sahip olmalı.
2. Girdi/çıktı beklentisi net yazılmalı.
3. Brand tone ile çelişmemeli.
4. Fake data üretimine izin vermemeli.
5. Final QA ile ölçülebilir olmalı.
6. İsimlendirme standardına uymalı.
7. SKILL.md içinde çağrılma sırası belirtilmeli.

---

## 8) Yönetim Özeti (Executive Operating Summary)

Bu işletim sistemi için ideal yönetim prensibi:

- **Tek merkezli kural yönetimi** (`AGENTS.md`)
- **Modüler uzmanlık** (`resources/*.md`)
- **Akış disiplini** (`SKILL.md`)
- **Doğrulanabilir ürün veri kaynağı** (`product-index.md`)
- **Zorunlu final kalite kilidi** (`final-qa-system` + AGENTS QA lock)

Bu prensip ile sistem, hem yaratıcı kaliteyi korur hem de ekip/kanal/artan iş yükü altında yapısal tutarlılığı kaybetmeden büyür.
