# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

A Python (FastAPI) + React (TypeScript) project with strict, gate-enforced quality
baked in from line one: ruff + strict mypy on the backend, ESLint + strict tsc on the
frontend, end-to-end typed via OpenAPI, all blocking in CI.

## Setup

```bash
# Backend
cd backend
uv sync --dev
uv run pytest                 # passes out of the box
uv run pre-commit install     # optional: local gates on commit

# Frontend
cd ../frontend
npm install
npm run generate:types        # generate API types from the backend OpenAPI schema
npm run check                 # lint + typecheck + test
```

After the first install, commit the generated `backend/uv.lock` and
`frontend/package-lock.json`, then tighten CI's `uv sync` → `uv sync --frozen` and
`npm install` → `npm ci` for reproducible builds.

## Run

```bash
cd backend && uv run uvicorn app.main:app --reload   # http://localhost:8000  (/docs for OpenAPI)
cd frontend && npm run dev                            # http://localhost:5173
```

## The gates

| | Lint | Types | Tests |
|---|---|---|---|
| backend | `uv run ruff check .` | `uv run mypy app` | `uv run pytest` |
| frontend | `npm run lint` | `npm run typecheck` | `npm run test` |

CI additionally runs a **type-drift** check: change a backend model without
regenerating `frontend/src/types/api.generated.ts` (`npm run generate:types`) and CI
fails — the frontend can never silently disagree with the backend about a shape.
