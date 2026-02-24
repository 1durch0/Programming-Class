from pydantic import BaseModel

# --- Pydantic Models ---
class UserCreate(BaseModel):
    """
    Schema for creating a new user.
    Requires name and email.
    """
    name: str
    email: str

class User(UserCreate):
    """
    Schema representing a complete user object, including the generated ID.
    """
    id: int
