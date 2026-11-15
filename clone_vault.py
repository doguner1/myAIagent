import os
import subprocess
import json
from datetime import datetime

REPOS = [
    {"id": "codebase-memory-mcp", "repo": "DeusData/codebase-memory-mcp", "url": "https://github.com/DeusData/codebase-memory-mcp.git", "category": "Otonom Ajan & Kod Tabanı Hafızası"},
    {"id": "claude-plugins-official", "repo": "anthropics/claude-plugins-official", "url": "https://github.com/anthropics/claude-plugins-official.git", "category": "Resmi Claude Eklentileri & Beceriler"},
    {"id": "one-skill-to-rule-them-all", "repo": "rebelytics/one-skill-to-rule-them-all", "url": "https://github.com/rebelytics/one-skill-to-rule-them-all.git", "category": "Meta-Öğrenme & Görev Gözlemcisi (task-observer)"},
    {"id": "api-anything", "repo": "goodnight000/api-anything", "url": "https://github.com/goodnight000/api-anything.git", "category": "Arayüzden Hızlı HTTP API Çıkarma"},
    {"id": "agent-reach", "repo": "Panniantong/agent-reach", "url": "https://github.com/Panniantong/agent-reach.git", "category": "16 Platformlu İnternet & Sosyal Medya Tarayıcısı"},
    {"id": "vane", "repo": "ItzCrazyKns/Vane", "url": "https://github.com/ItzCrazyKns/Vane.git", "category": "Yerel Web Arayüzü & Çalışma Alanı"},
    {"id": "agency-agents", "repo": "msitarzewski/agency-agents", "url": "https://github.com/msitarzewski/agency-agents.git", "category": "Çok Disiplinli Uzman Ajan Kadrosu"},
    {"id": "caveman", "repo": "JuliusBrussee/caveman", "url": "https://github.com/JuliusBrussee/caveman.git", "category": "Token Optimizasyonu & Cerrahi Müdahale"},
    {"id": "ai-memory", "repo": "akitaonrails/ai-memory", "url": "https://github.com/akitaonrails/ai-memory.git", "category": "Epizodik Uzun Vadeli Hafıza"},
    {"id": "mirofish", "repo": "666ghj/MiroFish", "url": "https://github.com/666ghj/MiroFish.git", "category": "Sürü Zekası & Virallik Simülasyonu"},
    {"id": "harper", "repo": "Automattic/harper", "url": "https://github.com/Automattic/harper.git", "category": "Çevrimdışı Dilbilgisi & Diksiyon Kontrolü"},
    {"id": "mattpocock-skills", "repo": "mattpocock/skills", "url": "https://github.com/mattpocock/skills.git", "category": "Wayfinder Navigasyonu & Strict Domain Modelleme"},
    {"id": "decepticon", "repo": "BitterSecurity/Decepticon", "url": "https://github.com/BitterSecurity/Decepticon.git", "category": "Otonom Red Team & Güvenlik Sızma Testi"},
    {"id": "ghidra", "repo": "NationalSecurityAgency/ghidra", "url": "https://github.com/NationalSecurityAgency/ghidra.git", "category": "ARM64 Tersine Mühendislik & Decompiler"},
    {"id": "airllm", "repo": "lyogavin/airllm", "url": "https://github.com/lyogavin/airllm.git", "category": "Katman Katman Düşük Bellekli LLM Çıkarımı"},
    {"id": "maka", "repo": "apache/maka", "url": "https://github.com/apache/maka.git", "category": "Olay Tabanlı Ajan Denetim İzi (Audit Trail)"},
    {"id": "ai-job-search", "repo": "MadsLorentzen/ai-job-search", "url": "https://github.com/MadsLorentzen/ai-job-search.git", "category": "Teknik Portföy & Yetkinlik Sentezi"},
    {"id": "rea", "repo": "morluto/rea", "url": "https://github.com/morluto/rea.git", "category": "207 Araçlı Otonom Tersine Mühendislik Çatısı"},
    {"id": "desktop", "repo": "desktop/desktop", "url": "https://github.com/desktop/desktop.git", "category": "Electron / ASAR İnceleme & IPC Denetimi"},
    {"id": "evolution-api", "repo": "evolution-foundation/evolution-api", "url": "https://github.com/evolution-foundation/evolution-api.git", "category": "Çok Kanallı Mesajlaşma & WhatsApp API Ağ Geçidi"},
    {"id": "open-seo", "repo": "every-app/open-seo", "url": "https://github.com/every-app/open-seo.git", "category": "Açık Kaynak SEO Analizi & AI Görünürlük (GEO)"},
    {"id": "superpowers", "repo": "obra/superpowers", "url": "https://github.com/obra/superpowers.git", "category": "Ajanik Yazılım Metodolojisi & TDD Çerçevesi"},
    {"id": "youtube-automation-agent", "repo": "darkzOGx/youtube-automation-agent", "url": "https://github.com/darkzOGx/youtube-automation-agent.git", "category": "Otonom YouTube / Shorts Video Üretim Fabrikası"}
]

TARGET_DIR = "/Users/qwerty/Desktop/ai/repos"
REGISTRY_FILE = "/Users/qwerty/Desktop/ai/vault_registry.json"

os.makedirs(TARGET_DIR, exist_ok=True)

registry = {}
if os.path.exists(REGISTRY_FILE):
    try:
        with open(REGISTRY_FILE, "r") as f:
            registry = json.load(f)
    except:
        registry = {}

print(f"Toplam Klonlanacak/Güncellenecek Repo: {len(REPOS)}")

for idx, item in enumerate(REPOS, 1):
    repo_id = item["id"]
    repo_url = item["url"]
    dest_path = os.path.join(TARGET_DIR, repo_id)
    
    print(f"[{idx}/{len(REPOS)}] İşleniyor: {item['repo']} -> {repo_id}...")
    
    if os.path.exists(dest_path) and os.path.exists(os.path.join(dest_path, ".git")):
        print(f"  Zaten mevcut, güncelleniyor (fetch & pull)...")
        try:
            subprocess.run(["git", "-C", dest_path, "pull", "--ff-only"], capture_output=True, timeout=60)
        except Exception as e:
            print(f"  Güncelleme atlandı: {e}")
    else:
        print(f"  Klonlanıyor (depth 1)...")
        try:
            cmd = ["git", "clone", "--depth", "1", repo_url, dest_path]
            res = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
            if res.returncode != 0:
                print(f"  HATA: {res.stderr.strip()[:150]}")
            else:
                print(f"  Başarıyla klonlandı.")
        except Exception as e:
            print(f"  Klonlama zaman aşımı/hata: {e}")
            
    # Commit hash al
    commit_hash = "unknown"
    if os.path.exists(dest_path):
        try:
            c = subprocess.run(["git", "-C", dest_path, "rev-parse", "HEAD"], capture_output=True, text=True)
            if c.returncode == 0:
                commit_hash = c.stdout.strip()
        except:
            pass

    registry[repo_id] = {
        "repo": item["repo"],
        "url": item["url"],
        "category": item["category"],
        "path": dest_path,
        "commit": commit_hash,
        "cloned_at": datetime.now().isoformat(),
        "status": "mirrored" if os.path.exists(dest_path) else "failed"
    }

with open(REGISTRY_FILE, "w") as f:
    json.dump(registry, f, indent=2, ensure_ascii=False)

print(f"\nİşlem tamamlandı! Kayıt dosyası: {REGISTRY_FILE}")
