from fastapi import FastAPI

from app.api.root import router as root_router

app = FastAPI(
    title="AI Developer Assistant",
    description="Production-ready AI Backend",
    version="1.0.0",
)

# Register Routes
app.include_router(root_router)