from datetime import date
from typing import Any

from fastapi import FastAPI, HTTPException, status
from scalar_fastapi import get_scalar_api_reference

app = FastAPI()

tasks_db = {
    1: {
        "id": 1,
        "title": "Setup project repository",
        "description": "Initialize Git repository and create project structure",
        "completed": False,
        "priority": "high",
        "created_at": "2026-04-01",
        "due_date": "2026-04-03",
        "tags": ["setup", "backend"],
        "user_id": 1,
    },
    2: {
        "id": 2,
        "title": "Design API endpoints",
        "description": "Plan REST endpoints for task management",
        "completed": False,
        "priority": "medium",
        "created_at": "2026-04-01",
        "due_date": "2026-04-05",
        "tags": ["api", "design"],
        "user_id": 1,
    },
    3: {
        "id": 3,
        "title": "Implement CRUD operations",
        "description": "Create create, read, update, delete task operations",
        "completed": False,
        "priority": "high",
        "created_at": "2026-04-02",
        "due_date": "2026-04-06",
        "tags": ["backend", "crud"],
        "user_id": 2,
    },
    4: {
        "id": 4,
        "title": "Add filtering and search",
        "description": "Allow filtering tasks by priority, completion status and title",
        "completed": False,
        "priority": "medium",
        "created_at": "2026-04-02",
        "due_date": "2026-04-07",
        "tags": ["api", "filter"],
        "user_id": 2,
    },
    5: {
        "id": 5,
        "title": "Create frontend interface",
        "description": "Build simple HTML interface for managing tasks",
        "completed": False,
        "priority": "low",
        "created_at": "2026-04-03",
        "due_date": "2026-04-10",
        "tags": ["frontend", "ui"],
        "user_id": 1,
    },
}


# GET -- Retrieve all tasks
# Returns a list of all tasks stored in the in-memory database
@app.get("/tasks")
async def get_all_tasks() -> list[dict[str, Any]]:
    # Convert dictionary values to a list so it can be returned as JSON
    return list(tasks_db.values())


# GET -- Retrieve a single task by ID
@app.get("/tasks/{task_id}")
async def get_task(task_id: int) -> dict[str, Any]:

    # Validate that the requested task exists
    if task_id not in tasks_db:
        # If the task does not exist, return HTTP 404
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found",
        )

    # Return the requested task
    return tasks_db[task_id]


# POST -- Create a new task
# Generates an ID automatically and stores the task in the database
@app.post("/tasks", status_code=status.HTTP_201_CREATED)
async def post_new_task(
    title: str,
    description: str,
    priority: str,
    due_date: str,
    tags: list[str],
    user_id: int,
) -> dict[str, Any]:

    # Generate a new task ID
    # If the database is empty, start with ID = 1
    if not tasks_db:
        new_task_id = 1
    else:
        # Otherwise take the highest ID and increment it
        new_task_id = max(tasks_db.keys()) + 1

    # Create the new task object
    tasks_db[new_task_id] = {
        "id": new_task_id,
        "title": title,
        "description": description,
        "completed": False,  # Tasks start as not completed
        "priority": priority,
        "created_at": date.today().isoformat(),  # Automatically set creation date
        "due_date": due_date,
        "tags": tags,
        "user_id": user_id,
    }

    # Return the created task with HTTP 201
    return tasks_db[new_task_id]


# Scalar documentation
@app.get("/scalar", include_in_schema=False)
async def scalar_html():
    return get_scalar_api_reference(
        # Your OpenAPI document
        openapi_url=app.openapi_url,
        # Avoid CORS issues (optional)
        scalar_proxy_url="https://proxy.scalar.com",
    )
