---
name: youtube-automation-agent
description: Autonomous end-to-end YouTube channel automation: topic research, scriptwriting, voice narration, visual generation, video rendering (MP4), metadata SEO, and human-in-the-loop scheduled publishing inspired by darkzOGx/youtube-automation-agent.
---

# YouTube Automation Agent

## Overview
Inspired by `darkzOGx/youtube-automation-agent`, this skill orchestrates an autonomous, self-hosted pipeline to operate a YouTube channel or YouTube Shorts brand end-to-end. Designed around a "human-in-the-loop" philosophy, the agent autonomously executes the research, creative, and technical production steps while holding final video upload for operator approval.

## Pipeline Architecture & Capabilities

### 1. Topic Research & Trend Discovery
- Monitor niche topics, competitor channels, and viral velocity.
- Score topic viability based on search demand, audience interest, and channel mandate alignment.
- Maintain an editorial calendar and queue of validated video proposals.

### 2. Scriptwriting & Storyboarding
- Generate high-retention video scripts tailored to YouTube formats (Long-form or Shorts/Reels).
- Formulate hook-driven introductions (first 3-5 seconds), pacing curves, and call-to-actions (CTAs).
- Produce time-coded visual cues and audio narration blocks.

### 3. Media Asset Generation & Voiceover
- **Narration (TTS):** Integrate with state-of-the-art voice synthesis (ElevenLabs, OpenAI TTS, EdgeTTS) for natural, emotive pacing.
- **Visuals & B-roll:** Automated prompt generation for AI image/video engines (Midjourney, DALL-E, Stable Diffusion, Runway, Pika) or local slideshow assemblers.
- **Audio Engineering:** Automatic ducking, sound effects (SFX) placement, and copyright-safe background music layering.

### 4. Video Assembly & Rendering
- Automated FFmpeg / Node-canvas video compilation into production MP4 files.
- Dynamic subtitle rendering with word-by-word highlights and responsive formatting.
- Real-time render progress tracking and visual artifact quality checks.

### 5. Metadata SEO & Publishing Gateway
- Generate click-worthy, non-clickbait titles, keyword-rich descriptions, chapters, and tags.
- Direct YouTube Data API v3 integration for automated draft uploading or scheduled publishing upon explicit human sign-off.
- Analytics feedback ingestion: parse viewer retention drop-offs, click-through rates (CTR), and comments to refine future video generation runs.

## Operational Discipline
- **Human Approval Gate:** Finished videos wait for operator fact review and media rights confirmation. Autonomy never bypasses the approval gate.
- **Portless / Local First:** Runs locally with your own API keys without external SaaS vendor lock-in.
