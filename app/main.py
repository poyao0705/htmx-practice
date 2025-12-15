from contextlib import asynccontextmanager
from fastapi import FastAPI
from .routers import contacts
from .db import database
from .models import Contact  # Ensure models are registered


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize DB on startup
    await database.init_db()
    yield


app = FastAPI(lifespan=lifespan)

# Include the router
app.include_router(contacts.router)
