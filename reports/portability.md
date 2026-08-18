# Portability Report

| Target | Source contract | Current status |
|---|---|---|
| OpenAI | `agents/interface.yaml` metadata adapter + root `SKILL.md` | Static contract present; real client install evidence is `missing evidence` |
| Claude | neutral source plus adapter notes | Static contract present; real client install evidence is `missing evidence` |
| Generic Agent Skills | canonical root package | Root entrypoint and package validator are available |
| VS Code | neutral source plus review notes | Static contract present; real client install evidence is `missing evidence` |

The package does not claim that every target has been executed. When an adapter or client cannot consume a resource, preserve the platform-neutral intent and degrade to the documented output contract instead of silently dropping safety, permission or evidence fields.
