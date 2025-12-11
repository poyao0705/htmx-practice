from sqlmodel import Session, select
from ..models import Contact

class ContactRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, contact_id: int) -> Contact | None:
        return self.session.get(Contact, contact_id)

    def update(self, contact_id: int, name: str, email: str) -> Contact | None:
        contact = self.session.get(Contact, contact_id)
        if contact:
            contact.name = name
            contact.email = email
            self.session.add(contact)
            self.session.commit()
            self.session.refresh(contact)
        return contact