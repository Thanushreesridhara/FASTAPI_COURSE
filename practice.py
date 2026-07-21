from fastapi import FastAPI, Header
from typing import Optional
from pydantic import BaseModel


app1 = FastAPI()

@app1.get('/')
async def read_root():
    return {"message":"Hello World"}

# When a function parameter is NOT part of the URL path (no {name} in the route),
# FastAPI treats it as a QUERY PARAMETER instead.
# That means it must be passed like: /greet?name=thanu
# instead of like a path param: /greet/thanu

@app1.get('/greet')
async def greet_name(name: str) -> dict:
    return {"message": f"Hello {name}"}


# Compare this to a PATH parameter version below —
# here {name} is explicitly part of the URL, so FastAPI expects it in the path itself.

@app1.get('/greet/{name}')
async def greet_name_path(name: str) -> dict:
    return {"message": f"Hello {name}"}

#demonstrating both path parameters and query parameters together

@app1.get('/hello/{name}')
async def name_age_path(name: str,age: int) -> dict:
    return {"message": f"Hello i am {name} and i am {age} years old"}

#demonstrating optional parameters
# use & to provide two values like /hi?name=xxx&age=xx

@app1.get('/hi')
async def opt_name_path(name: Optional[str] = "User",age: int = 0) -> dict:
    return {"message": f"Hello i am {name} and i am {age} years old"}

#creating body along with pydantic model validation
class BookCreateModel(BaseModel):
    title : str
    author : str

@app1.post('/create_book')
async def create_book(book_data:BookCreateModel):
    return{
        "title" : book_data.title,
        "author" : book_data.author
    }
    
@app1.get('/get_headers')
async def get_headers(
    accept:str = Header(None),
    content_type: str = Header(None),
    user_agent:str = Header(None),
    host:str = Header(None),
    accept_encoding: str = Header(None),
    server: str = Header(None)
):
    request_headers ={}
    
    request_headers["Accept"] = accept
    request_headers["Content-type"] = content_type
    request_headers["User-Agent"] = user_agent
    request_headers["Host"] = host
    request_headers["Accept-Encoding"]= accept_encoding
    request_headers["server"]= server
    return request_headers