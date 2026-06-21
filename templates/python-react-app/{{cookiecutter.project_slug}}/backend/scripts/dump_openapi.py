"""Emit the FastAPI OpenAPI schema to stdout — the source for the frontend types.

    uv run python scripts/dump_openapi.py > openapi.json

The frontend regenerates `src/types/api.generated.ts` from this; the type-drift CI
check fails if the committed types no longer match the live schema.
"""

import json

from app.main import app


def main() -> None:
    print(json.dumps(app.openapi(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
