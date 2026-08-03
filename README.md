<div align="center">

# AI for HR

[![Course](https://img.shields.io/badge/Course-C820-1f6feb?style=for-the-badge)](https://www.tertiarycourses.com.sg/ai-for-hr.html)
[![Duration](https://img.shields.io/badge/Duration-1_day_7_5_instructional_hours-5E5E5E?style=for-the-badge)](#course-toolkit)
[![Labs](https://img.shields.io/badge/Labs-6-34d399?style=for-the-badge)](labs/README.md)
[![License](https://img.shields.io/badge/License-Educational-fbbf24?style=for-the-badge)](#license)

**A connected, hands-on course in AI for HR — progress through 6 practical labs from Frame the Asteron HR Agent and Write the Prompt Contract to Run the Governance Gate and Rollout Plan.**

[📘 Course Page](https://www.tertiarycourses.com.sg/ai-for-hr.html) · [🧪 Hands-On Labs](labs/README.md) · [📖 Learner Guide](<LG-AI for HR.md>) · [🐛 Report Bug](https://github.com/tertiarycourses/C820---AI-for-HR/issues) · [💡 Request Feature](https://github.com/tertiarycourses/C820---AI-for-HR/issues)

</div>

> [!NOTE]
> **These are the official hands-on lab materials for the commercial course:**
> ### 🎓 AI for HR
> **Course Code:** `C820` · by Tertiary Courses / Tertiary Infotech<br>
> **Duration:** 1 day · 7.5 instructional hours<br>
> **Course page:** https://www.tertiarycourses.com.sg/ai-for-hr.html

---

## Lab Activities

The 6 labs form one connected practical journey. Complete them in order so each verified output can support the activities that follow.

### Topic 1 — Get Started with AI for HR

| # | Activity | Outcome |
|---:|----------|---------|
| **1** | [Frame the Asteron HR Agent and Write the Prompt Contract](labs/lab-01-frame-the-asteron-hr-agent-and-write-the-prompt-contract.md) | 01-foundation/hr-agent-foundation.md containing the selected pattern, four-boundary canvas, first prompt, initial and refined outputs, claim ledger, human decision and stop conditions. |
| **2** | [Build the Grounded HR Source and Employee FAQ Pack](labs/lab-02-build-the-grounded-hr-source-and-employee-faq-pack.md) | 01-foundation/hr-source-register.csv and 01-foundation/employee-faq-pack.md with current-version rules, six answer-or-handoff records, source citations, unknowns, escalation routes and a retrieval test log. |

### Topic 2 — Build HR AI Agents

| # | Activity | Outcome |
|---:|----------|---------|
| **3** | [Build the Fair Recruitment Evidence Assistant](labs/lab-03-build-the-fair-recruitment-evidence-assistant.md) | 02-hr-agents/recruitment-evidence-register.csv and 02-hr-agents/recruitment-review.md with criterion anchors, source evidence, unknowns, proposed and final scores, reviewer changes and human next-step decisions. |
| **4** | [Build the Onboarding and Employee Support Agent Pack](labs/lab-04-build-the-onboarding-and-employee-support-agent-pack.md) | 02-hr-agents/onboarding-support-pack.md and 02-hr-agents/support-routing-register.csv containing a first-week plan, six case routes, grounded drafts, source ledger, privacy check and human release decisions. |

### Topic 3 — Deploy Agentic AI Across the HR Function

| # | Activity | Outcome |
|---:|----------|---------|
| **5** | [Simulate the Controlled Onboarding Workflow](labs/lab-05-simulate-the-controlled-onboarding-workflow.md) | 03-deployment/onboarding-workflow-spec.md and 03-deployment/workflow-run-log.csv with states, transition rules, tool contracts, four complete traces, human approvals, stop reasons and manual fallback. |
| **6** | [Run the Governance Gate and Rollout Plan](labs/lab-06-run-the-governance-gate-and-rollout-plan.md) | 03-deployment/governance-evaluation.csv and 03-deployment/hr-agent-rollout-plan.md with risk controls, calculated metrics, fairness investigation, release decision, pilot stages, owners, monitoring and fallback. |

---

## About

This repository contains the complete lab and courseware package for **AI for HR** (**C820**) by Tertiary Courses / Tertiary Infotech. The practical activities build progressively from **Frame the Asteron HR Agent and Write the Prompt Contract** to **Run the Governance Gate and Rollout Plan**, with explicit checks that help learners verify each result before moving on.

### What you'll learn

- Complete **6 connected hands-on activities** and carry their outputs through one coherent learning journey.
- Practise with **Approved AI assistant · Spreadsheet · Text editor** and the supporting resources supplied in the repository.
- Begin with **Frame the Asteron HR Agent and Write the Prompt Contract** and finish with **Run the Governance Gate and Rollout Plan**.
- Apply safe data handling, evidence checks and named human review before using AI-generated or automated outputs.

> 📖 **Full walkthrough:** see the [Learner Guide](<LG-AI for HR.md>) for the complete course narrative, and [labs/README.md](labs/README.md) for the lab index. Slides, the Learner Guide and the Lesson Plan are in [courseware/](courseware/).

---

## Course Toolkit

| Category | Details |
|----------|---------|
| **Duration** | 1 day · 7.5 instructional hours |
| **Delivery** | Instructor-led, hands-on practical labs |
| **Core tools** | Approved AI assistant · Spreadsheet · Text editor |
| **Practical work** | 6 connected labs with verification steps |
| **Courseware** | PowerPoint and PDF slides, Word and PDF guides, Markdown lab instructions |

---

## Learning Journey

```text
START
  Lab 1    Frame the Asteron HR Agent and Write the Prompt Contract
     │
     ▼
  Topic 1 — Get Started with AI for HR
  Labs 1–2
     │
     ▼
  Topic 2 — Build HR AI Agents
  Labs 3–4
     │
     ▼
  Topic 3 — Deploy Agentic AI Across the HR Function
  Labs 5–6
     │
     ▼
FINISH
  Lab 6   Run the Governance Gate and Rollout Plan
```

---

## Project Structure

```text
C820---AI-for-HR/
├── README.md
├── LG-AI for HR.md
│
├── labs/
│   ├── README.md                 # Start here: complete lab index
│   └── lab-*.md                    # 6 connected practical activities
│
└── courseware/
    ├── *.pptx / *.pdf             # Trainer and learner slides
    ├── LG-*.docx / LG-*.pdf       # Learner Guide
    └── LP-*.docx / LP-*.pdf       # Lesson Plan
```

---

## Getting Started

### Prerequisites

- The accounts and software required for **Approved AI assistant · Spreadsheet · Text editor**. Follow the setup and access notes in each lab.
- A modern web browser and Git for cloning the materials.
- Synthetic or authorised data only. Do not place secrets, personal data or confidential material into an unapproved service.
- A named human reviewer for facts, calculations, decisions and any externally released output.

### 1. Clone the repository

```bash
git clone https://github.com/tertiarycourses/C820---AI-for-HR.git
cd C820---AI-for-HR
```

### 2. Open the lab index

Start with [labs/README.md](labs/README.md), then complete Labs 1–6 in order. Each lab provides the activity context, practical steps and a way to verify the result.

### 3. Keep your connected outputs

Store each lab output in the suggested working folder and retain the evidence or review notes requested by the lab. Later activities depend on these approved outputs.

---

## Contributing

Contributions, corrections and improvements are welcome:

1. **Fork** the repository.
2. Create a feature branch: `git checkout -b feature/my-improvement`.
3. Commit your changes: `git commit -m "Add my improvement"`.
4. Push the branch: `git push origin feature/my-improvement`.
5. Open a **Pull Request**.

Found a bug or have an idea? Open an [issue](https://github.com/tertiarycourses/C820---AI-for-HR/issues).

---

## License

This material is provided for **educational use** as part of the commercial course **AI for HR (C820)**. © Tertiary Infotech Pte. Ltd. All rights reserved.

---

## Developed By

**Tertiary Infotech Pte. Ltd.** — [Tertiary Courses](https://www.tertiarycourses.com.sg)<br>
Course: [AI for HR (C820)](https://www.tertiarycourses.com.sg/ai-for-hr.html)

## Acknowledgements

- The teams behind Approved AI assistant · Spreadsheet · Text editor.
- Course trainers and learners of C820.

---

<div align="center">

⭐ **If these materials helped you learn AI for HR, star the repository!**

Powered by [Tertiary Infotech Academy Pte Ltd](https://www.tertiaryinfotech.com/)

[📘 Course Page](https://www.tertiarycourses.com.sg/ai-for-hr.html) · [🧪 Hands-On Labs](labs/README.md) · [📖 Learner Guide](<LG-AI for HR.md>)

</div>
