FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Set environment for development mode
ENV FLASK_ENV=development

COPY src/ .

EXPOSE 5000

# Use python to run your app (no need to invoke livereload directly)
CMD ["python", "app.py"]
