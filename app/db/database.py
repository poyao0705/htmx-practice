from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import SQLModel
from app.core.config import settings

# Seed data
from app.models import Contact

# Create Async Engine
# check_same_thread=False is needed for SQLite, but less critical for async since we are async
engine = create_async_engine(
    settings.DATABASE_URL, echo=True, connect_args={"check_same_thread": False}
)


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

    async with AsyncSession(engine) as session:
        existing_contact = await session.get(Contact, 1)
        if not existing_contact:
            contact = Contact(id=1, name="Jane Doe", email="jane@sqlite.org")
            session.add(contact)
            await session.commit()


async def get_session():
    async with AsyncSession(engine, expire_on_commit=False) as session:
        yield session
