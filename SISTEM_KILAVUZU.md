# 🤖 Antigravity Yerel Ajan ve Kod Kasası Sistemi (Sistem Kılavuzu)

> **Bu dosyanın amacı:** Yapılan kurulumu, dosya konumlarını, çalışma mantığını ve gelecekte projeyi devralacak yapay zekaların (AI) sistemi anında anlamasını sağlamaktır.

---

## 1. Nereye Ne Konuldu? (Dosya ve Klasör Haritası)

* 📂 **`/Users/qwerty/Desktop/ai/repos/` (Yerel Kod Kasası):**
  * Listedeki 24 açık kaynak reponun tamamı buraya `git clone --depth 1` ile indirildi (Toplam: ~2.6 GB).
  * **Önemi:** Bu repolar GitHub'dan silinse, private yapılsa veya internet olmasa bile tam kaynak kodları diskinizde güvendedir.

* 📄 **`/Users/qwerty/Desktop/ai/vault_registry.json` (Envanter Kaydı):**
  * Kasadaki tüm repoların sabit commit hash'lerini, yerel yollarını ve kategorilerini tutan JSON indeksi.

* 🧠 **`/Users/qwerty/Desktop/ai/skills/` (Yerel Ajan Becerileri Klasörü):**
  * Tüm 460+ `SKILL.md` yönergesi artık gizli sistem dizinlerinde değil, doğrudan bu klasörün içindedir.
  * **Taşınabilirlik:** `ai` klasörünü kopyalayıp başka bir bilgisayara attığınızda hem 24 repo hem de tüm beceriler eksiksiz olarak birlikte gelir.

* ⚙️ **`/Users/qwerty/Desktop/ai/dispatcher.py` (Dinamik Yönlendirici):**
  * Verilen bir projeyi tarayıp, kasadaki 23 araç arasından **sadece o projeye gerekenleri** seçen akıllı filtre.

* ➕ **`/Users/qwerty/Desktop/ai/add_repo.py` (Tek Komutla Repo Ekleyici):**
  * Yeni bir GitHub linki verildiğinde otomatik klonlayan ve sisteme işleyen betik.

---

## 2. Sistem Nasıl Çalışır? (Just-In-Time / Yüksüz Model)

1. **Projeyi Verme:** Kullanıcı ajana herhangi bir proje yolu veya görev verir (Örn: `/Users/qwerty/projem`).
2. **Otomatik Tarama:** Ajan projeyi inceler (Dili ne? Web mi, iOS tweak mi, YouTube/video mu, SEO mu?).
3. **Geçici Yükleme:** Kasadaki araçlardan **yalnızca o iş için gereken 1-3 beceri** oturuma dahil edilir.
4. **Uyku Modu (Zero Waste):** Geriye kalan 370'ten fazla araç DORMANT (uykuda) kalır. Token harcamaz, RAM şişirmez.
5. **İş Bitince Temizlik:** Görev tamamlandığında açılan geçici servisler ve bellek yükü kapatılır.

---

## 3. Yeni Repo Nasıl Eklenir?

İki yöntemle de eklenebilir:
* **Yöntem A (Sohbetten):** Kullanıcı ajana sadece linki verir: *"Şu repoyu ekle: https://github.com/..."* Ajan indirir ve kaydeder.
* **Yöntem B (Terminalden):**
  ```bash
  python3 /Users/qwerty/Desktop/ai/add_repo.py <github_link> [kategori]
  ```
  Bu komut repoyu `repos/` içine klonlar, `vault_registry.json`'a ekler ve skill dosyasını üretir.

---

## 4. Gelecekteki Yapay Zeka Ajanı İçin Talimat (For Future AI Agents)

> Sen bu çalışma alanını devraldığında:
> 1. Araçların kaynak kodları için doğrudan [`repos/`](file:///Users/qwerty/Desktop/ai/repos/) klasörüne bak.
> 2. Kullanıcı sana bir proje veya görev verdiğinde gereksiz tüm araçları hafızaya yükleme.
> 3. İhtiyacı belirlemek için `python3 dispatcher.py <hedef_klasor>` çıktısını referans al.
> 4. Sadece ilgili 1-3 beceriyi devreye sok, iş bittiğinde temizle.
