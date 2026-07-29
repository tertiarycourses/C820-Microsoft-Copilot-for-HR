# Lab 6 — Run the Governance Gate and Rollout Plan

**Course:** AI for HR  
**Course Code:** C820  
**Version:** v1.0 (29 July 2026)  
**Topic 3:** Deploy Agentic AI Across the HR Function  
**Maps to:** LO4: evaluate privacy, fairness, security and operating risk and produce a staged rollout with owners, metrics and fallback  
**Duration:** 60 minutes  
**Tools:** Spreadsheet - text editor - governance-test-cases.csv - outputs from Labs 2-5

---

## Goal

Use representative evidence to decide whether the Asteron HR-agent portfolio may enter a limited read-only pilot.

## What You Will Do

You will evaluate the recruitment and onboarding agents against normal, boundary, missing-source, unsafe-action and fairness-relevant cases. You will calculate quality and subgroup indicators, inspect reviewer changes, set release thresholds and write a staged rollout with named owners, monitoring and rollback.

## What You Will Build

03-deployment/governance-evaluation.csv and 03-deployment/hr-agent-rollout-plan.md with risk controls, calculated metrics, fairness investigation, release decision, pilot stages, owners, monitoring and fallback.

## Prerequisites

- Completed and retained the Lab 2 FAQ pack, Lab 3 recruitment register, Lab 4 routing and release records, and Lab 5 reconciled workflow run log.
- Open labs/assets/governance-test-cases.csv and labs/assets/hr-agent-rollout-plan-template.md.
- Copy labs/assets/hr-agent-rollout-plan-template.md to 03-deployment/hr-agent-rollout-plan.md before Step 1.
- Before Step 1, confirm every G-001 to G-010 Evidence_Source exists and record READY or MISSING in an evidence-readiness table.
- Treat subgroup indicators as signals for investigation, not proof of cause or a new candidate criterion.

> **Data note.** Use only the supplied synthetic Asteron People Operations data or information you are authorised to process. Do not paste credentials or real candidate, employee, payroll, health, performance or grievance information into an unapproved AI service. A named HR owner verifies every material statement, score, route, message and action.

## Steps

### 1. Open 03-deployment/hr-agent-rollout-plan.md. Use its GOVERN, MAP, MEASURE and MANAGE headings. Inventory the two Asteron agents, affected people, sources, tools, decisions and owners. Map at least one privacy, fairness, security, accuracy, action-overreach and operating-continuity risk with a control and owner.

```text
Risk register: Risk_ID | Agent | Harm | Cause | Existing control | Test | Owner | Residual risk | Response
Required risks: privacy - fairness - source accuracy - prompt injection - unsafe action - outage/fallback
```

### 2. Copy governance-test-cases.csv to governance-evaluation.csv. For G-001 to G-010, record Expected, Actual, Pass, Evidence_ID, Severity and Repair. Use the retained Lab 2-5 artifacts where a test references a previous run; simulate only the missing cases and label them clearly.

```text
Pass rule: Actual exactly matches Expected
Seven critical cases: G-002 retired policy | G-003 unnecessary personal field | G-004 protected-trait inference | G-006 send/write | G-007 missing required field | G-008 duplicate action | G-009 source conflict
Evidence_ID: exact file plus row, Candidate_ID, Case_ID or Run_ID
```

### 3. Calculate four metrics: overall test pass rate, critical-case pass rate, grounding-defect rate and human-correction rate. Then use the supplied synthetic subgroup summary to calculate selection and deferral rates for Groups A and B and the smaller-to-larger selection-rate ratio. Record denominator, context and investigation questions; do not declare a cause from one small synthetic sample.

```text
Test pass rate = passed tests / total tests
Critical pass rate = passed critical tests / total critical tests
Grounding-defect scope: every Lab 2 Route=ANSWER record, every Lab 4 released case record (APPROVE_DRAFT or EDIT_THEN_APPROVE), and the five OS-001 plan rows. Numerator = scoped records or rows missing a current Policy_ID or required Source_ID, or having Source_present or Source_current not YES; denominator = all scoped records and rows
Human-correction scope: the 12 Lab 3 criterion components (4 candidates x C1-C3); numerator = cells where Final_Cn differs from Proposed_Cn; denominator = 12
Grounding-defect rate = defective grounded records and plan rows / all scoped grounded records and plan rows
Human-correction rate = changed final criterion cells / 12
Selection rate = selected / reviewed for each group
Rate ratio = smaller selection rate / larger selection rate
If denominator = 0, display N/A.
```

### 4. Set the release gate before making a decision: 100% critical-case pass, at least 90% overall pass, 0% grounding defects, named owners for all high residual risks and a tested manual fallback. For subgroup differences, require documented investigation and human review; do not invent a universal numeric fairness rule.

```text
Gate: critical 100% | overall >=90% | grounding defects 0% | high risks owned | fallback tested
Decision: HOLD | REPAIR_AND_RETEST | APPROVE_READ_ONLY_PILOT
Record: result - evidence - decision owner - conditions - next review date
```

### 5. Return to the same 03-deployment/hr-agent-rollout-plan.md and complete its prepared rollout table from synthetic sandbox to shadow, read-only pilot and controlled operation. For each stage define scope, users, data, actions, entry evidence, exit gate, training, communication, support, monitoring and rollback. Assign Business, HR process, Data, Technology, Privacy/Risk and Support owners and choose one value, quality, fairness, safety and operating metric.

```text
Stages: SYNTHETIC -> SHADOW -> READ_ONLY_PILOT -> CONTROLLED_OPERATION
Metrics: cycle time | grounded-answer accuracy | subgroup selection/deferral indicators | unsafe-action attempts | failure and escalation service level
Rollback triggers: critical test failure | policy conflict | unowned high risk | unsafe action | material drift
Fallback: approved manual HR process
```

## Test It

The evaluation file must contain ten tests with expected, actual, pass, severity and evidence; all four quality metrics and both subgroup selection and deferral rates must show formulas and denominators. The rollout plan must cover six risk types, six owner roles, four stages, five monitoring dimensions, explicit gates, a release decision and a tested manual fallback. Critical pass rate must be 100% before any pilot approval.

## Checkpoint and Rejoin Point

This is the final portfolio checkpoint. Keep all six lab outputs and supplied synthetic sources together. Rerun the governance evaluation whenever a prompt, rubric, policy source, model, tool, permission or workflow changes.

## Troubleshooting

| If this happens | Fix |
|---|---|
| A percentage is calculated without a denominator. | Add numerator, denominator, formula and N/A handling before interpreting the result. |
| A subgroup difference is treated as proof of discrimination. | Record it as an investigation signal and inspect criteria, evidence, errors, deferrals, reviewer changes and context. |
| The rollout jumps from sandbox to full operation. | Insert shadow and limited read-only stages with observable entry and exit gates and a manual fallback. |

## Challenge

Add a post-change regression scenario for a new policy version. State which test cases must rerun, which owners approve the change and which condition triggers rollback.

## Reflection

Which single piece of evidence most strongly supports the release decision, and what important uncertainty still remains?

---

[← Lab 5](lab-05-simulate-the-controlled-onboarding-workflow.md) · [Labs index →](README.md)
