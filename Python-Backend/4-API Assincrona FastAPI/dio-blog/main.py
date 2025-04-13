from fastapi import FastAPI, status
from datetime import datetime, UTC
from pydantic import BaseModel


app = FastAPI()

fake_db = [
    {'title': 'Creating an application using Django', 'date': datetime.now(UTC), 'published': True},
    {'title': 'Creating an application using Flask', 'date': datetime.now(UTC), 'published': True},
    {'title': 'Creating an application using FastAPI', 'date': datetime.now(UTC), 'published': True},
    {'title': 'Creating an application using Starlett', 'date': datetime.now(UTC), 'published': False},
]


class Post(BaseModel):
    title: str
    date: datetime = datetime.now(UTC)
    published: bool = False


@app.post("/posts/", status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    fake_db.append(post.model_dump())
    return post


@app.get('/posts/')
def read_posts(published: bool, limit: int, skip: int = 0):
    return [post for post in fake_db[skip: skip + limit] if post['published'] is published]


@app.get('/posts/{framework}')
def read_framework_posts(framework: str):
    return ...
