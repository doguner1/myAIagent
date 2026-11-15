---
name: offline-grammar-checker
description: High-speed, privacy-first grammar, diction, and phonetic subtitle linting inspired by Automattic/harper.
---

# Offline Grammar, Diction & Subtitle Linter (Harper Architecture)

## Overview
Inspired by Automattic's `harper` (open-source Rust grammar engine), this skill enforces flawless linguistic quality, phonetic readability for neural TTS engines, and visual timing for on-screen subtitles.

## Core Rules & Audits
1. **Phonetic Conversion for Neural Voices:**
   - Raw numerals (`10`, `3`, `100M`) confuse autoregressive neural TTS tokenizers. Always convert numbers to spoken words (`on`, `üç`, `yüz milyon`).
   - Eliminate awkward acronyms unless phonetically spelled.
2. **Punctuation & Breath Pacing:**
   - Use triple dots (`...`) for dramatic acoustic pauses and natural respiration.
   - Avoid double punctuation (`!!`, `??`) in voice scripts.
3. **Subtitle Synchronization Lint:**
   - Chunk subtitles into 1.5–2.5 second perceptual reading windows.
   - Ensure line breaks do not split compound nouns or phrases unnaturally.

## Application in Active Projects
- **Pixlabss Pınar Voice Engine:** Validates spoken scripts before passing to Chatterbox, preventing digital silence artifacts, mispronunciations, and word count drift.
- **Doğukan Shorts Slicer:** Audits generated ASS subtitle files to prevent overflow outside the vertical 1080x1920 safe zone.
