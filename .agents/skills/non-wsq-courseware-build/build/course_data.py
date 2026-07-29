"""Single source of truth for the C820 non-WSQ courseware package."""

TITLE = "AI for HR"
SHORT_TITLE = "AI for HR"
COURSE_CODE = "C820"
VERSION = "v1.0"
VERSION_DATE = "29 July 2026"
ORG = "Tertiary Infotech Academy Pte Ltd"
UEN = "UEN: 201200696W"
TRAINER = "Assigned Tertiary Infotech Academy Trainer"
COURSE_URL = "https://www.tertiarycourses.com.sg/ai-for-hr.html"
DAYS = 1
DAY_MINUTES = 480
INSTRUCTIONAL_MINUTES = 450
MODE = "Instructor-led, hands-on practical labs"
DAILY_TIMING = (
    "9:30 am-6:30 pm (1-hour lunch; two 15-minute tea breaks; "
    "7.5 instructional hours)"
)
DARK_THEME = False

LEARNING_OUTCOMES = [
    "LO1: Use an approved AI assistant with a structured prompt, source boundary and human review method for everyday HR work.",
    "LO2: Design bounded recruitment, onboarding, employee-support and communication agents with job-related criteria and explicit human decisions.",
    "LO3: Build and test a multi-step HR workflow that connects approved data and tools while preserving exceptions, approvals and run evidence.",
    "LO4: Evaluate privacy, fairness, security and operating risk, then produce a staged rollout plan with owners, metrics, monitoring and fallback.",
]

LO_TITLES = [
    "Prompt & Ground",
    "Design HR Agents",
    "Automate & Verify",
    "Govern & Roll Out",
]

