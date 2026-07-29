# Asteron Services - People Operations Brief

**Source ID:** ORG-01  
**Version:** 1.0  
**Owner:** People Operations Manager  
**Status:** Approved synthetic training source  
**Effective date:** 1 July 2026

## Organisation

Asteron Services is a synthetic regional business with 420 employees across Singapore and Malaysia. The People Operations team supports recruitment, onboarding, employee questions and manager communications.

## Current problem

- New-hire preparation is coordinated through email, a task list and policy documents.
- HR operators spend time finding the current policy version and answering repeated general questions.
- Missing location, start-date and role information creates rework.
- No AI tool may decide a personal policy exception, alter an employee record or send a message without a named human decision.

## Intended learning use case

Prepare a grounded first-week onboarding plan from an approved synthetic new-hire record and current policy excerpts. The plan may contain draft tasks and messages for human review.

## Approved roles

- People Operations Manager: owns the process and release decision.
- HR Operations Specialist: checks case facts and current policy.
- Hiring Manager: confirms role-specific first-week activities.
- IT Service Coordinator: owns equipment tasks after approved task creation.

## Operating boundaries

- Start with synthetic or authorised minimum necessary data.
- Retrieve only current approved policy excerpts.
- Keep read, draft, recommend, approve and action permissions separate.
- Stop on missing required facts, policy conflict, protected-trait inference, duplicate action or any request to bypass human review.
- Retain source identifiers, model draft, deterministic checks, reviewer changes, human decision and final status.

## Synthetic starter case

| Field | Value |
|---|---|
| Employee_ID | AST-NE-001 |
| Start_Date | 17 August 2026 |
| Location | Singapore |
| Department | Client Operations |
| Hiring_Manager | HM-014 |
| Work_Arrangement | Office-based |

No name, personal contact, family, health, pay, performance or grievance information is included.
