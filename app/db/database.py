from sqlmodel import SQLModel, create_engine, Session
from ..core.config import settings

# Create Engine
engine = create_engine(settings.DATABASE_URL, connect_args={"check_same_thread": False})

def init_db():
    SQLModel.metadata.create_all(engine)
    
    # Seed data
    from ..models import Contact
    with Session(engine) as session:
        existing_contact = session.get(Contact, 1)
        if not existing_contact:
            contact = Contact(id=1, name="Jane Doe", email="jane@sqlite.org")
            session.add(contact)
            session.commit()
def get_session():
    with Session(engine) as session:
        yield session