from typing import Optional
from sqlmodel import SQLModel, Field
from pydantic import EmailStr

class ContactBase(SQLModel):
    name: str
    email: EmailStr

class Contact(ContactBase, table=True):
    __tablename__ = "contacts"
    
    id: Optional[int] = Field(default=None, primary_key=True)

class ContactUpdate(ContactBase):
    pass
