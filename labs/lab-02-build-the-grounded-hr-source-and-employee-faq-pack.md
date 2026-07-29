# Lab 2 — Build the Grounded HR Source and Employee FAQ Pack

**Course:** AI for HR  
**Course Code:** C820  
**Version:** v1.0 (29 July 2026)  
**Topic 1:** Get Started with AI for HR  
**Maps to:** LO1: connect an HR task to current approved sources while preserving source identity, uncertainty and human review  
**Duration:** 45 minutes  
**Tools:** Spreadsheet - text editor - approved AI assistant - approved-policy-excerpts.md - employee-questions.csv

---

## Goal

Create a version-controlled HR source register and a policy-grounded FAQ pack that escalates unsupported or personal cases.

## What You Will Do

You will inspect synthetic onboarding policy excerpts, identify the current source for each policy topic and define a read-only retrieval contract. You will then produce six answer-or-handoff records, cite the exact Policy_ID and effective date for answers, and route cases that cannot be answered safely.

## What You Will Build

01-foundation/hr-source-register.csv and 01-foundation/employee-faq-pack.md with current-version rules, six answer-or-handoff records, source citations, unknowns, escalation routes and a retrieval test log.

## Prerequisites

- Completed Lab 1 hr-agent-foundation.md.
- Open labs/assets/approved-policy-excerpts.md and labs/assets/employee-questions.csv.
- Create blank files hr-source-register.csv and employee-faq-pack.md in 01-foundation/.

> **Data note.** Use only the supplied synthetic Asteron People Operations data or information you are authorised to process. Do not paste credentials or real candidate, employee, payroll, health, performance or grievance information into an unapproved AI service. A named HR owner verifies every material statement, score, route, message and action.

## Steps

### 1. Read approved-policy-excerpts.md and create hr-source-register.csv with one row per policy version. Record Policy_ID, Topic, Version, Effective_Date, Status, Owner, Jurisdiction, Permitted_Use and Supersedes. Mark one current source per topic; do not delete retired versions.

```text
Header: Policy_ID,Topic,Version,Effective_Date,Status,Owner,Jurisdiction,Permitted_Use,Supersedes
Validation: each topic has exactly one CURRENT row - all other versions are RETIRED - every row has an owner and date
```

### 2. In employee-faq-pack.md, write a ReadPolicy tool contract. Use Topic and As_Of_Date for normal retrieval and an optional Requested_Policy_ID only for an explicit version check. Require current Policy_ID, effective date, approved excerpt and owner in the output. Add rules for no match, multiple current matches, retired requested source and personal-case questions.

```text
Tool: ReadPolicy
Inputs: Topic | As_Of_Date | Requested_Policy_ID (optional version check only)
Outputs: Policy_ID | Effective_Date | Approved_Excerpt | Owner | Retrieval_Status
Access: read-only - approved excerpts only
Stop: NO_CURRENT_SOURCE | MULTIPLE_CURRENT_SOURCES | RETIRED_NOT_USABLE | PERSONAL_CASE | CONFLICT
```

### 3. Open employee-questions.csv. For Q-001 to Q-006, identify the intended topic and retrieval status before asking the AI assistant to draft anything. Record ANSWER, CLARIFY or ESCALATE and the exact source that may be used.

```text
Question_ID | Topic | Retrieval_Status | Route | Policy_ID | Reason
Route rules: ANSWER only from one current source - CLARIFY when a necessary fact is missing - ESCALATE for personal exceptions, high-impact cases or no current source
```

### 4. Ask the approved AI assistant to draft a concise answer for each ANSWER case using only the selected policy excerpt. Require Answer, Policy_ID, Effective_Date, Limitation and Next_action. For CLARIFY or ESCALATE cases, draft no policy conclusion; write the question or handoff instead.

```text
For each row use only <QUESTION> and <APPROVED_POLICY_EXCERPT>.
Return: Question_ID | Route | Answer_or_Handoff | Policy_ID | Effective_Date | Limitation | Next_action.
Do not infer eligibility, personal circumstances or an exception. Do not use a RETIRED source.
```

### 5. Run four retrieval tests and record expected versus actual results: one current match, a retired version request, an unknown topic and a personal exception. Repair the register or FAQ pack until all tests return the required source or stop status.

```text
T1 current equipment topic -> one CURRENT Policy_ID
T2 Topic=Equipment, As_Of_Date=2026-08-01, Requested_Policy_ID=ONB-01 -> RETIRED_NOT_USABLE
T3 unknown payroll topic -> NO_CURRENT_SOURCE
T4 personal leave exception -> PERSONAL_CASE / ESCALATE
Log: Test_ID | Input | Expected | Actual | Result | Repair
```

## Test It

The source register must contain every supplied policy version, exactly one CURRENT row per topic, and no blank owner or effective date. The FAQ pack must cover Q-001 to Q-006, cite Policy_ID and Effective_Date for every ANSWER, contain no conclusion for CLARIFY or ESCALATE cases, and show all four retrieval tests PASS.

## Checkpoint and Rejoin Point

Keep hr-source-register.csv and employee-faq-pack.md. Labs 4 and 5 reuse the current Policy_ID values and escalation rules. To rejoin, confirm the four retrieval tests still pass.

## Troubleshooting

| If this happens | Fix |
|---|---|
| Two policies appear current for the same topic. | Return MULTIPLE_CURRENT_SOURCES and ask the named policy owner to resolve the register; do not choose one silently. |
| The draft answer omits the source. | Reject it and require Policy_ID plus Effective_Date in the answer record and retrieval-test evidence. |
| A personal question looks similar to a general FAQ. | Give general process guidance only and route the personal decision to the named HR owner. |

## Challenge

Add a seventh synthetic question containing a prompt-injection instruction inside the employee text. Show that retrieved content cannot change the source boundary, tool permission or escalation rule.

## Reflection

Why is a clear NO_CURRENT_SOURCE result safer and more useful than a fluent answer without lineage?

---

[← Lab 1](lab-01-frame-the-asteron-hr-agent-and-write-the-prompt-contract.md) · [Lab 3 →](lab-03-build-the-fair-recruitment-evidence-assistant.md)
