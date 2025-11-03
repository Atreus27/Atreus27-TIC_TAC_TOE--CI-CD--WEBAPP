# Dockerfile
FROM python:3.11-slim

WORKDIR /app
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Create DB initially (so container has DB file)
RUN python - <<'PY'
import storage
storage.init_db()
print("DB initialized")
PY

EXPOSE 5050
CMD ["python", "app.py"]
