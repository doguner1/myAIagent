---
name: openseo-intelligence
description: Open-source SEO intelligence, competitor auditing, keyword research, rank tracking, backlink analysis, and AI search visibility (GEO/AEO) inspired by every-app/open-seo.
---

# OpenSEO Intelligence & AI Visibility Suite

## Overview
Inspired by `every-app/open-seo`, this skill empowers agents to execute data-driven search engine optimization, competitor intelligence, technical site audits, and AI Visibility (Generative Engine Optimization / GEO). It operates as an open-source, pay-as-you-go alternative to Semrush and Ahrefs with native MCP connectivity.

## Core Capabilities & Workflows

### 1. Keyword Research & Opportunity Discovery
- **Search Volume & Intent:** Analyze query metrics, keyword difficulty (KD), CPC, and search intent (Informational, Commercial, Navigational, Transactional).
- **Long-Tail Expansion:** Uncover high-intent questions and long-tail variants to dominate niche search clusters.
- **SERP Feature Mapping:** Identify featured snippets, "People Also Ask" (PAA), local packs, and knowledge panels.

### 2. Competitor Intelligence & Gap Analysis
- **Domain Comparisons:** Benchmark domain authority, organic traffic volume, and ranking distributions against direct competitors.
- **Keyword Gap:** Pinpoint keywords where competitors rank on Page 1 but your domain does not.
- **Content Footprint:** Audit competitor top-performing URLs and topic authority.

### 3. Backlink Auditing & Authority Building
- **Backlink Profile:** Ingest referring domains, total backlinks, dofollow/nofollow ratios, and domain quality tiers.
- **Anchor Text Distribution:** Detect unnatural anchor patterns or opportunities for targeted brand anchoring.
- **Toxic Link Identification:** Flag spammy links for disavow preparation.

### 4. Technical Site Audit & Core Web Vitals
- **Crawlability & Indexation:** Inspect robots.txt, XML sitemaps, canonical tags, noindex directives, and HTTP status codes (301, 302, 404, 500).
- **On-Page Optimization:** Audit title tags, meta descriptions, H1-H6 semantic hierarchy, OpenGraph tags, and image alt attributes.
- **Structured Data:** Validate JSON-LD schemas (Article, Organization, FAQPage, Product).

### 5. AI Search Visibility & GEO (Generative Engine Optimization)
- **AI Citation Auditing:** Track how often and in what context your brand appears in LLM responses (ChatGPT Search, Perplexity, Google AI Overviews, Gemini).
- **Prompt Share-of-Voice:** Measure mention frequency across industry query sets in AI answer engines.
- **Citation Source Tracking:** Identify which web domains AI models cite most frequently for your target keywords.

## Architecture & Integration
- **MCP Server Support:** Native MCP server allows AI agents to directly query DataForSEO endpoints and internal OpenSEO databases without manual UI interaction.
- **Self-Hosting Options:**
  - Docker Compose / Standalone container (`localhost:3000` or portless background job).
  - Cloudflare Workers + D1 database for serverless zero-idle deployments.
- **Data Engine:** Powered by direct DataForSEO API integration (pay-per-request model, zero bloated SaaS subscription costs).

## Agent Guidelines & Prompt Triggers
- Trigger this skill when the user asks to:
  - "Run an SEO audit on <domain>"
  - "Research keywords for <topic>"
  - "Compare my site against competitor <domain>"
  - "Track my rank / search visibility"
  - "Check my AI search / ChatGPT / Perplexity visibility"
  - "Audit backlinks or disavow toxic links"
