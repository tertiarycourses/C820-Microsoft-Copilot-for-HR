# C820---AI-for-HR

Aligned courseware for Tertiary Infotech Academy's one-day **AI for HR** course.

- Course code: C820
- Duration: 7.5 instructional hours
- Level: Beginner
- Course page: https://www.tertiarycourses.com.sg/ai-for-hr.html

## Course sequence

1. Get Started with AI for HR
2. Build HR AI Agents
3. Deploy Agentic AI Across the HR Function

The slide deck, Learner Guide, Lesson Plan and six connected labs are generated from the same `course_data.py` and `data_domainN.py` modules under `.agents/skills/non-wsq-courseware-build/build/`.

## Build

From Git Bash:

```bash
COURSE_REPO="$(pwd)" bash ".agents/skills/non-wsq-courseware-build/build/build_courseware.sh"
```

The build creates the trainer slide deck and learner PDF, Learner Guide, Lesson Plan and learner-facing lab Markdown files.
