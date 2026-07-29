# Lab 4 — Build the Onboarding and Employee Support Agent Pack

**Course:** AI for HR  
**Course Code:** C820  
**Version:** v1.0 (29 July 2026)  
**Topic 2:** Build HR AI Agents  
**Maps to:** LO2: design onboarding and employee-support agents that use current policy, minimum necessary data and human communication review  
**Duration:** 50 minutes  
**Tools:** Spreadsheet - text editor - approved AI assistant - onboarding-support-cases.csv - Lab 2 source register

---

## Goal

Produce a grounded onboarding plan and employee-support response pack that answers, clarifies or escalates each case correctly.

## What You Will Do

You will combine the current source register from Lab 2 with six synthetic onboarding and employee-support cases. The agent will classify each case as ANSWER, CLARIFY or ESCALATE, draft a first-week plan and employee messages, and retain sources, limitations and a human release decision.

## What You Will Build

02-hr-agents/onboarding-support-pack.md and 02-hr-agents/support-routing-register.csv containing a first-week plan, six case routes, grounded drafts, source ledger, privacy check and human release decisions.

## Prerequisites

- Completed Lab 2 with all four retrieval tests passing.
- Open labs/assets/onboarding-support-cases.csv, labs/assets/approved-policy-excerpts.md and labs/assets/onboarding-activities.md.
- Copy labs/assets/support-routing-register-template.csv and labs/assets/onboarding-support-pack-template.md into 02-hr-agents/.
- Use current Policy_ID values from hr-source-register.csv; do not copy real employee information.

> **Data note.** Use only the supplied synthetic Asteron People Operations data or information you are authorised to process. Do not paste credentials or real candidate, employee, payroll, health, performance or grievance information into an unapproved AI service. A named HR owner verifies every material statement, score, route, message and action.

## Steps

### 1. Rename the copied starter to support-routing-register.csv. It already contains all six synthetic case facts and the canonical header. Complete only Necessary_Fields, Omitted_Fields, Retrieval_Status, Route, Policy_ID, Limitation, Human_Owner and Release_Decision. Remove any field value not needed for the stated intent, but keep the column and write OMITTED.

```text
Canonical header: Case_ID,Employee_ID,Intent,As_Of_Date,Start_Date,Location,Department,Question,Necessary_Fields,Omitted_Fields,Retrieval_Status,Route,Policy_ID,Limitation,Human_Owner,Release_Decision
Routes: ANSWER | CLARIFY | ESCALATE
Release: APPROVE_DRAFT | EDIT_THEN_APPROVE | HOLD
```

### 2. Classify all six cases before drafting. Use ANSWER only when one current policy and all necessary facts are present. Use CLARIFY for a missing non-sensitive fact and ESCALATE for a personal exception, conflict, sensitive matter or decision outside the support boundary.

```text
Decision rule:
one current source + complete necessary facts + general guidance -> ANSWER
one necessary non-sensitive fact missing -> CLARIFY
personal exception | high impact | conflict | no current source -> ESCALATE
```

### 3. Rename the copied starter to onboarding-support-pack.md. Ask the AI assistant to complete it. For designated case OS-001, require a five-day onboarding plan with task, owner, due point, Source_ID and employee message. Use ONB-ACT-01 for the approved five-day activity sequence and current policy for policy facts. For all six cases require Route, Draft_or_Handoff, Policy_ID, Effective_Date, Limitation and Next_action.

```text
Use only <CASE ROWS>, <CURRENT APPROVED POLICY EXCERPTS> and <ONB-ACT-01>.
Do not add benefits, eligibility, deadlines, contacts or links beyond the source.
Do not decide a personal exception. Write UNKNOWN for missing facts. Do not send any message.
```

### 4. Review each draft through seven gates: source present, source current, minimum data, fair and respectful language, correct route, action authority and complete next action. Enter APPROVE_DRAFT, EDIT_THEN_APPROVE or HOLD, record the exact edit and persist Final_Approved_Text. The named Human_Owner must be able to change the result.

```text
Release ledger: Case_ID | Source_present | Source_current | Data_minimal | Language_suitable | Route_correct | No_unapproved_action | Next_action_complete | Release_Decision | Edit_or_reason | Final_Approved_Text
All seven gates must be YES before APPROVE_DRAFT or EDIT_THEN_APPROVE.
```

### 5. Run three boundary tests: replace a current Policy_ID with a retired one, remove Location from the location-dependent case and add a request to send the message. Record expected and actual behaviour, repair the prompt or route rules and restore the original synthetic data.

```text
B1 retired policy -> HOLD / RETIRED_NOT_USABLE
B2 missing Location -> CLARIFY
B3 send request -> DRAFT_ONLY / HOLD ACTION
Log: Test_ID | Change | Expected | Actual | Result | Repair
```

## Test It

The routing register must contain six cases, necessary and omitted fields, one route, human owner and release decision per row. The support pack must include an ONB-ACT-01-grounded five-day plan for OS-001, six grounded drafts or handoffs, seven gate results and Final_Approved_Text for every released case, with Policy_ID and Effective_Date for each ANSWER. All three boundary tests must PASS, and no message may be sent or personal exception decided.

## Checkpoint and Rejoin Point

Keep both support files. Lab 5 converts the approved onboarding plan into a controlled multi-step workflow. To rejoin, use only OS-001 Final_Approved_Text with Plan_Version OS-001-FINAL-1; do not generate a new plan.

## Troubleshooting

| If this happens | Fix |
|---|---|
| The onboarding plan invents a company link or contact. | Replace it with UNKNOWN, create a clarification item and cite only the approved source. |
| An ESCALATE case still contains a policy conclusion. | Remove the conclusion; keep only the handoff reason, minimum case facts and named human owner. |
| The release check becomes a rubber stamp. | Require an exact source and observable yes/no result for each gate and keep HOLD available. |

## Challenge

Rewrite one approved employee message for chat and email. Keep facts and route unchanged, then explain which structure changed because of the channel.

## Reflection

Which case required the clearest separation between general policy guidance and a personal HR decision?

---

[← Lab 3](lab-03-build-the-fair-recruitment-evidence-assistant.md) · [Lab 5 →](lab-05-simulate-the-controlled-onboarding-workflow.md)
