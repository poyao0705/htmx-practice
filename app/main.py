from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from .routers import contacts
from .db import database
from .models import Contact  # Ensure models are registered

app = FastAPI()

# Initialize DB on startup
# We can use a startup event or just call it if we are sure imports are done
database.init_db()

# Include the router
app.include_router(contacts.router)