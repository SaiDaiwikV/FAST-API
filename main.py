from fastapi import FastAPI

app = FastAPI() # This is an instance of the FastAPI Class

# Get is an operation in API
@app.get("/")
def index():
    return {"data" : 'blog list'}

@app.get("/blog/{id}")
def show(id):
    return {"data" : id}

