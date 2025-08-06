from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return 'This is Saidaiwik'

@app.get("/about")
def about():
    return "This page will be about me"