TOPICS = [
    dict(
        num=1,
        code="01",
        title="Get Started with AI for HR",
        subtitle=(
            "AI and agentic AI use cases - tools and platforms - effective prompting - "
            "approved HR data and documents"
        ),
        weighting="Morning - 2 connected labs",
        concepts=[
            ("Assistant, automation, agent", "Choose the least autonomous pattern that can complete the HR job reliably."),
            ("Human-owned purpose", "Name the employee or candidate outcome, process owner and decision that remains human."),
            ("Prompt contract", "State goal, context, criteria, sources, output, review and escalation before using a model."),
            ("Grounded evidence", "Constrain material claims to approved policy, role and case sources and preserve their identifiers."),
            ("Data minimisation", "Use synthetic or necessary authorised fields and keep confidential or sensitive data out of unapproved tools."),
            ("Observable quality", "Define acceptance checks before comparing model outputs or platforms."),
        ],
        sections=[
            dict(
                title="AI and Agentic AI in HR: Use Cases and Landscape",
                definition=(
                    "Generative AI produces or transforms language and other content from instructions and context. "
                    "An AI assistant responds to a person, a deterministic automation follows fixed rules, and an "
                    "agent lets a model choose among approved next steps and tools inside a bounded workflow."
                ),
                why=(
                    "HR work combines high-volume drafting with decisions that affect people. Separating assistance, "
                    "automation and agency prevents a fluent tool from being given authority that belongs to an HR "
                    "professional, hiring manager, data owner or employee."
                ),
                how=[
                    "Define the HR outcome, affected people, process owner and authoritative sources.",
                    "Classify each step as fixed rule, model-supported judgement or human decision.",
                    "Grant only the data and tools required for the current step.",
                    "Set completion, uncertainty, exception, time and action limits.",
                    "Retain the source, output, checks, edits, decision and final status as run evidence.",
                ],
                example=[
                    "Asteron Services wants faster onboarding support for new employees.",
                    "A deterministic rule identifies the employee's country and start date; an assistant drafts a policy-grounded reply.",
                    "A named HR owner reviews exceptions and any message about eligibility, conduct, pay or personal circumstances.",
                ],
                use_when=[
                    "The task contains repeated language work, unstructured documents or exceptions that fixed rules handle poorly.",
                    "A clear source boundary, observable checks and accountable reviewer can be defined.",
                ],
                avoid_when=[
                    "A template, search filter or spreadsheet rule solves the task more simply and predictably.",
                    "The system would make an adverse or irreversible people decision without meaningful human review.",
                ],
                quality=[
                    ("Bounded", "Purpose, sources, tools, limits, stop conditions and fallback are explicit."),
                    ("Grounded", "Material statements trace to approved facts or rules."),
                    ("Accountable", "A named role owns the final people decision and communication."),
                ],
                sources=[
                    "https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/",
                    "https://airc.nist.gov/airmf-resources/airmf/",
                ],
            ),
            dict(
                title="Popular AI Tools and Agent Platforms",
                definition=(
                    "HR teams can work with browser assistants such as ChatGPT or Claude, configurable workspace "
                    "agents, low-code platforms such as Copilot Studio, or custom software. The options combine "
                    "models, instructions, knowledge and tools but differ in data handling, integration, testing, "
                    "identity, observability, cost and operating skill."
                ),
                why=(
                    "Choosing a product before defining the use case encourages feature-led adoption. A task-and-risk "
                    "comparison makes the platform decision explainable and avoids connecting broad HR repositories "
                    "to a prototype that needs only a synthetic policy extract."
                ),
                how=[
                    "Start with the HR job, data class, actions, users, volume and acceptable failure mode.",
                    "Prototype a prompt with synthetic sources in an approved supervised assistant.",
                    "Move to a workspace agent when reusable instructions and governed knowledge are sufficient.",
                    "Use low-code flow tooling for triggers, connectors, branching, approvals and monitoring.",
                    "Use custom development only when identity, tools, evaluation, telemetry or isolation require it.",
                ],
                example=[
                    "A one-off job-description critique stays in a supervised assistant with a synthetic role brief.",
                    "A reusable employee-policy helper uses approved knowledge and read-only access.",
                    "An onboarding workflow uses a flow platform because it needs triggers, record lookups, tasks, approvals and run history.",
                ],
                use_when=[
                    "Comparing platforms against an already documented HR workflow and control matrix.",
                    "The organisation can confirm approved services, data locations, identities and support ownership.",
                ],
                avoid_when=[
                    "Selecting the tool with the most connectors or the highest apparent autonomy.",
                    "Allowing inherited user permissions to expose unrelated employee or candidate records.",
                ],
                quality=[
                    ("Fit", "Workflow and risk needs drive the tool choice."),
                    ("Control", "Identity, data, actions and environments can be restricted."),
                    ("Visibility", "Versions, runs, failures, approvals and costs can be inspected."),
                ],
                sources=[
                    "https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/",
                    "https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview",
                    "https://learn.microsoft.com/en-us/microsoft-copilot-studio/fundamentals-what-is-copilot-studio",
                ],
            ),
            dict(
                title="Effective Prompting for HR Tasks",
                definition=(
                    "An HR prompt is a working contract. This course uses G-C-C-S-O-R: Goal, Context, Criteria, "
                    "Sources, Output and Review. The contract separates stable instructions from case variables, "
                    "defines the evidence boundary and makes the desired result testable."
                ),
                why=(
                    "Requests such as 'screen these resumes' or 'write an onboarding email' hide the selection basis, "
                    "source truth and acceptance checks. A structured prompt reduces generic output and makes unsupported "
                    "claims, missing facts and inappropriate inferences easier to detect."
                ),
                how=[
                    "State one HR goal, intended reader and permitted decision support.",
                    "Provide only relevant context and label each approved source with a stable identifier.",
                    "Define job-related or policy-based criteria before asking for analysis.",
                    "Specify output fields for facts, source, uncertainty, recommendation and human action.",
                    "Require UNKNOWN, clarification or escalation when evidence is absent.",
                    "Review accuracy, fairness, privacy, rights, tone and action authority before use.",
                ],
                example=[
                    "Goal: draft a first-day email for a Singapore-based new employee.",
                    "Sources: offer-confirmation facts and approved onboarding policy excerpts; personal medical or family information is excluded.",
                    "Output: subject, message, source ledger and unresolved questions; any policy exception is marked ESCALATE TO HR.",
                ],
                use_when=[
                    "The same HR transformation or review task will recur with different approved inputs.",
                    "Success criteria can be checked against a source, rubric, schema or reviewer checklist.",
                ],
                avoid_when=[
                    "The purpose, authorised source or intended human decision is unclear.",
                    "The prompt would include real personal data in a service not approved for that data.",
                ],
                quality=[
                    ("Specific", "Goal, scope, audience, criteria and format are explicit."),
                    ("Evidence-led", "Sources are delimited and every material claim carries a reference."),
                    ("Fail-safe", "Missing or conflicting evidence triggers a question or escalation."),
                ],
                sources=[
                    "https://help.openai.com/en/articles/10032626-prompt-engineering-best-practices",
                    "https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview",
                ],
            ),
            dict(
                title="Connecting AI to HR Data and Documents",
                definition=(
                    "A governed HR connection exposes a defined source through a limited interface. Its data contract "
                    "records purpose, owner, fields, record grain, version, refresh time, permitted users, retention, "
                    "quality checks and whether the connection may read or write."
                ),
                why=(
                    "Candidate and employee repositories contain personal and sometimes sensitive information. Broad "
                    "access increases privacy, prompt-injection and accidental-action risk, while unclear versions allow "
                    "an agent to quote a retired policy as if it were current."
                ),
                how=[
                    "Classify the use case and minimise rows, fields, periods and documents before connection.",
                    "Begin with synthetic or de-identified snapshots and read-only tools.",
                    "Record authoritative owner, effective date, version, jurisdiction and expiry for every policy.",
                    "Validate completeness, duplicates, field meanings, access and document status before retrieval.",
                    "Return source identifiers and timestamps with retrieved content.",
                    "Separate retrieval from any write, send or status-change tool and place approvals before actions.",
                ],
                example=[
                    "The employee helper can retrieve three approved policy excerpts by Policy_ID and Effective_Date.",
                    "It cannot browse payroll, performance or medical folders and has no send permission.",
                    "A conflicting or expired excerpt stops the run and creates a question for the policy owner.",
                ],
                use_when=[
                    "A repeatable workflow needs approved structured records or policy documents.",
                    "A data owner can define purpose, quality, access, retention and lineage.",
                ],
                avoid_when=[
                    "The connector exposes an entire HR drive or inherited administrator privileges.",
                    "The source has no owner, effective date, stable identifier or current-version rule.",
                ],
                quality=[
                    ("Minimal", "Only the necessary records and fields are available."),
                    ("Current", "Version, effective date and authoritative owner are visible."),
                    ("Traceable", "Each output points to the exact source retrieved for that run."),
                ],
                sources=[
                    "https://www.pdpc.gov.sg/guidelines-and-consultation/2024/02/advisory-guidelines-on-use-of-personal-data-in-ai-recommendation-and-decision-systems",
                    "https://www.pdpc.gov.sg/help-and-resources/2020/01/model-ai-governance-framework",
                ],
            ),
        ],
    ),
    dict(
        num=2,
        code="02",
        title="Build HR AI Agents",
        subtitle=(
            "agent workflow design - recruitment decision support - onboarding and "
            "employee support - HR content and communications"
        ),
        weighting="Midday and afternoon - 2 connected labs",
        concepts=[
            ("Workflow contract", "Map trigger, sources, tools, branches, decisions, evidence and fallback before configuration."),
            ("Job-related rubric", "Translate role requirements into consistent observable criteria before reviewing candidates."),
            ("Decision support", "The agent organises evidence and questions; an authorised person owns the hiring decision."),
            ("Policy-grounded support", "Answer from current approved policy and escalate personal, ambiguous or high-impact cases."),
            ("Human communication", "Use AI for options and editing while a responsible sender verifies facts, tone and audience."),
            ("Verification", "Test normal, boundary, missing-data, conflicting-source and unsafe-action cases."),
        ],
        sections=[
            dict(
                title="Designing Agentic AI Workflows for HR",
                definition=(
                    "An HR agent workflow is a bounded sequence in which a model may choose among approved read, "
                    "transform, classify, ask and draft steps. The design contract defines triggers, inputs, state, "
                    "tools, branches, human decisions, evidence and stop conditions before a platform is configured."
                ),
                why=(
                    "A demonstration often shows only the happy path. HR operations also contain missing documents, "
                    "policy conflicts, candidate questions, protected information and exceptions that need a clear "
                    "owner rather than an improvised model response."
                ),
                how=[
                    "Write the outcome and non-goals, then draw the current human workflow.",
                    "Classify each step as deterministic rule, model task, human decision or external action.",
                    "Define tool inputs, outputs, permissions, timeouts and idempotency keys.",
                    "Add escalation for uncertainty, conflicting sources and high-impact cases.",
                    "Define completion evidence and a manual fallback before the first prototype.",
                ],
                example=[
                    "Trigger: an approved new-hire record is created with a start date and location.",
                    "The flow checks required fields, retrieves current policy, drafts tasks and asks HR to approve the plan.",
                    "Only after approval are tasks created; duplicate Employee_ID and Start_Date runs are blocked.",
                ],
                use_when=[
                    "The process is multi-step, has repeated exceptions and can be represented with explicit states.",
                    "Owners can specify allowed actions and what evidence proves completion.",
                ],
                avoid_when=[
                    "The desired outcome changes from case to case without a stable owner or policy basis.",
                    "The agent would need unrestricted access or an irreversible action without an approval boundary.",
                ],
                quality=[
                    ("Complete", "Trigger, inputs, states, branches, owners and finish conditions are mapped."),
                    ("Least privilege", "Every tool exposes only the fields and actions required."),
                    ("Recoverable", "Retries, duplicates, failures and manual fallback are designed."),
                ],
                sources=[
                    "https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/",
                    "https://learn.microsoft.com/en-us/microsoft-copilot-studio/flows-overview",
                ],
            ),
            dict(
                title="Recruitment and Candidate Screening Agents",
                definition=(
                    "A recruitment agent can extract role-relevant evidence, compare it with a pre-approved rubric, "
                    "identify missing information and prepare consistent interview questions. It is decision support: "
                    "it must not infer protected traits or replace the accountable hiring decision."
                ),
                why=(
                    "Unstructured resume review is vulnerable to inconsistent criteria and unsupported assumptions. "
                    "A transparent rubric tied to actual job requirements improves consistency, while source citations, "
                    "deferral and human review expose uncertainty instead of hiding it."
                ),
                how=[
                    "Complete job analysis and approve skills, experience and evidence anchors before candidate review.",
                    "Remove non-job-related fields and instruct the system not to infer protected characteristics.",
                    "Extract evidence with resume line or record references; mark missing facts UNKNOWN.",
                    "Apply the same anchored rubric to every candidate for the same role.",
                    "Compare proposed and final human scores and record adjustments with reasons.",
                    "Monitor outcomes, error patterns and subgroup effects where lawful and appropriate.",
                ],
                example=[
                    "A role requires service-case handling, spreadsheet reporting and stakeholder communication.",
                    "The agent cites evidence for each criterion and writes UNKNOWN when a resume lacks sufficient detail.",
                    "The hiring panel reviews all evidence, corrects one over-score and owns the shortlist and interview plan.",
                ],
                use_when=[
                    "Criteria are job-related, documented and applied consistently across the candidate set.",
                    "The agent can cite evidence and defer uncertain cases to trained reviewers.",
                ],
                avoid_when=[
                    "Inferring age, disability, family status, ethnicity, health, personality or other sensitive traits.",
                    "Automatically rejecting a candidate or changing criteria after seeing candidate identities.",
                ],
                quality=[
                    ("Relevant", "Every criterion is justified by the job analysis."),
                    ("Consistent", "The same rubric and evidence rules apply to all candidates."),
                    ("Reviewable", "Sources, unknowns, scores, changes and final human decision are retained."),
                ],
                sources=[
                    "https://www.tal.sg/tafep/getting-started/fair/tripartite-guidelines",
                    "https://www.tal.sg/tafep/resources/tools-and-templates/2025/tafep-recruitment-checklist",
                    "https://www.pdpc.gov.sg/guidelines-and-consultation/2024/02/advisory-guidelines-on-use-of-personal-data-in-ai-recommendation-and-decision-systems",
                ],
            ),
            dict(
                title="Onboarding and Employee Support Agents",
                definition=(
                    "An onboarding or employee-support agent retrieves approved policy, gathers only necessary case "
                    "facts, prepares tasks or a draft answer and routes exceptions to the correct owner. It should show "
                    "the source and effective date and make escalation easy."
                ),
                why=(
                    "Fast answers improve the employee experience only when they are current and appropriate for the "
                    "employee's context. A confident response from an expired policy can create more work and harm than "
                    "a clear handoff to HR."
                ),
                how=[
                    "Create an intent list and define which questions the agent may answer, draft or only route.",
                    "Retrieve current policy by stable identifier, jurisdiction and effective date.",
                    "Ask only for the minimum case facts needed to choose an approved route.",
                    "Return answer, source, confidence limits, next action and escalation path.",
                    "Separate support content from personal case decisions and employee-relations matters.",
                    "Log unanswered questions to improve the knowledge base through a controlled process.",
                ],
                example=[
                    "A new employee asks when to complete the equipment form and where to find it.",
                    "The agent cites ONB-02, provides the current deadline and link, and labels the response as general guidance.",
                    "A question about a personal leave exception is routed to an HR partner without the agent deciding eligibility.",
                ],
                use_when=[
                    "Approved policy and process sources are current, versioned and owned.",
                    "The support boundary and escalation routes are clear to employees and operators.",
                ],
                avoid_when=[
                    "A personal case requires judgement, accommodation, investigation, discipline or legal interpretation.",
                    "The knowledge source contains conflicting or expired versions without an authoritative rule.",
                ],
                quality=[
                    ("Current", "Every answer shows the source and effective date."),
                    ("Proportionate", "Only necessary case information is requested."),
                    ("Escalatable", "High-impact and unresolved questions reach a named human route."),
                ],
                sources=[
                    "https://learn.microsoft.com/en-us/microsoft-copilot-studio/fundamentals-what-is-copilot-studio",
                    "https://www.pdpc.gov.sg/guidelines-and-consultation/2024/02/advisory-guidelines-on-use-of-personal-data-in-ai-recommendation-and-decision-systems",
                ],
            ),
            dict(
                title="Drafting HR Content and Communications with AI",
                definition=(
                    "AI can generate and transform job descriptions, interview guides, onboarding messages, policy "
                    "summaries and employee updates. The responsible sender supplies approved facts, reader context, "
                    "tone and channel constraints, then verifies and edits before release."
                ),
                why=(
                    "HR language can shape access, trust and employee action. Generic or exclusionary wording, invented "
                    "benefits and an incorrect deadline can cause real consequences even when the message sounds polished."
                ),
                how=[
                    "Name the audience, communication purpose, required action and approved source facts.",
                    "Specify plain-language, accessibility, inclusive-language and channel requirements.",
                    "Request options or critique rather than accepting the first draft.",
                    "Use a claim ledger to check dates, policy statements, links and promises.",
                    "Run a fairness, privacy, tone and action review and retain the final human edit.",
                ],
                example=[
                    "An agent drafts a role advertisement from an approved job analysis and removes non-job-related preferences.",
                    "It produces a first-day email from current onboarding policy and flags a missing equipment-contact name.",
                    "The HR owner supplies the missing fact, edits the tone and approves the final versions.",
                ],
                use_when=[
                    "The communication has an accountable sender and a complete approved fact base.",
                    "The output can be checked against job, policy, brand and accessibility criteria.",
                ],
                avoid_when=[
                    "Sending high-impact or personalised messages automatically from an unreviewed draft.",
                    "Creating promises, role requirements or policy interpretations beyond the supplied source.",
                ],
                quality=[
                    ("Accurate", "Every date, promise, requirement and link is verified."),
                    ("Inclusive", "Language is job-related, respectful and accessible."),
                    ("Owned", "The named sender reviews the final message and intended audience."),
                ],
                sources=[
                    "https://help.openai.com/en/articles/10032626-prompt-engineering-best-practices",
                    "https://www.tal.sg/tafep/getting-started/fair/tripartite-guidelines",
                ],
            ),
        ],
    ),
    dict(
        num=3,
        code="03",
        title="Deploy Agentic AI Across the HR Function",
        subtitle=(
            "multi-step automation - HR system integration - privacy, fairness and "
            "human oversight - staged organisational rollout"
        ),
        weighting="Afternoon - 2 connected labs",
        concepts=[
            ("Control-first automation", "Design deterministic checks, model tasks and human gates as separate visible steps."),
            ("Integration contract", "Specify identity, source, schema, permission, failure, retry and evidence for each connector."),
            ("Action boundary", "Draft and recommend before any write, send, status change or people decision."),
            ("Risk-tiered oversight", "Increase human involvement with uncertainty, sensitivity, impact and reversibility."),
            ("Evaluation set", "Test normal, boundary, missing, conflicting, unsafe and fairness-relevant cases before pilot."),
            ("Staged rollout", "Move from synthetic sandbox to shadow, read-only pilot and controlled operation with fallback."),
        ],
        sections=[
            dict(
                title="Automating Multi-Step HR Workflows with AI Agents",
                definition=(
                    "A multi-step HR workflow coordinates triggers, deterministic rules, model tasks, human decisions "
                    "and controlled actions over a visible state. The system completes only when required checks, "
                    "approvals and evidence are present."
                ),
                why=(
                    "Automation can reduce handoffs but also repeats mistakes at speed. Separating deterministic truth, "
                    "model-supported judgement and human authority makes the process easier to test, stop and recover."
                ),
                how=[
                    "Define states such as RECEIVED, VALIDATED, DRAFTED, NEEDS_REVIEW, APPROVED, ACTIONED and CLOSED.",
                    "Use deterministic checks for required fields, dates, identifiers, duplicates and routing.",
                    "Use the model only for bounded extraction, classification, drafting or critique.",
                    "Place approval before external messages, record changes and high-impact decisions.",
                    "Make actions idempotent and log state transitions, evidence and errors.",
                    "Provide timeout, retry, exception queue and manual completion routes.",
                ],
                example=[
                    "An onboarding case enters RECEIVED and fails if Employee_ID, Start_Date or Location is absent.",
                    "The model drafts the plan from approved policy; HR reviews exceptions and approves task creation.",
                    "A repeated event with the same case key returns ALREADY_PROCESSED instead of creating duplicate tasks.",
                ],
                use_when=[
                    "The process has stable states, frequent handoffs and observable completion conditions.",
                    "Owners can define action permissions, approvals, exception service levels and fallback.",
                ],
                avoid_when=[
                    "A workflow is still changing daily and no stable current process exists.",
                    "Failures cannot be detected, reversed or completed through a manual route.",
                ],
                quality=[
                    ("Deterministic", "Rules own identifiers, dates, completeness, duplicates and thresholds."),
                    ("Bounded", "Model tasks have explicit inputs, outputs and escalation."),
                    ("Recoverable", "Every failure has an owner, retry rule and manual path."),
                ],
                sources=[
                    "https://learn.microsoft.com/en-us/microsoft-copilot-studio/flows-overview",
                    "https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/",
                ],
            ),
            dict(
                title="Integrating Agents with HR Systems and Tools",
                definition=(
                    "An integration contract describes one tool call: authenticated identity, permitted operation, "
                    "input schema, output schema, data scope, validation, timeout, retry, error handling, evidence and "
                    "owner. Read, calculate, draft and action tools should remain distinct."
                ),
                why=(
                    "A connector inherits technical reach that may exceed the business use case. Explicit contracts "
                    "reduce over-broad access and make it possible to test whether a run read the right record, used the "
                    "right version and changed only what an authorised person approved."
                ),
                how=[
                    "Use a service or user identity with least privilege and a named owner.",
                    "Whitelist operations, fields, destinations and case types; deny everything else.",
                    "Validate input and output schemas and reject unexpected fields or embedded instructions.",
                    "Require approval tokens for write, send and status-change actions.",
                    "Use correlation and idempotency keys to link events and prevent duplicate effects.",
                    "Log tool name, parameters, result, latency, error and approving role without exposing unnecessary data.",
                ],
                example=[
                    "ReadPolicy accepts Policy_ID and As_Of_Date and returns approved text, owner and effective date.",
                    "CreateOnboardingTask accepts a validated case key and approval token but cannot edit employee records.",
                    "SendMessage remains disabled in the sandbox; the lab records a simulated message and complete audit line.",
                ],
                use_when=[
                    "A stable API, connector or controlled file interface has an accountable system owner.",
                    "The workflow can prove the identity, scope and effect of each tool call.",
                ],
                avoid_when=[
                    "Using a shared administrator account or exposing an entire system to simplify a prototype.",
                    "Allowing retrieved documents to redefine tool permissions or bypass approval.",
                ],
                quality=[
                    ("Authorised", "Identity and operation match the current user's and workflow's authority."),
                    ("Validated", "Schemas, values, destinations and effects are checked."),
                    ("Auditable", "Every call and approval is linked to one traceable case."),
                ],
                sources=[
                    "https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced-use-flow",
                    "https://airc.nist.gov/airmf-resources/airmf/5-sec-core/",
                ],
            ),
            dict(
                title="Governance, Fairness and Human Oversight",
                definition=(
                    "HR AI governance assigns decision rights and controls across purpose, data, model, tools, users, "
                    "evaluation, operation and incident response. Human oversight is a designed decision point with "
                    "evidence, authority, time and fallback, not a generic instruction to review."
                ),
                why=(
                    "HR systems can affect access to work, employee experience and personal data. Trust depends on "
                    "job-related criteria, proportionate data use, transparent limitations, tested performance, "
                    "meaningful review and a route for correction or challenge."
                ),
                how=[
                    "Inventory the use case, affected people, decisions, data, vendors and owners.",
                    "Map benefits and harms, including privacy, bias, exclusion, security and automation overreach.",
                    "Choose human involvement by impact, uncertainty, reversibility and affected-person expectations.",
                    "Test source accuracy, unsafe actions, subgroup effects, deferral and override behaviour.",
                    "Communicate purpose, limitations, data use and routes for questions or correction.",
                    "Monitor incidents, complaints, drift, reviewer changes and policy updates after launch.",
                ],
                example=[
                    "The candidate assistant may propose rubric evidence but cannot reject, rank on protected traits or contact candidates.",
                    "A trained panel sees the source, unknowns and proposed score and records the final decision and reason.",
                    "Monthly review compares subgroup selection, deferral and correction rates and investigates material gaps.",
                ],
                use_when=[
                    "Before pilot, after material changes and throughout operation.",
                    "The organisation can assign business, HR, data, technology, privacy and risk ownership.",
                ],
                avoid_when=[
                    "Treating policy approval as a substitute for testing actual cases and workflow behaviour.",
                    "Using a human reviewer who lacks evidence, authority, time or a meaningful ability to change the result.",
                ],
                quality=[
                    ("Human-centric", "People outcomes, recourse and responsible decision rights shape the design."),
                    ("Fair", "Job-related criteria and subgroup effects are examined with context."),
                    ("Transparent", "Purpose, limits, sources, decisions and correction routes are visible."),
                ],
                sources=[
                    "https://www.pdpc.gov.sg/help-and-resources/2020/01/model-ai-governance-framework",
                    "https://www.imda.gov.sg/how-we-can-help/ai-verify",
                    "https://www.tal.sg/tafep/getting-started/fair/tripartite-guidelines",
                    "https://www.pdpc.gov.sg/guidelines-and-consultation/2024/02/advisory-guidelines-on-use-of-personal-data-in-ai-recommendation-and-decision-systems",
                ],
            ),
            dict(
                title="Rolling Out Agentic AI in Your Organisation",
                definition=(
                    "Rollout is a staged operating change. A use case moves through discovery, synthetic sandbox, "
                    "shadow run, read-only pilot and controlled operation only when value, quality, safety, ownership, "
                    "support and fallback evidence meet defined gates."
                ),
                why=(
                    "A successful prompt is not an operating service. HR adoption also requires current data, trained "
                    "reviewers, employee communication, monitoring, support, incident response, change control and a "
                    "manual route when the system is unavailable or unsafe."
                ),
                how=[
                    "Prioritise one bounded use case by value, feasibility, data readiness and residual risk.",
                    "Set a manual baseline, outcome metric, quality metric, risk metric and stop threshold.",
                    "Test on representative synthetic cases and repair failures before connecting live data.",
                    "Run in shadow or read-only mode and compare outputs with the approved current process.",
                    "Pilot with limited users, data and actions; train reviewers and communicate limitations.",
                    "Monitor, review, version, roll back or retire through named governance and support owners.",
                ],
                example=[
                    "Asteron pilots policy-grounded onboarding support for one office and two trained HR reviewers.",
                    "The pilot tracks resolution quality, grounding-defect rate, escalation accuracy, correction rate and cycle time.",
                    "Any policy-source conflict or unsafe-action attempt stops the run and triggers the documented manual process.",
                ],
                use_when=[
                    "The prototype has a measurable baseline, representative tests, named owners and reliable fallback.",
                    "Users and affected people can understand the system's role and correction path.",
                ],
                avoid_when=[
                    "Scaling because the demonstration looked fluent or because a platform is already licensed.",
                    "Removing the manual route before reliability, support and recovery have been demonstrated.",
                ],
                quality=[
                    ("Staged", "Exposure grows only after evidence-based gates are met."),
                    ("Measured", "Value, quality, fairness, safety and operating health are monitored."),
                    ("Operated", "Owners, support, incidents, changes, fallback and retirement are defined."),
                ],
                sources=[
                    "https://airc.nist.gov/airmf-resources/airmf/5-sec-core/",
                    "https://www.imda.gov.sg/how-we-can-help/ai-verify",
                    "https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/",
                ],
            ),
        ],
    ),
]

