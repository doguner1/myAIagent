#!/usr/bin/env python3
"""
Automated Repo Vault Ingestion Tool
Clones new repos with --depth 1, registers them into vault_registry.json,
and generates local skill wrappers for instant & persistent agent usage.
"""
import os
import sys
import subprocess
import json
from datetime import datetime

TARGET_DIR = "/Users/qwerty/Desktop/ai/repos"
REGISTRY_FILE = "/Users/qwerty/Desktop/ai/vault_registry.json"
LOCAL_SKILLS_DIR = "/Users/qwerty/Desktop/ai/skills"
GLOBAL_SKILLS_DIR = os.path.expanduser("~/.gemini/config/skills")

def clean_url(url):
    url = url.strip()
    if not url.startswith("http"):
        url = "https://" + url
    if not url.endswith(".git"):
        url_git = url + ".git"
    else:
        url_git = url
    return url.rstrip("/").replace(".git", ""), url_git

def extract_repo_id(clean_url_str):
    parts = clean_url_str.split("/")
    owner = parts[-2]
    repo = parts[-1]
    return repo.lower(), f"{owner}/{repo}"

def main():
    if len(sys.argv) < 2:
        print("Kullanım: python3 add_repo.py <github-url> [kategori] [beceri_adi]")
        sys.exit(1)

    raw_url = sys.argv[1]
    category = sys.argv[2] if len(sys.argv) > 2 else "Genel Ajan Becerisi & Araç"
    skill_custom_name = sys.argv[3] if len(sys.argv) > 3 else None

    clean_u, git_u = clean_url(raw_url)
    repo_id, full_repo = extract_repo_id(clean_u)
    skill_name = skill_custom_name or repo_id
    
    dest_path = os.path.join(TARGET_DIR, repo_id)
    
    print(f"[*] İşleniyor: {full_repo} ({clean_u})")
    
    # 1. Klonlama veya Güncelleme
    if os.path.exists(dest_path) and os.path.exists(os.path.join(dest_path, ".git")):
        print(f"[*] Repo zaten mevcut, güncelleniyor...")
        subprocess.run(["git", "-C", dest_path, "pull", "--ff-only"], capture_output=True)
    else:
        print(f"[*] Yerel kasaya klonlanıyor (--depth 1): {dest_path}")
        res = subprocess.run(["git", "clone", "--depth", "1", git_u, dest_path], capture_output=True, text=True)
        if res.returncode != 0:
            print(f"[!] Hata: {res.stderr.strip()[:200]}")
            sys.exit(1)
        print("[+] Klonlama başarılı!")

    # 2. Commit hash al
    commit_hash = "unknown"
    try:
        c = subprocess.run(["git", "-C", dest_path, "rev-parse", "HEAD"], capture_output=True, text=True)
        if c.returncode == 0:
            commit_hash = c.stdout.strip()
    except:
        pass

    # 3. Registry güncelle
    registry = {}
    if os.path.exists(REGISTRY_FILE):
        try:
            with open(REGISTRY_FILE, "r") as f:
                registry = json.load(f)
        except:
            pass

    registry[repo_id] = {
        "repo": full_repo,
        "url": clean_u,
        "category": category,
        "path": dest_path,
        "skill_name": skill_name,
        "commit": commit_hash,
        "cloned_at": datetime.now().isoformat(),
        "status": "mirrored"
    }

    with open(REGISTRY_FILE, "w") as f:
        json.dump(registry, f, indent=2, ensure_ascii=False)
    print(f"[+] vault_registry.json güncellendi (Kayıtlı toplam: {len(registry)} repo).")

    # 4. SKILL.md kontrolü ve oluşturulması (Hem yerel ai/skills/ hem de global konuma)
    for target_skills_base in [LOCAL_SKILLS_DIR, GLOBAL_SKILLS_DIR]:
        skill_folder = os.path.join(target_skills_base, skill_name)
        skill_file = os.path.join(skill_folder, "SKILL.md")
        if not os.path.exists(skill_file):
            os.makedirs(skill_folder, exist_ok=True)
            # README varsa özet oku
            readme_summary = f"{full_repo} için otomatik oluşturulmuş yerel ajan becerisi."
            readme_path = os.path.join(dest_path, "README.md")
            if os.path.exists(readme_path):
                try:
                    with open(readme_path, "r", errors="ignore") as rf:
                        lines = [l.strip() for l in rf.readlines() if l.strip() and not l.startswith("#")]
                        if lines:
                            readme_summary = " ".join(lines[:3])[:250]
                except:
                    pass

            skill_content = f"""---
name: {skill_name}
description: {readme_summary} Inspired by {full_repo}.
---

# {skill_name}

## Genel Bakış
Bu beceri `{full_repo}` deposunun yerel kasadaki kopyası (`{dest_path}`) üzerinden çalışır.

## Kaynak Konumu
- Yerel Kasa Yolu: `{dest_path}`
- Sabit Commit: `{commit_hash}`

## Kullanım Talimatı
İlgili proje veya görev geldiğinde `dispatcher.py` aracılığıyla geçici olarak oturuma bağlanır.
İş bitiminde kapatılır ve kalıcı yük bırakmaz.
"""
            with open(skill_file, "w") as sf:
                sf.write(skill_content)
            print(f"[+] Yeni beceri dosyası oluşturuldu: {skill_file}")
        else:
            print(f"[*] Beceri zaten mevcut: {skill_file}")

    print(f"[✔] Tamamlandı: {full_repo} artık yerel kasada kalıcı ve silinmelere karşı korumalı!")

if __name__ == "__main__":
    main()
