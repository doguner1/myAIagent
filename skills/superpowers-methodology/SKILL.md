---
name: superpowers-methodology
description: Complete software development methodology for coding agents: spec elicitation, plan design, subagent-driven development, strict TDD, and evidence-based verification inspired by obra/superpowers.
---

# Superpowers Agentic Software Development Methodology

## Overview
Inspired by `obra/superpowers`, this skill equips AI coding agents with a structured, disciplined software engineering framework. Rather than jumping directly into uncontrolled code writing, agents follow a rigorous cycle: spec teasing, interactive design review, implementation planning, subagent execution, red/green TDD, and proof-based completion verification.

## Core Phases & Disciplines

### 1. Spec Elicitation & Brainstorming (`brainstorming`)
- Interactively interrogate requirements before writing a single line of code.
- Present designs and architectural trade-offs in bite-sized, readable chunks for user sign-off.
- Anchor decisions in YAGNI (You Aren't Gonna Need It) and simplicity.

### 2. Implementation Planning (`writing-plans` & `executing-plans`)
- Break complex epics into atomic engineering steps.
- Formulate instructions so clear that an isolated subagent with zero project context can follow them deterministically without drift.
- Group independent tasks for parallel agent execution (`dispatching-parallel-agents`).

### 3. Test-Driven Development (`test-driven-development`)
- Enforce strict Red-Green-Refactor cycles:
  1. Write failing test that defines acceptance criteria.
  2. Implement minimum viable code to pass.
  3. Refactor cleanly under test protection.
- Ban assertions that always pass or mock away the actual failure domain.

### 4. Git Worktrees & Clean Branches (`using-git-worktrees`)
- Use isolated Git worktrees for non-destructive experimentation and multi-agent branch isolation.
- Structured branch teardown and merge reviews (`finishing-a-development-branch`).

### 5. Verification Before Completion (`verification-before-completion`)
- Demand concrete proof before claiming success:
  - Terminal output, test suite green status, build artifacts.
  - No claims without reproducible command evidence.
- Run rigorous code review intake (`receiving-code-review`).

## Agent Activation & Rules
- Trigger this methodology when embarking on:
  - New multi-step features or system components.
  - Complex architectural refactors.
  - Autonomous multi-agent development runs.
  - Tasks requiring strict TDD and test coverage gates.
