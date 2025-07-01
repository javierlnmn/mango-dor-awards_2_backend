# Django REST Backend

This project uses **Poetry** for dependency management, **Django + Django REST framework** for the backend, and **pre-commit hooks** for code formatting and linting.

Follow these steps to get your development environment ready:

## Prerequisites

- Python 3.13 or higher installed  
- Git installed  
- (Optional) Docker installed if you use it for development  

## Setup Steps

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd <your-repo-folder>
   ```

2. **Install Poetry** (if not already installed): follow the installation steps at https://python-poetry.org/docs/

3. **Install Python dependencies with Poetry**
   ```bash
   poetry install
   ```

4. **Activate Poetry shell**
   ```bash
   poetry shell
   ```

5. **Install pre-commit Git hooks**
   ```bash
   poetry run pre-commit install
   ```

6. **Run database migrations**
   ```bash
   poetry run python manage.py migrate
   ```

7. **Start the Django development server**
   ```bash
   poetry run python manage.py runserver
   ```

## Docker Development

Alternatively, you can run the project using Docker for development:

1. **Build and start the containers**
   ```bash
   cd docker/dev
   docker-compose up --build
   ```

2. **Access the application**
   - Django server: http://localhost:8000
   - Admin interface: http://localhost:8000/admin

3. **Stop the containers**
   ```bash
   docker-compose down
   ```

## Notes

- Code formatting and linting are enforced via pre-commit hooks. Please ensure you run `pre-commit install` to enable them locally.
- Use `poetry run <command>` if you're not inside the Poetry shell (e.g., `poetry run python manage.py runserver`).
- For frontend CORS and Django allowed hosts, see `.env` for configuration.
- Keep your `.env` file private and never commit secrets.

