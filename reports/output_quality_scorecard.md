# Output Quality Scorecard

This is a release-planning and static-contract scorecard, not provider-backed output evidence.

| Dimension | Static acceptance rule | Status |
|---|---|---|
| Intent fidelity | job, users, inputs, outputs and exclusions are present in `manifest.json` | pass after local validation |
| Trigger routing | four families cover positive, negative, near-neighbor and adversarial cases | pass after trigger eval |
| Package usability | root entry, README, interface, manifest and installation commands are present | pass after package validation |
| Context discipline | root `SKILL.md` remains within the selected budget | pass/warn from context report |
| Trust and permissions | remote execution, writes, secrets and rollback are explicit | pass after interface/manifest review |
| Public claim discipline | static evidence cannot be labeled provider/human quality evidence | pass by policy |

## Missing evidence

`provider_backed`, `human_blind_review`, `real_client_telemetry`, user satisfaction and business outcome evidence are not available in this first release. They must remain `missing evidence` until independently collected and reviewed.
