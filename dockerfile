FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY app.py .

# Cloud Run requires listening on $PORT
ENV PORT=8080

# Use gunicorn for production
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]
