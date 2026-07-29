# HR Agent Governance Evaluation and Rollout Plan

## Evidence readiness

| Test_ID | Evidence_Source | READY or MISSING | Repair owner |
|---|---|---|---|
| G-001 |  |  |  |
| G-002 |  |  |  |
| G-003 |  |  |  |
| G-004 |  |  |  |
| G-005 |  |  |  |
| G-006 |  |  |  |
| G-007 |  |  |  |
| G-008 |  |  |  |
| G-009 |  |  |  |
| G-010 |  |  |  |

## GOVERN - inventory and decision rights

| Agent | Purpose | Affected people | Sources | Tools | Human decision | Business owner | HR process owner |
|---|---|---|---|---|---|---|---|
| Recruitment evidence assistant |  |  |  |  |  |  |  |
| Onboarding support workflow |  |  |  |  |  |  |  |

## MAP - risk register

| Risk_ID | Agent | Harm | Cause | Existing control | Test | Owner | Residual risk | Response |
|---|---|---|---|---|---|---|---|---|
| R-PRIV |  |  |  |  |  |  |  |  |
| R-FAIR |  |  |  |  |  |  |  |  |
| R-SOURCE |  |  |  |  |  |  |  |  |
| R-INJECT |  |  |  |  |  |  |  |  |
| R-ACTION |  |  |  |  |  |  |  |  |
| R-OUTAGE |  |  |  |  |  |  |  |  |

## MEASURE - metrics

| Metric | Numerator | Denominator | Formula | Result | Threshold or investigation rule |
|---|---:|---:|---|---:|---|
| Overall test pass rate |  | 10 | passed / 10 |  | At least 90% |
| Critical-case pass rate |  | 7 | passed critical / 7 |  | 100% |
| Grounding-defect rate |  |  | defective grounded records and plan rows / all scoped grounded records and plan rows |  | 0% |
| Human-correction rate |  | 12 | changed criterion cells / 12 |  | Monitor and investigate patterns |
| Group A selection rate |  | 20 | selected / reviewed |  | Investigation signal |
| Group B selection rate |  | 20 | selected / reviewed |  | Investigation signal |
| Smaller-to-larger selection-rate ratio |  |  | smaller rate / larger rate |  | Investigation signal, not a universal rule |
| Group A deferral rate |  | 20 | deferred / reviewed |  | Investigation signal |
| Group B deferral rate |  | 20 | deferred / reviewed |  | Investigation signal |

## MANAGE - release decision

**Gate:** critical 100%; overall at least 90%; grounding defects 0%; high risks owned; manual fallback tested.

- Decision: `HOLD | REPAIR_AND_RETEST | APPROVE_READ_ONLY_PILOT`
- Evidence:
- Decision owner:
- Conditions:
- Next review date:

## Staged rollout

| Stage | Scope | Users | Data | Actions | Entry evidence | Exit gate | Training and communication | Support and monitoring | Rollback |
|---|---|---|---|---|---|---|---|---|---|
| SYNTHETIC |  |  | Synthetic only | No external action |  |  |  |  |  |
| SHADOW |  |  | Approved read-only copy | No outcome control |  |  |  |  |  |
| READ_ONLY_PILOT |  |  | Limited approved live data | Draft and recommend only |  |  |  |  |  |
| CONTROLLED_OPERATION |  |  | Approved scoped data | Approved bounded actions |  |  |  |  |  |

## Owners

| Role | Named owner | Decision or duty |
|---|---|---|
| Business |  |  |
| HR process |  |  |
| Data |  |  |
| Technology |  |  |
| Privacy/Risk |  |  |
| Support |  |  |

## Monitoring and fallback

Track one value, quality, fairness, safety and operating metric. State the approved manual HR process and exact rollback triggers.
