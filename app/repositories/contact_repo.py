from sqlmodel.ext.asyncio.session import AsyncSession
from app.models import Contact


class ContactRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_id(self, contact_id: int) -> Contact | None:
        return await self.session.get(Contact, contact_id)

    async def update(self, contact_id: int, name: str, email: str) -> Contact | None:
        contact = await self.session.get(Contact, contact_id)
        if contact:
            contact.name = name
            contact.email = email
            self.session.add(contact)
            await self.session.commit()
            await self.session.refresh(contact)
        return contact
