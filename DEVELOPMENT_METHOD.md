# CharityGraph development method

**Status:** Reference — current working development method; not product or semantic authority  
**Date:** 11 September 2026

This document describes the current working method across the CharityGraph
repositories. It does not override product, semantic, source, release or
implementation authorities.

## Human role

Greg owns the product objective, priorities, semantic and editorial decisions,
evidentiary sufficiency, material-authority expansion, merges and releases, and
stopping decisions.

## Supervisory and implementation roles

The long-lived ChatGPT project conversation is used for architecture and product
reasoning, interpretation of experimental results, selection of the next bounded
tranche, drafting Codex instructions and challenging whether work remains on the
critical path.

Codex in VS Code is the local execution and implementation agent. It inspects
repositories, changes code and tests, performs deterministic runtime work and
provider-free analysis, performs bounded provider or source execution only when
explicitly authorised, and reports durable results back to the supervisory loop.

## Gulp/Nibble heuristic

> Gulp when there is a navigable solution space. Nibble when the next unknown is a single decision, fact or hard boundary.

The working cadence is:

> Gulp → hard boundary → Nibble → resolve boundary → Gulp.

This is a development-workflow heuristic, not CharityGraph product architecture.

## Run-duration objective

Immediate genuine blockers should fail quickly, ideally in less than one minute.
Otherwise useful Codex tranches are intentionally large enough to reduce human
relay and idle time, with more than 15 minutes a current practical target.
Deterministic implementation defects are normally absorbed inside a viable
tranche. Elapsed duration is an operational heuristic, not a quality metric.

## Model routing

Luna is the default implementation and bounded diagnostic model. Terra is an
escalation resource for consequential ambiguity, contradictory evidence or
repeated Luna diagnostic failure. This routing is an economic/development choice,
not product doctrine.

## Hard boundaries

External provider calls, source acquisition, retries and resends, semantic
authority changes, governed promotion, publication and merge, and destructive
state mutation are explicit boundaries. Their authority is checked separately
from ordinary local implementation and testing.

## ChatGPT/Codex handoff

```text
project state/results
  → supervisory ChatGPT reasoning
  → bounded Codex instruction
  → local Codex implementation/execution
  → structured completion/blocker report
  → human transfers result back
  → next supervisory decision
```

Manual transfer currently exists and introduces human-loop latency.

## Host safety layer

The Codex/host execution-safety reviewer is separate from CharityGraph product
requirements. The development environment may independently block external
provider calls, source network activity, persistent authority-state changes and
Git publication even when CharityGraph's internal controls permit an operation.

Campaign manifests, standing mandates and concrete execution tickets have partly
been shaped by the need to operate paid or external actions safely. Reviewers
should distinguish enduring CharityGraph Factory controls from development-
environment or host-control accommodations. This document does not decide which
accommodations should remain.

## Private/runtime boundary

Raw source archives, provider responses, runtime SQLite databases, private
experiment artefacts and credentials are deliberately not public Git content.
Repository review can inspect code, contracts, tests and sanitised empirical
summaries, but cannot independently reproduce every private runtime fact from Git
alone.
