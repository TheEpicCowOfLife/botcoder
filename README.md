# Botcoder - AI Game Tournament Platform

A modern web platform for hosting AI game tournaments, similar to MIT Battlecode. This project uses Vue 3 for the frontend and Django for the backend.

## Project Structure

```
botcoder/
├── frontend/          # Vue 3 frontend application
├── backend/          # Django backend application
└── docker-compose.yml # Docker configuration
```

## Prerequisites

- Node.js (v18 or higher)
- Python 3.10 or higher
- Docker and Docker Compose
- Poetry (Python package manager)

## Development Setup

### Database Setup

1. Start the PostgreSQL container:
   ```bash
   docker-compose up -d
   ```

2. Wait a few seconds for the database to be ready. You can check the status with:
   ```bash
   docker-compose ps
   ```

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Install Poetry if you haven't already:
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```
   OR 
   ```bash
   sudo apt install python3-poetry
   ```

3. Install dependencies:
   ```bash
   poetry install
   ```

4. Set up environment variables:
   ```bash
   cp .env.example .env
   # The default database credentials in .env match the Docker setup
   ```

5. Run migrations:
   ```bash
   poetry run python manage.py migrate
   ```

6. Create a superuser:
   ```bash
   poetry run python manage.py createsuperuser
   ```

7. Run the development server:
   ```bash
   poetry run python manage.py runserver
   ```

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm run dev
   ```

## Development Tools

### Backend
- Black for code formatting
- Flake8 for linting
- Pre-commit hooks for automated checks
- Django REST framework for API
- Django CORS headers for frontend communication

### Frontend
- ESLint for linting
- Prettier for code formatting
- Husky for git hooks
- Vue Router for routing
- Pinia for state management

## Contributing

1. Install pre-commit hooks:
   ```bash
   # In backend directory
   poetry run pre-commit install

   # In frontend directory
   npm run prepare
   ```

2. Create a new branch for your feature:
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. Make your changes and commit them:
   ```bash
   git add .
   git commit -m "Your commit message"
   ```

The pre-commit hooks will automatically run linting and formatting checks before each commit.

## Stopping the Development Environment

To stop the development environment:

1. Stop the frontend development server (Ctrl+C)
2. Stop the backend development server (Ctrl+C)
3. Stop the PostgreSQL container:
   ```bash
   docker-compose down
   ```

## License

MIT License 