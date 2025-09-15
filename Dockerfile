FROM python:3.9-slim
# Updated by bot: Create a .dockerignore file to exclude files like .git, __pycache__, etc.
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "-u", "app.py"]
