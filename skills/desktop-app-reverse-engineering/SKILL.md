---
name: desktop-app-reverse-engineering
description: Reverse engineering, architecture extraction, and clean-room recreation of Electron and native desktop applications inspired by desktop/desktop and modern decompilation workflows.
---

# Desktop Application Reverse Engineering & Architecture Extraction

## Overview
Inspired by the industry-standard architecture of `desktop/desktop` (GitHub Desktop) and modern desktop decompilation workflows, this skill guides the deep reverse engineering of Electron, React, and native macOS desktop applications.

## Key Vectors of Investigation
1. **Packaging & Bundle Deconstruction:**
   - Locate and unpack `.asar` archives (`/Applications/<App>.app/Contents/Resources/app.asar`).
   - Extract bundled webpack/vite assets, source maps, and transpiled React/TypeScript trees.
   - De-minify bundled code into readable structural models.
2. **Process Architecture & IPC Audit:**
   - Trace communication across Electron's Main process (`BrowserWindow`, native OS bridge) and Renderer processes (`React`, UI state).
   - Inspect `contextBridge.exposeInMainWorld` APIs, `ipcRenderer.invoke`, and `ipcMain.handle` message contracts.
   - Identify undocumented local RPC interfaces, WebSocket daemon listeners, and local loopback API servers.
3. **Data Storage & Credential Mechanics:**
   - Audit local application state in `~/Library/Application Support/<App>/`.
   - Inspect embedded SQLite, IndexedDB, LevelDB, and Chromium LocalStorage stores.
   - Trace keychain/keytar integration for stored tokens and API credentials.
4. **Clean-Room Feature Recreation:**
   - Recreate observed desktop capabilities, reactive UI states, and Git/filesystem orchestration cleanly without copying proprietary source code.

## Tooling & Fast Commands
- Extract Electron bundle: `npx @electron/asar extract <app.asar> <output-dir>`
- List contents: `npx @electron/asar list <app.asar>`
- Trace IPC & Native Calls: `rea-agents list-electron-targets` & `rea-agents observe-javascript-runtime`

## Application in Active Projects
- **Desktop UI Design:** Reverse engineer proprietary desktop interfaces to extract component hierarchies, CSS layouts, and animation curves.
- **Guner AV:** Audit third-party desktop utilities, detect vulnerable Electron frameworks with outdated Chromium runtimes, and inspect native Node.js addons (`.node` Mach-O binaries).