DAY_THEMES = {
    1: "Prompt, Build and Govern - create a controlled HR-agent portfolio from approved evidence",
}


def SCHEDULE(lab_titles):
    return {
        1: (
            DAY_THEMES[1],
            [
                ("9:30", "9:40", 10, "admin", "Welcome, course orientation, synthetic scenario and responsible-use ground rules"),
                ("9:40", "10:10", 30, "topic", "Topic 1 - AI landscape, tool choices and human-owned use cases"),
                ("10:10", "10:55", 45, "lab", "Hands-on: " + lab_titles([1])),
                ("10:55", "11:10", 15, "break", "Tea break"),
                ("11:10", "11:35", 25, "topic", "Topic 1 - prompt contracts, grounding and governed HR sources"),
                ("11:35", "12:20", 45, "lab", "Hands-on: " + lab_titles([2])),
                ("12:20", "12:40", 20, "topic", "Topic 2 - HR-agent workflow, recruitment and communication concepts"),
                ("12:40", "13:40", 60, "lunch", "Lunch break"),
                ("13:40", "14:30", 50, "lab", "Hands-on: " + lab_titles([3])),
                ("14:30", "15:00", 30, "topic", "Topic 2 - onboarding, employee support and human communication"),
                ("15:00", "15:50", 50, "lab", "Hands-on: " + lab_titles([4])),
                ("15:50", "16:05", 15, "break", "Tea break"),
                ("16:05", "16:35", 30, "topic", "Topic 3 - integration, multi-step automation and oversight"),
                ("16:35", "17:20", 45, "lab", "Hands-on: " + lab_titles([5])),
                ("17:20", "18:20", 60, "lab", "Hands-on: " + lab_titles([6])),
                ("18:20", "18:30", 10, "recap", "Integrated LO1-LO4 recap, action planning and Q&A"),
            ],
        ),
    }


