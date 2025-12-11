from fastapi import APIRouter, Request, Form, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from sqlmodel import Session
from pathlib import Path

from ..db import database
from ..repositories.contact_repo import ContactRepository
from ..services.contact_service import ContactService

router = APIRouter()
BASE_DIR = Path(__file__).resolve().parent.parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

# --- DEPENDENCY INJECTION HELPER ---
def get_service(session: Session = Depends(database.get_session)) -> ContactService:
    """
    Constructs the Service with all its dependencies.
    Router -> Service -> Repository -> DB
    """
    repo = ContactRepository(session)
    return ContactService(repo)

# --- ROUTES ---

@router.get("/", response_class=HTMLResponse)
async def home(request: Request, service: ContactService = Depends(get_service)):
    contact = service.get_contact_for_display(1)
    return templates.TemplateResponse("index.html", {"request": request, "contact": contact})

@router.get("/contact", response_class=HTMLResponse)
async def get_contact_read(request: Request, service: ContactService = Depends(get_service)):
    contact = service.get_contact_for_display(1)
    return templates.TemplateResponse("partials/contact_read.html", {
        "request": request, 
        "contact": contact
    })

@router.get("/contact/edit", response_class=HTMLResponse)
async def get_contact_edit(request: Request, service: ContactService = Depends(get_service)):
    contact = service.get_contact_for_display(1)
    return templates.TemplateResponse("partials/contact_edit.html", {
        "request": request, 
        "contact": contact
    })

@router.put("/contact", response_class=HTMLResponse)
async def update_contact(
    request: Request,
    name: str = Form(...),
    email: str = Form(...),
    service: ContactService = Depends(get_service)
):
    # The router just hands off data to the service
    updated_contact = service.update_contact_details(1, name, email)
    
    return templates.TemplateResponse("partials/contact_read.html", {
        "request": request, 
        "contact": updated_contact
    })