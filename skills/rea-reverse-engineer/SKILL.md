---
name: rea-reverse-engineer
description: Autonomous reverse engineering across binaries, desktop applications, Electron bundles, and runtime behavior using morluto/rea and the REA MCP server.
---

# REA: Reverse Engineer Anything (morluto/rea)

## Overview
Based on `morluto/rea` (CLI: `/opt/homebrew/bin/rea-agents`, MCP: `rea`), this skill connects the agent to an elite reverse engineering toolkit capable of analyzing native binaries (Mach-O, ELF, PE), mobile packages (APK, IPA), and packaged desktop applications (Electron, React, Node.js) with 207 deep inspection tools.

## Core Capabilities
1. **Desktop & Electron App Deconstruction:**
   - Unpack Electron `.asar` bundles and analyze packaged JavaScript/TypeScript apps.
   - Recover readable frontend code, React components, and state management logic.
   - Trace IPC communication channels (`ipcRenderer` <-> `ipcMain`), secret endpoints, and local storage/SQLite databases.
2. **Native Binary Disassembly & Decompilation:**
   - Disassemble and decompile functions, extract control flow graphs (CFGs), and resolve cross-references (`xrefs`).
   - Parse executable headers (Mach-O `LC_LOAD_DYLIB`, dynamic library bindings, code signing entitlements).
   - Trace native UI actions to their underlying Objective-C/C++ handlers.
3. **Dynamic Runtime Observation:**
   - Observe native calls under LLDB and record entries into Objective-C methods and exported symbols.
   - Instrument processes dynamically using Frida (`instrument-with-frida`).
   - Passively inspect V8 Inspector/Electron CDP runtime targets.

## Command-Line & MCP Usage
- **CLI Commands:**
  - `rea-agents analyze-mach-o <binary-path>`
  - `rea-agents analyze-javascript-application <dir>`
  - `rea-agents recover-javascript-sources <bundle>`
  - `rea-agents decompile --address <addr>`
  - `rea-agents trace-application-feature <seed>`
  - `rea-agents inspect-sqlite-database <db-path>`
- **MCP Server:** Configured under `"rea"` in `~/.gemini/config/mcp_config.json` with 207 specialized tools available for automated agent invocation.

## Application in Active Projects
- **Guner AV:** Analyze malware samples, deconstruct packing/obfuscation techniques, and extract structural signatures without executing malicious payloads.
- **iOS 15.8.x Dopamine Tweaks:** Trace SpringBoard and system daemon methods to locate exact selectors for ElleKit/Substrate hooking.
- **Product Feature Extraction:** Inspect proprietary desktop applications to understand how complex features are built and recreate clean-room implementations.
