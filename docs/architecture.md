📐 ShopEase – System Architecture
1️⃣ High-Level Architecture Overview

ShopEase follows a layered microservices architecture with caching and persistent storage.

User
  │
  ▼
Frontend (Port: 3000)
  │
  ▼
Backend API (Port: 5000)
  │
  ├──────────────► PostgreSQL (Port: 5432)
  │
  └──────────────► Redis (Port: 6379)
2️⃣ Component Description
🧑 User

End user accessing the platform via browser or mobile device.

🎨 Frontend Service

Technology: React / Next.js

Runs on: Port 3000

Responsibility:

Render UI

Call backend APIs

Handle authentication tokens

Manage client-side state

Communication:

HTTP/HTTPS → Backend API

🧠 Backend API

Technology: Node.js + Express

Runs on: Port 5000

Responsibility:

Authentication

Business logic

Order processing

Product management

Database operations

Cache interaction

Dependencies:

PostgreSQL (primary database)

Redis (caching + session storage)

🗄 PostgreSQL Database

Port: 5432

Role: Persistent data storage

Stores:

Users

Orders

Products

Transactions

Data Characteristics:

ACID compliant

Relational schema

Indexed for performance

⚡ Redis

Port: 6379

Role: In-memory cache

Used for:

Session storage

Caching product queries

Rate limiting

Reducing DB load

3️⃣ Architecture Flow (Detailed)
🔄 Request Lifecycle

User sends request from browser

Frontend (3000) calls Backend API (5000)

Backend:

Checks Redis cache

If cache miss → queries PostgreSQL

Stores response in Redis

Response sent back to frontend

UI updated

4️⃣ Network Design (Container Perspective)

In Docker/Kubernetes environment:

All services run inside isolated containers

Communication happens via internal service DNS

Only frontend and backend are exposed externally

PostgreSQL and Redis remain internal services

Example (Docker Compose networking):

frontend → backend (http://backend:5000
)

backend → postgres (postgres:5432)

backend → redis (redis:6379)

5️⃣ Port Configuration Summary
Service	Port	Exposure Type
Frontend	3000	Public
Backend	5000	Public
PostgreSQL	5432	Internal Only
Redis	6379	Internal Only
6️⃣ Scalability Strategy (Future Design)

Horizontal scaling of backend containers

Redis for reducing database load

Read replicas for PostgreSQL (future stage)

Kubernetes HPA for auto-scaling

Load balancer before backend

7️⃣ Production Considerations

Security:

JWT-based authentication

Environment variables for secrets

DB not publicly exposed

Rate limiting via Redis

Reliability:

Health check endpoints

Retry mechanisms

Graceful shutdown support

Observability (Next Phase):

Logging

Metrics

Distributed tracing
