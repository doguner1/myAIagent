---
name: ghidra-reverse-engineering
description: Software reverse engineering, ARM64 Mach-O disassembly, decompilation, and tweak offset discovery inspired by NSA Ghidra.
---

# Software Reverse Engineering & Binary Analysis (Ghidra Framework)

## Overview
Based on NSA's `ghidra`, this skill guides disassembly, decompilation, binary patching, and symbol analysis across Mach-O, ELF, and PE binaries, with specialized focus on ARM64 and iOS rootless tweak development.

## Reverse Engineering Methodology
1. **Binary Ingestion & Header Analysis:**
   - Parse executable headers (Mach-O `LC_LOAD_DYLIB`, `LC_SEGMENT_64`, code signing entitlements).
   - Identify architecture, endianness, ASLR slide behavior, and symbol tables.
2. **Decompilation & Control Flow Analysis:**
   - Trace function calls, class interfaces (Objective-C runtime metadata, Swift vtables).
   - Identify cross-references (`XREFs`) to locate hookable methods or cryptographic routines.
3. **Hook Formulation & Offset Identification:**
   - Locate memory offsets or Objective-C selectors for Substrate/ElleKit hooking.
   - Analyze calling conventions (ARM64 `X0-X7` register passing) for safe `%orig` execution.

## Application in Active Projects
- **iPhone 7 (iOS 15.8.x Dopamine 2 Rootless):** Reverse-engineer SpringBoard and system daemons to develop stable rootless tweaks without causing respring loops.
- **Guner AV:** Analyze suspicious binary samples, unpack packed executables, and derive detection signatures from disassembly graphs.
