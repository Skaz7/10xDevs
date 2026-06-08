---
project: Embedded Projects Assistant
version: 1
status: draft
created: 2026-05-25
context_type: greenfield
product_type: web-app
target_scale:
  users: small
timeline_budget:
  mvp_weeks: 3
  after_hours_only: true
  hard_deadline: null
---

## Vision & Problem Statement

Users interested in electronics and embedded systems hobby projects today face workflow friction: they must manually check the components they already have on hand, then manually search for projects that match their inventory. This process is tedious and discourages project discovery. The market for this use case is niche enough that no mainstream platform has tackled it — existing component databases and project repositories don't connect to each other or to a user's personal inventory.

## User & Persona

**Primary Persona: The Electronics Hobbyist**

Hobbyist electronics enthusiasts worldwide (Arduino tinkerers, ESP32 makers, retro-computing fans, general DIY electronics builders) who own a collection of components and devices and are looking for their next project. They have the technical knowledge to understand datasheets and follow assembly guides, but lack a systematic way to discover projects that match what they already own. They're distributed across many regions and communities.

## Success Criteria

### Primary
A hobbyist can log in, view their parts inventory, describe a project they want to build ("weather station"), and receive a matching project recommendation with the full parts list from the AI agent.

### Secondary
The system shows where missing parts can be purchased and estimated costs (nice-to-have for v1; can be added later).

### Guardrails
- User privacy: each user's parts inventory remains private and is never shared or exposed
- Accuracy of parts matching: project recommendations must be reliable; false matches or incorrect parts lists damage trust

## User Stories

### US-01: Discover a matching project by inventory
**Given** a hobbyist has logged in and added their parts to their inventory,
**When** they describe a project they want to build ("weather station"),
**Then** the AI agent searches the web, finds weather station projects, checks which ones the hobbyist can build with their current parts, and shows ranked recommendations with full parts lists.

## Functional Requirements

### Parts Inventory
- FR-001: Hobbyist can add electronic parts/devices to their personal inventory. Priority: must-have
  > Socrates: Free-form entry is fine for MVP; input validation will prevent non-electronic items (e.g., "chicken").
- FR-002: Hobbyist can search/filter their parts inventory by name or category. Priority: must-have
  > Socrates: Search is essential even for small inventories; kept as must-have.
- FR-003: Hobbyist can edit (modify quantities/details) or remove parts from their inventory. Priority: must-have
  > Socrates: Direct edit/remove is acceptable for MVP; historical tracking can be added later if needed.

### Project Recommendation
- FR-004: Hobbyist can enter a project description in natural language (e.g., "weather station") to the AI agent. Priority: must-have
  > Socrates: Natural language is core to the user experience and differentiates this from category-based discovery; kept.
- FR-005: AI agent can search the web for projects matching the hobbyist's description and check against available parts. Priority: must-have
  > Socrates: Web search + matching is the core value proposition; complexity accepted.
- FR-006: Hobbyist can view project recommendations ranked by how many parts they already own. Priority: must-have
  > Socrates: Ranking by "parts you already own" provides clear, useful ordering without hidden algorithmic bias; kept.
- FR-007: Hobbyist can accept a recommended project and save it to their account. Priority: must-have
  > Socrates: Users need to save projects they decide on; ephemeral results would be frustrating.

### Export & Information
- FR-008: Hobbyist can export a project (description + parts list) to PDF format. Priority: must-have
  > Socrates: PDF is a portable, printable format that matches the user's stated workflow (print at home); kept.
- FR-009: System can estimate costs for missing parts and suggest purchase sources (e.g., eBay, Amazon, local electronics stores). Priority: nice-to-have
  > Socrates: Already prioritized as nice-to-have; complexity deferred to v2.

## Non-Functional Requirements

- **Response time**: User-perceived search and matching completes in under 15 seconds so the experience feels responsive and iteration is practical.
- **Privacy**: User parts inventory is always private to that user; never shared, aggregated, or visible to other users or external parties.

## Business Logic

The application decides project feasibility by matching a user's owned parts against project requirements.

The user provides a project description (e.g., "weather station"). The application searches the web for projects matching that description, checks each project's parts against the user's owned parts database, and outputs the project that best matches what the user already owns. The user then decides whether to build the suggested project or ask for another recommendation.

## Access Control

Users log in with email and password to create a persistent account. All users have the same permissions and see the same content — this is a flat user model with no role hierarchy. User inventories are personal (each user has their own list of components); project recommendations are shared across the platform.

## Non-Goals

- **Avoid**: Building our own project recommendation/ranking algorithm. Rely on web search as the source of truth for projects; users see what's available on the web, not a proprietary algorithm.
- **Avoid**: Mobile app for v1; web-first only. Mobile responsiveness and native apps can be added later if demand justifies it.

## Open Questions

1. **Web search integration specifics** — Which web search API or service will be used? How will projects be discovered and indexed? (Block: no; defer to tech-stack selection.)
2. **Parts matching algorithm details** — How granular is the match? Will "resistor 1k" match "resistor" generically, or require exact specifications? (Block: no; implementation detail for tech-stack selection.)
3. **Project source curation** — Will the platform rank/filter projects by community rating, date published, or other quality signals? Or show all raw web results? (Block: no; product refinement post-MVP.)
4. **Parts database coverage** — Is there a pre-existing parts database the system will use, or will users define their own parts via free-form text? (Block: yes; affects UX and matching accuracy.)
5. **Secondary feature (FR-009) prioritization** — When/if should parts pricing and purchase links be added? (Block: no; post-MVP.)
