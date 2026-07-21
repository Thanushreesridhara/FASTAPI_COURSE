import asyncio
import os
import sys
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import text

if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
print(DATABASE_URL)

async def test_connection():
    engine = create_async_engine(
    DATABASE_URL,
    echo=True,
    connect_args={"ssl": "require"})
    async with engine.connect() as conn:
        result = await conn.execute(text("SELECT 1"))
        print("✅ Connection successful:", result.scalar())

asyncio.run(test_connection())