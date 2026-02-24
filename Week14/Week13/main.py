from fastapi import FastAPI
from routes import users

# --- FastAPI App Initialization ---
app = FastAPI(
    title="User Management API",
    description="FastAPI backend for managing users",
    version="1.0.0",
)

# --- Include Routers ---
app.include_router(users.router, prefix="/users", tags=["Users"])

# --- Health Check Endpoints ---
@app.get("/", tags=["Health"])
@app.get("/health", tags=["Health"])
async def read_root():
    """
    Health check endpoint to confirm the API is running.
    """
    return {"status": "healthy", "message": "API is running"}
