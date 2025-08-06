from fastapi import FastAPI
from typing import Optional

app = FastAPI() # This is an instance of the FastAPI Class

# Get is an operation in API
@app.get("/blog")
def index(limit: int=10, published: bool=True, sort: Optional[str] = None):
    # only get 10 published blogs
    if published:
        return {"data" : f'{limit} published blog list from db'}
    else:
        return {"data" : f"{limit} blog list from db"}

@app.get("/blog/unpublished")
def unpublished():
    return {"data" : "All Unpublished blogs are here"}

@app.get("/blog/{id}")
def show(id: int): # you can use data type as you need like int, float, string
    return {"data" : id}


@app.get("/blog/{id}/comments")
def comments(id):
    return {"data" : {'1','2'}}
