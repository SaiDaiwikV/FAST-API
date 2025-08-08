from fastapi import FastAPI
from . import scehemas

app = FastAPI()

@app.post("/blog")
def create(request: scehemas.Blog):
    # return {'title': request.title,'body' : request.body}
    return request
