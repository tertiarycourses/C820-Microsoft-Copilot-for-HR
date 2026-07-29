# Controlled Onboarding Workflow Specification

## State model

`RECEIVED -> VALIDATED -> GROUNDED -> DRAFTED -> NEEDS_REVIEW -> APPROVED -> ACTIONED -> CLOSED`

Any failed required, source, duplicate, approval or action check moves the run to terminal state `STOPPED`.

## Transition table

Complete the owner, evidence and failure-route cells. Keep the prepared state order.

| From | Trigger | Deterministic rule | Model or imported task | Human decision | Owner | To | Evidence | Failure route |
|---|---|---|---|---|---|---|---|---|
| RECEIVED | New synthetic case | Required fields present | None | None | HR operator | VALIDATED |  | STOPPED |
| VALIDATED | Valid case | One current approved source | None | None | HR policy owner | GROUNDED |  | STOPPED |
| GROUNDED | Source ready | Idempotency key is new; plan version and source IDs present | Import OS-001-FINAL-1 | None | Workflow operator | DRAFTED |  | STOPPED |
| DRAFTED | Draft available | Seven-gate record complete | None | Review draft | HR reviewer | NEEDS_REVIEW |  | STOPPED |
| NEEDS_REVIEW | Review complete | Reviewer and timestamp present | None | Approve, edit or hold | HR approver | APPROVED |  | STOPPED |
| APPROVED | Approval token present | Atomically repeat idempotency check before effect | None | Authorise simulated task | Workflow operator | ACTIONED |  | STOPPED |
| ACTIONED | Simulated task recorded | One unique simulated Task_ID | None | Confirm evidence | HR operator | CLOSED |  | STOPPED |

## Tool contracts

| Tool | Identity | Input schema | Output schema | Permitted scope | Timeout and retry | Validation | Evidence | Denied actions |
|---|---|---|---|---|---|---|---|---|
| ReadPolicy |  | Topic, As_Of_Date | Policy_ID, Effective_Date, Excerpt, Status | Read approved excerpts | 10 seconds; one retry |  |  | Write, send |
| DraftPlan |  | Case_ID, Approved_Source | Draft, Source_Ledger, Unknowns | Import or prepare draft only | 45 seconds; no automatic retry |  |  | Write, send, decide |
| CreateTask |  | Case_ID, Task_Code, Approval_Token | SIMULATED_Task_ID, Status | Synthetic simulation only | 10 seconds; no automatic retry |  |  | Live system action |

**Idempotency key:** `Employee_ID + Task_Code + Start_Date`

## Manual fallback

Record how an HR operator receives the case, checks minimum fields, retrieves current policy, obtains human approval and records completion when the workflow is unavailable or stopped.
