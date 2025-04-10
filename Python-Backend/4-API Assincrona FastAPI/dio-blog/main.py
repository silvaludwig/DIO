from fastapi import FastAPI
from datetime import datetime, UTC


app = FastAPI()

fake_db = [
    {'title': 'Creating an application using Django', 'date': datetime.now(UTC), 'published': True},
    {'title': 'Creating an application using Flask', 'date': datetime.now(UTC), 'published': True},
    {'title': 'Creating an application using FastAPI', 'date': datetime.now(UTC), 'published': True},
    {'title': 'Creating an application using Starlett', 'date': datetime.now(UTC), 'published': False},
]

@app.get('/posts')
def read_posts(published: bool, skip: int = 0, limit: int = len(fake_db)):
    return [post for post in fake_db[skip: skip + limit] if post['published'] is published]


@app.get('/posts/{framework}')
def read_framework_posts(framework: str):
    return ...
