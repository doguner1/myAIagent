---
name: evolution-api-gateway
description: Open-source REST API and multi-channel messaging gateway for WhatsApp (Baileys WhatsApp Web & Meta Cloud API), Typebot, Chatwoot, Dify, and event queues (RabbitMQ, Kafka, SQS, Webhooks). Inspired by evolution-foundation/evolution-api.
---

# Evolution API Messaging Gateway & WhatsApp Integration

## Overview
Inspired by `evolution-foundation/evolution-api`, this skill equips agents to architect, deploy, and integrate open-source, multi-instance WhatsApp and omnichannel messaging backends. It bridges conversational AI agents with real-world messaging channels (WhatsApp, Typebot, Chatwoot, Dify, n8n) via standardized REST APIs and asynchronous event pipelines.

## Architectural Capabilities

### 1. WhatsApp Connection Modes
- **Baileys Engine (WhatsApp Web Multi-Device):**
  - QR Code or Pairing Code authentication.
  - Multi-instance support (multiple phone numbers managed simultaneously on a single server).
  - Handles text, media, location, contacts, reactions, buttons, and interactive lists.
  - Presence management, typing indicators, read receipts, and status/story publishing.
- **WhatsApp Cloud API (Meta Official):**
  - Enterprise-grade, official Meta Graph API integration.
  - Business templates, HSM messages, interactive buttons, and verified business identity.

### 2. Native AI & Bot Integrations
- **Typebot Integration:** Direct webhook forwarding to visual flow conversational bots.
- **Chatwoot Live Support:** Bidirectional omnichannel inbox for human-in-the-loop support escalation.
- **Dify & Flowise:** Automated pipeline execution with LLM agent backends.
- **OpenAI / Custom AI Agents:** Native integration for automated query completion and intent classification.
- **n8n / Zapier:** Webhook event triggers for low-code automation flows.

### 3. Asynchronous Event Streams & Reliability
- **Event Forwarding:** Webhooks, WebSockets, RabbitMQ, Apache Kafka, Amazon SQS, NATS, and Pusher.
- **State & Session Persistence:** PostgreSQL (Prisma ORM) for database storage and Redis for high-speed session caching and instance lock management.
- **Media Storage:** Amazon S3 / MinIO compatible object storage integration for incoming and outgoing voice notes, PDFs, images, and videos.

## Deployment & Operational Standards
- **Docker Deployment:**
  ```bash
  docker run -d \
    --name evolution-api \
    -p 8080:8080 \
    -e AUTHENTICATION_API_KEY=YOUR_SECURE_API_KEY \
    -e SERVER_PORT=8080 \
    -v evolution_instances:/evolution/instances \
    atendai/evolution-api:v2.3.7
  ```
- **Port Discipline:** Confined to `localhost:8080` (or routed through a local reverse proxy if multi-tenant UI is needed). Never expose without authentication.
- **Security & Hygiene:**
  - Mandatory global API Key (`AUTHENTICATION_API_KEY`).
  - Webhook secret verification to prevent forgery.
  - Encrypted credential storage for WhatsApp session keys.
  - Respect Meta rate limits and anti-ban safeguards when operating Baileys instances.

## Common Agent Workflows
- **Outreach & Notification:** Dispatching transaction confirmations, verification codes, or alert notifications via WhatsApp.
- **Conversational Support:** Ingesting inbound customer messages via webhook, routing to autonomous triage agents, and replying asynchronously.
- **Omnichannel Escalation:** Handing off customer context from autonomous agent to human agents inside Chatwoot when human escalation is triggered.
