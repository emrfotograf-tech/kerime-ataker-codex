# ÇIKTI_KİMLİĞİ
- RequestType: `single_product`
- RequestDateUTC: `2026-05-22`
- Product: `Black sculptural leather bustier`
- ChannelScope: `instagram_feed + instagram_story + reels + paid_meta + boutique_pitch`

# GİRDİ_DOĞRULAMA_DURUMU
- ProductNameVerified: true
- MaterialVerified: true
- PriceVerified: na
- AvailabilityVerified: na
- SourceList:
  - User-provided product brief (current request)
  - Internal OS constraints (`AGENTS.md`)
- MissingData:
  - Exact price band
  - Inventory depth by size
  - SKU-level construction details (panel count, closure spec)

# OPERATÖR_ÖZETİ
Router sınıflandırması `single_product` olarak kesinleşti. Deterministik akış: `INTAKE -> CLASSIFY -> ROUTE -> ENFORCE -> DECIDE -> SIMULATE -> AUDIT -> FINAL QA` uygulandı. Lingerie-first riskini düşürmek için dış giyim ve heykelsi yapı (sculptural structure) önceliklendirildi; satış baskısı kaldırıldı.

# ÜRÜN_ANALİZİ
1. **Product Character**: Geceye yakın, kontrollü ve güçlü feminenlik taşıyan hero piece. [OBSERVATIONAL_INFERENCE]
2. **Material Reading**: Siyah deri; ışığı emerek parlaklıktan çok formu öne çıkaran yüzey davranışı. [OBSERVATIONAL_INFERENCE]
3. **Silhouette Reading**: Bustier formu, heykelsi kontur ile bel-omuz aksını netleştiriyor; styling’e göre tailoring veya evening eksenine kayabilir. [OBSERVATIONAL_INFERENCE]
4. **Seasonal Fit**: FW ve transitional dönemlerde güçlü; SS için gece iç mekan ve hafif katmanlama ile uygun. [OBSERVATIONAL_INFERENCE]
5. **Boutique Fit**: Avant-garde luxury ve feminine couture leaning butiklerde yüksek uyum. [OBSERVATIONAL_INFERENCE]
6. **U.S. City Fit**: NYC/LA için yüksek, Miami için gece-event odaklı seçici, Chicago/Dallas için event-season bazlı güçlü. [OBSERVATIONAL_INFERENCE]
7. **Meta Ads Logic**: Awareness + consideration başlangıcı; ilk fazda materyal/siluet anlatımı, ikinci fazda soft intent. [OBSERVATIONAL_INFERENCE]
8. **Instagram Positioning**: Aura-first, product-second; caption dilinde “commanding/structured/material-first” ritim. [OBSERVATIONAL_INFERENCE]
9. **Final QA Check**: Fake metrik, agresif CTA, spam hashtag, rakip dili kopyası yok. [VERIFIED_SOURCE]

# STORY_AKIŞI
## Frame_01_Aura
- Amaç: Ürünün atmosferini satıştan önce konumlamak.
- OnScreenText: "After dark, structure speaks softly."
- VisualCue: Düşük kontrast ışıkta gövde konturu; yüz değil form odak.
- Interaction: "Tap to continue"

## Frame_02_Material
- Amaç: Deri yüzey ve dikiş disiplinini göstermek.
- OnScreenText: "Black leather with sculpted intent."
- VisualCue: Yakın plan dikiş hattı ve panel geçişleri.
- Interaction: "Texture slider"

## Frame_03_Silhouette
- Amaç: Heykelsi formun hareketle okunmasını sağlamak.
- OnScreenText: "Cut to hold the line."
- VisualCue: Yavaş dönüş, yan profil, bel hattı vurgusu.
- Interaction: "Which styling: tailored jacket or silk skirt?"

## Frame_04_Direction
- Amaç: Düşük baskılı yönlendirme.
- OnScreenText: "Discover the sculptural edit online."
- VisualCue: Tam look + minimal aksesuar.
- Interaction: "Reply for sizing guidance"