COURSE_OVERVIEW = dict(
    section_title="The Human-Owned HR Agent",
    concepts_title="Four Boundaries Before Any Build",
    concepts=[
        ("Purpose boundary", "Define the HR outcome, affected people, non-goals and accountable owner."),
        ("Evidence boundary", "Use necessary approved sources with version, owner and lineage."),
        ("Action boundary", "Separate read, draft, recommend, approve and execute permissions."),
        ("Decision boundary", "Keep consequential people decisions with an authorised human who can change the result."),
    ],
    framework_title="One Controlled HR-Agent Run",
    framework=[
        ("Receive", "Validate requester, purpose, case and permitted data."),
        ("Ground", "Retrieve the current approved role, policy or workflow source."),
        ("Work", "Apply fixed rules and bounded model tasks."),
        ("Review", "Check evidence, fairness, privacy, tone and action authority."),
        ("Decide", "A named human approves, edits, escalates or stops."),
        ("Record", "Retain sources, checks, decision, action and final status."),
    ],
    statement=dict(
        headline="Use AI to organise HR work - never to hide how a people decision was made.",
        body="Every material claim has a source, every exception has an owner and every consequential decision remains human-owned.",
        kicker="COURSE OPERATING PRINCIPLE",
    ),
    pillars_title="What You Will Build",
    pillars=[
        ("Foundation", ["HR use-case and control canvas", "grounded prompt and source pack"]),
        ("HR Agents", ["recruitment evidence assistant", "onboarding and employee-support pack"]),
        ("Deployment", ["multi-step workflow simulation", "governance test and rollout plan"]),
    ],
    arc_title="How Every Lab Progresses",
    arc=[
        "Open the approved synthetic Asteron People Operations checkpoint.",
        "Apply a prompt contract, rubric or workflow rule to bounded inputs.",
        "Separate source facts, model output, deterministic checks and human decisions.",
        "Run the observable Test It checks and repair defects.",
        "Save the evidence and rejoin checkpoint for the next lab.",
    ],
    deep_dives=[
        dict(
            title="Assistant, Automation or Agent?",
            kicker="CONCEPT DEEP DIVE",
            items=[
                ("Assistant", "A person chooses each request and decides what to do with the answer."),
                ("Automation", "Fixed rules execute a known sequence with predictable branches."),
                ("Agent", "A model chooses among approved next actions inside explicit limits."),
                ("Design rule", "Use the least autonomy that meets the HR need."),
            ],
        ),
        dict(
            title="The HR Evidence Stack",
            kicker="CONCEPT DEEP DIVE",
            items=[
                ("Authoritative source", "Current role, policy, record or approved process definition."),
                ("Deterministic layer", "Required fields, dates, identifiers, formulas, thresholds and routing."),
                ("Model layer", "Extraction, classification, drafting, critique and exception explanation."),
                ("Decision layer", "Named human authority, reason, communication and controlled action."),
            ],
        ),
        dict(
            title="The Five Human Review Questions",
            kicker="CONCEPT DEEP DIVE",
            items=[
                ("Evidence", "Which approved source supports each material statement?"),
                ("Fairness", "Are criteria job-related, consistent and free of unsupported inference?"),
                ("Privacy", "Is each data field necessary and handled in an approved service?"),
                ("Authority", "May this system only draft, or may it take the proposed action?"),
                ("Recourse", "Can the affected person or operator question and correct the result?"),
            ],
        ),
    ],
)

