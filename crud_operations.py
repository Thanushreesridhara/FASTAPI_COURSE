from fastapi import FastAPI

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

@app.get('/books',response_model=)
async def get_all_books():
    return books

@app.post('/books')
async def create_a_book() -> dict:
    pass

@app.get('/book/{book_id}')
async def get_book(book_id:int) -> dict:
    pass

@app.get('/book/{book_id}')
async def update_book(book_id:int) -> dict:
    pass

@app.get('/book/{book_id}')
async def delete_book(book_id:int) -> dict:
    pass