Shopease Microservices Architecture
📌 Overview

Shopease is a microservices-based e-commerce backend designed with production-grade DevOps practices.

This project simulates a real-world deployment architecture including:

Containerization

CI/CD

Infrastructure as Code

Monitoring & Observability

Kubernetes deployment (future phase)

🛠 Tech Stack
Backend

Python (FastAPI)

PostgreSQL

Redis (future)

Docker

Frontend

HTML / JavaScript (Phase 1)

React (Future upgrade)

DevOps & Infra

Docker

Docker Compose

GitHub Actions

AWS (ECS / EKS – later phase)

Terraform (future)

Nginx (reverse proxy)

🔌 Default Ports
Service	Port
Backend API	8000
Frontend	3000
PostgreSQL	5432
Redis	6379
🔁 High-Level Architecture Flow
User
  ↓
Frontend (Browser)
  ↓
Backend API (FastAPI)
  ↓
PostgreSQL

Future enhancement:

User
 ↓
Nginx
 ↓
Frontend
 ↓
Backend
 ↓
Postgres
 ↓
Redis (cache)
