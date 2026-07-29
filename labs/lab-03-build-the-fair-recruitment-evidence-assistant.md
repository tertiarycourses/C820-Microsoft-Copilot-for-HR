# Lab 3 — Build the Fair Recruitment Evidence Assistant

**Course:** AI for HR  
**Course Code:** C820  
**Version:** v1.0 (29 July 2026)  
**Topic 2:** Build HR AI Agents  
**Maps to:** LO2: design a recruitment decision-support agent with job-related criteria, source evidence and explicit human decisions  
**Duration:** 50 minutes  
**Tools:** Spreadsheet - text editor - approved AI assistant - role-profile.md - synthetic-candidates.csv

---

## Goal

Apply one approved rubric consistently to four synthetic candidates and retain a complete evidence-to-decision trail.

## What You Will Do

You will turn an approved Asteron role profile into a transparent screening rubric, remove non-job-related fields from four synthetic candidate records and ask an AI assistant to cite evidence for each criterion. A human reviewer will correct proposed scores, record reasons and prepare interview questions without automatically rejecting or selecting anyone.

## What You Will Build

02-hr-agents/recruitment-evidence-register.csv and 02-hr-agents/recruitment-review.md with criterion anchors, source evidence, unknowns, proposed and final scores, reviewer changes and human next-step decisions.

## Prerequisites

- Completed Lab 1 four-boundary canvas.
- Open labs/assets/role-profile.md and labs/assets/synthetic-candidates.csv.
- Use Candidate_ID only; do not add a name, photograph, age, family, health, ethnicity or other protected information.

> **Data note.** Use only the supplied synthetic Asteron People Operations data or information you are authorised to process. Do not paste credentials or real candidate, employee, payroll, health, performance or grievance information into an unapproved AI service. A named HR owner verifies every material statement, score, route, message and action.

## Steps

### 1. Create recruitment-review.md and copy the approved role outcome, responsibilities and three required criteria from role-profile.md. For each criterion, write 0, 1 and 2 score anchors tied to observable resume evidence. Record why each criterion is job-related.

```text
C1 Service case handling: 0 absent | 1 related exposure | 2 direct evidence with outcome
C2 Spreadsheet reporting: 0 absent | 1 basic use | 2 recurring report with validation
C3 Stakeholder communication: 0 absent | 1 general contact | 2 structured cross-team example
Total range: 0-6 - UNKNOWN remains visible - score is decision support only
```

### 2. Create recruitment-evidence-register.csv. Copy Candidate_ID and the real source columns EVIDENCE_L1 through EVIDENCE_L4 from synthetic-candidates.csv. Add Proposed_C1 to Proposed_C3, Proposed_Total, Evidence_C1 to Evidence_C3, Unknowns, Final_C1 to Final_C3, Final_Total, Adjustment_Reason and Human_Next_Step.

```text
Header: Candidate_ID,EVIDENCE_L1,EVIDENCE_L2,EVIDENCE_L3,EVIDENCE_L4,Proposed_C1,Proposed_C2,Proposed_C3,Proposed_Total,Evidence_C1,Evidence_C2,Evidence_C3,Unknowns,Final_C1,Final_C2,Final_C3,Final_Total,Adjustment_Reason,Human_Next_Step
Permitted next steps: INVITE_STRUCTURED_INTERVIEW | CLARIFY_EVIDENCE | HOLD_FOR_PANEL_REVIEW
```

### 3. Give the AI assistant the role profile, anchored rubric and all four minimised candidate records in one batch. Require identical treatment, exact EVIDENCE line references and UNKNOWN for missing facts. Prohibit inference and prohibit a final hiring or rejection recommendation.

```text
Use only ROLE-01 and supplied Candidate_ID records.
For each candidate return C1-C3 proposed score, exact evidence line, unknowns and one job-related clarification question. Apply identical anchors. Do not infer protected traits. Do not select, rank, reject or contact a candidate.
```

### 4. Enter the proposed output, then independently verify each source citation and score. Record final scores and an Adjustment_Reason for every change. Calculate both totals and confirm each equals the sum of its three components. Keep UNKNOWN visible even when the final score is high.

```text
Spreadsheet checks:
Proposed_Total = Proposed_C1 + Proposed_C2 + Proposed_C3
Final_Total = Final_C1 + Final_C2 + Final_C3
Score range per criterion = 0..2
If evidence is absent, score 0 and record UNKNOWN; never infer the missing skill.
```

### 5. Hold a human panel review. Assign one permitted Human_Next_Step to every candidate and give a one-sentence job-related reason. Add six structured interview questions: one per criterion and three candidate-specific clarification questions. Retain the source, rubric, prompt, proposed output, reviewer changes and final human decisions.

```text
Decision record: Candidate_ID | Human_Next_Step | Job-related reason | Reviewer | Date
Question rule: competency-based - same core question by criterion - candidate-specific clarification uses only cited resume evidence - no protected-trait question
```

## Test It

The register must contain four Candidate_ID rows, three proposed and final components per row, exact evidence references, visible unknowns, totals from 0 to 6, and an Adjustment_Reason for every changed score. The review file must contain criterion anchors, six structured questions and one human-owned next step per candidate; it must contain no automated selection, ranking, rejection or protected-trait inference.

## Checkpoint and Rejoin Point

Keep both recruitment files as the decision-support evidence trail. Lab 6 reuses the rubric, proposed versus final changes and human next steps for governance tests. To rejoin, verify all component totals.

## Troubleshooting

| If this happens | Fix |
|---|---|
| The assistant ranks candidates or recommends a hire. | Discard that field and repeat: evidence extraction and criterion scoring only; the panel owns the next step. |
| A score has no exact resume support. | Set it to 0, record UNKNOWN and create a structured clarification question. |
| Different criteria appear for different candidates. | Return to ROLE-01 and apply the same three anchored criteria to the complete batch. |

## Challenge

Have a partner independently review the four proposed scores. Compare only criteria with a two-point difference and rewrite any ambiguous anchor without changing the role requirements.

## Reflection

Which human correction most improved fairness or evidence quality, and why would the original score have been misleading?

---

[← Lab 2](lab-02-build-the-grounded-hr-source-and-employee-faq-pack.md) · [Lab 4 →](lab-04-build-the-onboarding-and-employee-support-agent-pack.md)
