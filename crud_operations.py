from fastapi import FastAPI,status
from pydantic import BaseModel
from typing import List
from fastapi.exceptions import HTTPException

app = FastAPI()


books = [
    {
        "id": 1,
        "title": "Think Python",
        "author": "Allen B. Downey",
        "publisher": "O'Reilly Media",
        "published_date": "2021-01-01",
        "page_count": 1234,
        "language": "English",
    },
    
    {
    "id": 2,
    "title": "Automate the Boring Stuff with Python",
    "author": "Al Sweigart",
    "publisher": "No Starch Press",
    "published_date": "2019-11-12",
    "page_count": 592,
    "language": "English",
    },
{
    "id": 3,
    "title": "Fluent Python",
    "author": "Luciano Ramalho",
    "publisher": "O'Reilly Media",
    "published_date": "2022-04-26",
    "page_count": 1012,
    "language": "English",
},
{
    "id": 4,
    "title": "Clean Code",
    "author": "Robert C. Martin",
    "publisher": "Prentice Hall",
    "published_date": "2008-08-01",
    "page_count": 464,
    "language": "English",
},
{
    "id": 5,
    "title": "Designing Data-Intensive Applications",
    "author": "Martin Kleppmann",
    "publisher": "O'Reilly Media",
    "published_date": "2017-03-16",
    "page_count": 616,
    "language": "English",
},
{
    "id": 6,
    "title": "Deep Learning with Python",
    "author": "François Chollet",
    "publisher": "Manning Publications",
    "published_date": "2021-12-21",
    "page_count": 504,
    "language": "English",
}, 
]



class Book(BaseModel):
        id: int
        title: str
        author: str
        publisher: str
        published_date: str
        page_count: int
        language: str
        
class BookUpdateModel(BaseModel):
        title: str
        author: str
        publisher: str
        page_count: int
        language: str

@app.get('/books',response_model=List[Book])
async def get_all_books():
    return books

@app.post('/books',status_code=status.HTTP_201_CREATED) #using fastapi status module to create http status 
async def create_a_book(book_data:Book) -> dict:
    new_book = book_data.model_dump() # model dump is used to convert the data to dict
    books.append(new_book)
    return new_book

@app.get('/books/{book_id}')
async def get_book(book_id:int) -> dict:
    for book in books:
        if book['id'] == book_id:
            return book
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Book not found")

@app.patch('/books/{book_id}')
async def update_book(book_id:int,book_update:BookUpdateModel) -> dict:
    for book in books:
        if book['id'] == book_id:
            book['title'] = book_update.title
            book['author'] = book_update.author
            book['publisher'] = book_update.publisher
            book['page_count'] = book_update.page_count
            book['language'] = book_update.language
            
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="book not found") 
            

@app.delete('/books/{book_id}',status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id:int):
    for book in books:
        if book['id'] == book_id:
            books.remove(book)
    
            return {}
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="book not found")