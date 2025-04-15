from fastapi import *
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def root():
    return { "message" : "Hello World" }

class Post(BaseModel):
    title: str
    content: str

@app.post("/posts")
def create_posts(payload: Post):
    print(payload)
    return payload
