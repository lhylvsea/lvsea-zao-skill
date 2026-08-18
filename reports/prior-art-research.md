# Prior-Art Research

- Researched at: 2026-08-18
- Requested sources: [joeseesun/qiaomu-meta-skill](https://github.com/joeseesun/qiaomu-meta-skill), [yaojingang/yao-meta-skill](https://github.com/yaojingang/yao-meta-skill)
- Inspected commits: Qiaomu `9d9eafe` / `v2.8.1`; Yao `f5d8f68`
- Intent queries: `create reusable agent skill package`; `skill engineering trigger evaluation`; `agent skill governance portability`; `publish agent skill GitHub release`
- Catalogs: skills.sh, SkillsMP, GitHub source
- Rating evidence: unavailable; installs and repository stars are not ratings or correctness evidence

## Catalog evidence

| Catalog | Observation | Meaning | Limitation |
|---|---|---|---|
| skills.sh | Four manual `npx.cmd skills find` queries completed on 2026-08-18; examples included `daymade/claude-code-skills@skill-reviewer` (1K installs), `jezweb/claude-skills@github-release` (1.2K installs), and `archieindian/openclaw-superpowers@skill-portability-checker` (24 installs) | Ecosystem adoption/discovery signal | These candidates were not adopted without source review; installs do not prove quality |
| SkillsMP | The bundled runner returned 33 deduplicated candidate families across the four queries | Broad discovery signal; repository stars kept separate in the generated JSON | Results were noisy and require source review; no public rating evidence was available |
| GitHub | The two requested repositories were cloned and their root Skill, interface, manifest, README, license and relevant references were inspected | Canonical source, structure, permissions and license evidence | Repository attention is not Skill output quality |

The machine-generated, source-separated discovery snapshot is `../prior-art-candidates.json` in the local work area used during creation; it is intentionally not copied into this public package because it contains noisy catalog candidates that were not reviewed or adopted.

## Reference skills studied

### Qiaomu Meta Skill

- Source: [joeseesun/qiaomu-meta-skill](https://github.com/joeseesun/qiaomu-meta-skill), inspected at `v2.8.1`.
- Role: publication and practical release anchor.
- Mechanisms learned: dual-catalog prior-art runner, source verification, `keep / adapt / reject / invent`, lightweight trigger evaluation, evidence-aware claims, root-entrypoint isolation, version checks, feature-branch/PR/Release flow, public discovery and clean npx installation.
- Destination in this package: `references/skill-engineering-method.md`, `references/evaluation-and-governance.md`, `scripts/trigger_eval.py`, `scripts/validate_skill.py`, `scripts/release_check.py`, `scripts/publish_skill.py` and the `reports/` contract.

### Yao Meta Skill

- Source: [yaojingang/yao-meta-skill](https://github.com/yaojingang/yao-meta-skill), inspected at commit `f5d8f68`.
- Role: governance, portability and evidence anchor.
- Mechanisms learned: intent-first package design, platform-neutral Skill IR, scaffold/production/library/governed modes, trigger families and holdout thinking, context discipline, output contracts, owner/review cadence, trust/permission/rollback boundaries and explicit `missing evidence` labels.
- Destination in this package: `manifest.json`, `agents/interface.yaml`, `schemas/skill-ir.schema.json`, `scripts/export_skill_ir.py`, `scripts/context_sizer.py`, `references/intent-dialogue.md`, `references/portability-and-trust.md`, `references/operating-modes.md` and the four-bucket `evals/trigger_cases.json`.

## Synthesis ledger

### keep

- Keep the Qiaomu rule that research and release are part of the Skill lifecycle, not optional README prose.
- Keep the Yao separation between a lean runtime entry, on-demand references, deterministic scripts, eval fixtures and evidence reports.
- Keep separate metrics and evidence classes; never turn installs, stars, static fixtures or plans into a single quality score.

### adapt

- Adapt Qiaomu’s publisher from Qiaomu-owned naming and profile injection to the requested `lhylvsea` owner; no personal QR or promotional assets are included.
- Adapt Yao’s extensive Skill OS into a first-release compact contract: IR, context budget, trust, rollback, lifecycle and trigger families are retained; telemetry, review studio and world-class evidence systems are not pulled in without a real need.
- Adapt shell assumptions for Windows by resolving `npx.cmd`, `gh`, `git` and `python` before subprocess calls.

### reject

- Reject direct default-branch pushes, released-version reuse and unreviewed third-party script execution.
- Reject copying either upstream repository wholesale; it would increase context, maintenance and license/attribution surface without proving user value.
- Reject Qiaomu profile assets and branding because the requested owner is `lhylvsea`.
- Reject claims of superiority, provider quality, human preference or production outcome without named evidence.

### invent

- A compact “轻入口 + 硬门禁” package that joins Qiaomu’s practical publishing chain with Yao’s IR/governance contract.
- Four trigger families (`should_trigger`, `should_not_trigger`, `near_neighbor`, `adversarial`) in one small evaluator, rather than a keyword-only positive list.
- A cross-platform runtime resolver and a local gate that measures context, trust, version consistency and output-evidence status together.
- A Chinese-first README and trigger surface tailored to the user’s Skill packaging and GitHub publishing workflow.

## Missing evidence

- No provider-backed output comparison was run for a generated Skill.
- No independent human blind review or real client telemetry was available.
- The selected third-party catalog candidates were discovery-only; source-level quality comparison was not performed.
- Public GitHub publication and clean installation evidence will be added by the release flow after the package is accepted by local gates.
