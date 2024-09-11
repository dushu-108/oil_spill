from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import api_router
from contextlib import asynccontextmanager

# Lifespan event handler
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup logic
    print("Starting up...")
    yield
    # Shutdown logic
    print("Shutting down...")

# Create the FastAPI app instance with lifespan context
app = FastAPI(
    title="Oil Spill Detection System",
    description="API for detecting oil spills using satellite data and vessel tracking.",
    version="1.0.0",
    lifespan=lifespan  # Attach the lifespan event handler
)

# Include CORS middleware (optional, but useful for cross-origin requests)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update this to specific domains in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the API routes
app.include_router(api_router)

# Root endpoint to check if the service is running
@app.get("/")
def read_root():
    return {"message": "Welcome to the Oil Spill Detection System"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
