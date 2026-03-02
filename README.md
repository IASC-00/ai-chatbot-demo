# Project 1: AI Business Assistant Chatbot

## Service Demonstrated
**Custom AI Chatbot & Business Assistant** — clients pay for a tailored chatbot
embedded in their site, trained on their products/services/FAQs.

## Goal
Build a fully functional chatbot demo for a fictional business ("Harbor Coffee Co.")
that answers product questions, handles reservations, and captures leads — showing
exactly what a real client would receive.

## Demo Deliverable
- Live Flask web app with embedded chat widget
- Persona: Harbor Coffee Co. customer support agent
- Handles: menu questions, hours, reservations, complaints, lead capture
- Persistent conversation memory per session
- Admin panel: view conversations, leads, and common questions

## Tech Stack
- Python 3.12
- Flask (web server + API routes)
- Anthropic SDK (Claude claude-haiku-4-5-20251001 for cost efficiency)
- SQLite + SQLAlchemy (conversation + lead storage)
- Vanilla JS chat widget (no framework, embeddable via `<script>` tag)
- Tailwind CSS (via CDN for admin panel)

---

## Roadmap

### Phase 1 — Foundation
- [ ] Create project scaffold: `app.py`, `models.py`, `config.py`
- [ ] Define system prompt: Harbor Coffee Co. persona, menu, hours, policies
- [ ] POST `/api/chat` — accepts `session_id` + `message`, returns AI reply
- [ ] SQLite schema: `conversations(session_id, role, content, ts)`, `leads(name, email, ts)`
- [ ] Basic HTML test page with fetch() to `/api/chat`

### Phase 2 — Chat Widget
- [ ] Build embeddable JS widget (floating button → slide-up panel)
- [ ] Session ID generation (localStorage UUID)
- [ ] Typing indicator animation
- [ ] Message history rendered in widget
- [ ] Lead capture: if user asks about booking → collect name + email → store to DB

### Phase 3 — Business Logic
- [ ] Context injection: inject current day/hours into system prompt dynamically
- [ ] Escalation detection: if Claude can't answer → "I'll have a human follow up"
- [ ] Rate limiting: max 20 messages/session (abuse prevention)
- [ ] Conversation summarization: after 10 turns, summarize context to save tokens

### Phase 4 — Admin Panel
- [ ] `/admin` route (password-protected, env var)
- [ ] View all conversations (paginated, grouped by session)
- [ ] View captured leads table (name, email, timestamp)
- [ ] Common questions summary (manual review view)
- [ ] Export leads as CSV

### Phase 5 — Polish & Demo Packaging
- [ ] Harbor Coffee Co. landing page (hero, menu, contact)
- [ ] Chat widget styled to match fictional brand
- [ ] README with "how to customize for your business" section
- [ ] Record demo GIF / screenshot for portfolio card
- [ ] Deploy to Render.com free tier (or Railway)
- [ ] Add to iswain.dev projects section

---

## Success Criteria
- Chatbot correctly answers 10/10 test questions about Harbor Coffee Co.
- Lead capture works end-to-end (name + email saved to DB)
- Admin panel shows conversation history and leads
- Widget embeds cleanly in a plain HTML page via single `<script>` tag
- Live URL for portfolio demo

## Key Files
```
01-ai-chatbot/
├── app.py              # Flask app + routes
├── models.py           # SQLAlchemy models
├── config.py           # env vars, system prompt loader
├── prompts/
│   └── harbor_coffee.txt   # system prompt / business context
├── static/
│   ├── widget.js       # embeddable chat widget
│   └── style.css
├── templates/
│   ├── index.html      # Harbor Coffee landing page
│   └── admin.html      # admin panel
├── .env.example
└── requirements.txt
```