LAB_SHOTS = {}

LG_INTRO = (
    "This Learner Guide accompanies AI for HR (C820), a one-day course on practical, human-owned use of "
    "AI and agentic workflows across recruitment, onboarding, employee support and HR operations. It follows "
    "the published three-topic sequence exactly and uses six connected Asteron People Operations labs."
)
LG_INTRO2 = (
    "Use the guide as a post-course reference. Each published sub-topic is taught through a definition, "
    "purpose, process, worked HR example, decision guide and practitioner controls before its related lab. "
    "Source links point to primary AI-platform, Singapore data-governance, fair-employment and risk-management guidance. "
    "The materials are educational and do not replace organisational HR, privacy, security or legal review."
)

LG_SETUP = dict(
    needs=[
        "A Windows or macOS laptop with a modern browser, spreadsheet application and text editor.",
        "Access to one organisation-approved AI assistant such as ChatGPT, Claude or Copilot.",
        "The supplied synthetic files in labs/assets/; do not substitute real candidate or employee records during class.",
        "A local folder named C820-Asteron-HR-Agent for all lab outputs.",
    ],
    verify_text=(
        "Create the workspace, open every supplied Markdown and CSV file and confirm that commas, dates and UTF-8 text "
        "display correctly. If no AI assistant is available, use the prompt templates to produce a manual draft and "
        "complete every evidence, rubric, workflow and review step yourself."
    ),
    verify_code=(
        "C820-Asteron-HR-Agent/\n"
        "  01-foundation/\n"
        "  02-hr-agents/\n"
        "  03-deployment/\n"
        "  run-evidence/"
    ),
    conventions=[
        "Use only the supplied synthetic Asteron data or information you are authorised to process.",
        "Label SOURCE FACT, MODEL DRAFT, DETERMINISTIC CHECK, UNKNOWN and HUMAN DECISION separately.",
        "Write the source ID beside every material policy, candidate or workflow statement.",
        "Keep draft, reviewer edit, approval or escalation reason and final status for each lab checkpoint.",
    ],
)

