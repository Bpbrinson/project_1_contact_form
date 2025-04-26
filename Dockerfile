# Pull Base image
FROM python:3.13-alpine

# Set environment variables to prevent .pyc files and enable unbuffered logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system dependencies (important for MySQL & compiling packages)
RUN apk add --no-cache gcc musl-dev libffi-dev openssl-dev python3-dev mariadb-dev

# Install dependencies
COPY requirements.txt .
RUN pip install -r --no-cache-dir requirements.txt

# Copy source code
COPY . .

# Expose port
EXPOSE 5000

# Run the application
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:create_app()"]