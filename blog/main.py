from fastapi import FastAPI
from . import scehemas
from . import models
from .database import engine

app = FastAPI()

models.Base.metadata.create_all(engine)


@app.post("/blog")
def create(request: scehemas.Blog):
    # return {'title': request.title,'body' : request.body}
    return request
