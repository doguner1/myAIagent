---
name: agent-longterm-memory
description: Long-term persistent episodic and semantic memory for AI agents across sessions and workflows, inspired by akitaonrails/ai-memory.
---

# Agent Long-Term Memory & Context Persistence

## Overview
Based on the architecture of `akitaonrails/ai-memory`, this skill enables AI agents to maintain persistent episodic, structural, and semantic memory across tool boundaries, session boundaries, and model transitions. It eliminates context amnesia, preserves architectural rationale, and ensures work resumes seamlessly.

## Core Principles
1. **Never Start Cold:** Before initializing new tasks, inspect existing state, decisions, and past constraints.
2. **Episodic Logging:** Record critical milestones, user preferences, bug root causes, and explicit negative constraints ("do not do X").
3. **Cross-Agent Handoff:** Structure memory artifacts in deterministic JSON/Markdown so peer agents or future sessions can pick up without re-explaining.

## Memory Dimensions
- **Project Decisions:** Why a specific library, API pattern, or architecture was selected.
- **Quota & Platform Realities:** Rolling window timestamps, rate limits, token constraints.
- **Negative Constraints:** Failed approaches that must never be repeated.
- **Entities & Artifacts:** Paths, IDs, and endpoints of active resources.

## Application in Active Projects
- **Doğukan & Pixlabss Shorts:** Preserves `pending_pool.json`, YouTube 24-hour quota windows, and processed video IDs to prevent duplicate work or wasted API calls.
- **Guner AV & iOS Tweaks:** Records kernel offsets, rootless paths (`/var/jb/`), daemon power states, and Mach-O symbols across debugging sessions.