# REELS_ZAMAN_AKISI
## 00:00-00:02 Hook Aura
- Amaç: İlk 2 sn’de editorial aura kurmak.
- VisualAction: Siyah fonda bustier konturunun ışıkla açılması.
- OnScreenText: "A sculpted black line."
- Voiceover: "Not loud. Just precise."
- EditNote: Hızlı değil; tek kesit, sinematik sabır.

## 00:02-00:05 Material Detail
- Amaç: Malzeme gerçekliğini kanıtlamak.
- VisualAction: Dikiş, kenar bitişi, deri grain detayı.
- OnScreenText: "Leather, cut with intention."
- Voiceover: "Material before statement."
- EditNote: Macro + doğal ışık falloff.

## 00:05-00:08 Silhouette Motion
- Amaç: Formun bedende taşıma etkisini göstermek.
- VisualAction: Modelin yarım dönüşü, omuz-bel oranı.
- OnScreenText: "Structured to define movement."
- Voiceover: "A silhouette that holds shape."
- EditNote: Stabil kamera, dramatik ama gerçekçi ton.

## 00:08-00:12 Direction Close
- Amaç: Soft CTA ile kapanış.
- VisualAction: Look’un tam kadrajı + kısa yürüyüş.
- OnScreenText: "Explore the sculptural leather edit."
- Voiceover: "Discover it in the evening collection."
- EditNote: Son 2 sn logo/kimlik alanı bırak.

# MARKA_METNİ_İNGİLİZCE
## BRAND_COPY.CAPTION
Black leather, sculpted with restraint.
A bustier that frames the body with architectural precision, balancing strength and softness in a single line.
Discover the sculptural edit online.

## BRAND_COPY.HASHTAGS
#KerimeAtaker #SculpturalLeather #EveningWardrobe #RefinedFemininity #LuxuryReadyToWear

# META_REKLAM_NOTU
- SearchableInterests:
  - Leather fashion
  - Luxury ready-to-wear
  - Designer eveningwear
  - Contemporary womenswear
- LuxuryBehaviorSignals:
  - Engaged shoppers (platform-available behavior labels may vary by account)
  - High-value fashion purchase propensity (requires platform-side availability check)
  - Premium brand interaction history
- StrategicAudienceSignals:
  - 30/60-day Instagram engagers
  - Product page viewers (if pixel/CAPI configured)
  - 1-2% lookalike of verified purchasers (if compliant source exists)
- AssumptionFlag: true
- Note: Hedefleme seçenekleri hesap/bölgeye göre değişebilir; kesin aktivasyon Ads Manager içinde doğrulanmalıdır.

# BOUTIQUE_UYUMU
- Avant-garde luxury: **High fit** — sculptural leather kimliği ve editorial taşıma gücü yüksek.
- Polished minimal luxury: **Medium-High fit** — sade styling ile çok güçlü; merchandising’de materyal hikayesi önemli.
- Feminine couture leaning: **High fit** — gece ve özel davet ekseninde net konumlanır.
- Taşıma notu: Ürün “lingerie” değil “structured evening top” anlatısıyla sunulmalı.

# ABD_ŞEHİR_UYUMU
- NYC: High — gallery dinner, fashion event, after-dark wardrobe uyumu güçlü.
- LA: High — red-carpet-adjacent social dressing ve styling esnekliği yüksek.
- Miami: Medium-High — climate nedeniyle indoor evening/event kullanımına odaklanmalı.
- Dallas: Medium-High — occasion-led luxury shopping dönemlerinde güçlü performans potansiyeli.
- Chicago: Medium — sezon ve event takvimiyle eşlendiğinde daha güçlü.
- SF: Medium — minimal-luxury styling ile daha iyi çalışır, aşırı glam dilinden kaçınılmalı.

# FINAL_QA_KAPISI
- Tone Check: PASS (premium, controlled, feminine, editorial)
- Realism Check: PASS (doğrulanmamış metrik/performans claim’i yok)
- Luxury Consistency: PASS
- Seasonal Logic: PASS (FW/transitional ağırlık doğru)
- Boutique Compatibility: PASS
- Duplicate Language Check: PASS
- Over-selling Check: PASS
- Fake Claims Check: PASS
- Release Status: `APPROVED_FOR_USE`
