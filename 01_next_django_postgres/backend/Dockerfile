# backend/Dockerfile
FROM python:3.12.5-slim

# Set environment variables
# Avoid Python from creating .pyc files
ENV PYTHONDONTWRITEBYTECODE 1
# Avoid buffering stdin stdout
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requiremenst into the /usr/src/next_django_postgres folder
COPY ./requirements.txt .

# Install dependencies
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy the Django app code into the /usr/src/next_django_postgres folder
COPY . .

# Expose port for Django
EXPOSE 8010

# Run Django's server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8010"]
