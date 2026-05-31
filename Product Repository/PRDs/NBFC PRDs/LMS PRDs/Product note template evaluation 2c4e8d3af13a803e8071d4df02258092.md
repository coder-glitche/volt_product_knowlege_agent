# Product note template evaluation

Last Edited: March 19, 2026 9:44 PM
PRD Owner: Vaibhav Arora
Status: Completed

### Lifecycle of a feature (Why product note):

```json
                   ┌────────────────────┐
                   │                    │
                   │ (initial problem,  │
                   │   scope, context)  │
                   └─────────┬──────────┘
                             │
                             ▼
       ┌──────────────── Grooming / Kickoff ───────────────┐
       │                                                    │
       │  • Align on scope                                  │
       │  • Identify edge cases                             │
       │  • Refine requirements                             │
       └─────────┬───────────────────────────┬─────────────┘
                 │                           │
                 ▼                           ▼
       ┌───────────────────┐       ┌────────────────────────┐
       │ Design Handoff    │       │ Cross-Functional        │
       │ (UX, flows,       │       │ Sign-offs               │
       │ mocks, journeys)  │       │ • Finance               │
       └─────────┬─────────┘       │ • Compliance            │
                 │                 │ • Business Ops          │
                 ▼                 └─────────┬──────────────┘
          ┌───────────────┐                  │
          │               │                  │
          │  Product Note │◄─────────────────┘
          └─────────┬─────┘
                    ▼
          ┌───────────────────┐
          │      PRD          │
          │ (final detailed   │
          │ specifications)   │
          └─────────┬─────────┘
                    ▼
            ┌──────────────┐
            │ Engineering   │
            │  (breakdown,  │
            │   estimation, │
            │    sprinting) │
            └────────────── ┘

```

### What is a product note?

A product note is a succinct, structured document that brings all stakeholders onto the same page before execution begins. 

Execution here is function specific:

- PRDs for PMs
- Low fidelity mockups and high fidelity for Design
- System design documents for Engineering team
- Development of core product

 It distils the problem, the scope, the target audience, the desired outcomes, and the key decisions into a single source of truth. Its goal is alignment ensuring everyone understands what we’re solving, why it matters, what success looks like, and what the first version will include.

### Use cases of a product note:

**1. What is the problem?**

- Clear articulation of the problem statement. (What are we not solving)

**2. Who are we solving it for?**

- Target audience definition and roll-out strategy. (GTM should be separate from defining the target audience) / Phasing can be a part of the product note however GTM may not be a product note

**3. How will we know the problem is solved?**

- Success criteria and measurable outcomes.

**4. How are we planning to solve it?**

- Scope of the solution and key components of the approach.
- Entry points (User flow diagram) / Use cases

**5. Why does this problem matter now?**

- Prioritisation rationale and business/user impact. (Merge with what is the problem?)

**6. When will we solve it and who owns what?**

- Timeline, milestones, and ownership across teams. (Can be a part of solution scope)

**7. How does this evolve over time?**

- Long-term vision and what the first cut (v0/v1) looks like. (Can be a part of solution scope)

### What makes a good product note:

### **Customer-first clarity**

- The problem and audience are stated *before* any solution.
- Written in simple language, no jargon and is succinct (no more than 2 pages).
- Anyone (engineering, design, leadership, ops) can understand it in one read.

### **Single Source of Truth**

- One document that captures:
    - What, who, why, when, how, and success
- Eliminates parallel decks, messages, or verbal context scattering.

### **Scoping discipline**

- Explicitly calls out **what is in**, **what is out**, and **why**.
- Forces teams to commit to a crisp v1 → reduces chaos downstream.

### **Measurable success criteria**

- Success is quantifiable, not descriptive.
- Includes north-star metric + guardrails (conversion, drop-offs, latency, error rates, etc.).

### **Decision transparency**

- Captures trade-offs, rationale, and rejected options.
- Helps future readers understand *why* choices were made.

### **Thinks beyond v1**

- Defines long-term vision → prevents building dead ends.
- Makes the first cut feel like a meaningful step toward something bigger.

### **10. Risks & assumptions clearly stated**

- Surface unknowns early:
    - data gaps
    - tech limitations
    - partner dependencies
    - operational constraints
