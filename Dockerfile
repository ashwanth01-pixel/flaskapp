# Updated by bot: Use a specific Python version, e.g., FROM python:3.9-slim
# Updated by bot: Use a specific Python version, e.g., FROM python:3.9-slim
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "-u", "app.py"]

# Appended by bot: Use a specific Python version, e.g., FROM python:3.9-slim
