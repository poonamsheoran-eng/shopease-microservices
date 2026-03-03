Shopease – System Architecture
1️⃣ High-Level Flow
Browser
   ↓
HTML / JavaScript (Frontend)
   ↓
FastAPI Backend (Port 8000)
   ↓
PostgreSQL (Port 5432)
   ↓
Redis (Port 6379 - caching layer)
Flow Explanation

User interacts with the browser.

Frontend (HTML/JS) sends HTTP requests to backend.

Backend (FastAPI) processes request.

Backend:

Reads/writes to PostgreSQL

Uses Redis for caching frequently accessed data

2️⃣ Technology Components
Backend

Python

FastAPI

Uvicorn (ASGI server)

Database

PostgreSQL (primary relational database)

Cache

Redis (in-memory caching, session storage, rate limiting)

Frontend (Phase 1)

HTML

JavaScript

Simple static server (later)

3️⃣ Port Configuration
Component	Port
Backend API	8000
PostgreSQL	5432
Redis	6379
Frontend	3000 (later phase)

All ports will be configurable via environment variables in production.

4️⃣ Current Deployment Strategy (Phase 1)

Single server deployment

All services run locally

No load balancer

No reverse proxy yet

Direct browser → backend communication

This keeps development simple while preserving production structure.

5️⃣ Future Scaling Plan
Phase 2 – Dockerization

Containerize:

Backend

PostgreSQL

Redis

Use Docker Compose for local multi-service orchestration

Phase 3 – Reverse Proxy

Add Nginx in front

Route traffic to backend

Handle HTTPS

Phase 4 – Cloud Deployment

Deploy containers to:

AWS ECS (initial cloud)

Later migrate to Kubernetes (EKS)

Phase 5 – Horizontal Scaling

When traffic increases:

Run multiple backend instances

Introduce load balancer

Redis becomes shared cache

PostgreSQL moved to managed service

6️⃣ Production Engineering Notes

Backend must remain stateless.

Configuration via environment variables.

Secrets must not be committed to Git.

Health endpoint required for container orchestration.

Logs must be structured (JSON format in future).
