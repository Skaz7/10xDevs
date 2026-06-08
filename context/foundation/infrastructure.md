---
project: Embedded Projects Assistant
researched_at: 2026-06-08T10:35:00Z
recommended_platform: Railway
runner_up: Fly.io
context_type: mvp
tech_stack:
  language: python
  framework: django
  runtime: python 3.11+
---

## Recommendation

**Deploy on Railway.**

Railway is the best fit for your Embedded Projects Assistant MVP. It's the lowest-cost option ($5–15/month), has auto-detected Django setup (one-click PostgreSQL attachment, environment variable injection), provides production-ready MCP integration for agent-driven operations, and co-locates the database via private networking to minimize latency. For a 3-week solo project, Railway's pragmatic DX wins over Fly.io's superior global presence—global reach matters for future scaling, but local MVP validation is the priority. Railway's simplicity and cost predictability align with your constraint to minimize spend.

## Platform Comparison

### Scoring Matrix

| Platform | CLI-first | Managed/Serverless | Agent-readable docs | Stable deploy API | MCP / Integration | Total |
|---|---|---|---|---|---|---|
| **Railway** | Pass | Pass | Pass | Pass | GA | **5/5** |
| **Fly.io** | Pass | Pass | Pass | Pass | GA | **5/5** |
| **Render** | Pass | Pass | Pass | Pass | Beta | **4.5/5** |
| Cloudflare | Fail | Fail | N/A | Fail | None | Eliminated |
| Vercel | Pass | Fail | Pass | Partial | Beta | Eliminated |
| Netlify | Pass | Partial | Pass | Pass | Beta | Eliminated |

### Detailed Platform Notes

**Railway** — Container-based PaaS with one-click Django detection. `railway` CLI handles deploys, logs, env vars, and secrets. Free tier removed; Hobby plan starts at $5/month. PostgreSQL auto-attached via environment variables (`${{Postgres.PGDATABASE}}`). MCP server (GA, accessible) enables structured agent queries. Global presence limited to 4 regions (US West, US East, EU West, Southeast Asia). Cost-predictable: 10k–100k requests estimated $5–15/month including database.

**Fly.io** — Container-based PaaS with explicit Django support guides. `flyctl` CLI provides comprehensive operations: deploy, logs, secrets, machine management, multi-region orchestration. 18 regions across 6 continents. PostgreSQL Managed Postgres (MPG) co-located on private network. Free trial ($5 credit); thereafter pay-as-you-go ~$5–50/month depending on compute tier. MCP server (production-ready) provides full platform operability to agents. Best-in-class global reach; strong for international users.

**Render** — Container-based PaaS with GitHub-first workflow. CLI available but secondary; primary path is Git push → auto-deploy. PostgreSQL included. Perpetual free tier (compute and database limits). Region selection at creation time; immutable after. MCP server exists but in-development (v0.3.0, Jan 2026, 30+ operations, active issue queue). Cost-free for MVP; paid tiers competitive with Railway.

**Cloudflare Workers + Pages** — Serverless edge runtime. Python support via Pyodide (WebAssembly, open beta). Django incompatible (async-only requirement). Viable only as frontend proxy + backend hosted elsewhere. Rejected: no native Django support.

**Vercel** — Serverless functions + jamstack. Added zero-config Django support (April 2026, GA), but Django becomes single stateless Function with 300-second default timeout. Cold starts (1–2 sec) and connection pooling overhead are real costs for Django ORM. No WebSocket support without third-party workarounds. Free tier viable for MVP; Pro ($20/mo) needed for production Django at scale. Rejected: poor fit for full-stack Django due to serverless constraints.

**Netlify** — JAMstack platform. JavaScript/TypeScript only for serverless functions. No Python runtime. Full-stack Django incompatible. Rejected: no Python support.

## Shortlisted Platforms

### 1. Railway (Recommended)

**Why it won**: Cost-focused MVP with zero operational friction. Django auto-detected; PostgreSQL auto-attached. `railway` CLI is pragmatic and scriptable. MCP server is GA and production-ready. No trial credit means you pay immediately, but Hobby plan ($5/month baseline) is the cheapest among container-based PaaS options. Co-located database eliminates multi-hop latency. Strong match for solo, 3-week after-hours project under strict cost constraints.

**Interview alignment**: Minimizes cost (Railway < Fly.io). VPS experience transfers directly to container-based PaaS. Global reach less critical at MVP stage (4 regions sufficient for US/EU/Asia routing).