LAB_NOTE = (
    "Use only the supplied synthetic Asteron People Operations data or information you are authorised to process. "
    "Do not paste credentials or real candidate, employee, payroll, health, performance or grievance information into "
    "an unapproved AI service. A named HR owner verifies every material statement, score, route, message and action."
)

LG_WRAPUP = dict(
    title="Wrap-Up - Operate the Human-Owned HR Agent Portfolio",
    intro=(
        "The six labs create one connected portfolio from use-case framing and grounded sources through recruitment "
        "and onboarding agents to a controlled workflow and staged rollout. The valuable artifact is the evidence chain, "
        "not a collection of prompts."
    ),
    sections=[
        dict(
            title="The Six Questions Before Every HR-Agent Run",
            text="Use the same questions when adapting a course pattern to workplace use.",
            bullets=[
                "What exact HR outcome and people decision are in scope?",
                "Which current approved sources define truth for this case?",
                "Which data is necessary, and which fields or documents are prohibited?",
                "Which steps are fixed rules, model tasks, human decisions and controlled actions?",
                "Which checks, approvals and records prove a safe and useful outcome?",
                "How will a person question, correct or complete the process when the agent cannot?",
            ],
        ),
        dict(
            title="A Safe Workplace Handoff",
            text="Adapt the synthetic patterns to organisational controls before using live HR information.",
            bullets=[
                "Confirm approved services, data classes, identities, retention and system owners.",
                "Replace synthetic sources only with current, minimised and authorised HR data products.",
                "Pilot read-only or in shadow mode and compare with the approved current process.",
                "Train reviewers, communicate limitations and keep a tested manual fallback.",
            ],
        ),
    ],
)

