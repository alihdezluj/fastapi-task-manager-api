
# Task Manager API

A simple **RESTful Task Management API** built with **Python and FastAPI**.  
This project demonstrates backend fundamentals such as API design, CRUD operations, HTTP status codes, and in-memory data storage.

---

## Features

- RESTful API built with FastAPI
- CRUD operations for task management
- Automatic ID generation
- Error handling using HTTP status codes
- In-memory data storage
- Interactive API documentation

---

## Installation

Clone the repository:

```bash
git clone https://github.com/alihdezluj/fastapi-task-manager-api.git
cd fastapi-task-manager-api
```

Create a virtual environment:

```bash
uv venv
```

Activate it:

Windows

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
uv add fastapi[all] scalar-fastapi
```

---

## Running the API

Start the development server:

```bash
uv run fastapi dev
```

The API will run at:

```
http://127.0.0.1:8000
```

---

## API Documentation

FastAPI automatically generates interactive API documentation.

Scalar Documentation:

```
http://127.0.0.1:8000/scalar
```

---

## API Endpoints

### Get all tasks

```
GET /tasks
```

Returns a list of all tasks.

---

### Get a task by ID

```
GET /tasks/{task_id}
```

Returns a specific task.

---

### Create a new task

```
POST /tasks
```

Creates a new task.

---

### Replace a task

```
PUT /tasks/{task_id}
```

Replaces an existing task while preserving server-managed fields.

---

## Example Task Object

```json
{
  "id": 1,
  "title": "Setup project repository",
  "description": "Initialize Git repository and create project structure",
  "completed": false,
  "priority": "high",
  "created_at": "2026-04-01",
  "due_date": "2026-04-03",
  "tags": ["setup", "backend"],
  "user_id": 1
}
```

---

## Future Improvements

- Add PATCH endpoint for partial updates
- Add DELETE endpoint
- Add Pydantic models for validation
- Add database integration (PostgreSQL or SQLite)
- Deploy API to a cloud service
