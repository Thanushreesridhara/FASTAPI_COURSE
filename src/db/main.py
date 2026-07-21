from sqlmodel import create_engine
from sqlalchemy.ext.asyncio import AsyncEngine
from src.config import Config


engine = AsyncEngine(
    create_engine(
    url=Config.DATABASE_URL,
    echo=True # SQLAlchemy prints out the actual raw SQL it's running behind the scenes, every time you do a query.
)
)