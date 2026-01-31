# 🚀 FastAPI JWT Authentication Boilerplate

### PostgreSQL • SQLAlchemy • Docker-Ready • Production Architecture

A **production-grade FastAPI backend boilerplate** designed for building **secure, scalable REST APIs** with JWT authentication and PostgreSQL.

This repository defines a **clear backend architecture**, sane defaults, and extensible patterns that can be used as the foundation for real-world systems, from internal platforms to SaaS backends.

---

## 🎯 Why This Project Exists

Modern backend systems rarely fail because of missing features.

They fail because of **poor structure, unclear boundaries, and configuration chaos** .

This project exists to:

- 🧱 Establish a **clean, modular FastAPI architecture**
- 🔐 Provide a **reliable authentication and database foundation**
- 📐 Prevent architectural drift as the codebase grows
- 🧠 Make future features predictable to implement

It is intentionally opinionated, favoring **clarity, maintainability, and correctness** over shortcuts.

---

## 🧰 Core Technologies

- ⚡ **FastAPI** — high-performance async API framework
- 🐘 **PostgreSQL** — relational database for production workloads
- 🧬 **SQLAlchemy ORM** — explicit, controlled database access
- 🔑 **JWT (JSON Web Tokens)** — stateless authentication
- 📦 **Pydantic v2** — validation & settings management
- 🌱 **python-dotenv** — environment-based configuration
- 🐳 **Docker / Docker Compose (planned)** — reproducible deployments

---

## 🏗 High-Level Architecture

The system follows a **layered backend architecture** , separating configuration, database access, business logic, and API routing.

### 🔁 Request Lifecycle

1. 🌍 Client sends HTTP request
2. 🚦 FastAPI router receives the request
3. 🧩 Dependencies handle:
   - Database session injection
   - JWT validation (where required)
4. 🧠 Business logic executes
5. 🗄 SQLAlchemy interacts with PostgreSQL
6. 📤 Structured JSON response is returned

This separation ensures:

- Low coupling
- Easier testing
- Predictable behavior under scale

---

## 🗂 Project Structure

<pre class="overflow-visible! px-0!" data-start="2583" data-end="3729"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-[calc(--spacing(9)+var(--header-height))] @w-xl/main:top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-text"><span><span>.
├── app/
│   ├── core/
│   │   ├── config.py          # Centralized settings & environment loading
│   │   └── security.py        # JWT utilities (planned)
│   │
│   ├── db/
│   │   ├── base.py            # SQLAlchemy declarative base
│   │   ├── session.py         # Engine & session factory
│   │   └── init_db.py         # Table initialization entrypoint
│   │
│   ├── models/
│   │   └── user.py            # Database models
│   │
│   ├── schemas/               # Pydantic request/response schemas (planned)
│   │
│   ├── api/
│   │   ├── deps.py            # Shared dependencies (JWT, DB)
│   │   └── routes/            # Versioned API routers (planned)
│   │
│   ├── services/              # Business logic layer (planned)
│   │
│   └── main.py                # FastAPI application entrypoint
│
├── showcase_pictures/         # Architecture diagrams & screenshots
├── test_env.py                # Environment validation utility
├── test_base_dir.py           # Path resolution diagnostics
├── .env                       # Runtime configuration (gitignored in real deployments)
├── .gitignore
├── README.md
└── requirements.txt
</span></span></code></div></div></pre>

---

## ⚙️ Configuration Strategy

All runtime configuration is driven by **environment variables** , loaded via `.env` and validated using **pydantic-settings** .

This ensures:

- 🔒 No hardcoded secrets
- 🔁 Easy environment switching (local / staging / production)
- ☁️ Compatibility with Docker, CI/CD, and cloud platforms

### 📄 Example `.env`

<pre class="overflow-visible! px-0!" data-start="4081" data-end="4288"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-[calc(--spacing(9)+var(--header-height))] @w-xl/main:top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-env"><span>app_name=FastAPI JWT Auth Boilerplate
env=development
database_url=postgresql://postgres:password@localhost:5432/fastapi_db
secret_key=supersecretkey
algorithm=HS256
access_token_expire_minutes=30
</span></code></div></div></pre>

---

## 🗄 Database Design

- PostgreSQL treated as a first-class dependency
- Explicit engine and session management
- SQLAlchemy declarative models
- No implicit magic or hidden globals

### 🧩 Example Model

<pre class="overflow-visible! px-0!" data-start="4509" data-end="4833"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-[calc(--spacing(9)+var(--header-height))] @w-xl/main:top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>class</span><span></span><span>User</span><span>(</span><span>Base</span><span>):
    __tablename__ = </span><span>"users"</span><span>

    </span><span>id</span><span> = Column(Integer, primary_key=</span><span>True</span><span>, index=</span><span>True</span><span>)
    email = Column(String, unique=</span><span>True</span><span>, index=</span><span>True</span><span>, nullable=</span><span>False</span><span>)
    hashed_password = Column(String, nullable=</span><span>False</span><span>)
    is_active = Column(Boolean, default=</span><span>True</span><span>)
    role = Column(String, default=</span><span>"user"</span><span>)
</span></span></code></div></div></pre>

Minimal, explicit, and extensible.

---

## 🔐 Authentication Design (JWT)

The architecture supports:

- Stateless authentication via JWT
- Token validation using FastAPI dependencies
- Route-level access control
- Role-based authorization (planned)

JWT logic is kept **outside route handlers** , ensuring routes remain readable and focused.

---

## 🧪 Development Utilities

Included utilities for reliability and debugging:

| Tool               | Purpose                     |
| ------------------ | --------------------------- |
| `test_env.py`      | Validate `.env`loading      |
| `test_base_dir.py` | Confirm BASE_DIR resolution |
| `init_db.py`       | Create database tables      |

These scripts eliminate configuration ambiguity early.

---

## 🐳 Docker & Deployment (Planned)

The project structure supports:

- Dockerized FastAPI service
- Dockerized PostgreSQL
- Environment-based configuration injection
- Deterministic local and production builds

Planned additions:

- `Dockerfile`
- `docker-compose.yml`
- Non-root containers
- Health checks

---

## 🛣 Roadmap

Architecture first, features second.

- [x] Application structure
- [x] PostgreSQL integration
- [x] Environment & settings management
- [x] Database models & initialization
- [ ] Authentication routes
- [ ] Password hashing
- [ ] Refresh tokens
- [ ] Role-based access control
- [ ] Alembic migrations
- [ ] Docker support
- [ ] API versioning
- [ ] Automated tests

---

## 📊 Mermaid Architecture Diagram (Source)

![FAST API PostgreSQL Architecture Flow](showcase_pictures\01_fastapi_jwt_postgresql_architecture_flow.png "FAST API PostgreSQL Architecture Flow")

---

## 🧠 Design Philosophy

- Explicit over implicit
- Structure over shortcuts
- Maintainability over speed
- Scalability over convenience

This backend is designed to **grow without rewrites**.

---

## 🔍 Technologies

**FastAPI, PostgreSQL, JWT Authentication, SQLAlchemy, Python Backend, REST API, API Architecture, Pydantic, Docker Backend, Backend Boilerplate, Secure API, Authentication System, Production FastAPI**
