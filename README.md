# FAQ API

This project is a Django-based API for managing FAQs, with multilingual support and caching using Redis. It provides a REST API for retrieving and managing FAQs, including the ability to store translations and leverage a WYSIWYG editor for rich-text answers.

## Features

- FAQ management (question and answer storage).
- Support for multiple languages.
- Caching with Redis to improve performance.
- WYSIWYG editor for formatting answers.
- Docker support for easy setup and deployment.

## Prerequisites

- Docker
- Docker Compose
- Python

## Setup and Installation

1. **Clone the repository:**

git clone <repository_url>
cd faq_api


2. **Build Docker containers:**

docker-compose up --build


3. **Migrate the database:**

docker-compose exec web python manage.py migrate


4. **Create a superuser (optional):**

docker-compose exec web python manage.py createsuperuser


5. **Access the application:**

The Django app will be available at http://localhost:8000.
The Redis service will run on port 6379 (default for Redis).

6. **Testing (Unit Tests):**

docker-compose exec web pytest


## API Endpoints

### `GET /api/faqs/`

Fetch all FAQs.  Supports language filtering via the `lang` query parameter (e.g., `?lang=es`). Defaults to English.

curl http://localhost:8000/api/faqs/
curl http://localhost:8000/api/faqs/?lang=es


### `POST /api/faqs/`

Create a new FAQ.  Requires a JSON payload with `question`, `answer` (HTML from WYSIWYG), and optionally `language` (defaults to 'en').

curl -X POST http://localhost:8000/api/faqs/ 

-H "Content-Type: application/json" 

-d '{"question": "What is Django?", "answer": "<p>Django is a Python web framework.</p>"}'

curl -X POST http://localhost:8000/api/faqs/ 

-H "Content-Type: application/json" 

-d '{"question": "¿Qué es Django?", "answer": "<p>Django es un marco web de Python.</p>", "language": "es"}'


## Docker Commands

- **Start:** `docker-compose up`
- **Stop:** `docker-compose down`
- **Rebuild:** `docker-compose up --build`
- **Logs:** `docker-compose logs -f`
- **Execute in container:** `docker-compose exec web <command>` (e.g., `docker-compose exec web python manage.py shell`)

## Environment Variables

- `REDIS_HOST`: Redis host (default: `redis`)
- `REDIS_PORT`: Redis port (default: `6379`)
- `LANGUAGE_CODE`: Default language (default: `en`)
- `ALLOWED_HOSTS`: Allowed hostnames (important for production: e.g., `ALLOWED_HOSTS=example.com,api.example.com`)



