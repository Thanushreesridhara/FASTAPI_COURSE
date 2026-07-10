from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get('/')
async def read_root():
    return {"message":"Hello World"}

# When a function parameter is NOT part of the URL path (no {name} in the route),
# FastAPI treats it as a QUERY PARAMETER instead.
# That means it must be passed like: /greet?name=thanu
# instead of like a path param: /greet/thanu

@app.get('/greet')
async def greet_name(name: str) -> dict:
    return {"message": f"Hello {name}"}


# Compare this to a PATH parameter version below —
# here {name} is explicitly part of the URL, so FastAPI expects it in the path itself.

@app.get('/greet/{name}')
async def greet_name_path(name: str) -> dict:
    return {"message": f"Hello {name}"}

#demonstrating both path parameters and query parameters together

@app.get('/hello/{name}')
async def name_age_path(name: str,age: int) -> dict:
    return {"message": f"Hello i am {name} and i am {age} years old"}

#demonstrating optional parameters
# use & to provide two values like /hi?name=xxx&age=xx

@app.get('/hi')
async def opt_name_path(name: Optional[str] = "User",age: int = 0) -> dict:
    return {"message": f"Hello i am {name} and i am {age} years old"}