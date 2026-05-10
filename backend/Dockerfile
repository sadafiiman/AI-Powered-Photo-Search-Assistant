FROM python:3.11-slim

WORKDIR /app

# system deps (cached layer)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# dependency layer FIRST (important for caching)
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# app code LAST (so changes don't reinstall deps)
COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]