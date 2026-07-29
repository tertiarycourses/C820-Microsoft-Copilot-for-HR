# Lab 1 — Frame the Asteron HR Agent and Write the Prompt Contract

**Course:** AI for HR  
**Course Code:** C820  
**Version:** v1.0 (29 July 2026)  
**Topic 1:** Get Started with AI for HR  
**Maps to:** LO1: use an approved AI assistant with a structured prompt, source boundary and human review method  
**Duration:** 45 minutes  
**Tools:** Text editor - approved AI assistant - asteron-people-operations-brief.md

---

## Goal

Define one bounded HR-agent use case and prove that its first prompt stays inside approved evidence and action limits.

## What You Will Do

You will inspect the synthetic Asteron People Operations brief, compare an assistant, fixed automation and agent pattern, and choose a bounded onboarding-support use case. You will map its purpose, evidence, action and decision boundaries before running a G-C-C-S-O-R prompt and reviewing the result.

## What You Will Build

01-foundation/hr-agent-foundation.md containing the selected pattern, four-boundary canvas, first prompt, initial and refined outputs, claim ledger, human decision and stop conditions.

## Prerequisites

- Create the C820-Asteron-HR-Agent/01-foundation/ folder.
- Open labs/assets/asteron-people-operations-brief.md.
- Confirm that you will use only supplied synthetic information.

> **Data note.** Use only the supplied synthetic Asteron People Operations data or information you are authorised to process. Do not paste credentials or real candidate, employee, payroll, health, performance or grievance information into an unapproved AI service. A named HR owner verifies every material statement, score, route, message and action.

## Steps

### 1. Create 01-foundation/hr-agent-foundation.md. Record the exact HR outcome, affected people, accountable owner and non-goals from the Asteron brief. Compare Assistant, Automation and Agent, then select the least autonomous pattern that fits the onboarding-support use case.

```text
Outcome: prepare a grounded first-week onboarding plan
Affected people: synthetic new employees and HR operators
Owner: People Operations Manager
Non-goals: no eligibility decision - no employee-record edit - no message sent
Pattern: <ASSISTANT | AUTOMATION | AGENT>
Reason: <WHY THIS IS THE LEAST AUTONOMOUS FIT>
```

### 2. Add a Four-boundary canvas. Under Purpose, Evidence, Action and Decision, write what is allowed, prohibited and owned. Add completion, uncertainty, time, duplicate and unsafe-action stop conditions.

```text
Purpose: intended outcome | people affected | non-goals | owner
Evidence: permitted sources | prohibited data | version rule | lineage
Action: read | draft | recommend | write | send
Decision: model may | human must | escalation route
Completion: grounded draft + clean ledger + named human decision
Uncertainty stop: missing or conflicting source -> ask or escalate
Time stop: end the run after 10 minutes or two prompt attempts
Duplicate stop: repeated Employee_ID + Start_Date -> ALREADY_PROCESSED
Unsafe-action stop: protected-trait inference or write/send request -> STOPPED
```

### 3. Write a G-C-C-S-O-R prompt using Goal, Context, Criteria, Sources, Output and Review. Delimit the Asteron brief as SOURCE ORG-01. Require a table with Statement, Source_ID, Status and Human_action; require UNKNOWN rather than invention and prohibit external action.

```text
Goal: Draft a first-week onboarding-plan outline for synthetic employee AST-NE-001.
Context: Asteron People Operations training scenario.
Criteria: useful - role-neutral - minimum necessary data - no policy invention.
Sources: <SOURCE id="ORG-01">PASTE APPROVED BRIEF</SOURCE>
Output: Plan plus Statement | Source_ID | Status | Human_action.
Review: use only ORG-01; write UNKNOWN for missing facts; do not send, write or decide eligibility.
```

### 4. Run the prompt in one approved AI assistant and paste the response under Initial output. Review each material statement against ORG-01. Mark SUPPORTED, UNKNOWN or REMOVE in the ledger and identify the most important defect. Add one instruction that would have prevented it, rerun and save Refined output.

```text
Ledger: Version | Statement | Source_ID | Status | Human_action
Defect: <UNSUPPORTED FACT | OVER-BROAD ACTION | MISSING QUESTION | OTHER>
Added instruction: <ONE PREVENTIVE INSTRUCTION>
Rule: unsupported content is removed or marked UNKNOWN; it is never repaired by inventing a source.
```

### 5. Finish with a Human decision block. Decide whether the pattern is READY FOR SYNTHETIC PROTOTYPE or NEEDS REPAIR, give the reason, name the next owner and list the retained run evidence.

```text
Decision: <READY FOR SYNTHETIC PROTOTYPE | NEEDS REPAIR>
Reason: <EVIDENCE-BASED RATIONALE>
Next owner: People Operations Manager
Retain: source version - prompt - both outputs - ledger - reviewer edit - decision - timestamp
```

## Test It

Open 01-foundation/hr-agent-foundation.md. It must name one pattern and justify it; contain all four boundaries; contain one explicit completion, uncertainty, time, duplicate and unsafe-action condition; contain one complete G-C-C-S-O-R prompt, initial and refined outputs, a version-tagged claim ledger with no unsupported statement marked SUPPORTED, and one human decision.

## Checkpoint and Rejoin Point

Keep hr-agent-foundation.md as the portfolio control record. Lab 2 reuses its purpose, evidence and decision boundaries. To rejoin, use the selected onboarding-support outcome and the final refined prompt.

## Troubleshooting

| If this happens | Fix |
|---|---|
| The first output invents an Asteron policy or deadline. | Mark it REMOVE, add 'Use only SOURCE ORG-01; write UNKNOWN for all other facts' and rerun. |
| The chosen pattern is more autonomous than the task requires. | Move drafting to an assistant or fixed flow and keep the person in control of every next action. |
| The four boundaries repeat the same sentence. | Separate why the system exists, what it may know, what it may do and who makes the people decision. |

## Challenge

Write an alternative fixed-automation design for the same use case. Identify the one step, if any, where model-supported judgement adds enough value to justify an agent pattern.

## Reflection

Which boundary most reduced the risk of the first prompt, and what observable change appeared in the refined output?

---

[← Labs index](README.md) · [Lab 2 →](lab-02-build-the-grounded-hr-source-and-employee-faq-pack.md)
