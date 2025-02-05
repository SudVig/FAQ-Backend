# Use an official Python runtime as the base image
FROM python:3.10

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Copy the project files into the container
COPY . /app/

# Upgrade pip and install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Collect static files for production
RUN python manage.py collectstatic --noinput

# Expose port 8000 for the application
EXPOSE 8000

# Set environment variable to tell Django to run in production
ENV DJANGO_SETTINGS_MODULE=faq_api.settings

# Start the Gunicorn server instead of runserver
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "faq_api.wsgi:application"]
