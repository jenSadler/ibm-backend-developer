FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

# Upgrade pip
RUN pip3 install --upgrade pip

# Set environment variable to allow deprecated sklearn package
ENV SKLEARN_ALLOW_DEPRECATED_SKLEARN_PACKAGE_INSTALL=True

# Install dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

# Run the Flask app
CMD ["flask", "run", "--host=0.0.0.0", "--port=8000"]
