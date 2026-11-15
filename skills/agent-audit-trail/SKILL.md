---
name: agent-audit-trail
description: Immutable event-sourced audit logging, deterministic state recording, and execution tracing for autonomous AI agents, inspired by apache/maka.
---

# Agent Audit Trail & Execution Observability (Apache Maka)

## Overview
Based on `apache/maka` (Incubating), this skill governs the recording, event-sourcing, and auditing of all actions, tool calls, and state transitions performed by autonomous agent pipelines.

## Audit Principles
1. **Event-Sourced Traceability:**
   - Record inputs, intermediate tool outputs, external API responses, and final actions in deterministic logs.
2. **Crash & Quota Forensics:**
   - When an unhandled error or platform rate-limit occurs, persist the complete execution snapshot so subsequent runs can diagnose root cause or resume without data loss.
3. **Sensitive Data Redaction:**
   - Ensure OAuth tokens, passwords, and API secrets are never written into persistent trace logs or committed to repositories.

## Application in Active Projects
- **ViralShortsClipper GitHub Workflows:** Provides structured JSON logs (`upload_receipts.json`, `pending_pool.json`, `latest_plan.json`) committed via GitHub Actions, giving full transparency into every automated run.
