---
name: engineer-core-skills
description: Elite software engineering, architectural discipline, domain modeling, and Wayfinder navigation inspired by mattpocock/skills.
---

# Elite Engineering & Architectural Discipline (Matt Pocock Skills)

## Overview
Synthesizes best practices from `mattpocock/skills` (by Total TypeScript author Matt Pocock), emphasizing type safety, modular domain modeling, Wayfinder orientation, and robust prompt engineering for autonomous agents.

## Core Pillars
1. **Wayfinder Codebase Navigation:**
   - Map module boundaries and data flow before modifying code.
   - Trace entry points, shared state, and external dependencies.
2. **Domain Modeling & Strict Types:**
   - Model the problem domain explicitly with discriminated unions, schemas, and strict data transfer contracts.
   - Parse, don't validate: make invalid states unrepresentable.
3. **Spec-to-Implementation Discipline:**
   - Write or review the exact contract before writing code.
   - Surgical implementation: touch only the layers responsible for the behavior.
4. **Writing for Agents (Agentic DX):**
   - Provide explicit negative constraints, clear schemas, and verified output formats.
   - Keep instructions unambiguous and testable.

## Application in Active Projects
- **ViralShortsClipper & Pixlabss Pipelines:** Ensures clean modularity between creative director, production engine, and uploader engines.
- **TypeScript & Web Projects:** Strict adherence to modern TypeScript/Vite patterns without `any` escapes.
