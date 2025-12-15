from fastapi import HTTPException
from app.repositories.contact_repo import ContactRepository


class ContactService:
    def __init__(self, repo: ContactRepository):
        self.repo = repo

    async def get_contact_for_display(self, contact_id: int):
        contact = await self.repo.get_by_id(contact_id)
        if not contact:
            raise HTTPException(status_code=404, detail="Contact not found")
        return contact

    async def update_contact_details(self, contact_id: int, name: str, email: str):
        # --- BUSINESS LOGIC HERE ---
        # 1. Sanitize inputs
        clean_name = name.strip()
        clean_email = email.lower().strip()

        # 2. Validation (Example)
        if "@" not in clean_email:
            raise HTTPException(status_code=400, detail="Invalid email format")

        # 3. Call Repository to save
        return await self.repo.update(contact_id, clean_name, clean_email)
