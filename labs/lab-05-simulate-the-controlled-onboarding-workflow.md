# Lab 5 — Simulate the Controlled Onboarding Workflow

**Course:** AI for HR  
**Course Code:** C820  
**Version:** v1.0 (29 July 2026)  
**Topic 3:** Deploy Agentic AI Across the HR Function  
**Maps to:** LO3: build and test a multi-step HR workflow with approved data, limited tools, human gates and complete run evidence  
**Duration:** 45 minutes  
**Tools:** Text editor - spreadsheet - approved AI assistant - workflow-cases.csv - workflow-run-log-template.csv

---

## Goal

Run four synthetic onboarding cases through a visible state machine and prove that duplicates, missing facts and unsafe actions stop correctly.

## What You Will Do

You will convert the Lab 4 onboarding plan into a state-based workflow. ReadPolicy, DraftPlan and CreateTask are represented by explicit tool contracts; write and send effects remain simulated. You will run normal, missing-data, duplicate and policy-conflict cases and reconcile every final state.

## What You Will Build

03-deployment/onboarding-workflow-spec.md and 03-deployment/workflow-run-log.csv with states, transition rules, tool contracts, four complete traces, human approvals, stop reasons and manual fallback.

## Prerequisites

- Completed Lab 4 onboarding-support pack.
- Open labs/assets/workflow-cases.csv, labs/assets/workflow-spec-template.md and labs/assets/workflow-run-log-template.csv.
- Confirm that OS-001 Final_Approved_Text is labelled Plan_Version OS-001-FINAL-1.
- All system changes and messages are simulations; do not connect a live HR system.

> **Data note.** Use only the supplied synthetic Asteron People Operations data or information you are authorised to process. Do not paste credentials or real candidate, employee, payroll, health, performance or grievance information into an unapproved AI service. A named HR owner verifies every material statement, score, route, message and action.

## Steps

### 1. Copy workflow-spec-template.md to onboarding-workflow-spec.md. Confirm its states RECEIVED, VALIDATED, GROUNDED, DRAFTED, NEEDS_REVIEW, APPROVED, ACTIONED, CLOSED and STOPPED. Complete the prepared transition rows with trigger, rule, owner, evidence and failure route.

```text
Transition table: From | Trigger | Deterministic rule | Model task | Human decision | Owner | To | Evidence | Failure route
Completion: CLOSED only after required evidence and approval are present
Failure: STOPPED keeps reason, owner and manual next action
```

### 2. Add contracts for ReadPolicy, DraftPlan and CreateTask. Keep ReadPolicy read-only, DraftPlan non-actioning and CreateTask simulated. Specify input and output schemas, identity, permitted scope, timeout, retry, idempotency key, validation and evidence.

```text
ReadPolicy input: Topic,As_Of_Date -> Policy_ID,Effective_Date,Excerpt,Status
DraftPlan input: Case_ID,Approved_Source -> Draft,Source_Ledger,Unknowns
CreateTask input: Case_ID,Task_Code,Approval_Token -> SIMULATED_Task_ID,Status
Idempotency key: Employee_ID + Task_Code + Start_Date
Timeout/retry: ReadPolicy 10 seconds, one retry; DraftPlan 45 seconds, no automatic retry; CreateTask 10 seconds, no automatic retry
No tool may send a message or edit an employee record.
```

### 3. Copy the pre-populated workflow-run-log-template.csv into 03-deployment/workflow-run-log.csv. Process WF-001 to WF-004 one prepared row at a time. Apply required-field, source-status and duplicate checks before the DRAFTED state; repeat the duplicate check atomically with the approval-token check before CreateTask. Complete Actual_Result, To_State, evidence, owner and manual action cells.

```text
Case expectations:
WF-001 normal -> CLOSED
WF-002 missing Location -> STOPPED / MISSING_REQUIRED_FIELD
WF-003 duplicate key -> STOPPED / ALREADY_PROCESSED
WF-004 conflicting current policy -> STOPPED / SOURCE_CONFLICT
```

### 4. For WF-001 only, import the exact Lab 4 OS-001 Final_Approved_Text and cite Plan_Version OS-001-FINAL-1 as the DraftPlan output; do not generate a fresh plan. Confirm the Lab 4 seven-gate release record and create a synthetic approval token. Record a simulated task effect only after approval; every other case must stop before DraftPlan or CreateTask as specified.

```text
Approval token: APPR-WF-001-HR-001
Evidence before ACTIONED: required fields PASS | source current | Plan_Version OS-001-FINAL-1 | claim ledger clean | seven gates YES | named reviewer | approval timestamp
Simulated effect: TASK-WF-001-IT-SETUP; no external write occurs.
```

### 5. Reconcile the log. Every case must have one terminal state, a reason, an owner and a manual next action. Count cases by CLOSED and STOPPED, confirm no duplicate simulated Task_ID and add a one-paragraph fallback procedure for system outage or unresolved source conflict.

```text
Reconciliation: total cases = CLOSED + STOPPED = 4
Unique simulated Task_ID count = simulated action rows
Every STOPPED row: Stop_Reason + Human_Owner + Manual_Next_Action
Fallback: receive case - validate minimum fields - retrieve approved source manually - human review - record completion
```

## Test It

The workflow specification must contain all nine states, three tool contracts, an approval gate and manual fallback. The run log must show WF-001 CLOSED and WF-002 to WF-004 STOPPED with the specified reasons; four terminal states must reconcile, no simulated Task_ID may repeat, and no external action may occur.

## Checkpoint and Rejoin Point

Keep the specification and run log as the deployment evidence. Lab 6 uses the four traces, stop behaviour and approval evidence. To rejoin, confirm the reconciliation equation equals four.

## Troubleshooting

| If this happens | Fix |
|---|---|
| A stopped case continues to later states. | Enforce terminal STOPPED behaviour and start a separate corrected run with a new Run_ID. |
| The duplicate case creates another simulated task. | Check the composite idempotency key before drafting or action and return ALREADY_PROCESSED. |
| The tool contract says 'appropriate access'. | Replace vague language with exact identity, operation, fields, destination and denied actions. |

## Challenge

Add a safe retry for a temporary ReadPolicy timeout. Set maximum attempts, backoff, terminal status and evidence without allowing the retry to bypass source or approval checks.

## Reflection

Which workflow truth belonged in a deterministic rule rather than the model, and what failure did that prevent?

---

[← Lab 4](lab-04-build-the-onboarding-and-employee-support-agent-pack.md) · [Lab 6 →](lab-06-run-the-governance-gate-and-rollout-plan.md)
