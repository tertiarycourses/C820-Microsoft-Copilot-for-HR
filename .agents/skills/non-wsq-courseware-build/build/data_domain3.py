"""Topic 3 labs for C820."""

DOMAIN3 = [
    dict(
        num=5,
        topic=3,
        title="Simulate the Controlled Onboarding Workflow",
        duration=45,
        objective="LO3: build and test a multi-step HR workflow with approved data, limited tools, human gates and complete run evidence",
        goal="Run four synthetic onboarding cases through a visible state machine and prove that duplicates, missing facts and unsafe actions stop correctly.",
        workflow=["Map states", "Contract tools", "Run four cases", "Reconcile evidence"],
        desc=(
            "You will convert the Lab 4 onboarding plan into a state-based workflow. ReadPolicy, DraftPlan and "
            "CreateTask are represented by explicit tool contracts; write and send effects remain simulated. You will "
            "run normal, missing-data, duplicate and policy-conflict cases and reconcile every final state."
        ),
        build=(
            "03-deployment/onboarding-workflow-spec.md and 03-deployment/workflow-run-log.csv with states, transition "
            "rules, tool contracts, four complete traces, human approvals, stop reasons and manual fallback."
        ),
        services="Text editor - spreadsheet - approved AI assistant - workflow-cases.csv - workflow-run-log-template.csv",
        prerequisites=[
            "Completed Lab 4 onboarding-support pack.",
            "Open labs/assets/workflow-cases.csv, labs/assets/workflow-spec-template.md and labs/assets/workflow-run-log-template.csv.",
            "Confirm that OS-001 Final_Approved_Text is labelled Plan_Version OS-001-FINAL-1.",
            "All system changes and messages are simulations; do not connect a live HR system.",
        ],
        steps=[
            (
                "Copy workflow-spec-template.md to onboarding-workflow-spec.md. Confirm its states RECEIVED, VALIDATED, "
                "GROUNDED, DRAFTED, NEEDS_REVIEW, APPROVED, ACTIONED, CLOSED and STOPPED. Complete the prepared "
                "transition rows with trigger, rule, owner, evidence and failure route.",
                "Transition table: From | Trigger | Deterministic rule | Model task | Human decision | Owner | To | Evidence | Failure route\n"
                "Completion: CLOSED only after required evidence and approval are present\n"
                "Failure: STOPPED keeps reason, owner and manual next action",
            ),
            (
                "Add contracts for ReadPolicy, DraftPlan and CreateTask. Keep ReadPolicy read-only, DraftPlan "
                "non-actioning and CreateTask simulated. Specify input and output schemas, identity, permitted scope, "
                "timeout, retry, idempotency key, validation and evidence.",
                "ReadPolicy input: Topic,As_Of_Date -> Policy_ID,Effective_Date,Excerpt,Status\n"
                "DraftPlan input: Case_ID,Approved_Source -> Draft,Source_Ledger,Unknowns\n"
                "CreateTask input: Case_ID,Task_Code,Approval_Token -> SIMULATED_Task_ID,Status\n"
                "Idempotency key: Employee_ID + Task_Code + Start_Date\n"
                "Timeout/retry: ReadPolicy 10 seconds, one retry; DraftPlan 45 seconds, no automatic retry; "
                "CreateTask 10 seconds, no automatic retry\n"
                "No tool may send a message or edit an employee record.",
            ),
            (
                "Copy the pre-populated workflow-run-log-template.csv into 03-deployment/workflow-run-log.csv. Process "
                "WF-001 to WF-004 one prepared row at a time. Apply required-field, source-status and duplicate checks "
                "before the DRAFTED state; repeat the duplicate check atomically with the approval-token check before "
                "CreateTask. Complete Actual_Result, To_State, evidence, owner and manual action cells.",
                "Case expectations:\n"
                "WF-001 normal -> CLOSED\n"
                "WF-002 missing Location -> STOPPED / MISSING_REQUIRED_FIELD\n"
                "WF-003 duplicate key -> STOPPED / ALREADY_PROCESSED\n"
                "WF-004 conflicting current policy -> STOPPED / SOURCE_CONFLICT",
            ),
            (
                "For WF-001 only, import the exact Lab 4 OS-001 Final_Approved_Text and cite Plan_Version "
                "OS-001-FINAL-1 as the DraftPlan output; do not generate a fresh plan. Confirm the Lab 4 seven-gate "
                "release record and create a synthetic approval token. Record a simulated task effect only after "
                "approval; every other case must stop before DraftPlan or CreateTask as specified.",
                "Approval token: APPR-WF-001-HR-001\n"
                "Evidence before ACTIONED: required fields PASS | source current | Plan_Version OS-001-FINAL-1 | "
                "claim ledger clean | seven gates YES | "
                "named reviewer | approval timestamp\n"
                "Simulated effect: TASK-WF-001-IT-SETUP; no external write occurs.",
            ),
            (
                "Reconcile the log. Every case must have one terminal state, a reason, an owner and a manual next action. "
                "Count cases by CLOSED and STOPPED, confirm no duplicate simulated Task_ID and add a one-paragraph "
                "fallback procedure for system outage or unresolved source conflict.",
                "Reconciliation: total cases = CLOSED + STOPPED = 4\n"
                "Unique simulated Task_ID count = simulated action rows\n"
                "Every STOPPED row: Stop_Reason + Human_Owner + Manual_Next_Action\n"
                "Fallback: receive case - validate minimum fields - retrieve approved source manually - human review - record completion",
            ),
        ],
        test=(
            "The workflow specification must contain all nine states, three tool contracts, an approval gate and manual "
            "fallback. The run log must show WF-001 CLOSED and WF-002 to WF-004 STOPPED with the specified reasons; "
            "four terminal states must reconcile, no simulated Task_ID may repeat, and no external action may occur."
        ),
        checkpoint=(
            "Keep the specification and run log as the deployment evidence. Lab 6 uses the four traces, stop behaviour "
            "and approval evidence. To rejoin, confirm the reconciliation equation equals four."
        ),
        troubleshooting=[
            (
                "A stopped case continues to later states.",
                "Enforce terminal STOPPED behaviour and start a separate corrected run with a new Run_ID.",
            ),
            (
                "The duplicate case creates another simulated task.",
                "Check the composite idempotency key before drafting or action and return ALREADY_PROCESSED.",
            ),
            (
                "The tool contract says 'appropriate access'.",
                "Replace vague language with exact identity, operation, fields, destination and denied actions.",
            ),
        ],
        challenge=(
            "Add a safe retry for a temporary ReadPolicy timeout. Set maximum attempts, backoff, terminal status and "
            "evidence without allowing the retry to bypass source or approval checks."
        ),
        reflection=(
            "Which workflow truth belonged in a deterministic rule rather than the model, and what failure did that prevent?"
        ),
    ),
    dict(
        num=6,
        topic=3,
        title="Run the Governance Gate and Rollout Plan",
        duration=60,
        objective="LO4: evaluate privacy, fairness, security and operating risk and produce a staged rollout with owners, metrics and fallback",
        goal="Use representative evidence to decide whether the Asteron HR-agent portfolio may enter a limited read-only pilot.",
        workflow=["Map risks", "Run evaluation", "Set release gate", "Plan staged rollout"],
        desc=(
            "You will evaluate the recruitment and onboarding agents against normal, boundary, missing-source, unsafe-"
            "action and fairness-relevant cases. You will calculate quality and subgroup indicators, inspect reviewer "
            "changes, set release thresholds and write a staged rollout with named owners, monitoring and rollback."
        ),
        build=(
            "03-deployment/governance-evaluation.csv and 03-deployment/hr-agent-rollout-plan.md with risk controls, "
            "calculated metrics, fairness investigation, release decision, pilot stages, owners, monitoring and fallback."
        ),
        services="Spreadsheet - text editor - governance-test-cases.csv - outputs from Labs 2-5",
        prerequisites=[
            "Completed and retained the Lab 2 FAQ pack, Lab 3 recruitment register, Lab 4 routing and release records, and Lab 5 reconciled workflow run log.",
            "Open labs/assets/governance-test-cases.csv and labs/assets/hr-agent-rollout-plan-template.md.",
            "Copy labs/assets/hr-agent-rollout-plan-template.md to 03-deployment/hr-agent-rollout-plan.md before Step 1.",
            "Before Step 1, confirm every G-001 to G-010 Evidence_Source exists and record READY or MISSING in an evidence-readiness table.",
            "Treat subgroup indicators as signals for investigation, not proof of cause or a new candidate criterion.",
        ],
        steps=[
            (
                "Open 03-deployment/hr-agent-rollout-plan.md. Use its GOVERN, MAP, MEASURE and MANAGE headings. Inventory the two "
                "Asteron agents, affected people, sources, tools, decisions and owners. Map at least one privacy, "
                "fairness, security, accuracy, action-overreach and operating-continuity risk with a control and owner.",
                "Risk register: Risk_ID | Agent | Harm | Cause | Existing control | Test | Owner | Residual risk | Response\n"
                "Required risks: privacy - fairness - source accuracy - prompt injection - unsafe action - outage/fallback",
            ),
            (
                "Copy governance-test-cases.csv to governance-evaluation.csv. For G-001 to G-010, record Expected, "
                "Actual, Pass, Evidence_ID, Severity and Repair. Use the retained Lab 2-5 artifacts where a test "
                "references a previous run; simulate only the missing cases and label them clearly.",
                "Pass rule: Actual exactly matches Expected\n"
                "Seven critical cases: G-002 retired policy | G-003 unnecessary personal field | G-004 protected-trait "
                "inference | G-006 send/write | G-007 missing required field | G-008 duplicate action | G-009 source conflict\n"
                "Evidence_ID: exact file plus row, Candidate_ID, Case_ID or Run_ID",
            ),
            (
                "Calculate four metrics: overall test pass rate, critical-case pass rate, grounding-defect rate and "
                "human-correction rate. Then use the supplied synthetic subgroup summary to calculate selection and "
                "deferral rates for Groups A and B and the smaller-to-larger selection-rate ratio. Record denominator, "
                "context and investigation questions; do not declare a cause from one small synthetic sample.",
                "Test pass rate = passed tests / total tests\n"
                "Critical pass rate = passed critical tests / total critical tests\n"
                "Grounding-defect scope: every Lab 2 Route=ANSWER record, every Lab 4 released case record "
                "(APPROVE_DRAFT or EDIT_THEN_APPROVE), and the five OS-001 plan rows. Numerator = scoped records or "
                "rows missing a current Policy_ID or required Source_ID, or having Source_present or Source_current "
                "not YES; denominator = all scoped records and rows\n"
                "Human-correction scope: the 12 Lab 3 criterion components (4 candidates x C1-C3); numerator = cells "
                "where Final_Cn differs from Proposed_Cn; denominator = 12\n"
                "Grounding-defect rate = defective grounded records and plan rows / all scoped grounded records and plan rows\n"
                "Human-correction rate = changed final criterion cells / 12\n"
                "Selection rate = selected / reviewed for each group\n"
                "Rate ratio = smaller selection rate / larger selection rate\n"
                "If denominator = 0, display N/A.",
            ),
            (
                "Set the release gate before making a decision: 100% critical-case pass, at least 90% overall pass, "
                "0% grounding defects, named owners for all high residual risks and a tested manual fallback. "
                "For subgroup differences, require documented investigation and human review; do not invent a universal "
                "numeric fairness rule.",
                "Gate: critical 100% | overall >=90% | grounding defects 0% | high risks owned | fallback tested\n"
                "Decision: HOLD | REPAIR_AND_RETEST | APPROVE_READ_ONLY_PILOT\n"
                "Record: result - evidence - decision owner - conditions - next review date",
            ),
            (
                "Return to the same 03-deployment/hr-agent-rollout-plan.md and complete its prepared rollout table "
                "from synthetic sandbox to shadow, read-only pilot and controlled operation. "
                "For each stage define scope, users, data, actions, entry evidence, exit gate, training, communication, "
                "support, monitoring and rollback. Assign Business, HR process, Data, Technology, Privacy/Risk and "
                "Support owners and choose one value, quality, fairness, safety and operating metric.",
                "Stages: SYNTHETIC -> SHADOW -> READ_ONLY_PILOT -> CONTROLLED_OPERATION\n"
                "Metrics: cycle time | grounded-answer accuracy | subgroup selection/deferral indicators | unsafe-action "
                "attempts | failure and escalation service level\n"
                "Rollback triggers: critical test failure | policy conflict | unowned high risk | unsafe action | material drift\n"
                "Fallback: approved manual HR process",
            ),
        ],
        test=(
            "The evaluation file must contain ten tests with expected, actual, pass, severity and evidence; all four "
            "quality metrics and both subgroup selection and deferral rates must show formulas and denominators. The "
            "rollout plan must cover six risk types, six owner roles, four stages, five monitoring dimensions, explicit "
            "gates, a release decision and a tested manual fallback. Critical pass rate must be 100% before any pilot approval."
        ),
        checkpoint=(
            "This is the final portfolio checkpoint. Keep all six lab outputs and supplied synthetic sources together. "
            "Rerun the governance evaluation whenever a prompt, rubric, policy source, model, tool, permission or workflow changes."
        ),
        troubleshooting=[
            (
                "A percentage is calculated without a denominator.",
                "Add numerator, denominator, formula and N/A handling before interpreting the result.",
            ),
            (
                "A subgroup difference is treated as proof of discrimination.",
                "Record it as an investigation signal and inspect criteria, evidence, errors, deferrals, reviewer changes and context.",
            ),
            (
                "The rollout jumps from sandbox to full operation.",
                "Insert shadow and limited read-only stages with observable entry and exit gates and a manual fallback.",
            ),
        ],
        challenge=(
            "Add a post-change regression scenario for a new policy version. State which test cases must rerun, which "
            "owners approve the change and which condition triggers rollback."
        ),
        reflection=(
            "Which single piece of evidence most strongly supports the release decision, and what important uncertainty still remains?"
        ),
    ),
]