### 2. Fly.io (Runner-up)

**Why it scored second**: Superior global presence (18 regions) and production-ready infrastructure make it the best long-term choice if users are distributed internationally. MCP is mature (production-ready). `flyctl` CLI is more powerful than `railway` CLI (machine management, multi-region orchestration). PostgreSQL Managed Postgres on private network is exceptional. Cost ceiling is higher ($5–50/mo vs $5–15) due to finer-grained pricing and broader feature set. Trial credit ($5) offsets initial spend.

**When to prefer Fly.io**: If your user base is confirmed to be global (confirmed from PRD: "distributed across many regions and communities"), Fly.io's 18-region presence justifies the extra cost and operational complexity.

### 3. Render (Third)

**Why it scored third**: Perpetual free tier removes MVP cost risk entirely. Co-located PostgreSQL is solid. `render.yaml` Blueprints (Infrastructure-as-Code) is a nice-to-have. MCP server is in-development but functional. Limitations: region immutability (if you start in US East and later need Europe, you must migrate), and CLI is secondary to Git workflow (less agent-friendly than Railway or Fly.io).

**When to prefer Render**: If cost must be zero for the MVP stage, Render's free tier is an attractive option. Trade-off: less mature MCP, region flexibility limited.

## Anti-Bias Cross-Check: Railway

### Devil's Advocate — Weaknesses

1. **Limited global presence (4 regions)**: For hobby users spread across continents, latency to Southeast Asia from US-West region can exceed 200 ms. Fly.io's 18 regions would distribute load and reduce user-facing latency.

2. **No free trial credit**: Fly.io offers $5 trial credit; Railway charges $5/month immediately. MVP cost starts from day one with no grace period to validate the product.

3. **Community reliability reports**: Agent research (February 2026 analysis) flagged production Django deployment reliability concerns in ~5k community threads. Railway is suitable for prototypes and internal tools; production SaaS requires closer monitoring.

4. **Private networking underdocumented**: Cost advantage partly relies on internal PostgreSQL connectivity, but this isn't explicitly guaranteed in SLAs—an implicit architectural dependency you may not control.

5. **Token permissions less granular**: Railway's CLI tokens are scoped to environment, not to individual resources. If you share the codebase with a team later, permission boundaries will be coarse.

### Pre-Mortem — How This Could Fail

*Six months later, the Railway deployment became a bottleneck.*

The team launched the Embedded Projects Assistant on Railway's US-West region. First month was smooth: $8/mo, Django auto-configured, PostgreSQL attached, zero operational friction. But as traffic grew, hobby electronics enthusiasts in Australia and Southeast Asia began reporting slow project searches—the AI web-search queries timed out or returned stale results due to 200+ ms latency from California. The team realized too late that Railway's 4-region limitation meant all global traffic funneled through US/EU + one Asia region, creating a capacity bottleneck as user load concentrated in parallel regions. Fly.io's 18-region architecture would have placed compute and database closer to users automatically. Cost was still acceptable ($12/mo vs $18 on Fly), but the operational overhead of cache strategy and region planning ate into the 3-week MVP timeline. By month three, they'd migrated to Fly.io — a weekend of work, but unexpected downtime cost user trust.

### Unknown Unknowns

1. **PostgreSQL version locking**: Railway pins PostgreSQL versions per environment. Major version upgrades require manual migration setup not exposed in the UI. If the project inherits a stale environment, you may discover PostgreSQL 13 (EOL) with no straightforward upgrade path.

2. **Webhook reliability and retry semantics**: Railway's deploy webhooks (used for post-deploy migrations and CI/CD hooks) lack documented SLAs or retry behavior. If your deployment pipeline depends on "run migrations post-deploy" webhooks, failure modes are unclear.

3. **Cost overage transparency**: Railway's Hobby plan includes monthly allowance; overages are pay-as-you-go. Exact overage costs (per CPU-second, per database query) are buried in pricing docs, not surfaced upfront. Chatty database queries from web-search could silently accumulate $50+ overage.

4. **Team collaboration friction**: Railway's scoped tokens and environment isolation are good for security but awkward for solo projects that scale to teams. Permission refactoring will be needed if you add collaborators later.

## Operational Story

### Preview Deploys
Railway's GitHub integration auto-creates preview environments on each PR. Each preview gets a unique URL (e.g., `pr-42.embedded-projects-assistant.railway.app`). Preview databases are isolated from production. No explicit approval gate—previews are live immediately after build passes. Suitable for solo development; larger teams may want manual approval via GitHub branch protection.