- Mature teams call these out explicitly to avoid last-minute surprises.

### Benchmark

| # | Framework / Benchmark | Source(s) / Link(s) / Where to Read More | Use Case | Pros | Cons | Sample |
| --- | --- | --- | --- | --- | --- | --- |
| **1** | **Amazon — PR/FAQ (Working Backwards)** | “PR/FAQ: The Amazon Working Backwards Framework for Product Innovation” (PS.co – productstrategy.co) | Written before building the product to articulate the ideal customer experience and force clarity on the problem. | - Deeply customer and user-story driven

- Excellent for vision-setting; highly narrative and future-oriented

- Forces clarity of thought — writing the launch PR exposes fuzzy thinking

- Promotes simplicity and avoids jargon via PR-like style | - Often verbose and long to produce

- Lacks explicit structure for engineering/design

- Difficult to scale as a repeatable process for large programs | [Link](https://drive.google.com/file/d/1AnqLXBw0OhIxT_3WPXzR7rtHwMVk49RR/view?usp=sharing) |
| **2** | **Squarespace / Industry-Standard RFC-Style Proposals** | No single public Stripe document; many PM/engineering resources describe RFC-style processes. Common in companies like Stripe, GitHub, Google. | Used to gather structured input from stakeholders and document decisions for feature proposals, architectural changes, and cross-team initiatives. | - Highly structured and formal- Assigns clear authorship, approvers, and stakeholder responsibilities

- Captures internal/external dependencies well

- Covers impacts across functions (ops, compliance, privacy)

- Supports revision history within the same document | - Can add process friction and bureaucratic overhead- GTM / rollout strategy not included by default

- Doesn’t explicitly identify target user/audience- Success metrics often not part of the template | [Link](https://slab.com/library/templates/squarespace-rfc-template/?utm_source=chatgpt.com) |
| **3** | **Google — Product Requirements Documents (PRDs)** | Not publicly published; many PM education sites reflect “Google-style PRD formats” covering goals, non-goals, user journeys, and acceptance criteria. | Traditional product requirements spec used after problem clarity to define scope, flows, constraints, and cross-functional execution plans. | - Built-in versioning and change history

- Includes user research / interviews explicitly

- Clear pre-launch and post-launch task tracking

- Encourages linking references, past decisions, and related docs — scales well as org grows

- Structured feedback loop within the doc | - Success criteria often vaguely defined unless added manually

- Rollout strategy (cohorts / phased launches) not deeply enforced- “Solves” tables (effort/impact) can be subjective

- Feedback sections can turn into clutter without discipline | [Link](https://app.notion.com/p/0ee5b3ae07224664a4b86f797900fd96?pvs=21) |
| **4** | **Airbnb — Narrative / Experience-First One-Pagers** | Mentioned in PM blogs referencing Airbnb’s emphasis on narrative thinking and user-journey centric product writing (e.g., Hustle Badger). | Best for capturing the emotional/user experience vision; great for early problem framing and communicating a north-star experience. | - Strong experience-first framing

- Captures audiences, goals, and success measures clearly

- Narrative makes alignment easier for design & leadership

- Version control supported in written docs | - Less structured; can feel verbose

- Harder to convert directly into engineering-ready requirements

- Needs follow-up PRD/spec to operationalize into execution | [Link](https://app.notion.com/p/11f3578dc3f081419caed8b2f50cf32e?pvs=21) |
| **5** | **Airtable — Lightweight Modular Product Specs** | Various walkthroughs describe Airtable’s “lightweight, visual, modular” spec approach tailored to rapid iteration. | Ideal for fast-moving teams needing flexible, linked documents that evolve with the project and integrate with tasks, research, and design. | - Explicitly covers assumptions, constraints, and dependencies- Breaks large product into independently defined features- Includes UX flows and design notes for visibility- Captures metrics and risks clearly | - Rollout plan / GTM often not included- Target audience / segmentation not clearly enforced | [Link](https://app.notion.com/p/11f3578dc3f0819e91a9f4d60f451a43?pvs=21) |

### Product note template:

[Product Note](../../PRDs/Product%20Note%202c5e8d3af13a806889bbfa327146c05c.md) (Template)

### Feedback and next steps

-