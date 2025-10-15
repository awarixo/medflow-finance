# Use official Python image as base
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /code

# Install system dependencies (database driver, build tools, etc)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements.txt and install Python dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy application code into the container
COPY app ./app

# Expose port for Uvicorn
EXPOSE 8000

# Set environment variables (your app expects a .env file at runtime)
# COPY .env .    # If you want to build the .env into the image (not recommended for secrets!)
# Best to mount .env at runtime instead

# Start the FastAPI app with uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
