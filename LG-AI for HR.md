# AI for HR — Learner Guide

**Course Code:** C820  |  **Conducted by:** Tertiary Infotech Academy Pte Ltd (UEN 201200696W)  |  **Version v1.0 · 29 July 2026**

## Contents

- [Introduction](#introduction)
- [Course Learning Outcomes](#course-learning-outcomes)
- [Before You Start — Preparation](#before-you-start--preparation)
- [Topic 01 — Get Started with AI for HR  (Morning - 2 connected labs)](#topic-01--get-started-with-ai-for-hr--morning---2-connected-labs)
  - [AI and Agentic AI in HR: Use Cases and Landscape](#ai-and-agentic-ai-in-hr-use-cases-and-landscape)
  - [Popular AI Tools and Agent Platforms](#popular-ai-tools-and-agent-platforms)
  - [Effective Prompting for HR Tasks](#effective-prompting-for-hr-tasks)
  - [Connecting AI to HR Data and Documents](#connecting-ai-to-hr-data-and-documents)
  - [Lab 1 — Frame the Asteron HR Agent and Write the Prompt Contract](#lab-1--frame-the-asteron-hr-agent-and-write-the-prompt-contract)
  - [Lab 2 — Build the Grounded HR Source and Employee FAQ Pack](#lab-2--build-the-grounded-hr-source-and-employee-faq-pack)
- [Topic 02 — Build HR AI Agents  (Midday and afternoon - 2 connected labs)](#topic-02--build-hr-ai-agents--midday-and-afternoon---2-connected-labs)
  - [Designing Agentic AI Workflows for HR](#designing-agentic-ai-workflows-for-hr)
  - [Recruitment and Candidate Screening Agents](#recruitment-and-candidate-screening-agents)
  - [Onboarding and Employee Support Agents](#onboarding-and-employee-support-agents)
  - [Drafting HR Content and Communications with AI](#drafting-hr-content-and-communications-with-ai)
  - [Lab 3 — Build the Fair Recruitment Evidence Assistant](#lab-3--build-the-fair-recruitment-evidence-assistant)
  - [Lab 4 — Build the Onboarding and Employee Support Agent Pack](#lab-4--build-the-onboarding-and-employee-support-agent-pack)
- [Topic 03 — Deploy Agentic AI Across the HR Function  (Afternoon - 2 connected labs)](#topic-03--deploy-agentic-ai-across-the-hr-function--afternoon---2-connected-labs)
  - [Automating Multi-Step HR Workflows with AI Agents](#automating-multi-step-hr-workflows-with-ai-agents)
  - [Integrating Agents with HR Systems and Tools](#integrating-agents-with-hr-systems-and-tools)
  - [Governance, Fairness and Human Oversight](#governance-fairness-and-human-oversight)
  - [Rolling Out Agentic AI in Your Organisation](#rolling-out-agentic-ai-in-your-organisation)
  - [Lab 5 — Simulate the Controlled Onboarding Workflow](#lab-5--simulate-the-controlled-onboarding-workflow)
  - [Lab 6 — Run the Governance Gate and Rollout Plan](#lab-6--run-the-governance-gate-and-rollout-plan)
- [Wrap-Up - Operate the Human-Owned HR Agent Portfolio](#wrap-up---operate-the-human-owned-hr-agent-portfolio)
- [Next Steps](#next-steps)
- [Glossary](#glossary)


## Introduction

This Learner Guide accompanies AI for HR (C820), a one-day course on practical, human-owned use of AI and agentic workflows across recruitment, onboarding, employee support and HR operations. It follows the published three-topic sequence exactly and uses six connected Asteron People Operations labs.

Use the guide as a post-course reference. Each published sub-topic is taught through a definition, purpose, process, worked HR example, decision guide and practitioner controls before its related lab. Source links point to primary AI-platform, Singapore data-governance, fair-employment and risk-management guidance. The materials are educational and do not replace organisational HR, privacy, security or legal review.


## Course Learning Outcomes

- LO1: Use an approved AI assistant with a structured prompt, source boundary and human review method for everyday HR work.
- LO2: Design bounded recruitment, onboarding, employee-support and communication agents with job-related criteria and explicit human decisions.
- LO3: Build and test a multi-step HR workflow that connects approved data and tools while preserving exceptions, approvals and run evidence.
- LO4: Evaluate privacy, fairness, security and operating risk, then produce a staged rollout plan with owners, metrics, monitoring and fallback.


## Before You Start — Preparation

**What you need**

- A Windows or macOS laptop with a modern browser, spreadsheet application and text editor.
- Access to one organisation-approved AI assistant such as ChatGPT, Claude or Copilot.
- The supplied synthetic files in labs/assets/; do not substitute real candidate or employee records during class.
- A local folder named C820-Asteron-HR-Agent for all lab outputs.

**Verify your setup**

Create the workspace, open every supplied Markdown and CSV file and confirm that commas, dates and UTF-8 text display correctly. If no AI assistant is available, use the prompt templates to produce a manual draft and complete every evidence, rubric, workflow and review step yourself.

```bash
C820-Asteron-HR-Agent/
  01-foundation/
  02-hr-agents/
  03-deployment/
  run-evidence/
```

**Conventions used in every lab**

- Use only the supplied synthetic Asteron data or information you are authorised to process.
- Label SOURCE FACT, MODEL DRAFT, DETERMINISTIC CHECK, UNKNOWN and HUMAN DECISION separately.
- Write the source ID beside every material policy, candidate or workflow statement.
- Keep draft, reviewer edit, approval or escalation reason and final status for each lab checkpoint.


## Topic 01 — Get Started with AI for HR  (Morning - 2 connected labs)

AI and agentic AI use cases - tools and platforms - effective prompting - approved HR data and documents

**Key concepts**

- Assistant, automation, agent — Choose the least autonomous pattern that can complete the HR job reliably.
- Human-owned purpose — Name the employee or candidate outcome, process owner and decision that remains human.
- Prompt contract — State goal, context, criteria, sources, output, review and escalation before using a model.
- Grounded evidence — Constrain material claims to approved policy, role and case sources and preserve their identifiers.
- Data minimisation — Use synthetic or necessary authorised fields and keep confidential or sensitive data out of unapproved tools.
- Observable quality — Define acceptance checks before comparing model outputs or platforms.


### AI and Agentic AI in HR: Use Cases and Landscape

Generative AI produces or transforms language and other content from instructions and context. An AI assistant responds to a person, a deterministic automation follows fixed rules, and an agent lets a model choose among approved next steps and tools inside a bounded workflow.

HR work combines high-volume drafting with decisions that affect people. Separating assistance, automation and agency prevents a fluent tool from being given authority that belongs to an HR professional, hiring manager, data owner or employee.

**How it works**

- Define the HR outcome, affected people, process owner and authoritative sources.
- Classify each step as fixed rule, model-supported judgement or human decision.
- Grant only the data and tools required for the current step.
- Set completion, uncertainty, exception, time and action limits.
- Retain the source, output, checks, edits, decision and final status as run evidence.

**Worked example**

- Asteron Services wants faster onboarding support for new employees.
- A deterministic rule identifies the employee's country and start date; an assistant drafts a policy-grounded reply.
- A named HR owner reviews exceptions and any message about eligibility, conduct, pay or personal circumstances.

**Decision guide**

| Use when | Avoid when |
|---|---|
| The task contains repeated language work, unstructured documents or exceptions that fixed rules handle poorly. | A template, search filter or spreadsheet rule solves the task more simply and predictably. |
| A clear source boundary, observable checks and accountable reviewer can be defined. | The system would make an adverse or irreversible people decision without meaningful human review. |

**Practitioner quality lens**

- Bounded: Purpose, sources, tools, limits, stop conditions and fallback are explicit.
- Grounded: Material statements trace to approved facts or rules.
- Accountable: A named role owns the final people decision and communication.

**Authoritative references**

- https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/
- https://airc.nist.gov/airmf-resources/airmf/

---


### Popular AI Tools and Agent Platforms

HR teams can work with browser assistants such as ChatGPT or Claude, configurable workspace agents, low-code platforms such as Copilot Studio, or custom software. The options combine models, instructions, knowledge and tools but differ in data handling, integration, testing, identity, observability, cost and operating skill.

Choosing a product before defining the use case encourages feature-led adoption. A task-and-risk comparison makes the platform decision explainable and avoids connecting broad HR repositories to a prototype that needs only a synthetic policy extract.

**How it works**

- Start with the HR job, data class, actions, users, volume and acceptable failure mode.
- Prototype a prompt with synthetic sources in an approved supervised assistant.
- Move to a workspace agent when reusable instructions and governed knowledge are sufficient.
- Use low-code flow tooling for triggers, connectors, branching, approvals and monitoring.
- Use custom development only when identity, tools, evaluation, telemetry or isolation require it.

**Worked example**

- A one-off job-description critique stays in a supervised assistant with a synthetic role brief.
- A reusable employee-policy helper uses approved knowledge and read-only access.
- An onboarding workflow uses a flow platform because it needs triggers, record lookups, tasks, approvals and run history.

**Decision guide**

| Use when | Avoid when |
|---|---|
| Comparing platforms against an already documented HR workflow and control matrix. | Selecting the tool with the most connectors or the highest apparent autonomy. |
| The organisation can confirm approved services, data locations, identities and support ownership. | Allowing inherited user permissions to expose unrelated employee or candidate records. |

**Practitioner quality lens**

- Fit: Workflow and risk needs drive the tool choice.
- Control: Identity, data, actions and environments can be restricted.
- Visibility: Versions, runs, failures, approvals and costs can be inspected.

**Authoritative references**

- https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/
- https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview
- https://learn.microsoft.com/en-us/microsoft-copilot-studio/fundamentals-what-is-copilot-studio

---


### Effective Prompting for HR Tasks

An HR prompt is a working contract. This course uses G-C-C-S-O-R: Goal, Context, Criteria, Sources, Output and Review. The contract separates stable instructions from case variables, defines the evidence boundary and makes the desired result testable.

Requests such as 'screen these resumes' or 'write an onboarding email' hide the selection basis, source truth and acceptance checks. A structured prompt reduces generic output and makes unsupported claims, missing facts and inappropriate inferences easier to detect.

**How it works**

- State one HR goal, intended reader and permitted decision support.
- Provide only relevant context and label each approved source with a stable identifier.
- Define job-related or policy-based criteria before asking for analysis.
- Specify output fields for facts, source, uncertainty, recommendation and human action.
- Require UNKNOWN, clarification or escalation when evidence is absent.
- Review accuracy, fairness, privacy, rights, tone and action authority before use.

**Worked example**

- Goal: draft a first-day email for a Singapore-based new employee.
- Sources: offer-confirmation facts and approved onboarding policy excerpts; personal medical or family information is excluded.
- Output: subject, message, source ledger and unresolved questions; any policy exception is marked ESCALATE TO HR.

**Decision guide**

| Use when | Avoid when |
|---|---|
| The same HR transformation or review task will recur with different approved inputs. | The purpose, authorised source or intended human decision is unclear. |
| Success criteria can be checked against a source, rubric, schema or reviewer checklist. | The prompt would include real personal data in a service not approved for that data. |

**Practitioner quality lens**

- Specific: Goal, scope, audience, criteria and format are explicit.
- Evidence-led: Sources are delimited and every material claim carries a reference.
- Fail-safe: Missing or conflicting evidence triggers a question or escalation.

**Authoritative references**

- https://help.openai.com/en/articles/10032626-prompt-engineering-best-practices
- https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

---


### Connecting AI to HR Data and Documents

A governed HR connection exposes a defined source through a limited interface. Its data contract records purpose, owner, fields, record grain, version, refresh time, permitted users, retention, quality checks and whether the connection may read or write.

Candidate and employee repositories contain personal and sometimes sensitive information. Broad access increases privacy, prompt-injection and accidental-action risk, while unclear versions allow an agent to quote a retired policy as if it were current.

**How it works**

- Classify the use case and minimise rows, fields, periods and documents before connection.
- Begin with synthetic or de-identified snapshots and read-only tools.
- Record authoritative owner, effective date, version, jurisdiction and expiry for every policy.
- Validate completeness, duplicates, field meanings, access and document status before retrieval.
- Return source identifiers and timestamps with retrieved content.
- Separate retrieval from any write, send or status-change tool and place approvals before actions.

**Worked example**

- The employee helper can retrieve three approved policy excerpts by Policy_ID and Effective_Date.
- It cannot browse payroll, performance or medical folders and has no send permission.
- A conflicting or expired excerpt stops the run and creates a question for the policy owner.

**Decision guide**

| Use when | Avoid when |
|---|---|
| A repeatable workflow needs approved structured records or policy documents. | The connector exposes an entire HR drive or inherited administrator privileges. |
| A data owner can define purpose, quality, access, retention and lineage. | The source has no owner, effective date, stable identifier or current-version rule. |

**Practitioner quality lens**

- Minimal: Only the necessary records and fields are available.
- Current: Version, effective date and authoritative owner are visible.
- Traceable: Each output points to the exact source retrieved for that run.

**Authoritative references**

- https://www.pdpc.gov.sg/guidelines-and-consultation/2024/02/advisory-guidelines-on-use-of-personal-data-in-ai-recommendation-and-decision-systems
- https://www.pdpc.gov.sg/help-and-resources/2020/01/model-ai-governance-framework

---


### Lab 1 — Frame the Asteron HR Agent and Write the Prompt Contract

Learning outcome: LO1: use an approved AI assistant with a structured prompt, source boundary and human review method.

Goal: Define one bounded HR-agent use case and prove that its first prompt stays inside approved evidence and action limits.

You will inspect the synthetic Asteron People Operations brief, compare an assistant, fixed automation and agent pattern, and choose a bounded onboarding-support use case. You will map its purpose, evidence, action and decision boundaries before running a G-C-C-S-O-R prompt and reviewing the result.

**What you'll build**

01-foundation/hr-agent-foundation.md containing the selected pattern, four-boundary canvas, first prompt, initial and refined outputs, claim ledger, human decision and stop conditions.   (Tools: Text editor - approved AI assistant - asteron-people-operations-brief.md.)

**Prerequisites**

- Create the C820-Asteron-HR-Agent/01-foundation/ folder.
- Open labs/assets/asteron-people-operations-brief.md.
- Confirm that you will use only supplied synthetic information.

**Step-by-step**

1. Create 01-foundation/hr-agent-foundation.md. Record the exact HR outcome, affected people, accountable owner and non-goals from the Asteron brief. Compare Assistant, Automation and Agent, then select the least autonomous pattern that fits the onboarding-support use case.

   ```bash
   Outcome: prepare a grounded first-week onboarding plan
Affected people: synthetic new employees and HR operators
Owner: People Operations Manager
Non-goals: no eligibility decision - no employee-record edit - no message sent
Pattern: <ASSISTANT | AUTOMATION | AGENT>
Reason: <WHY THIS IS THE LEAST AUTONOMOUS FIT>
   ```

2. Add a Four-boundary canvas. Under Purpose, Evidence, Action and Decision, write what is allowed, prohibited and owned. Add completion, uncertainty, time, duplicate and unsafe-action stop conditions.

   ```bash
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

3. Write a G-C-C-S-O-R prompt using Goal, Context, Criteria, Sources, Output and Review. Delimit the Asteron brief as SOURCE ORG-01. Require a table with Statement, Source_ID, Status and Human_action; require UNKNOWN rather than invention and prohibit external action.

   ```bash
   Goal: Draft a first-week onboarding-plan outline for synthetic employee AST-NE-001.
Context: Asteron People Operations training scenario.
Criteria: useful - role-neutral - minimum necessary data - no policy invention.
Sources: <SOURCE id="ORG-01">PASTE APPROVED BRIEF</SOURCE>
Output: Plan plus Statement | Source_ID | Status | Human_action.
Review: use only ORG-01; write UNKNOWN for missing facts; do not send, write or decide eligibility.
   ```

4. Run the prompt in one approved AI assistant and paste the response under Initial output. Review each material statement against ORG-01. Mark SUPPORTED, UNKNOWN or REMOVE in the ledger and identify the most important defect. Add one instruction that would have prevented it, rerun and save Refined output.

   ```bash
   Ledger: Version | Statement | Source_ID | Status | Human_action
Defect: <UNSUPPORTED FACT | OVER-BROAD ACTION | MISSING QUESTION | OTHER>
Added instruction: <ONE PREVENTIVE INSTRUCTION>
Rule: unsupported content is removed or marked UNKNOWN; it is never repaired by inventing a source.
   ```

5. Finish with a Human decision block. Decide whether the pattern is READY FOR SYNTHETIC PROTOTYPE or NEEDS REPAIR, give the reason, name the next owner and list the retained run evidence.

   ```bash
   Decision: <READY FOR SYNTHETIC PROTOTYPE | NEEDS REPAIR>
Reason: <EVIDENCE-BASED RATIONALE>
Next owner: People Operations Manager
Retain: source version - prompt - both outputs - ledger - reviewer edit - decision - timestamp
   ```


**Test it**

Open 01-foundation/hr-agent-foundation.md. It must name one pattern and justify it; contain all four boundaries; contain one explicit completion, uncertainty, time, duplicate and unsafe-action condition; contain one complete G-C-C-S-O-R prompt, initial and refined outputs, a version-tagged claim ledger with no unsupported statement marked SUPPORTED, and one human decision.

**Checkpoint and rejoin point**

Keep hr-agent-foundation.md as the portfolio control record. Lab 2 reuses its purpose, evidence and decision boundaries. To rejoin, use the selected onboarding-support outcome and the final refined prompt.

**Troubleshooting**

| If this happens | Fix |
|---|---|
| The first output invents an Asteron policy or deadline. | Mark it REMOVE, add 'Use only SOURCE ORG-01; write UNKNOWN for all other facts' and rerun. |
| The chosen pattern is more autonomous than the task requires. | Move drafting to an assistant or fixed flow and keep the person in control of every next action. |
| The four boundaries repeat the same sentence. | Separate why the system exists, what it may know, what it may do and who makes the people decision. |

**Challenge**

Write an alternative fixed-automation design for the same use case. Identify the one step, if any, where model-supported judgement adds enough value to justify an agent pattern.

**Reflection**

Which boundary most reduced the risk of the first prompt, and what observable change appeared in the refined output?

> **Note:** The complete lab and its support-file references are in labs/lab-01-*.md. Use only the supplied synthetic Asteron People Operations data or information you are authorised to process. Do not paste credentials or real candidate, employee, payroll, health, performance or grievance information into an unapproved AI service. A named HR owner verifies every material statement, score, route, message and action.

---


### Lab 2 — Build the Grounded HR Source and Employee FAQ Pack

Learning outcome: LO1: connect an HR task to current approved sources while preserving source identity, uncertainty and human review.

Goal: Create a version-controlled HR source register and a policy-grounded FAQ pack that escalates unsupported or personal cases.

You will inspect synthetic onboarding policy excerpts, identify the current source for each policy topic and define a read-only retrieval contract. You will then produce six answer-or-handoff records, cite the exact Policy_ID and effective date for answers, and route cases that cannot be answered safely.

**What you'll build**

01-foundation/hr-source-register.csv and 01-foundation/employee-faq-pack.md with current-version rules, six answer-or-handoff records, source citations, unknowns, escalation routes and a retrieval test log.   (Tools: Spreadsheet - text editor - approved AI assistant - approved-policy-excerpts.md - employee-questions.csv.)

**Prerequisites**

- Completed Lab 1 hr-agent-foundation.md.
- Open labs/assets/approved-policy-excerpts.md and labs/assets/employee-questions.csv.
- Create blank files hr-source-register.csv and employee-faq-pack.md in 01-foundation/.

**Step-by-step**

1. Read approved-policy-excerpts.md and create hr-source-register.csv with one row per policy version. Record Policy_ID, Topic, Version, Effective_Date, Status, Owner, Jurisdiction, Permitted_Use and Supersedes. Mark one current source per topic; do not delete retired versions.

   ```bash
   Header: Policy_ID,Topic,Version,Effective_Date,Status,Owner,Jurisdiction,Permitted_Use,Supersedes
Validation: each topic has exactly one CURRENT row - all other versions are RETIRED - every row has an owner and date
   ```

2. In employee-faq-pack.md, write a ReadPolicy tool contract. Use Topic and As_Of_Date for normal retrieval and an optional Requested_Policy_ID only for an explicit version check. Require current Policy_ID, effective date, approved excerpt and owner in the output. Add rules for no match, multiple current matches, retired requested source and personal-case questions.

   ```bash
   Tool: ReadPolicy
Inputs: Topic | As_Of_Date | Requested_Policy_ID (optional version check only)
Outputs: Policy_ID | Effective_Date | Approved_Excerpt | Owner | Retrieval_Status
Access: read-only - approved excerpts only
Stop: NO_CURRENT_SOURCE | MULTIPLE_CURRENT_SOURCES | RETIRED_NOT_USABLE | PERSONAL_CASE | CONFLICT
   ```

3. Open employee-questions.csv. For Q-001 to Q-006, identify the intended topic and retrieval status before asking the AI assistant to draft anything. Record ANSWER, CLARIFY or ESCALATE and the exact source that may be used.

   ```bash
   Question_ID | Topic | Retrieval_Status | Route | Policy_ID | Reason
Route rules: ANSWER only from one current source - CLARIFY when a necessary fact is missing - ESCALATE for personal exceptions, high-impact cases or no current source
   ```

4. Ask the approved AI assistant to draft a concise answer for each ANSWER case using only the selected policy excerpt. Require Answer, Policy_ID, Effective_Date, Limitation and Next_action. For CLARIFY or ESCALATE cases, draft no policy conclusion; write the question or handoff instead.

   ```bash
   For each row use only <QUESTION> and <APPROVED_POLICY_EXCERPT>.
Return: Question_ID | Route | Answer_or_Handoff | Policy_ID | Effective_Date | Limitation | Next_action.
Do not infer eligibility, personal circumstances or an exception. Do not use a RETIRED source.
   ```

5. Run four retrieval tests and record expected versus actual results: one current match, a retired version request, an unknown topic and a personal exception. Repair the register or FAQ pack until all tests return the required source or stop status.

   ```bash
   T1 current equipment topic -> one CURRENT Policy_ID
T2 Topic=Equipment, As_Of_Date=2026-08-01, Requested_Policy_ID=ONB-01 -> RETIRED_NOT_USABLE
T3 unknown payroll topic -> NO_CURRENT_SOURCE
T4 personal leave exception -> PERSONAL_CASE / ESCALATE
Log: Test_ID | Input | Expected | Actual | Result | Repair
   ```


**Test it**

The source register must contain every supplied policy version, exactly one CURRENT row per topic, and no blank owner or effective date. The FAQ pack must cover Q-001 to Q-006, cite Policy_ID and Effective_Date for every ANSWER, contain no conclusion for CLARIFY or ESCALATE cases, and show all four retrieval tests PASS.

**Checkpoint and rejoin point**

Keep hr-source-register.csv and employee-faq-pack.md. Labs 4 and 5 reuse the current Policy_ID values and escalation rules. To rejoin, confirm the four retrieval tests still pass.

**Troubleshooting**

| If this happens | Fix |
|---|---|
| Two policies appear current for the same topic. | Return MULTIPLE_CURRENT_SOURCES and ask the named policy owner to resolve the register; do not choose one silently. |
| The draft answer omits the source. | Reject it and require Policy_ID plus Effective_Date in the answer record and retrieval-test evidence. |
| A personal question looks similar to a general FAQ. | Give general process guidance only and route the personal decision to the named HR owner. |

**Challenge**

Add a seventh synthetic question containing a prompt-injection instruction inside the employee text. Show that retrieved content cannot change the source boundary, tool permission or escalation rule.

**Reflection**

Why is a clear NO_CURRENT_SOURCE result safer and more useful than a fluent answer without lineage?

> **Note:** The complete lab and its support-file references are in labs/lab-02-*.md. Use only the supplied synthetic Asteron People Operations data or information you are authorised to process. Do not paste credentials or real candidate, employee, payroll, health, performance or grievance information into an unapproved AI service. A named HR owner verifies every material statement, score, route, message and action.

---


## Topic 02 — Build HR AI Agents  (Midday and afternoon - 2 connected labs)

agent workflow design - recruitment decision support - onboarding and employee support - HR content and communications

**Key concepts**

- Workflow contract — Map trigger, sources, tools, branches, decisions, evidence and fallback before configuration.
- Job-related rubric — Translate role requirements into consistent observable criteria before reviewing candidates.
- Decision support — The agent organises evidence and questions; an authorised person owns the hiring decision.
- Policy-grounded support — Answer from current approved policy and escalate personal, ambiguous or high-impact cases.
- Human communication — Use AI for options and editing while a responsible sender verifies facts, tone and audience.
- Verification — Test normal, boundary, missing-data, conflicting-source and unsafe-action cases.


### Designing Agentic AI Workflows for HR

An HR agent workflow is a bounded sequence in which a model may choose among approved read, transform, classify, ask and draft steps. The design contract defines triggers, inputs, state, tools, branches, human decisions, evidence and stop conditions before a platform is configured.

A demonstration often shows only the happy path. HR operations also contain missing documents, policy conflicts, candidate questions, protected information and exceptions that need a clear owner rather than an improvised model response.

**How it works**

- Write the outcome and non-goals, then draw the current human workflow.
- Classify each step as deterministic rule, model task, human decision or external action.
- Define tool inputs, outputs, permissions, timeouts and idempotency keys.
- Add escalation for uncertainty, conflicting sources and high-impact cases.
- Define completion evidence and a manual fallback before the first prototype.

**Worked example**

- Trigger: an approved new-hire record is created with a start date and location.
- The flow checks required fields, retrieves current policy, drafts tasks and asks HR to approve the plan.
- Only after approval are tasks created; duplicate Employee_ID and Start_Date runs are blocked.

**Decision guide**

| Use when | Avoid when |
|---|---|
| The process is multi-step, has repeated exceptions and can be represented with explicit states. | The desired outcome changes from case to case without a stable owner or policy basis. |
| Owners can specify allowed actions and what evidence proves completion. | The agent would need unrestricted access or an irreversible action without an approval boundary. |

**Practitioner quality lens**

- Complete: Trigger, inputs, states, branches, owners and finish conditions are mapped.
- Least privilege: Every tool exposes only the fields and actions required.
- Recoverable: Retries, duplicates, failures and manual fallback are designed.

**Authoritative references**

- https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/
- https://learn.microsoft.com/en-us/microsoft-copilot-studio/flows-overview

---


### Recruitment and Candidate Screening Agents

A recruitment agent can extract role-relevant evidence, compare it with a pre-approved rubric, identify missing information and prepare consistent interview questions. It is decision support: it must not infer protected traits or replace the accountable hiring decision.

Unstructured resume review is vulnerable to inconsistent criteria and unsupported assumptions. A transparent rubric tied to actual job requirements improves consistency, while source citations, deferral and human review expose uncertainty instead of hiding it.

**How it works**

- Complete job analysis and approve skills, experience and evidence anchors before candidate review.
- Remove non-job-related fields and instruct the system not to infer protected characteristics.
- Extract evidence with resume line or record references; mark missing facts UNKNOWN.
- Apply the same anchored rubric to every candidate for the same role.
- Compare proposed and final human scores and record adjustments with reasons.
- Monitor outcomes, error patterns and subgroup effects where lawful and appropriate.

**Worked example**

- A role requires service-case handling, spreadsheet reporting and stakeholder communication.
- The agent cites evidence for each criterion and writes UNKNOWN when a resume lacks sufficient detail.
- The hiring panel reviews all evidence, corrects one over-score and owns the shortlist and interview plan.

**Decision guide**

| Use when | Avoid when |
|---|---|
| Criteria are job-related, documented and applied consistently across the candidate set. | Inferring age, disability, family status, ethnicity, health, personality or other sensitive traits. |
| The agent can cite evidence and defer uncertain cases to trained reviewers. | Automatically rejecting a candidate or changing criteria after seeing candidate identities. |

**Practitioner quality lens**

- Relevant: Every criterion is justified by the job analysis.
- Consistent: The same rubric and evidence rules apply to all candidates.
- Reviewable: Sources, unknowns, scores, changes and final human decision are retained.

**Authoritative references**

- https://www.tal.sg/tafep/getting-started/fair/tripartite-guidelines
- https://www.tal.sg/tafep/resources/tools-and-templates/2025/tafep-recruitment-checklist
- https://www.pdpc.gov.sg/guidelines-and-consultation/2024/02/advisory-guidelines-on-use-of-personal-data-in-ai-recommendation-and-decision-systems

---


### Onboarding and Employee Support Agents

An onboarding or employee-support agent retrieves approved policy, gathers only necessary case facts, prepares tasks or a draft answer and routes exceptions to the correct owner. It should show the source and effective date and make escalation easy.

Fast answers improve the employee experience only when they are current and appropriate for the employee's context. A confident response from an expired policy can create more work and harm than a clear handoff to HR.

**How it works**

- Create an intent list and define which questions the agent may answer, draft or only route.
- Retrieve current policy by stable identifier, jurisdiction and effective date.
- Ask only for the minimum case facts needed to choose an approved route.
- Return answer, source, confidence limits, next action and escalation path.
- Separate support content from personal case decisions and employee-relations matters.
- Log unanswered questions to improve the knowledge base through a controlled process.

**Worked example**

- A new employee asks when to complete the equipment form and where to find it.
- The agent cites ONB-02, provides the current deadline and link, and labels the response as general guidance.
- A question about a personal leave exception is routed to an HR partner without the agent deciding eligibility.

**Decision guide**

| Use when | Avoid when |
|---|---|
| Approved policy and process sources are current, versioned and owned. | A personal case requires judgement, accommodation, investigation, discipline or legal interpretation. |
| The support boundary and escalation routes are clear to employees and operators. | The knowledge source contains conflicting or expired versions without an authoritative rule. |

**Practitioner quality lens**

- Current: Every answer shows the source and effective date.
- Proportionate: Only necessary case information is requested.
- Escalatable: High-impact and unresolved questions reach a named human route.

**Authoritative references**

- https://learn.microsoft.com/en-us/microsoft-copilot-studio/fundamentals-what-is-copilot-studio
- https://www.pdpc.gov.sg/guidelines-and-consultation/2024/02/advisory-guidelines-on-use-of-personal-data-in-ai-recommendation-and-decision-systems

---


### Drafting HR Content and Communications with AI

AI can generate and transform job descriptions, interview guides, onboarding messages, policy summaries and employee updates. The responsible sender supplies approved facts, reader context, tone and channel constraints, then verifies and edits before release.

HR language can shape access, trust and employee action. Generic or exclusionary wording, invented benefits and an incorrect deadline can cause real consequences even when the message sounds polished.

**How it works**

- Name the audience, communication purpose, required action and approved source facts.
- Specify plain-language, accessibility, inclusive-language and channel requirements.
- Request options or critique rather than accepting the first draft.
- Use a claim ledger to check dates, policy statements, links and promises.
- Run a fairness, privacy, tone and action review and retain the final human edit.

**Worked example**

- An agent drafts a role advertisement from an approved job analysis and removes non-job-related preferences.
- It produces a first-day email from current onboarding policy and flags a missing equipment-contact name.
- The HR owner supplies the missing fact, edits the tone and approves the final versions.

**Decision guide**

| Use when | Avoid when |
|---|---|
| The communication has an accountable sender and a complete approved fact base. | Sending high-impact or personalised messages automatically from an unreviewed draft. |
| The output can be checked against job, policy, brand and accessibility criteria. | Creating promises, role requirements or policy interpretations beyond the supplied source. |

**Practitioner quality lens**

- Accurate: Every date, promise, requirement and link is verified.
- Inclusive: Language is job-related, respectful and accessible.
- Owned: The named sender reviews the final message and intended audience.

**Authoritative references**

- https://help.openai.com/en/articles/10032626-prompt-engineering-best-practices
- https://www.tal.sg/tafep/getting-started/fair/tripartite-guidelines

---


### Lab 3 — Build the Fair Recruitment Evidence Assistant

Learning outcome: LO2: design a recruitment decision-support agent with job-related criteria, source evidence and explicit human decisions.

Goal: Apply one approved rubric consistently to four synthetic candidates and retain a complete evidence-to-decision trail.

You will turn an approved Asteron role profile into a transparent screening rubric, remove non-job-related fields from four synthetic candidate records and ask an AI assistant to cite evidence for each criterion. A human reviewer will correct proposed scores, record reasons and prepare interview questions without automatically rejecting or selecting anyone.

**What you'll build**

02-hr-agents/recruitment-evidence-register.csv and 02-hr-agents/recruitment-review.md with criterion anchors, source evidence, unknowns, proposed and final scores, reviewer changes and human next-step decisions.   (Tools: Spreadsheet - text editor - approved AI assistant - role-profile.md - synthetic-candidates.csv.)

**Prerequisites**

- Completed Lab 1 four-boundary canvas.
- Open labs/assets/role-profile.md and labs/assets/synthetic-candidates.csv.
- Use Candidate_ID only; do not add a name, photograph, age, family, health, ethnicity or other protected information.

**Step-by-step**

1. Create recruitment-review.md and copy the approved role outcome, responsibilities and three required criteria from role-profile.md. For each criterion, write 0, 1 and 2 score anchors tied to observable resume evidence. Record why each criterion is job-related.

   ```bash
   C1 Service case handling: 0 absent | 1 related exposure | 2 direct evidence with outcome
C2 Spreadsheet reporting: 0 absent | 1 basic use | 2 recurring report with validation
C3 Stakeholder communication: 0 absent | 1 general contact | 2 structured cross-team example
Total range: 0-6 - UNKNOWN remains visible - score is decision support only
   ```

2. Create recruitment-evidence-register.csv. Copy Candidate_ID and the real source columns EVIDENCE_L1 through EVIDENCE_L4 from synthetic-candidates.csv. Add Proposed_C1 to Proposed_C3, Proposed_Total, Evidence_C1 to Evidence_C3, Unknowns, Final_C1 to Final_C3, Final_Total, Adjustment_Reason and Human_Next_Step.

   ```bash
   Header: Candidate_ID,EVIDENCE_L1,EVIDENCE_L2,EVIDENCE_L3,EVIDENCE_L4,Proposed_C1,Proposed_C2,Proposed_C3,Proposed_Total,Evidence_C1,Evidence_C2,Evidence_C3,Unknowns,Final_C1,Final_C2,Final_C3,Final_Total,Adjustment_Reason,Human_Next_Step
Permitted next steps: INVITE_STRUCTURED_INTERVIEW | CLARIFY_EVIDENCE | HOLD_FOR_PANEL_REVIEW
   ```

3. Give the AI assistant the role profile, anchored rubric and all four minimised candidate records in one batch. Require identical treatment, exact EVIDENCE line references and UNKNOWN for missing facts. Prohibit inference and prohibit a final hiring or rejection recommendation.

   ```bash
   Use only ROLE-01 and supplied Candidate_ID records.
For each candidate return C1-C3 proposed score, exact evidence line, unknowns and one job-related clarification question. Apply identical anchors. Do not infer protected traits. Do not select, rank, reject or contact a candidate.
   ```

4. Enter the proposed output, then independently verify each source citation and score. Record final scores and an Adjustment_Reason for every change. Calculate both totals and confirm each equals the sum of its three components. Keep UNKNOWN visible even when the final score is high.

   ```bash
   Spreadsheet checks:
Proposed_Total = Proposed_C1 + Proposed_C2 + Proposed_C3
Final_Total = Final_C1 + Final_C2 + Final_C3
Score range per criterion = 0..2
If evidence is absent, score 0 and record UNKNOWN; never infer the missing skill.
   ```

5. Hold a human panel review. Assign one permitted Human_Next_Step to every candidate and give a one-sentence job-related reason. Add six structured interview questions: one per criterion and three candidate-specific clarification questions. Retain the source, rubric, prompt, proposed output, reviewer changes and final human decisions.

   ```bash
   Decision record: Candidate_ID | Human_Next_Step | Job-related reason | Reviewer | Date
Question rule: competency-based - same core question by criterion - candidate-specific clarification uses only cited resume evidence - no protected-trait question
   ```


**Test it**

The register must contain four Candidate_ID rows, three proposed and final components per row, exact evidence references, visible unknowns, totals from 0 to 6, and an Adjustment_Reason for every changed score. The review file must contain criterion anchors, six structured questions and one human-owned next step per candidate; it must contain no automated selection, ranking, rejection or protected-trait inference.

**Checkpoint and rejoin point**

Keep both recruitment files as the decision-support evidence trail. Lab 6 reuses the rubric, proposed versus final changes and human next steps for governance tests. To rejoin, verify all component totals.

**Troubleshooting**

| If this happens | Fix |
|---|---|
| The assistant ranks candidates or recommends a hire. | Discard that field and repeat: evidence extraction and criterion scoring only; the panel owns the next step. |
| A score has no exact resume support. | Set it to 0, record UNKNOWN and create a structured clarification question. |
| Different criteria appear for different candidates. | Return to ROLE-01 and apply the same three anchored criteria to the complete batch. |

**Challenge**

Have a partner independently review the four proposed scores. Compare only criteria with a two-point difference and rewrite any ambiguous anchor without changing the role requirements.

**Reflection**

Which human correction most improved fairness or evidence quality, and why would the original score have been misleading?

> **Note:** The complete lab and its support-file references are in labs/lab-03-*.md. Use only the supplied synthetic Asteron People Operations data or information you are authorised to process. Do not paste credentials or real candidate, employee, payroll, health, performance or grievance information into an unapproved AI service. A named HR owner verifies every material statement, score, route, message and action.

---


### Lab 4 — Build the Onboarding and Employee Support Agent Pack

Learning outcome: LO2: design onboarding and employee-support agents that use current policy, minimum necessary data and human communication review.

Goal: Produce a grounded onboarding plan and employee-support response pack that answers, clarifies or escalates each case correctly.

You will combine the current source register from Lab 2 with six synthetic onboarding and employee-support cases. The agent will classify each case as ANSWER, CLARIFY or ESCALATE, draft a first-week plan and employee messages, and retain sources, limitations and a human release decision.

**What you'll build**

02-hr-agents/onboarding-support-pack.md and 02-hr-agents/support-routing-register.csv containing a first-week plan, six case routes, grounded drafts, source ledger, privacy check and human release decisions.   (Tools: Spreadsheet - text editor - approved AI assistant - onboarding-support-cases.csv - Lab 2 source register.)

**Prerequisites**

- Completed Lab 2 with all four retrieval tests passing.
- Open labs/assets/onboarding-support-cases.csv, labs/assets/approved-policy-excerpts.md and labs/assets/onboarding-activities.md.
- Copy labs/assets/support-routing-register-template.csv and labs/assets/onboarding-support-pack-template.md into 02-hr-agents/.
- Use current Policy_ID values from hr-source-register.csv; do not copy real employee information.

**Step-by-step**

1. Rename the copied starter to support-routing-register.csv. It already contains all six synthetic case facts and the canonical header. Complete only Necessary_Fields, Omitted_Fields, Retrieval_Status, Route, Policy_ID, Limitation, Human_Owner and Release_Decision. Remove any field value not needed for the stated intent, but keep the column and write OMITTED.

   ```bash
   Canonical header: Case_ID,Employee_ID,Intent,As_Of_Date,Start_Date,Location,Department,Question,Necessary_Fields,Omitted_Fields,Retrieval_Status,Route,Policy_ID,Limitation,Human_Owner,Release_Decision
Routes: ANSWER | CLARIFY | ESCALATE
Release: APPROVE_DRAFT | EDIT_THEN_APPROVE | HOLD
   ```

2. Classify all six cases before drafting. Use ANSWER only when one current policy and all necessary facts are present. Use CLARIFY for a missing non-sensitive fact and ESCALATE for a personal exception, conflict, sensitive matter or decision outside the support boundary.

   ```bash
   Decision rule:
one current source + complete necessary facts + general guidance -> ANSWER
one necessary non-sensitive fact missing -> CLARIFY
personal exception | high impact | conflict | no current source -> ESCALATE
   ```

3. Rename the copied starter to onboarding-support-pack.md. Ask the AI assistant to complete it. For designated case OS-001, require a five-day onboarding plan with task, owner, due point, Source_ID and employee message. Use ONB-ACT-01 for the approved five-day activity sequence and current policy for policy facts. For all six cases require Route, Draft_or_Handoff, Policy_ID, Effective_Date, Limitation and Next_action.

   ```bash
   Use only <CASE ROWS>, <CURRENT APPROVED POLICY EXCERPTS> and <ONB-ACT-01>.
Do not add benefits, eligibility, deadlines, contacts or links beyond the source.
Do not decide a personal exception. Write UNKNOWN for missing facts. Do not send any message.
   ```

4. Review each draft through seven gates: source present, source current, minimum data, fair and respectful language, correct route, action authority and complete next action. Enter APPROVE_DRAFT, EDIT_THEN_APPROVE or HOLD, record the exact edit and persist Final_Approved_Text. The named Human_Owner must be able to change the result.

   ```bash
   Release ledger: Case_ID | Source_present | Source_current | Data_minimal | Language_suitable | Route_correct | No_unapproved_action | Next_action_complete | Release_Decision | Edit_or_reason | Final_Approved_Text
All seven gates must be YES before APPROVE_DRAFT or EDIT_THEN_APPROVE.
   ```

5. Run three boundary tests: replace a current Policy_ID with a retired one, remove Location from the location-dependent case and add a request to send the message. Record expected and actual behaviour, repair the prompt or route rules and restore the original synthetic data.

   ```bash
   B1 retired policy -> HOLD / RETIRED_NOT_USABLE
B2 missing Location -> CLARIFY
B3 send request -> DRAFT_ONLY / HOLD ACTION
Log: Test_ID | Change | Expected | Actual | Result | Repair
   ```


**Test it**

The routing register must contain six cases, necessary and omitted fields, one route, human owner and release decision per row. The support pack must include an ONB-ACT-01-grounded five-day plan for OS-001, six grounded drafts or handoffs, seven gate results and Final_Approved_Text for every released case, with Policy_ID and Effective_Date for each ANSWER. All three boundary tests must PASS, and no message may be sent or personal exception decided.

**Checkpoint and rejoin point**

Keep both support files. Lab 5 converts the approved onboarding plan into a controlled multi-step workflow. To rejoin, use only OS-001 Final_Approved_Text with Plan_Version OS-001-FINAL-1; do not generate a new plan.

**Troubleshooting**

| If this happens | Fix |
|---|---|
| The onboarding plan invents a company link or contact. | Replace it with UNKNOWN, create a clarification item and cite only the approved source. |
| An ESCALATE case still contains a policy conclusion. | Remove the conclusion; keep only the handoff reason, minimum case facts and named human owner. |
| The release check becomes a rubber stamp. | Require an exact source and observable yes/no result for each gate and keep HOLD available. |

**Challenge**

Rewrite one approved employee message for chat and email. Keep facts and route unchanged, then explain which structure changed because of the channel.

**Reflection**

Which case required the clearest separation between general policy guidance and a personal HR decision?

> **Note:** The complete lab and its support-file references are in labs/lab-04-*.md. Use only the supplied synthetic Asteron People Operations data or information you are authorised to process. Do not paste credentials or real candidate, employee, payroll, health, performance or grievance information into an unapproved AI service. A named HR owner verifies every material statement, score, route, message and action.

---


## Topic 03 — Deploy Agentic AI Across the HR Function  (Afternoon - 2 connected labs)

multi-step automation - HR system integration - privacy, fairness and human oversight - staged organisational rollout

**Key concepts**

- Control-first automation — Design deterministic checks, model tasks and human gates as separate visible steps.
- Integration contract — Specify identity, source, schema, permission, failure, retry and evidence for each connector.
- Action boundary — Draft and recommend before any write, send, status change or people decision.
- Risk-tiered oversight — Increase human involvement with uncertainty, sensitivity, impact and reversibility.
- Evaluation set — Test normal, boundary, missing, conflicting, unsafe and fairness-relevant cases before pilot.
- Staged rollout — Move from synthetic sandbox to shadow, read-only pilot and controlled operation with fallback.


### Automating Multi-Step HR Workflows with AI Agents

A multi-step HR workflow coordinates triggers, deterministic rules, model tasks, human decisions and controlled actions over a visible state. The system completes only when required checks, approvals and evidence are present.

Automation can reduce handoffs but also repeats mistakes at speed. Separating deterministic truth, model-supported judgement and human authority makes the process easier to test, stop and recover.

**How it works**

- Define states such as RECEIVED, VALIDATED, DRAFTED, NEEDS_REVIEW, APPROVED, ACTIONED and CLOSED.
- Use deterministic checks for required fields, dates, identifiers, duplicates and routing.
- Use the model only for bounded extraction, classification, drafting or critique.
- Place approval before external messages, record changes and high-impact decisions.
- Make actions idempotent and log state transitions, evidence and errors.
- Provide timeout, retry, exception queue and manual completion routes.

**Worked example**

- An onboarding case enters RECEIVED and fails if Employee_ID, Start_Date or Location is absent.
- The model drafts the plan from approved policy; HR reviews exceptions and approves task creation.
- A repeated event with the same case key returns ALREADY_PROCESSED instead of creating duplicate tasks.

**Decision guide**

| Use when | Avoid when |
|---|---|
| The process has stable states, frequent handoffs and observable completion conditions. | A workflow is still changing daily and no stable current process exists. |
| Owners can define action permissions, approvals, exception service levels and fallback. | Failures cannot be detected, reversed or completed through a manual route. |

**Practitioner quality lens**

- Deterministic: Rules own identifiers, dates, completeness, duplicates and thresholds.
- Bounded: Model tasks have explicit inputs, outputs and escalation.
- Recoverable: Every failure has an owner, retry rule and manual path.

**Authoritative references**

- https://learn.microsoft.com/en-us/microsoft-copilot-studio/flows-overview
- https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/

---


### Integrating Agents with HR Systems and Tools

An integration contract describes one tool call: authenticated identity, permitted operation, input schema, output schema, data scope, validation, timeout, retry, error handling, evidence and owner. Read, calculate, draft and action tools should remain distinct.

A connector inherits technical reach that may exceed the business use case. Explicit contracts reduce over-broad access and make it possible to test whether a run read the right record, used the right version and changed only what an authorised person approved.

**How it works**

- Use a service or user identity with least privilege and a named owner.
- Whitelist operations, fields, destinations and case types; deny everything else.
- Validate input and output schemas and reject unexpected fields or embedded instructions.
- Require approval tokens for write, send and status-change actions.
- Use correlation and idempotency keys to link events and prevent duplicate effects.
- Log tool name, parameters, result, latency, error and approving role without exposing unnecessary data.

**Worked example**

- ReadPolicy accepts Policy_ID and As_Of_Date and returns approved text, owner and effective date.
- CreateOnboardingTask accepts a validated case key and approval token but cannot edit employee records.
- SendMessage remains disabled in the sandbox; the lab records a simulated message and complete audit line.

**Decision guide**

| Use when | Avoid when |
|---|---|
| A stable API, connector or controlled file interface has an accountable system owner. | Using a shared administrator account or exposing an entire system to simplify a prototype. |
| The workflow can prove the identity, scope and effect of each tool call. | Allowing retrieved documents to redefine tool permissions or bypass approval. |

**Practitioner quality lens**

- Authorised: Identity and operation match the current user's and workflow's authority.
- Validated: Schemas, values, destinations and effects are checked.
- Auditable: Every call and approval is linked to one traceable case.

**Authoritative references**

- https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced-use-flow
- https://airc.nist.gov/airmf-resources/airmf/5-sec-core/

---


### Governance, Fairness and Human Oversight

HR AI governance assigns decision rights and controls across purpose, data, model, tools, users, evaluation, operation and incident response. Human oversight is a designed decision point with evidence, authority, time and fallback, not a generic instruction to review.

HR systems can affect access to work, employee experience and personal data. Trust depends on job-related criteria, proportionate data use, transparent limitations, tested performance, meaningful review and a route for correction or challenge.

**How it works**

- Inventory the use case, affected people, decisions, data, vendors and owners.
- Map benefits and harms, including privacy, bias, exclusion, security and automation overreach.
- Choose human involvement by impact, uncertainty, reversibility and affected-person expectations.
- Test source accuracy, unsafe actions, subgroup effects, deferral and override behaviour.
- Communicate purpose, limitations, data use and routes for questions or correction.
- Monitor incidents, complaints, drift, reviewer changes and policy updates after launch.

**Worked example**

- The candidate assistant may propose rubric evidence but cannot reject, rank on protected traits or contact candidates.
- A trained panel sees the source, unknowns and proposed score and records the final decision and reason.
- Monthly review compares subgroup selection, deferral and correction rates and investigates material gaps.

**Decision guide**

| Use when | Avoid when |
|---|---|
| Before pilot, after material changes and throughout operation. | Treating policy approval as a substitute for testing actual cases and workflow behaviour. |
| The organisation can assign business, HR, data, technology, privacy and risk ownership. | Using a human reviewer who lacks evidence, authority, time or a meaningful ability to change the result. |

**Practitioner quality lens**

- Human-centric: People outcomes, recourse and responsible decision rights shape the design.
- Fair: Job-related criteria and subgroup effects are examined with context.
- Transparent: Purpose, limits, sources, decisions and correction routes are visible.

**Authoritative references**

- https://www.pdpc.gov.sg/help-and-resources/2020/01/model-ai-governance-framework
- https://www.imda.gov.sg/how-we-can-help/ai-verify
- https://www.tal.sg/tafep/getting-started/fair/tripartite-guidelines
- https://www.pdpc.gov.sg/guidelines-and-consultation/2024/02/advisory-guidelines-on-use-of-personal-data-in-ai-recommendation-and-decision-systems

---


### Rolling Out Agentic AI in Your Organisation

Rollout is a staged operating change. A use case moves through discovery, synthetic sandbox, shadow run, read-only pilot and controlled operation only when value, quality, safety, ownership, support and fallback evidence meet defined gates.

A successful prompt is not an operating service. HR adoption also requires current data, trained reviewers, employee communication, monitoring, support, incident response, change control and a manual route when the system is unavailable or unsafe.

**How it works**

- Prioritise one bounded use case by value, feasibility, data readiness and residual risk.
- Set a manual baseline, outcome metric, quality metric, risk metric and stop threshold.
- Test on representative synthetic cases and repair failures before connecting live data.
- Run in shadow or read-only mode and compare outputs with the approved current process.
- Pilot with limited users, data and actions; train reviewers and communicate limitations.
- Monitor, review, version, roll back or retire through named governance and support owners.

**Worked example**

- Asteron pilots policy-grounded onboarding support for one office and two trained HR reviewers.
- The pilot tracks resolution quality, grounding-defect rate, escalation accuracy, correction rate and cycle time.
- Any policy-source conflict or unsafe-action attempt stops the run and triggers the documented manual process.

**Decision guide**

| Use when | Avoid when |
|---|---|
| The prototype has a measurable baseline, representative tests, named owners and reliable fallback. | Scaling because the demonstration looked fluent or because a platform is already licensed. |
| Users and affected people can understand the system's role and correction path. | Removing the manual route before reliability, support and recovery have been demonstrated. |

**Practitioner quality lens**

- Staged: Exposure grows only after evidence-based gates are met.
- Measured: Value, quality, fairness, safety and operating health are monitored.
- Operated: Owners, support, incidents, changes, fallback and retirement are defined.

**Authoritative references**

- https://airc.nist.gov/airmf-resources/airmf/5-sec-core/
- https://www.imda.gov.sg/how-we-can-help/ai-verify
- https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/

---


### Lab 5 — Simulate the Controlled Onboarding Workflow

Learning outcome: LO3: build and test a multi-step HR workflow with approved data, limited tools, human gates and complete run evidence.

Goal: Run four synthetic onboarding cases through a visible state machine and prove that duplicates, missing facts and unsafe actions stop correctly.

You will convert the Lab 4 onboarding plan into a state-based workflow. ReadPolicy, DraftPlan and CreateTask are represented by explicit tool contracts; write and send effects remain simulated. You will run normal, missing-data, duplicate and policy-conflict cases and reconcile every final state.

**What you'll build**

03-deployment/onboarding-workflow-spec.md and 03-deployment/workflow-run-log.csv with states, transition rules, tool contracts, four complete traces, human approvals, stop reasons and manual fallback.   (Tools: Text editor - spreadsheet - approved AI assistant - workflow-cases.csv - workflow-run-log-template.csv.)

**Prerequisites**

- Completed Lab 4 onboarding-support pack.
- Open labs/assets/workflow-cases.csv, labs/assets/workflow-spec-template.md and labs/assets/workflow-run-log-template.csv.
- Confirm that OS-001 Final_Approved_Text is labelled Plan_Version OS-001-FINAL-1.
- All system changes and messages are simulations; do not connect a live HR system.

**Step-by-step**

1. Copy workflow-spec-template.md to onboarding-workflow-spec.md. Confirm its states RECEIVED, VALIDATED, GROUNDED, DRAFTED, NEEDS_REVIEW, APPROVED, ACTIONED, CLOSED and STOPPED. Complete the prepared transition rows with trigger, rule, owner, evidence and failure route.

   ```bash
   Transition table: From | Trigger | Deterministic rule | Model task | Human decision | Owner | To | Evidence | Failure route
Completion: CLOSED only after required evidence and approval are present
Failure: STOPPED keeps reason, owner and manual next action
   ```

2. Add contracts for ReadPolicy, DraftPlan and CreateTask. Keep ReadPolicy read-only, DraftPlan non-actioning and CreateTask simulated. Specify input and output schemas, identity, permitted scope, timeout, retry, idempotency key, validation and evidence.

   ```bash
   ReadPolicy input: Topic,As_Of_Date -> Policy_ID,Effective_Date,Excerpt,Status
DraftPlan input: Case_ID,Approved_Source -> Draft,Source_Ledger,Unknowns
CreateTask input: Case_ID,Task_Code,Approval_Token -> SIMULATED_Task_ID,Status
Idempotency key: Employee_ID + Task_Code + Start_Date
Timeout/retry: ReadPolicy 10 seconds, one retry; DraftPlan 45 seconds, no automatic retry; CreateTask 10 seconds, no automatic retry
No tool may send a message or edit an employee record.
   ```

3. Copy the pre-populated workflow-run-log-template.csv into 03-deployment/workflow-run-log.csv. Process WF-001 to WF-004 one prepared row at a time. Apply required-field, source-status and duplicate checks before the DRAFTED state; repeat the duplicate check atomically with the approval-token check before CreateTask. Complete Actual_Result, To_State, evidence, owner and manual action cells.

   ```bash
   Case expectations:
WF-001 normal -> CLOSED
WF-002 missing Location -> STOPPED / MISSING_REQUIRED_FIELD
WF-003 duplicate key -> STOPPED / ALREADY_PROCESSED
WF-004 conflicting current policy -> STOPPED / SOURCE_CONFLICT
   ```

4. For WF-001 only, import the exact Lab 4 OS-001 Final_Approved_Text and cite Plan_Version OS-001-FINAL-1 as the DraftPlan output; do not generate a fresh plan. Confirm the Lab 4 seven-gate release record and create a synthetic approval token. Record a simulated task effect only after approval; every other case must stop before DraftPlan or CreateTask as specified.

   ```bash
   Approval token: APPR-WF-001-HR-001
Evidence before ACTIONED: required fields PASS | source current | Plan_Version OS-001-FINAL-1 | claim ledger clean | seven gates YES | named reviewer | approval timestamp
Simulated effect: TASK-WF-001-IT-SETUP; no external write occurs.
   ```

5. Reconcile the log. Every case must have one terminal state, a reason, an owner and a manual next action. Count cases by CLOSED and STOPPED, confirm no duplicate simulated Task_ID and add a one-paragraph fallback procedure for system outage or unresolved source conflict.

   ```bash
   Reconciliation: total cases = CLOSED + STOPPED = 4
Unique simulated Task_ID count = simulated action rows
Every STOPPED row: Stop_Reason + Human_Owner + Manual_Next_Action
Fallback: receive case - validate minimum fields - retrieve approved source manually - human review - record completion
   ```


**Test it**

The workflow specification must contain all nine states, three tool contracts, an approval gate and manual fallback. The run log must show WF-001 CLOSED and WF-002 to WF-004 STOPPED with the specified reasons; four terminal states must reconcile, no simulated Task_ID may repeat, and no external action may occur.

**Checkpoint and rejoin point**

Keep the specification and run log as the deployment evidence. Lab 6 uses the four traces, stop behaviour and approval evidence. To rejoin, confirm the reconciliation equation equals four.

**Troubleshooting**

| If this happens | Fix |
|---|---|
| A stopped case continues to later states. | Enforce terminal STOPPED behaviour and start a separate corrected run with a new Run_ID. |
| The duplicate case creates another simulated task. | Check the composite idempotency key before drafting or action and return ALREADY_PROCESSED. |
| The tool contract says 'appropriate access'. | Replace vague language with exact identity, operation, fields, destination and denied actions. |

**Challenge**

Add a safe retry for a temporary ReadPolicy timeout. Set maximum attempts, backoff, terminal status and evidence without allowing the retry to bypass source or approval checks.

**Reflection**

Which workflow truth belonged in a deterministic rule rather than the model, and what failure did that prevent?

> **Note:** The complete lab and its support-file references are in labs/lab-05-*.md. Use only the supplied synthetic Asteron People Operations data or information you are authorised to process. Do not paste credentials or real candidate, employee, payroll, health, performance or grievance information into an unapproved AI service. A named HR owner verifies every material statement, score, route, message and action.

---


### Lab 6 — Run the Governance Gate and Rollout Plan

Learning outcome: LO4: evaluate privacy, fairness, security and operating risk and produce a staged rollout with owners, metrics and fallback.

Goal: Use representative evidence to decide whether the Asteron HR-agent portfolio may enter a limited read-only pilot.

You will evaluate the recruitment and onboarding agents against normal, boundary, missing-source, unsafe-action and fairness-relevant cases. You will calculate quality and subgroup indicators, inspect reviewer changes, set release thresholds and write a staged rollout with named owners, monitoring and rollback.

**What you'll build**

03-deployment/governance-evaluation.csv and 03-deployment/hr-agent-rollout-plan.md with risk controls, calculated metrics, fairness investigation, release decision, pilot stages, owners, monitoring and fallback.   (Tools: Spreadsheet - text editor - governance-test-cases.csv - outputs from Labs 2-5.)

**Prerequisites**

- Completed and retained the Lab 2 FAQ pack, Lab 3 recruitment register, Lab 4 routing and release records, and Lab 5 reconciled workflow run log.
- Open labs/assets/governance-test-cases.csv and labs/assets/hr-agent-rollout-plan-template.md.
- Copy labs/assets/hr-agent-rollout-plan-template.md to 03-deployment/hr-agent-rollout-plan.md before Step 1.
- Before Step 1, confirm every G-001 to G-010 Evidence_Source exists and record READY or MISSING in an evidence-readiness table.
- Treat subgroup indicators as signals for investigation, not proof of cause or a new candidate criterion.

**Step-by-step**

1. Open 03-deployment/hr-agent-rollout-plan.md. Use its GOVERN, MAP, MEASURE and MANAGE headings. Inventory the two Asteron agents, affected people, sources, tools, decisions and owners. Map at least one privacy, fairness, security, accuracy, action-overreach and operating-continuity risk with a control and owner.

   ```bash
   Risk register: Risk_ID | Agent | Harm | Cause | Existing control | Test | Owner | Residual risk | Response
Required risks: privacy - fairness - source accuracy - prompt injection - unsafe action - outage/fallback
   ```

2. Copy governance-test-cases.csv to governance-evaluation.csv. For G-001 to G-010, record Expected, Actual, Pass, Evidence_ID, Severity and Repair. Use the retained Lab 2-5 artifacts where a test references a previous run; simulate only the missing cases and label them clearly.

   ```bash
   Pass rule: Actual exactly matches Expected
Seven critical cases: G-002 retired policy | G-003 unnecessary personal field | G-004 protected-trait inference | G-006 send/write | G-007 missing required field | G-008 duplicate action | G-009 source conflict
Evidence_ID: exact file plus row, Candidate_ID, Case_ID or Run_ID
   ```

3. Calculate four metrics: overall test pass rate, critical-case pass rate, grounding-defect rate and human-correction rate. Then use the supplied synthetic subgroup summary to calculate selection and deferral rates for Groups A and B and the smaller-to-larger selection-rate ratio. Record denominator, context and investigation questions; do not declare a cause from one small synthetic sample.

   ```bash
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

4. Set the release gate before making a decision: 100% critical-case pass, at least 90% overall pass, 0% grounding defects, named owners for all high residual risks and a tested manual fallback. For subgroup differences, require documented investigation and human review; do not invent a universal numeric fairness rule.

   ```bash
   Gate: critical 100% | overall >=90% | grounding defects 0% | high risks owned | fallback tested
Decision: HOLD | REPAIR_AND_RETEST | APPROVE_READ_ONLY_PILOT
Record: result - evidence - decision owner - conditions - next review date
   ```

5. Return to the same 03-deployment/hr-agent-rollout-plan.md and complete its prepared rollout table from synthetic sandbox to shadow, read-only pilot and controlled operation. For each stage define scope, users, data, actions, entry evidence, exit gate, training, communication, support, monitoring and rollback. Assign Business, HR process, Data, Technology, Privacy/Risk and Support owners and choose one value, quality, fairness, safety and operating metric.

   ```bash
   Stages: SYNTHETIC -> SHADOW -> READ_ONLY_PILOT -> CONTROLLED_OPERATION
Metrics: cycle time | grounded-answer accuracy | subgroup selection/deferral indicators | unsafe-action attempts | failure and escalation service level
Rollback triggers: critical test failure | policy conflict | unowned high risk | unsafe action | material drift
Fallback: approved manual HR process
   ```


**Test it**

The evaluation file must contain ten tests with expected, actual, pass, severity and evidence; all four quality metrics and both subgroup selection and deferral rates must show formulas and denominators. The rollout plan must cover six risk types, six owner roles, four stages, five monitoring dimensions, explicit gates, a release decision and a tested manual fallback. Critical pass rate must be 100% before any pilot approval.

**Checkpoint and rejoin point**

This is the final portfolio checkpoint. Keep all six lab outputs and supplied synthetic sources together. Rerun the governance evaluation whenever a prompt, rubric, policy source, model, tool, permission or workflow changes.

**Troubleshooting**

| If this happens | Fix |
|---|---|
| A percentage is calculated without a denominator. | Add numerator, denominator, formula and N/A handling before interpreting the result. |
| A subgroup difference is treated as proof of discrimination. | Record it as an investigation signal and inspect criteria, evidence, errors, deferrals, reviewer changes and context. |
| The rollout jumps from sandbox to full operation. | Insert shadow and limited read-only stages with observable entry and exit gates and a manual fallback. |

**Challenge**

Add a post-change regression scenario for a new policy version. State which test cases must rerun, which owners approve the change and which condition triggers rollback.

**Reflection**

Which single piece of evidence most strongly supports the release decision, and what important uncertainty still remains?

> **Note:** The complete lab and its support-file references are in labs/lab-06-*.md. Use only the supplied synthetic Asteron People Operations data or information you are authorised to process. Do not paste credentials or real candidate, employee, payroll, health, performance or grievance information into an unapproved AI service. A named HR owner verifies every material statement, score, route, message and action.

---


## Wrap-Up - Operate the Human-Owned HR Agent Portfolio

The six labs create one connected portfolio from use-case framing and grounded sources through recruitment and onboarding agents to a controlled workflow and staged rollout. The valuable artifact is the evidence chain, not a collection of prompts.

**The Six Questions Before Every HR-Agent Run**

Use the same questions when adapting a course pattern to workplace use.

- What exact HR outcome and people decision are in scope?
- Which current approved sources define truth for this case?
- Which data is necessary, and which fields or documents are prohibited?
- Which steps are fixed rules, model tasks, human decisions and controlled actions?
- Which checks, approvals and records prove a safe and useful outcome?
- How will a person question, correct or complete the process when the agent cannot?

**A Safe Workplace Handoff**

Adapt the synthetic patterns to organisational controls before using live HR information.

- Confirm approved services, data classes, identities, retention and system owners.
- Replace synthetic sources only with current, minimised and authorised HR data products.
- Pilot read-only or in shadow mode and compare with the approved current process.
- Train reviewers, communicate limitations and keep a tested manual fallback.

---


## Next Steps

- Choose one low-risk, read-only HR workflow and write its purpose, sources, action limits and human decision.
- Create at least ten representative test cases, including missing, conflicting, unsafe and fairness-relevant cases.
- Measure one value metric, one quality metric and one risk metric before and during a limited pilot.
- Run in shadow mode, retain every reviewer correction and decide whether the residual risk is acceptable.


## Glossary

- **Agent** — A system in which a model manages part of a workflow and selects approved tools inside explicit limits.
- **Agent run** — One traceable execution from validated request through sources, tools, checks, human decision and final status.
- **Approval gate** — A defined decision point with evidence, authorised role, choices, response time and fallback.
- **Authoritative source** — The current approved role, policy, record or process definition for a stated purpose.
- **Data contract** — A documented agreement on source, fields, grain, quality, ownership, access, lineage and permitted use.
- **Data minimisation** — Using only the personal data reasonably necessary for the stated purpose.
- **Deferral** — Routing a case to a human when evidence, confidence or authority is insufficient.
- **Deterministic check** — A rule that produces the same result from the same input, such as a required-field or duplicate check.
- **Fairness** — Job-related, consistent and transparent treatment with harmful bias identified and managed in context.
- **Grounding** — Constraining an output to approved retrieved evidence and preserving links to that evidence.
- **Human oversight** — A designed human decision with evidence, authority, time and the ability to change the result.
- **Idempotency** — The property that repeating an action does not create a duplicate effect.
- **Least privilege** — Granting only the data and action permissions required for one task.
- **Lineage** — The trace from an output to source records, versions, rules, transformations and decisions.
- **Model task** — A bounded use of a model for extraction, classification, drafting or critique.
- **Prompt contract** — Structured instructions defining goal, context, criteria, sources, output, review and escalation.
- **Protected characteristic** — A personal attribute that must not be used as an unsupported basis for employment decisions.
- **Run evidence** — The retained sources, prompts, tool calls, checks, edits, approvals, actions and final status.
- **Shadow mode** — Running a system alongside the approved process without allowing it to control the outcome.
- **Tool** — A governed function or connector an agent may call to retrieve, calculate, create or act.
