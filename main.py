from fastapi import *
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: int | None = None

my_posts: dict[Post] = []

@app.get("/posts")
def root():
    return my_posts

@app.post("/posts")
def create_posts(post: Post):
    my_posts.append(post)
    return post
