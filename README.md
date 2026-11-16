# Topic 6 code review workshop
Review two focused changes to a simplified booking application. Explain findings, respond to feedback and verify revisions before integration.

## Start
Read SETUP.md. Use one shared repository per pair and a clone per learner. All commands run from the project root unless stated otherwise. Do not copy activity templates until the relevant activity.

## Route through the session
- 00:00–00:05 Introduction and outcomes.
- 00:05–00:15 Compare comments: docs/comment-examples.md.
- 00:15–00:25 Choose approaches: docs/scenarios.md.
- 00:25–00:40 Setup and tutor demonstration.
- 00:40–01:00 Activity 1: docs/activity-1.md.
- 01:00–01:10 Break.
- 01:10–01:30 Activity 2: docs/activity-2.md.
- 01:30–01:45 Review decisions and integration: docs/integration.md.
- 01:45–01:55 Individual evidence and reflection.
- 01:55–02:00 Knowledge check and next steps.

## Checks
Windows: `py -m unittest discover -s tests -v` and `py tools/lint.py`.
macOS/Linux: `python3 -m unittest discover -s tests -v` and `python3 tools/lint.py`.
Baseline: seven tests pass. The bundled lint checker has four limited rules; it is not a general-purpose linter. There is no hosted CI configuration.

## Scope
This is a pure-function teaching example, not a complete booking service. No database, authentication, concurrent capacity updates or web API is implemented. Input types and non-negative state counts are preconditions supplied by the caller. Each activity specifies additional business validation.

## Evidence
Copy docs/evidence-log.md outside the shared repository. Record your own contribution and actual results. Do not invent defects just to fill the checklist. Record incomplete steps accurately.
