from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json
import os
from typing import List, Optional

# --- Configuration ---
DATA_FILE = "tasks.txt"

# --- Pydantic Models ---
class TaskCreate(BaseModel):
    title: str
    description: str | None = None

class Task(TaskCreate):
    id: int
    completed: bool = False

# --- Data Persistence ---
def load_tasks() -> List[dict]:
    """
    Loads tasks from the data file.
    Returns an empty list if the file doesn't exist.
    """
    if not os.path.exists(DATA_FILE):
        return []
    tasks = []
    with open(DATA_FILE, "r") as f:
        for line in f:
            if line.strip():
                tasks.append(json.loads(line))
    return tasks

def save_tasks(tasks: List[dict]):
    """
    Saves a list of tasks to the data file, overwriting existing content.
    """
    with open(DATA_FILE, "w") as f:
        for task in tasks:
            f.write(json.dumps(task) + "\n")

# --- FastAPI App ---
app = FastAPI(
    title="Task Management API",
    description="A simple FastAPI application to manage tasks with persistence in a text file.",
    version="1.0.0",
)

# --- CORS Middleware ---
# This is crucial for allowing the React frontend to communicate with the backend.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# --- Helper function to find a task ---
def find_task_by_id(task_id: int, tasks: List[dict]):
    """Helper to find a task by its ID."""
    for task in tasks:
        if task['id'] == task_id:
            return task
    return None

# --- API Endpoints ---
@app.get("/")
async def read_root():
    """Confirms the API is running."""
    return {"message": "Welcome to the Task Management API!"}

@app.get("/tasks", response_model=List[Task])
async def get_tasks(completed: Optional[bool] = None):
    """
    Retrieves all tasks, with an optional filter for completion status.
    """
    tasks = load_tasks()
    if completed is not None:
        return [task for task in tasks if task['completed'] == completed]
    return tasks

@app.get("/tasks/stats")
async def get_task_stats():
    """
    Returns a summary of task statistics.
    """
    tasks = load_tasks()
    total_tasks = len(tasks)
    if total_tasks == 0:
        return {
            "total_tasks": 0,
            "completed_count": 0,
            "pending_count": 0,
            "completion_percentage": 0.0,
        }

    completed_count = sum(1 for task in tasks if task['completed'])
    pending_count = total_tasks - completed_count
    completion_percentage = (completed_count / total_tasks) * 100 if total_tasks > 0 else 0

    return {
        "total_tasks": total_tasks,
        "completed_count": completed_count,
        "pending_count": pending_count,
        "completion_percentage": round(completion_percentage, 2),
    }

@app.get("/tasks/{task_id}", response_model=Task)
async def get_task(task_id: int):
    """
    Retrieves a single task by its ID.
    """
    tasks = load_tasks()
    task = find_task_by_id(task_id, tasks)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.post("/tasks", response_model=Task, status_code=201)
async def create_task(task_in: TaskCreate):
    """
    Adds a new task.
    """
    tasks = load_tasks()
    new_id = max([t['id'] for t in tasks]) + 1 if tasks else 1
    new_task = Task(id=new_id, **task_in.dict())
    tasks.append(new_task.dict())
    save_tasks(tasks)
    return new_task

@app.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: int, task_update: TaskCreate):
    """
    Modifies an existing task completely.
    """
    tasks = load_tasks()
    task_index = -1
    for i, task in enumerate(tasks):
        if task['id'] == task_id:
            task_index = i
            break

    if task_index == -1:
        raise HTTPException(status_code=404, detail="Task not found")

    # Keep the original completed status unless specified otherwise
    # In a full PUT, the client should provide the full representation.
    # We assume here they only provide title/description.
    updated_task_data = task_update.model_dump()
    updated_task = tasks[task_index].copy()
    updated_task.update(updated_task_data)


    tasks[task_index] = updated_task
    save_tasks(tasks)
    return updated_task

@app.delete("/tasks/{task_id}", status_code=204)
async def delete_task(task_id: int):
    """
    Removes a single task from storage.
    """
    tasks = load_tasks()
    original_count = len(tasks)
    tasks_to_keep = [task for task in tasks if task['id'] != task_id]

    if len(tasks_to_keep) == original_count:
        raise HTTPException(status_code=404, detail="Task not found")

    save_tasks(tasks_to_keep)
    return

@app.delete("/tasks", status_code=204)
async def delete_all_tasks():
    """
    Removes all tasks from storage.
    """
    if os.path.exists(DATA_FILE):
        save_tasks([])
    return

# To run this application:
# 1. Make sure you have FastAPI and Uvicorn installed:
#    pip install fastapi "uvicorn[standard]"
# 2. Save this code as main.py in your project directory.
# 3. Run the application from your terminal:
#    uvicorn main:app --reload
# 4. Access the API documentation at http://127.0.0.1:8000/docs
