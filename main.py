from fastapi import FastAPI
from typing import Optional # this is for query parameter purpose
from pydantic import BaseModel # this is for POST operation in API
import uvicorn

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

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool] = None


@app.post("/blog")
def create_blog(blog: Blog):
    return {'data' : f"Blog is created with title called {blog.title}"}

# For debugging purpose uncomment these lines when you are debugging
# if __name__ == "__main__":
#     uvicorn.run(app,host="127.0.0.1",port=9000)
