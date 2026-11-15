# 🧠 myAIagent: Universal Just-In-Time (JIT) Skill Vault & Toolchain for AI Agents

> **"Give this vault to your AI agent: it loads only the skills it needs, does the work, and cleans up without wasting tokens."**

[![Skills Count](https://img.shields.io/badge/Skills-475%2B-blueviolet.svg?style=flat-square)](#-beceri-kataloğu)
[![Architecture](https://img.shields.io/badge/Architecture-Just--In--Time%20(JIT)-brightgreen.svg?style=flat-square)](#-mimari-felsefe-neden-jit)
[![Tools Mirrored](https://img.shields.io/badge/Mirrored%20Tools-24%20Repos-blue.svg?style=flat-square)](#-araç-ve-repo-kasası-vault_registryjson)
[![Compatible With](https://img.shields.io/badge/Compatible-Antigravity%20|%20Claude%20Code%20|%20Cursor%20|%20Copilot-orange.svg?style=flat-square)](#-nasıl-kullanılır)
[![License](https://img.shields.io/badge/License-MIT-lightgrey.svg?style=flat-square)](LICENSE)

---

## ⚡ Nedir? / What is this?

**myAIagent**, modern yapay zeka ajanları (Google Antigravity, Claude Code, Cursor, Copilot, Cline vb.) için tasarlanmış **475'ten fazla modüler beceri (`SKILL.md`)** ve **24 kurumsal seviye açık kaynaklı aracı** içeren evrensel bir **İhtiyaç Anında (Just-In-Time) Yetenek Kasasıdır**.

Geleneksel yaklaşımlarda tüm becerileri ve araçları ajanın sistem promptuna yüklemek; modelin token bütçesini tüketir, bağlam penceresini (context window) şişirir ve modelin odağını dağıtır. 

**myAIagent bu sorunu çözer:**
Ajanınız bu depoyu bir kütüphane gibi kullanır; üzerinde çalıştığı projeyi `dispatcher.py` ile tarar, **yalnızca o an gereken 1 ila 3 beceriyi hafızasına alır**, işini tamamlar ve geçici alanı temizler.

---

## 🎯 Mimari Felsefe: Neden Just-In-Time (JIT)?

```
                    ┌───────────────────────────────────┐
                    │      Hedef Projeniz / Görev       │
                    └─────────────────┬─────────────────┘
                                      │
                                      ▼
                        python3 dispatcher.py <hedef>
                                      │
                   ┌──────────────────┴──────────────────┐
                   ▼                                     ▼
      ┌─────────────────────────┐           ┌─────────────────────────┐
      │ 475+ Skill Kütüphanesi  │           │   24 Araç Envanteri     │
      │       (./skills/)       │           │  (vault_registry.json)  │
      └────────────┬────────────┘           └────────────┬────────────┘
                   │                                     │
                   └──────────────────┬──────────────────┘
                                      │
                  [Sadece Eşleşen 1-3 Beceri Aktif Edilir]
                                      │
                                      ▼
                    ┌───────────────────────────────────┐
                    │          Yapay Zeka Ajanı         │
                    │   (Hafif, Odaklı, Sıfır Şişkinlik) │
                    └─────────────────┬─────────────────┘
                                      │
                        [Görev Bittiğinde Temizlik]
                                      │
                                      ▼
                          🧹 Sıfır Token İsrafı
```

1. **Sıfır Bağlam Kirliliği (Zero Context Bloat):** Yüzlerce kuralı ezberletmek yerine, ajana görev anında sadece ilgili `SKILL.md` verilir.
2. **Kendi Kendine Temizlenen Yapı:** Ajan işi bitirdiğinde ilgili beceriyi devreden çıkarır, arkasında çöp dosya veya açık port bırakmaz.
3. **Taşınabilir & Çevrimdışı:** İnternet erişimi kesilse bile tüm yetenek tanımları ve yönergeleri yerelinizde hazır bulunur.

---

## 🚀 Nasıl Kullanılır?

### 1. AI Ajanınıza Bu Depoyu Tanıtın (En Kolay Yol)
Ajanınıza (Antigravity, Claude Code, Cursor vb.) sadece şu talimatı vermeniz yeterlidir:

```markdown
Bu projede çalışırken myAIagent kasasını referans al.
1. İhtiyacın olan becerileri './skills/' klasöründen veya 'python3 dispatcher.py .' çalıştırarak belirle.
2. Sadece bu göreve doğrudan hizmet eden 1-3 beceriyi oku ve uygula.
3. Görev bittiğinde geçici dosyaları temizle.
Detaylı anayasa için 'AGENTS.md' dosyasını takip et.
```

### 2. Akıllı Yönlendiriciyi (Dispatcher) Manuel Çalıştırma
Bir projenin hangi becerilere ihtiyaç duyduğunu otomatik analiz etmek için:

```bash
python3 dispatcher.py /path/to/your/project
```

**Örnek Çıktı:**
```json
{
  "detected_domain": "frontend_ui_web",
  "recommended_skills": [
    "ui-ux-pro-max",
    "impeccable",
    "frontend-design",
    "agency-frontend-developer"
  ],
  "recommended_tools": [
    "ui-ux-pro-max-skill",
    "impeccable"
  ]
}
```

### 3. İhtiyaç Duyduğunuz Bir Beceriyi Projenize Kopyalama
Bir beceriyi projenizin yerel ajan klasörüne taşımak için:

```bash
# Projenizin kök dizininde
mkdir -p .agents/skills/frontend-design
cp /path/to/myAIagent/skills/frontend-design/SKILL.md .agents/skills/frontend-design/
```

İşiniz bittiğinde:
```bash
rm -rf .agents/skills/frontend-design
```

---

## 🗂️ Beceri Kataloğu (475+ Specialized Skills)

Kasadaki beceriler endüstri standardı uzmanlık rolleri ve framework'ler etrafında gruplanmıştır:

| Kategori | Öne Çıkan Beceriler | Açıklama |
| :--- | :--- | :--- |
| **🎨 UI, UX & Frontend** | `frontend-design`, `ui-ux-pro-max`, `impeccable`, `diagram-design`, `penpot` | Şablonlaşmış yapay zeka çıktılarından uzak, özgün ve yüksek standartlı arayüz tasarımı. |
| **⚙️ Backend & Veritabanı** | `agency-backend-architect`, `agency-database-optimizer`, `agency-api-tester` | Mikroservis, API mimarisi, SQL optimizasyonu ve veri modelleme. |
| **🔍 SEO, Büyüme & Analitik** | `openseo-intelligence`, `agency-seo-specialist`, `agency-growth-hacker` | Yapay zeka arama motoru görünürlüğü (GEO/AEO), anahtar kelime kümeleme ve rakip analizi. |
| **🛡️ Güvenlik & Tersine Mühendislik** | `ghidra-reverse-engineering`, `rea-reverse-engineer`, `autonomous-redteam-pentest`, `desktop-app-reverse-engineering` | ARM64 Mach-O decompile, Electron ASAR denetimi, sızma testleri ve ikili analiz. |
| **🎬 Video & Medya Otomasyonu** | `youtube-automation-agent`, `remotion-video`, `video-shotcraft`, `hyperframes`, `offline-grammar-checker` | Programatik video üretimi, altyazı senkronizasyonu ve kurgu otomasyonu. |
| **🤖 Ajan Metodolojisi & Kalite** | `superpowers-methodology`, `agent-longterm-memory`, `task-observer`, `caveman`, `safe-refactor` | Test-driven development (TDD), oturumlar arası kalıcı hafıza ve minimal cerrahi kod müdahalesi. |
| **🚗 Otomotiv, 3D & Gömülü** | `lemo-opuscar`, `mcp-for-blender`, `img2threejs`, `agency-3d-scene-developer` | Gösterge paneli/kokpit sistemleri, WebGL, procedural 3D modelleme. |

Tüm 475 becerinin alfabetik tam dökümü için: 👉 [tam_yetenek_ve_beceri_katalogu.md](tam_yetenek_ve_beceri_katalogu.md)

---

## 🧰 Araç ve Repo Kasası (`vault_registry.json`)

Kasa, GitHub üzerindeki en güçlü 24 açık kaynaklı ajan ve geliştirici aracının metaverisini tutar:

* **Hafıza & Algı:** `DeusData/codebase-memory-mcp`, `akitaonrails/ai-memory`, `rebelytics/one-skill-to-rule-them-all`
* **Web & API:** `goodnight000/api-anything`, `Panniantong/agent-reach`, `every-app/open-seo`
* **Mühendislik & Kalite:** `obra/superpowers`, `JuliusBrussee/caveman`, `Automattic/harper`
* **Tersine Mühendislik:** `morluto/rea`, `NationalSecurityAgency/ghidra`, `desktop/desktop`
* **Çoklu Ajan Kadroları:** `msitarzewski/agency-agents`, `666ghj/MiroFish`

### İlgili Depoları Yerel Olarak Klonlama
Kayıtlı repoları yerel diskinize indirmek isterseniz:
```bash
python3 clone_vault.py
```

### Kasaya Yeni Repo Ekleme
Sisteme yeni bir açık kaynak aracı eklemek için:
```bash
python3 add_repo.py https://github.com/sahip/yeni-arac "Kategori Adı"
```

---

## 📜 Temel Belgeler

* 📘 [AGENTS.md](AGENTS.md) — Herhangi bir AI ajanı için başlangıç anayasası ve çalışma kuralları.
* 📗 [SISTEM_KILAVUZU.md](SISTEM_KILAVUZU.md) — Detaylı sistem mimarisi ve operasyonel kılavuz.
* 📙 [tam_yetenek_ve_beceri_katalogu.md](tam_yetenek_ve_beceri_katalogu.md) — 475 becerinin detaylı içerik dizini.
* 📕 [docs/TOOLCHAIN_SETUP.md](docs/TOOLCHAIN_SETUP.md) — Yerel Antigravity ve MCP stdio altyapı kurulum spesifikasyonu.

---

## 📄 Lisans

Bu proje açık kaynak topluluğu için hazırlanmıştır. Bireysel beceriler ve araçlar kendi orijinal lisanslarına (MIT, Apache 2.0 vb.) tabidir.
