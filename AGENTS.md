# 🧠 AGENTS.md — Yapay Zeka Ajanı Başlangıç Anayasası

> **ZORUNLU KURAL (TÜM YAPAY ZEKA VE AJANLAR İÇİN):**  
> Bu çalışma alanında çalışmaya başladığında veya kullanıcı sana herhangi bir istek/proje verdiğinde **KOD YAZMADAN VEYA CEVAP VERMEDEN ÖNCE** aşağıdaki adımları sırasıyla uygula.

---

## 1. İlk Refleks: Becerileri ve Depoları Tara
Kullanıcı senden bir şey istediğinde (örn: çocuk videosu, iOS tweak, SEO analizi, WhatsApp botu, web tasarımı vb.):
1. Doğrudan ezberden iş yapmaya kalkma.
2. İlk olarak `./skills/` klasöründeki becerileri (`SKILL.md`) ve `./repos/` klasöründeki hazır araçları tara.
3. İhtiyacı analiz etmek için gerekirse `python3 dispatcher.py <hedef_proje>` çıktısını kullan.

## 2. Yalnızca Gerekeni Kullan (Just-In-Time)
* Kasada 460+ beceri ve 24 repo bulunur.
* Yalnızca o anki göreve hizmet eden **1 ile 4 arasındaki beceriyi** aktif kıl.
* Tüm diğer araçları uykuda (DORMANT) bırakarak bellek ve token tasarrufu sağla.

## 3. İnsan Onay Kapısı (Human-in-the-Loop)
* Kod yazmadan, video render etmeden veya API'leri dışarı açmadan önce planını kullanıcıya özetle.
* Kullanıcı onay verince adımları kanıtlayarak uygula.

## 4. Görev Bittiğinde Temizlik
* Açılan geçici portlar, arka plan işlemleri veya Docker konteynerleri varsa iş bitince kapat.
* Sistemde kalıcı çöp dosya bırakma.