LG_NEXT_STEPS = [
    "Choose one low-risk, read-only HR workflow and write its purpose, sources, action limits and human decision.",
    "Create at least ten representative test cases, including missing, conflicting, unsafe and fairness-relevant cases.",
    "Measure one value metric, one quality metric and one risk metric before and during a limited pilot.",
    "Run in shadow mode, retain every reviewer correction and decide whether the residual risk is acceptable.",
]

LG_GLOSSARY = [
    ("Agent", "A system in which a model manages part of a workflow and selects approved tools inside explicit limits."),
    ("Agent run", "One traceable execution from validated request through sources, tools, checks, human decision and final status."),
    ("Approval gate", "A defined decision point with evidence, authorised role, choices, response time and fallback."),
    ("Authoritative source", "The current approved role, policy, record or process definition for a stated purpose."),
    ("Data contract", "A documented agreement on source, fields, grain, quality, ownership, access, lineage and permitted use."),
    ("Data minimisation", "Using only the personal data reasonably necessary for the stated purpose."),
    ("Deferral", "Routing a case to a human when evidence, confidence or authority is insufficient."),
    ("Deterministic check", "A rule that produces the same result from the same input, such as a required-field or duplicate check."),
    ("Fairness", "Job-related, consistent and transparent treatment with harmful bias identified and managed in context."),
    ("Grounding", "Constraining an output to approved retrieved evidence and preserving links to that evidence."),
    ("Human oversight", "A designed human decision with evidence, authority, time and the ability to change the result."),
    ("Idempotency", "The property that repeating an action does not create a duplicate effect."),
    ("Least privilege", "Granting only the data and action permissions required for one task."),
    ("Lineage", "The trace from an output to source records, versions, rules, transformations and decisions."),
    ("Model task", "A bounded use of a model for extraction, classification, drafting or critique."),
    ("Prompt contract", "Structured instructions defining goal, context, criteria, sources, output, review and escalation."),
    ("Protected characteristic", "A personal attribute that must not be used as an unsupported basis for employment decisions."),
    ("Run evidence", "The retained sources, prompts, tool calls, checks, edits, approvals, actions and final status."),
    ("Shadow mode", "Running a system alongside the approved process without allowing it to control the outcome."),
    ("Tool", "A governed function or connector an agent may call to retrieve, calculate, create or act."),
]

TRAINER_TEAM = [
    (
        "Assigned Tertiary Infotech Academy Trainer",
        "HR-technology and agentic-AI facilitator who guides human-owned workflow design, evidence-led prompting, "
        "fair recruitment support, policy-grounded employee service and practical deployment controls.",
    ),
]

NEXT_STEPS = dict(
    title="Continue with a Read-Only HR Pilot",
    items=[
        "Choose one bounded HR support task with current approved sources and an accountable owner.",
        "Create a prompt contract, workflow map and representative evaluation set.",
        "Run in shadow mode, compare with the approved process and capture every correction.",
        "Expand only when value, quality, fairness, privacy, support and fallback thresholds are met.",
    ],
)

THANK_YOU = dict(
    body=(
        "You can now prompt, design, test and roll out HR agents that keep evidence visible "
        "and consequential people decisions human-owned."
    ),
    kicker="C820 - KEEP PEOPLE DECISIONS HUMAN-OWNED",
)

VERSION_HISTORY = [
    (
        "1.0",
        VERSION_DATE,
        "Initial aligned release of the slide deck, Learner Guide, Lesson Plan and six connected labs.",
        TRAINER,
    ),
]
