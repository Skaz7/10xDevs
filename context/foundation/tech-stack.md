---
starter_id: django
package_manager: uv
project_name: embedded-projects-assistant
hints:
  language_family: python
  team_size: solo
  deployment_target: traditional-vps
  ci_provider: github-actions
  ci_default_flow: auto-deploy-on-merge
  bootstrapper_confidence: verified
  path_taken: standard
  quality_override: false
  self_check_answers: null
  has_auth: true
  has_payments: false
  has_realtime: false
  has_ai: true
  has_background_jobs: false
---

## Why this stack

Django is a mature, convention-heavy framework that ships with authentication, ORM, admin panel, and form handling out of the box—all features your project requires (user login, parts inventory CRUD, project management). Python's rich ecosystem (LangChain, OpenAI SDK, BeautifulSoup, WeasyPrint) makes it straightforward to integrate AI agent matching, web search, and PDF export. The 3-week, solo, after-hours timeline benefits from Django's "batteries included" philosophy. You'll deploy to a traditional VPS with GitHub Actions managing tests and deployments on each merge—simple, reliable, and well-documented. The framework's popularity and documentation ensure you can find solutions and community support if you hit friction.
