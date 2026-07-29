"""Topic 2 labs for C820."""

DOMAIN2 = [
    dict(
        num=3,
        topic=2,
        title="Build the Fair Recruitment Evidence Assistant",
        duration=50,
        objective="LO2: design a recruitment decision-support agent with job-related criteria, source evidence and explicit human decisions",
        goal="Apply one approved rubric consistently to four synthetic candidates and retain a complete evidence-to-decision trail.",
        workflow=["Approve criteria", "Minimise inputs", "Extract evidence", "Human review"],
        desc=(
            "You will turn an approved Asteron role profile into a transparent screening rubric, remove non-job-related "
            "fields from four synthetic candidate records and ask an AI assistant to cite evidence for each criterion. "
            "A human reviewer will correct proposed scores, record reasons and prepare interview questions without "
            "automatically rejecting or selecting anyone."
        ),
        build=(
            "02-hr-agents/recruitment-evidence-register.csv and 02-hr-agents/recruitment-review.md with criterion "
            "anchors, source evidence, unknowns, proposed and final scores, reviewer changes and human next-step decisions."
        ),
        services="Spreadsheet - text editor - approved AI assistant - role-profile.md - synthetic-candidates.csv",
        prerequisites=[
            "Completed Lab 1 four-boundary canvas.",
            "Open labs/assets/role-profile.md and labs/assets/synthetic-candidates.csv.",
            "Use Candidate_ID only; do not add a name, photograph, age, family, health, ethnicity or other protected information.",
        ],
        steps=[
            (
                "Create recruitment-review.md and copy the approved role outcome, responsibilities and three required "
                "criteria from role-profile.md. For each criterion, write 0, 1 and 2 score anchors tied to observable "
                "resume evidence. Record why each criterion is job-related.",
                "C1 Service case handling: 0 absent | 1 related exposure | 2 direct evidence with outcome\n"
                "C2 Spreadsheet reporting: 0 absent | 1 basic use | 2 recurring report with validation\n"
                "C3 Stakeholder communication: 0 absent | 1 general contact | 2 structured cross-team example\n"
                "Total range: 0-6 - UNKNOWN remains visible - score is decision support only",
            ),
            (
                "Create recruitment-evidence-register.csv. Copy Candidate_ID and the real source columns EVIDENCE_L1 "
                "through EVIDENCE_L4 from synthetic-candidates.csv. Add Proposed_C1 to Proposed_C3, Proposed_Total, "
                "Evidence_C1 to Evidence_C3, Unknowns, Final_C1 to Final_C3, Final_Total, Adjustment_Reason and "
                "Human_Next_Step.",
                "Header: Candidate_ID,EVIDENCE_L1,EVIDENCE_L2,EVIDENCE_L3,EVIDENCE_L4,Proposed_C1,Proposed_C2,"
                "Proposed_C3,Proposed_Total,Evidence_C1,Evidence_C2,Evidence_C3,Unknowns,Final_C1,Final_C2,Final_C3,"
                "Final_Total,Adjustment_Reason,Human_Next_Step\n"
                "Permitted next steps: INVITE_STRUCTURED_INTERVIEW | CLARIFY_EVIDENCE | HOLD_FOR_PANEL_REVIEW",
            ),
            (
                "Give the AI assistant the role profile, anchored rubric and all four minimised candidate records in "
                "one batch. Require identical treatment, exact EVIDENCE line references and UNKNOWN for missing facts. "
                "Prohibit inference and prohibit a final hiring or rejection recommendation.",
                "Use only ROLE-01 and supplied Candidate_ID records.\n"
                "For each candidate return C1-C3 proposed score, exact evidence line, unknowns and one job-related "
                "clarification question. Apply identical anchors. Do not infer protected traits. Do not select, rank, "
                "reject or contact a candidate.",
            ),
            (
                "Enter the proposed output, then independently verify each source citation and score. Record final "
                "scores and an Adjustment_Reason for every change. Calculate both totals and confirm each equals the "
                "sum of its three components. Keep UNKNOWN visible even when the final score is high.",
                "Spreadsheet checks:\n"
                "Proposed_Total = Proposed_C1 + Proposed_C2 + Proposed_C3\n"
                "Final_Total = Final_C1 + Final_C2 + Final_C3\n"
                "Score range per criterion = 0..2\n"
                "If evidence is absent, score 0 and record UNKNOWN; never infer the missing skill.",
            ),
            (
                "Hold a human panel review. Assign one permitted Human_Next_Step to every candidate and give a "
                "one-sentence job-related reason. Add six structured interview questions: one per criterion and three "
                "candidate-specific clarification questions. Retain the source, rubric, prompt, proposed output, "
                "reviewer changes and final human decisions.",
                "Decision record: Candidate_ID | Human_Next_Step | Job-related reason | Reviewer | Date\n"
                "Question rule: competency-based - same core question by criterion - candidate-specific clarification "
                "uses only cited resume evidence - no protected-trait question",
            ),
        ],
        test=(
            "The register must contain four Candidate_ID rows, three proposed and final components per row, exact "
            "evidence references, visible unknowns, totals from 0 to 6, and an Adjustment_Reason for every changed score. "
            "The review file must contain criterion anchors, six structured questions and one human-owned next step per "
            "candidate; it must contain no automated selection, ranking, rejection or protected-trait inference."
        ),
        checkpoint=(
            "Keep both recruitment files as the decision-support evidence trail. Lab 6 reuses the rubric, proposed "
            "versus final changes and human next steps for governance tests. To rejoin, verify all component totals."
        ),
        troubleshooting=[
            (
                "The assistant ranks candidates or recommends a hire.",
                "Discard that field and repeat: evidence extraction and criterion scoring only; the panel owns the next step.",
            ),
            (
                "A score has no exact resume support.",
                "Set it to 0, record UNKNOWN and create a structured clarification question.",
            ),
            (
                "Different criteria appear for different candidates.",
                "Return to ROLE-01 and apply the same three anchored criteria to the complete batch.",
            ),
        ],
        challenge=(
            "Have a partner independently review the four proposed scores. Compare only criteria with a two-point "
            "difference and rewrite any ambiguous anchor without changing the role requirements."
        ),
        reflection=(
            "Which human correction most improved fairness or evidence quality, and why would the original score have been misleading?"
        ),
    ),
    dict(
        num=4,
        topic=2,
        title="Build the Onboarding and Employee Support Agent Pack",
        duration=50,
        objective="LO2: design onboarding and employee-support agents that use current policy, minimum necessary data and human communication review",
        goal="Produce a grounded onboarding plan and employee-support response pack that answers, clarifies or escalates each case correctly.",
        workflow=["Classify cases", "Retrieve policy", "Draft two packs", "Release review"],
        desc=(
            "You will combine the current source register from Lab 2 with six synthetic onboarding and employee-support "
            "cases. The agent will classify each case as ANSWER, CLARIFY or ESCALATE, draft a first-week plan and employee "
            "messages, and retain sources, limitations and a human release decision."
        ),
        build=(
            "02-hr-agents/onboarding-support-pack.md and 02-hr-agents/support-routing-register.csv containing a "
            "first-week plan, six case routes, grounded drafts, source ledger, privacy check and human release decisions."
        ),
        services="Spreadsheet - text editor - approved AI assistant - onboarding-support-cases.csv - Lab 2 source register",
        prerequisites=[
            "Completed Lab 2 with all four retrieval tests passing.",
            "Open labs/assets/onboarding-support-cases.csv, labs/assets/approved-policy-excerpts.md and labs/assets/onboarding-activities.md.",
            "Copy labs/assets/support-routing-register-template.csv and labs/assets/onboarding-support-pack-template.md into 02-hr-agents/.",
            "Use current Policy_ID values from hr-source-register.csv; do not copy real employee information.",
        ],
        steps=[
            (
                "Rename the copied starter to support-routing-register.csv. It already contains all six synthetic case "
                "facts and the canonical header. Complete only Necessary_Fields, Omitted_Fields, Retrieval_Status, "
                "Route, Policy_ID, Limitation, Human_Owner and Release_Decision. Remove any field value not needed for "
                "the stated intent, but keep the column and write OMITTED.",
                "Canonical header: Case_ID,Employee_ID,Intent,As_Of_Date,Start_Date,Location,Department,Question,"
                "Necessary_Fields,Omitted_Fields,Retrieval_Status,Route,Policy_ID,Limitation,Human_Owner,Release_Decision\n"
                "Routes: ANSWER | CLARIFY | ESCALATE\n"
                "Release: APPROVE_DRAFT | EDIT_THEN_APPROVE | HOLD",
            ),
            (
                "Classify all six cases before drafting. Use ANSWER only when one current policy and all necessary "
                "facts are present. Use CLARIFY for a missing non-sensitive fact and ESCALATE for a personal exception, "
                "conflict, sensitive matter or decision outside the support boundary.",
                "Decision rule:\n"
                "one current source + complete necessary facts + general guidance -> ANSWER\n"
                "one necessary non-sensitive fact missing -> CLARIFY\n"
                "personal exception | high impact | conflict | no current source -> ESCALATE",
            ),
            (
                "Rename the copied starter to onboarding-support-pack.md. Ask the AI assistant to complete it. For "
                "designated case OS-001, require a five-day onboarding plan with task, owner, due point, Source_ID and "
                "employee message. Use ONB-ACT-01 for the approved five-day activity sequence and current policy for "
                "policy facts. For all six cases require Route, Draft_or_Handoff, Policy_ID, Effective_Date, Limitation "
                "and Next_action.",
                "Use only <CASE ROWS>, <CURRENT APPROVED POLICY EXCERPTS> and <ONB-ACT-01>.\n"
                "Do not add benefits, eligibility, deadlines, contacts or links beyond the source.\n"
                "Do not decide a personal exception. Write UNKNOWN for missing facts. Do not send any message.",
            ),
            (
                "Review each draft through seven gates: source present, source current, minimum data, fair and "
                "respectful language, correct route, action authority and complete next action. Enter APPROVE_DRAFT, "
                "EDIT_THEN_APPROVE or HOLD, record the exact edit and persist Final_Approved_Text. The named "
                "Human_Owner must be able to change the result.",
                "Release ledger: Case_ID | Source_present | Source_current | Data_minimal | Language_suitable | "
                "Route_correct | No_unapproved_action | Next_action_complete | Release_Decision | Edit_or_reason | "
                "Final_Approved_Text\n"
                "All seven gates must be YES before APPROVE_DRAFT or EDIT_THEN_APPROVE.",
            ),
            (
                "Run three boundary tests: replace a current Policy_ID with a retired one, remove Location from the "
                "location-dependent case and add a request to send the message. Record expected and actual behaviour, "
                "repair the prompt or route rules and restore the original synthetic data.",
                "B1 retired policy -> HOLD / RETIRED_NOT_USABLE\n"
                "B2 missing Location -> CLARIFY\n"
                "B3 send request -> DRAFT_ONLY / HOLD ACTION\n"
                "Log: Test_ID | Change | Expected | Actual | Result | Repair",
            ),
        ],
        test=(
            "The routing register must contain six cases, necessary and omitted fields, one route, human owner and "
            "release decision per row. The support pack must include an ONB-ACT-01-grounded five-day plan for OS-001, "
            "six grounded drafts or handoffs, seven gate results and Final_Approved_Text for every released case, with "
            "Policy_ID and Effective_Date for each ANSWER. All three boundary tests must PASS, and no message may be "
            "sent or personal exception decided."
        ),
        checkpoint=(
            "Keep both support files. Lab 5 converts the approved onboarding plan into a controlled multi-step workflow. "
            "To rejoin, use only OS-001 Final_Approved_Text with Plan_Version OS-001-FINAL-1; do not generate a new plan."
        ),
        troubleshooting=[
            (
                "The onboarding plan invents a company link or contact.",
                "Replace it with UNKNOWN, create a clarification item and cite only the approved source.",
            ),
            (
                "An ESCALATE case still contains a policy conclusion.",
                "Remove the conclusion; keep only the handoff reason, minimum case facts and named human owner.",
            ),
            (
                "The release check becomes a rubber stamp.",
                "Require an exact source and observable yes/no result for each gate and keep HOLD available.",
            ),
        ],
        challenge=(
            "Rewrite one approved employee message for chat and email. Keep facts and route unchanged, then explain "
            "which structure changed because of the channel."
        ),
        reflection=(
            "Which case required the clearest separation between general policy guidance and a personal HR decision?"
        ),
    ),
]
