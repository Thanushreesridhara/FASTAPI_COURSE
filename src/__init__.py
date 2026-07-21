from fastapi import FastAPI
from src.books.routes import book_router
from contextlib import asynccontextmanager

version = "v2"
app = FastAPI(
    title="Bookly",
    description="A REST API for a boon review web service"
)


app.include_router(book_router, prefix=f"/api/{version}/books", tags=['books'])