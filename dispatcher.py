#!/usr/bin/env python3
"""
Just-In-Time Skill & Tool Dispatcher
Inspects a target project directory, identifies tech stack and domain,
and recommends ONLY the necessary mirrored skills and tools from the vault.
"""
import os
import sys
import json

VAULT_REGISTRY = "/Users/qwerty/Desktop/ai/vault_registry.json"

RULES = {
    "youtube_media": {
        "keywords": ["youtube", "video", "shorts", "ffmpeg", "tts", "elevenlabs", "audio", "subtitle", "remotion", "hyperframes", "shotcraft"],
        "files": ["video", "render", "audio", "script", "remotion.config.ts"],
        "skills": ["remotion-video", "video-shotcraft", "hyperframes", "youtube-automation-agent", "agency-video-optimization-specialist", "offline-grammar-checker"],
        "tools": ["remotion", "video-shotcraft", "hyperframes", "youtube-automation-agent", "agent-reach", "harper"]
    },
    "security_reverse_engineering": {
        "keywords": ["macho", "arm64", "tweak", "jailbreak", "dopamine", "hook", "cydia", "theos", "reverse", "decompil", "antivirus", "malware"],
        "files": ["Makefile", "control", "Tweak.x", "Tweak.xm", "RootListController"],
        "skills": ["ghidra-reverse-engineering", "autonomous-redteam-pentest", "desktop-app-reverse-engineering", "rea-reverse-engineer"],
        "tools": ["ghidra", "rea", "decepticon", "desktop"]
    },
    "seo_growth_marketing": {
        "keywords": ["seo", "keyword", "serp", "backlink", "competitor", "sitemap", "crawler", "semrush", "ahrefs", "geo"],
        "files": ["robots.txt", "sitemap.xml", "llms.txt"],
        "skills": ["openseo-intelligence", "agency-seo-specialist", "agency-baidu-seo-specialist", "agency-growth-hacker"],
        "tools": ["open-seo", "agent-reach", "api-anything"]
    },
    "messaging_whatsapp_bots": {
        "keywords": ["whatsapp", "baileys", "typebot", "chatwoot", "bot", "messaging", "dify", "webhook", "sms"],
        "files": ["bot", "message", "whatsapp"],
        "skills": ["evolution-api-gateway", "agency-api-platform-engineer"],
        "tools": ["evolution-api", "api-anything"]
    },
    "frontend_ui_web": {
        "keywords": ["react", "vue", "tailwind", "next", "vite", "frontend", "ui", "ux", "css", "html", "penpot", "impeccable", "diagram"],
        "files": ["package.json", "tailwind.config.js", "vite.config.ts", "next.config.js"],
        "skills": ["ui-ux-pro-max", "impeccable", "diagram-design", "penpot", "frontend-design", "agency-frontend-developer", "agency-ui-designer"],
        "tools": ["ui-ux-pro-max-skill", "impeccable", "penpot", "diagram-design"]
    },
    "3d_webgl_blender": {
        "keywords": ["blender", "three.js", "threejs", "webgl", "3d", "canvas", "mesh", "gltf", "fbx", "shader"],
        "files": ["three", "blend", "model", "scene"],
        "skills": ["img2threejs", "mcp-for-blender", "agency-3d-scene-developer", "agency-technical-artist"],
        "tools": ["img2threejs", "mcp-for-blender"]
    },
    "automotive_cockpit_cluster": {
        "keywords": ["car", "cluster", "cockpit", "automotive", "ivi", "chery", "canbus", "vdbus", "dash", "gauge", "speedometer"],
        "files": ["cluster", "cockpit", "qnx", "navi", "car"],
        "skills": ["lemo-opuscar", "rea-reverse-engineer", "desktop-app-reverse-engineering"],
        "tools": ["lemo-opuscar", "rea", "desktop"]
    },
    "backend_api_database": {
        "keywords": ["postgres", "mysql", "sqlite", "prisma", "drizzle", "fastapi", "express", "api", "database", "docker"],
        "files": ["Dockerfile", "docker-compose.yml", "schema.prisma", "migrations"],
        "skills": ["agency-backend-architect", "agency-database-optimizer", "agency-api-tester", "api-anything"],
        "tools": ["codebase-memory-mcp", "api-anything"]
    },
    "agentic_architecture_tdd": {
        "keywords": ["agent", "llm", "prompt", "subagent", "eval", "benchmark", "tdd", "refactor"],
        "files": ["test", "tests", "spec", "AGENTS.md", "CLAUDE.md"],
        "skills": ["superpowers-methodology", "agent-longterm-memory", "task-observer", "caveman", "safe-refactor", "tdd"],
        "tools": ["superpowers", "ai-memory", "one-skill-to-rule-them-all", "caveman"]
    }
}

def analyze_target(target_path):
    if not os.path.exists(target_path):
        return {"error": f"Path not found: {target_path}"}
    
    file_list = []
    text_content = ""
    for root, dirs, files in os.walk(target_path):
        # Ignore .git, node_modules, etc.
        dirs[:] = [d for d in dirs if d not in [".git", "node_modules", ".venv", "dist", "build", "repos"]]
        for f in files:
            file_list.append(f.lower())
            if f in ["package.json", "README.md", "requirements.txt", "Makefile", "control", "Cargo.toml"]:
                try:
                    with open(os.path.join(root, f), "r", errors="ignore") as fp:
                        text_content += " " + fp.read(4000).lower()
                except:
                    pass

    scores = {}
    matched_skills = set()
    matched_tools = set()

    all_tokens = " ".join(file_list) + " " + text_content

    for category, cfg in RULES.items():
        score = 0
        for kw in cfg["keywords"]:
            if kw in all_tokens:
                score += 1
        for fl in cfg["files"]:
            if any(fl in fn for fn in file_list):
                score += 2
        
        if score > 0:
            scores[category] = score
            for s in cfg["skills"]:
                matched_skills.add(s)
            for t in cfg["tools"]:
                matched_tools.add(t)

    sorted_categories = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    return {
        "target": target_path,
        "matched_categories": [c[0] for c in sorted_categories[:3]],
        "recommended_skills": list(matched_skills)[:6],
        "active_mirrored_tools": list(matched_tools)[:4],
        "all_other_skills_status": "DORMANT (Belleğe yük bindirmez, sıfır token/RAM tüketimi)"
    }

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "/Users/qwerty/Desktop/ai"
    result = analyze_target(path)
    print(json.dumps(result, indent=2, ensure_ascii=False))
