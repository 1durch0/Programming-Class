from typing import List
from fastapi import APIRouter, HTTPException, Query
from schema import User, UserCreate
from user_store import UserStore

# --- Router and Store Initialization ---
router = APIRouter()
# The store is initialized with the path to the SQLite database file.
# The UserStore class will handle creating the file and table if they don't exist.
store = UserStore("users.db")

# --- API Endpoints ---

@router.post("/", response_model=User, status_code=201)
async def create_user(user_in: UserCreate):
    """
    Creates a new user and saves it to the database.
    """
    new_user = store.add_user(user_in.dict())
    if new_user is None:
        raise HTTPException(status_code=400, detail="Email already exists.")
    return new_user

@router.get("/", response_model=List[User])
async def get_all_users():
    """
    Retrieves all users from the database.
    """
    return store.load()

@router.get("/search", response_model=List[User])
async def search_users(q: str = Query(..., min_length=1, description="Search term for user names")):
    """
    Searches for users by name using a case-insensitive LIKE query.
    """
    return store.search_by_name(q)

@router.get("/{user_id}", response_model=User)
async def get_user_by_id(user_id: int):
    """
    Retrieves a single user by their ID.
    """
    user = store.find_by_id(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{user_id}", response_model=User)
async def update_user(user_id: int, user_update: UserCreate):
    """
    Updates an existing user's information in the database.
    """
    if not store.update_user(user_id, user_update.dict()):
        raise HTTPException(status_code=404, detail="User not found")
    
    updated_user_data = store.find_by_id(user_id)
    if updated_user_data is None:
        raise HTTPException(status_code=404, detail="User not found after update")
    return updated_user_data


@router.delete("/{user_id}", status_code=204)
async def delete_user(user_id: int):
    """
    Deletes a user from the database by their ID.
    """
    if not store.delete_user(user_id):
        raise HTTPException(status_code=404, detail="User not found")
    return

