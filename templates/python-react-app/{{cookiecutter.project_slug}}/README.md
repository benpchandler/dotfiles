# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

## Architecture

This project follows the vertical slice architecture pattern with:

- **Frontend**: Vite + TypeScript + React
- **Backend**: FastAPI with hybrid GraphQL/REST API
- **Database**: PostgreSQL{% if cookiecutter.use_vector_search == "yes" %} with pgvector extension{% endif %}
- **UI**: shadcn/ui components with Tailwind CSS

## Project Structure

```
{{ cookiecutter.project_slug }}/
├── backend/                 # FastAPI backend
│   ├── app/
│   │   ├── api/            # REST endpoints
│   │   ├── graphql/        # GraphQL schema & resolvers
│   │   ├── core/           # Configuration, database
│   │   ├── models/         # SQLAlchemy models
│   │   └── main.py
├── frontend/               # React frontend
│   ├── src/
│   │   ├── features/       # Vertical slice features
│   │   ├── shared/         # Shared utilities
│   │   └── App.tsx
├── docker-compose.yml{% if cookiecutter.use_docker == "yes" %}
├── .env.example
└── README.md
```

## Quick Start

### Prerequisites
- Python {{ cookiecutter.python_version }}+
- Node.js 18+
- PostgreSQL{% if cookiecutter.use_vector_search == "yes" %} with pgvector extension{% endif %}

### Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Set up database (PostgreSQL must be running)
alembic upgrade head

# Start the server
uvicorn app.main:app --reload
```

### Frontend Setup
```bash
cd frontend
npm install
npm run dev
```