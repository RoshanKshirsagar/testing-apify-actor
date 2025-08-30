# Use official Python runtime as a parent image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Install system dependencies (for building wheels, etc.)
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    g++ \
    make \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first (to leverage Docker layer caching)
COPY requirements.txt ./

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files
COPY . .

# Set environment variables for Apify
ENV PYTHONPATH=/app
ENV APIFY_MEMORY_MBYTES=2048
ENV APIFY_TIMEOUT_SECS=300

# Run the actor
CMD ["python", "-m", "apify", "run", "main"]
