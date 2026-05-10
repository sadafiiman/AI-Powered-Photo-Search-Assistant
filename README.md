# 📸 AI-Powered Photo Search Assistant

An AI-powered system that processes user-uploaded images, extracts semantic keywords using GPT-4o vision, searches for similar images, downloads results, and stores structured metadata in PostgreSQL.

The system is fully async and containerized with Docker.

---

## 🚀 Features

- 📤 Image upload API
- 🧠 AI-powered keyword extraction (GPT-4o vision-ready)
- 🔍 Image similarity search (Google / SerpAPI ready)
- 📥 Automatic image downloading
- 🗄️ PostgreSQL + JSONB metadata storage
- ⚡ Async processing with Celery + Redis
- 📡 Real-time job tracking (planned via WebSockets)
- 🐳 Fully Dockerized environment

---

## 🏗️ Architecture

Frontend (React)
      ↓
FastAPI (API Layer)
      ↓
Redis Queue
      ↓
Celery Worker (AI Pipeline)
      ↓
OpenAI + Image Search + Downloader
      ↓
PostgreSQL (JSONB storage)

---

## 📦 Tech Stack

### Backend
- FastAPI
- SQLAlchemy
- PostgreSQL (JSONB)
- Celery
- Redis

### AI
- OpenAI GPT-4o (vision)

### Infrastructure
- Docker
- Docker Compose

---

## 🐳 Setup (Docker)

---

### 1. Create .env file

```bash
DB_HOST=postgres
DB_PORT=5432
DB_USER=postgres
DB_PASSWORD=postgres
DB_NAME=photo_search

REDIS_URL=redis://redis:6379/0

OPENAI_API_KEY=your_openai_key
```
---

### 2. Build and run

```bash
docker-compose up --build
```
---

### 3. API will be available at

```bash
4. API will be available at
```

---

## 📡 API Endpoints

- Create a job (upload image)

```bash
POST /upload
```

Response: 
```bash
{
  "id": "job_id",
  "status": "pending"
}
```

- Get job status
```bash
GET /job/{job_id}
```

Response:

```bash
{
  "id": "job_id",
  "status": "processing",
  "extracted_keywords": {
    "keywords": ["dog", "park", "outdoor"]
  },
  "results": {
    "images": []
  }
}
```

---


## 🧠 Data Model

### Table: image_jobs
- id (UUID)
- status (pending / processing / done / failed)
- original_image_url
- extracted_keywords (JSONB)
- results (JSONB)
- created_at
- updated_at

---

## ⚙️ Development (without Docker)
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```
