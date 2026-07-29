"""Topic 1 labs for C820."""

DOMAIN1 = [
    dict(
        num=1,
        topic=1,
        title="Frame the Asteron HR Agent and Write the Prompt Contract",
        duration=45,
        objective="LO1: use an approved AI assistant with a structured prompt, source boundary and human review method",
        goal="Define one bounded HR-agent use case and prove that its first prompt stays inside approved evidence and action limits.",
        workflow=["Choose the use case", "Map four boundaries", "Write G-C-C-S-O-R", "Run and review"],
        desc=(
            "You will inspect the synthetic Asteron People Operations brief, compare an assistant, fixed automation "
            "and agent pattern, and choose a bounded onboarding-support use case. You will map its purpose, evidence, "
            "action and decision boundaries before running a G-C-C-S-O-R prompt and reviewing the result."
        ),
        build=(
            "01-foundation/hr-agent-foundation.md containing the selected pattern, four-boundary canvas, first prompt, "
            "initial and refined outputs, claim ledger, human decision and stop conditions."
        ),
        services="Text editor - approved AI assistant - asteron-people-operations-brief.md",
        prerequisites=[
            "Create the C820-Asteron-HR-Agent/01-foundation/ folder.",
            "Open labs/assets/asteron-people-operations-brief.md.",
            "Confirm that you will use only supplied synthetic information.",
        ],
        steps=[
            (
                "Create 01-foundation/hr-agent-foundation.md. Record the exact HR outcome, affected people, "
                "accountable owner and non-goals from the Asteron brief. Compare Assistant, Automation and Agent, "
                "then select the least autonomous pattern that fits the onboarding-support use case.",
                "Outcome: prepare a grounded first-week onboarding plan\n"
                "Affected people: synthetic new employees and HR operators\n"
                "Owner: People Operations Manager\n"
                "Non-goals: no eligibility decision - no employee-record edit - no message sent\n"
                "Pattern: <ASSISTANT | AUTOMATION | AGENT>\n"
                "Reason: <WHY THIS IS THE LEAST AUTONOMOUS FIT>",
            ),
            (
                "Add a Four-boundary canvas. Under Purpose, Evidence, Action and Decision, write what is allowed, "
                "prohibited and owned. Add completion, uncertainty, time, duplicate and unsafe-action stop conditions.",
                "Purpose: intended outcome | people affected | non-goals | owner\n"
                "Evidence: permitted sources | prohibited data | version rule | lineage\n"
                "Action: read | draft | recommend | write | send\n"
                "Decision: model may | human must | escalation route\n"
                "Completion: grounded draft + clean ledger + named human decision\n"
                "Uncertainty stop: missing or conflicting source -> ask or escalate\n"
                "Time stop: end the run after 10 minutes or two prompt attempts\n"
                "Duplicate stop: repeated Employee_ID + Start_Date -> ALREADY_PROCESSED\n"
                "Unsafe-action stop: protected-trait inference or write/send request -> STOPPED",
            ),
            (
                "Write a G-C-C-S-O-R prompt using Goal, Context, Criteria, Sources, Output and Review. Delimit the "
                "Asteron brief as SOURCE ORG-01. Require a table with Statement, Source_ID, Status and Human_action; "
                "require UNKNOWN rather than invention and prohibit external action.",
                "Goal: Draft a first-week onboarding-plan outline for synthetic employee AST-NE-001.\n"
                "Context: Asteron People Operations training scenario.\n"
                "Criteria: useful - role-neutral - minimum necessary data - no policy invention.\n"
                "Sources: <SOURCE id=\"ORG-01\">PASTE APPROVED BRIEF</SOURCE>\n"
                "Output: Plan plus Statement | Source_ID | Status | Human_action.\n"
                "Review: use only ORG-01; write UNKNOWN for missing facts; do not send, write or decide eligibility.",
            ),
            (
                "Run the prompt in one approved AI assistant and paste the response under Initial output. Review each "
                "material statement against ORG-01. Mark SUPPORTED, UNKNOWN or REMOVE in the ledger and identify the "
                "most important defect. Add one instruction that would have prevented it, rerun and save Refined output.",
                "Ledger: Version | Statement | Source_ID | Status | Human_action\n"
                "Defect: <UNSUPPORTED FACT | OVER-BROAD ACTION | MISSING QUESTION | OTHER>\n"
                "Added instruction: <ONE PREVENTIVE INSTRUCTION>\n"
                "Rule: unsupported content is removed or marked UNKNOWN; it is never repaired by inventing a source.",
            ),
            (
                "Finish with a Human decision block. Decide whether the pattern is READY FOR SYNTHETIC PROTOTYPE or "
                "NEEDS REPAIR, give the reason, name the next owner and list the retained run evidence.",
                "Decision: <READY FOR SYNTHETIC PROTOTYPE | NEEDS REPAIR>\n"
                "Reason: <EVIDENCE-BASED RATIONALE>\n"
                "Next owner: People Operations Manager\n"
                "Retain: source version - prompt - both outputs - ledger - reviewer edit - decision - timestamp",
            ),
        ],
        test=(
            "Open 01-foundation/hr-agent-foundation.md. It must name one pattern and justify it; contain all four "
            "boundaries; contain one explicit completion, uncertainty, time, duplicate and unsafe-action condition; "
            "contain one complete G-C-C-S-O-R prompt, initial and refined outputs, "
            "a version-tagged claim ledger with no unsupported statement marked SUPPORTED, and one human decision."
        ),
        checkpoint=(
            "Keep hr-agent-foundation.md as the portfolio control record. Lab 2 reuses its purpose, evidence and "
            "decision boundaries. To rejoin, use the selected onboarding-support outcome and the final refined prompt."
        ),
        troubleshooting=[
            (
                "The first output invents an Asteron policy or deadline.",
                "Mark it REMOVE, add 'Use only SOURCE ORG-01; write UNKNOWN for all other facts' and rerun.",
            ),
            (
                "The chosen pattern is more autonomous than the task requires.",
                "Move drafting to an assistant or fixed flow and keep the person in control of every next action.",
            ),
            (
                "The four boundaries repeat the same sentence.",
                "Separate why the system exists, what it may know, what it may do and who makes the people decision.",
            ),
        ],
        challenge=(
            "Write an alternative fixed-automation design for the same use case. Identify the one step, if any, where "
            "model-supported judgement adds enough value to justify an agent pattern."
        ),
        reflection=(
            "Which boundary most reduced the risk of the first prompt, and what observable change appeared in the refined output?"
        ),
    ),
    dict(
        num=2,
        topic=1,
        title="Build the Grounded HR Source and Employee FAQ Pack",
        duration=45,
        objective="LO1: connect an HR task to current approved sources while preserving source identity, uncertainty and human review",
        goal="Create a version-controlled HR source register and a policy-grounded FAQ pack that escalates unsupported or personal cases.",
        workflow=["Validate sources", "Set retrieval rules", "Draft answers", "Verify lineage"],
        desc=(
            "You will inspect synthetic onboarding policy excerpts, identify the current source for each policy topic "
            "and define a read-only retrieval contract. You will then produce six answer-or-handoff records, cite the "
            "exact Policy_ID and effective date for answers, and route cases that cannot be answered safely."
        ),
        build=(
            "01-foundation/hr-source-register.csv and 01-foundation/employee-faq-pack.md with current-version rules, "
            "six answer-or-handoff records, source citations, unknowns, escalation routes and a retrieval test log."
        ),
        services="Spreadsheet - text editor - approved AI assistant - approved-policy-excerpts.md - employee-questions.csv",
        prerequisites=[
            "Completed Lab 1 hr-agent-foundation.md.",
            "Open labs/assets/approved-policy-excerpts.md and labs/assets/employee-questions.csv.",
            "Create blank files hr-source-register.csv and employee-faq-pack.md in 01-foundation/.",
        ],
        steps=[
            (
                "Read approved-policy-excerpts.md and create hr-source-register.csv with one row per policy version. "
                "Record Policy_ID, Topic, Version, Effective_Date, Status, Owner, Jurisdiction, Permitted_Use and "
                "Supersedes. Mark one current source per topic; do not delete retired versions.",
                "Header: Policy_ID,Topic,Version,Effective_Date,Status,Owner,Jurisdiction,Permitted_Use,Supersedes\n"
                "Validation: each topic has exactly one CURRENT row - all other versions are RETIRED - every row has an owner and date",
            ),
            (
                "In employee-faq-pack.md, write a ReadPolicy tool contract. Use Topic and As_Of_Date for normal "
                "retrieval and an optional Requested_Policy_ID only for an explicit version check. Require current "
                "Policy_ID, effective date, approved excerpt and owner in the output. Add rules for no match, multiple "
                "current matches, retired requested source and personal-case questions.",
                "Tool: ReadPolicy\n"
                "Inputs: Topic | As_Of_Date | Requested_Policy_ID (optional version check only)\n"
                "Outputs: Policy_ID | Effective_Date | Approved_Excerpt | Owner | Retrieval_Status\n"
                "Access: read-only - approved excerpts only\n"
                "Stop: NO_CURRENT_SOURCE | MULTIPLE_CURRENT_SOURCES | RETIRED_NOT_USABLE | PERSONAL_CASE | CONFLICT",
            ),
            (
                "Open employee-questions.csv. For Q-001 to Q-006, identify the intended topic and retrieval status "
                "before asking the AI assistant to draft anything. Record ANSWER, CLARIFY or ESCALATE and the exact "
                "source that may be used.",
                "Question_ID | Topic | Retrieval_Status | Route | Policy_ID | Reason\n"
                "Route rules: ANSWER only from one current source - CLARIFY when a necessary fact is missing - "
                "ESCALATE for personal exceptions, high-impact cases or no current source",
            ),
            (
                "Ask the approved AI assistant to draft a concise answer for each ANSWER case using only the selected "
                "policy excerpt. Require Answer, Policy_ID, Effective_Date, Limitation and Next_action. For CLARIFY or "
                "ESCALATE cases, draft no policy conclusion; write the question or handoff instead.",
                "For each row use only <QUESTION> and <APPROVED_POLICY_EXCERPT>.\n"
                "Return: Question_ID | Route | Answer_or_Handoff | Policy_ID | Effective_Date | Limitation | Next_action.\n"
                "Do not infer eligibility, personal circumstances or an exception. Do not use a RETIRED source.",
            ),
            (
                "Run four retrieval tests and record expected versus actual results: one current match, a retired "
                "version request, an unknown topic and a personal exception. Repair the register or FAQ pack until all "
                "tests return the required source or stop status.",
                "T1 current equipment topic -> one CURRENT Policy_ID\n"
                "T2 Topic=Equipment, As_Of_Date=2026-08-01, Requested_Policy_ID=ONB-01 -> RETIRED_NOT_USABLE\n"
                "T3 unknown payroll topic -> NO_CURRENT_SOURCE\n"
                "T4 personal leave exception -> PERSONAL_CASE / ESCALATE\n"
                "Log: Test_ID | Input | Expected | Actual | Result | Repair",
            ),
        ],
        test=(
            "The source register must contain every supplied policy version, exactly one CURRENT row per topic, and no "
            "blank owner or effective date. The FAQ pack must cover Q-001 to Q-006, cite Policy_ID and Effective_Date "
            "for every ANSWER, contain no conclusion for CLARIFY or ESCALATE cases, and show all four retrieval tests PASS."
        ),
        checkpoint=(
            "Keep hr-source-register.csv and employee-faq-pack.md. Labs 4 and 5 reuse the current Policy_ID values and "
            "escalation rules. To rejoin, confirm the four retrieval tests still pass."
        ),
        troubleshooting=[
            (
                "Two policies appear current for the same topic.",
                "Return MULTIPLE_CURRENT_SOURCES and ask the named policy owner to resolve the register; do not choose one silently.",
            ),
            (
                "The draft answer omits the source.",
                "Reject it and require Policy_ID plus Effective_Date in the answer record and retrieval-test evidence.",
            ),
            (
                "A personal question looks similar to a general FAQ.",
                "Give general process guidance only and route the personal decision to the named HR owner.",
            ),
        ],
        challenge=(
            "Add a seventh synthetic question containing a prompt-injection instruction inside the employee text. "
            "Show that retrieved content cannot change the source boundary, tool permission or escalation rule."
        ),
        reflection=(
            "Why is a clear NO_CURRENT_SOURCE result safer and more useful than a fluent answer without lineage?"
        ),
    ),
]
