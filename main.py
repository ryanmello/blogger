from fastapi import *

app = FastAPI()

@app.get("/")
def root():
    return { "message" : "Hello World" }

@app.post("/posts")
def create_posts(payload: dict = Body(...)):
    print(payload)
    return { "message" : "Post created!" }