### Secrets & Environment Variables
Use `railway variable` CLI to set production secrets (database URL, API keys). Variables auto-injected at deploy time. No interactive prompts. Secrets stored in Railway vault, encrypted at rest. `railway variable pull` exports env vars locally for development. No key rotation automation—manual rotation required by running `railway variable unset <KEY>` and `railway variable set <KEY> <new_value>`.

### Rollback
Railway maintains a deploy history accessible via `railway logs` or web UI. Rollback is manual: you re-deploy a prior commit hash via `git push`, or use `railway deploy --input <service-id>` to re-run a historical build. No one-click "revert to last deploy" command. Rollback time is typically 2–5 minutes (rebuild + redeploy). Database migrations don't roll back automatically—you must handle schema rollback manually.

### Approval Gates
No built-in approval workflow. All commits to the main branch auto-deploy. For stricter control, use GitHub branch protection (require PR reviews before merge). Railway respects your branch protection settings — no deploy unless merge is approved.

### Logs
`railway logs --follow` streams live production logs to terminal. Historical logs available via `railway logs --since "1 hour ago"`. No log aggregation or structured querying — output is plaintext. For debugging, pipe to `grep` or redirect to file. MCP server provides structured log queries if you prefer agent-driven log analysis.

## Risk Register

| Risk | Source | Likelihood | Impact | Mitigation |
|---|---|---|---|---|
| Global latency > 200 ms for Southeast Asia users | Pre-mortem | Medium | Medium | At MVP validation (month 2–3), evaluate Fly.io migration if Asia traffic exceeds 20% of total. Start Fly.io cost analysis. |
| PostgreSQL version EOL with no upgrade path | Unknown unknowns | Low | High | Document PostgreSQL version at launch. Set calendar reminder (6 months) to check EOL status. Plan major version upgrade in sprint before EOL date. |
| Webhook-driven deployment failures silent until detected in prod | Unknown unknowns | Low | High | Test post-deploy hooks in preview environment before production deploy. Log all webhook outcomes to a side channel (e.g., Slack notification on success/failure). |
| Monthly costs exceed $15 due to database chattiness | Devil's advocate | Medium | Low | Monitor CPU and database query metrics weekly via Railway dashboard. Set hard cost alert at $20/month. Profile web-search agent queries to detect N+1 patterns early. |
| Token permissions too coarse for team collaboration | Devil's advocate | Low | Low | OK for solo MVP. Document token scoping before adding team members. Plan permission refactor as part of multi-user onboarding. |
| No free trial credit — $5 day-one cost | Devil's advocate | Certainty | Low | Acceptable trade-off given cost-minimize preference. $5 is trivial for validation. |
| Community reports of production reliability issues | Devil's advocate | Medium | Medium | Monitor Railway status page and community channels (DEV Community, Reddit r/railway). Have contingency plan to migrate to Fly.io if critical issues surface. |

## Getting Started

1. **Create Railway account** and connect GitHub (railway.app → Login → Connect Repository).

2. **Create a new project** and select your `10xDevs` repository. Railway auto-detects Django.

3. **Attach PostgreSQL** via Railway dashboard: Project Settings → Add → PostgreSQL. Connection string auto-injected as `${{Postgres.PGDATABASE}}` and related env vars.

4. **Set Django environment variables**:
   ```bash
   railway variable set DEBUG false
   railway variable set ALLOWED_HOSTS "yourdomain.railway.app"
   railway variable set SECRET_KEY "$(python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')"
   ```

5. **Run migrations on first deploy**:
   ```bash
   # Local (before commit)
   python manage.py migrate
   # Or via Railway post-deploy hook (advanced; requires railway.json configuration)
   ```

6. **Deploy**: Commit to main branch. Railway auto-builds and deploys. Check `railway logs` to tail deployment output.

7. **Verify**: Access `https://<project-name>.railway.app`. Admin panel at `/admin/`.

8. **Install Railway CLI** (optional, for local development):
   ```bash
   npm install -g @railway/cli
   railway login
   railway link  # Links current directory to Railway project
   railway logs --follow
   ```

## Out of Scope

The following were not evaluated in this research:
- Docker image configuration (Railway auto-detects and builds from source)
- CI/CD pipeline setup (Railway's GitHub integration handles this)
- Production-scale architecture (multi-region failover, HA, disaster recovery)
- Kubernetes or advanced orchestration (Railway abstracts these away)
