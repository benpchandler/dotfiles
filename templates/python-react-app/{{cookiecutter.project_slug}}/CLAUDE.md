# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

Python (FastAPI) backend + React/TypeScript frontend. **Quality is gate-enforced** —
the gates are the source of truth, not a sense that it "looks done."

## Gates (all blocking, zero baseline)

| | Lint | Types | Tests |
|---|---|---|---|
| **backend/** (uv) | `uv run ruff check .` + `ruff format --check .` | `uv run mypy app` (strict) | `uv run pytest` |
| **frontend/** (npm) | `npm run lint` (`--max-warnings 0`) | `npm run typecheck` | `npm run test` |

Run them before declaring work done. CI (`.github/workflows/ci.yml`) enforces all of
the above **plus type-drift**: the frontend's `src/types/api.generated.ts` is generated
from the backend's OpenAPI schema, and CI fails if they fall out of sync.

## The type contract

Backend Pydantic models (`backend/app/models.py`) → OpenAPI → `npm run generate:types`
→ `frontend/src/types/api.generated.ts`. Change a model, regenerate the types. Never
hand-edit the generated file.

## Agents

Dispatch the bundled specialists (in `.claude/agents/`) instead of a generic agent:
- **python-engineer** / **python-reviewer** — backend work.
- **typescript-engineer** / **typescript-reviewer** — frontend work.

They prove their work with the gates above rather than self-certifying.

## Conventions

- **Backend:** typed public signatures; Pydantic models (never bare dicts) at the API
  boundary; specific exceptions, never bare `except`; `with` for resources.
- **Frontend:** `unknown` over `any` at boundaries then narrow; hooks unconditionally
  at the top with effect cleanup; no floating promises.
