import json
import os
from typing import List
from fastapi import APIRouter, HTTPException, Query
from schema import User, UserCreate

# --- Configuration ---
DATA_FILE = "users.txt"

# --- APIRouter Initialization ---
router = APIRouter()

# --- Data Persistence Helper Functions ---

def read_users() -> List[dict]:
    """
    Reads the list of users from the data file.
    Returns an empty list if the file doesn't exist or is empty.
    """
    if not os.path.exists(DATA_FILE) or os.path.getsize(DATA_FILE) == 0:
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def write_users(users: List[dict]):
    """
    Writes the list of users to the data file, overwriting existing content.
    """
    with open(DATA_FILE, "w") as f:
        json.dump(users, f, indent=4)

def get_next_id(users: List[dict]) -> int:
    """
    Calculates the next available user ID.
    """
    return max([user['id'] for user in users]) + 1 if users else 1

# --- API Endpoints ---

@router.post("/", response_model=User, status_code=201)
async def create_user(user_in: UserCreate):
    """
    Creates a new user and saves it to the database.
    """
    users = read_users()
    new_user = User(id=get_next_id(users), **user_in.dict())
    users.append(new_user.dict())
    write_users(users)
    return new_user

@router.get("/", response_model=List[User])
async def get_all_users():
    """
    Retrieves all users from the database.
    """
    return read_users()

@router.get("/search", response_model=List[User])
async def search_users(q: str = Query(..., min_length=1, description="Search term for user names")):
    """
    Searches for users by name (case-insensitive).
    """
    users = read_users()
    results = [user for user in users if q.lower() in user['name'].lower()]
    return results

@router.get("/{user_id}", response_model=User)
async def get_user_by_id(user_id: int):
    """
    Retrieves a single user by their ID.
    """
    users = read_users()
    user = next((user for user in users if user['id'] == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{user_id}", response_model=User)
async def update_user(user_id: int, user_update: UserCreate):
    """
    Updates an existing user's information.
    """
    users = read_users()
    user_index = -1
    for i, user in enumerate(users):
        if user['id'] == user_id:
            user_index = i
            break

    if user_index == -1:
        raise HTTPException(status_code=404, detail="User not found")

    updated_user = users[user_index].copy()
    updated_user.update(user_update.dict())
    users[user_index] = updated_user
    write_users(users)
    return updated_user

@router.delete("/{user_id}", status_code=204)
async def delete_user(user_id: int):
    """
    Deletes a user from the database by their ID.
    """
    users = read_users()
    original_count = len(users)
    users_to_keep = [user for user in users if user['id'] != user_id]

    if len(users_to_keep) == original_count:
        raise HTTPException(status_code=404, detail="User not found")

    write_users(users_to_keep)
    return
