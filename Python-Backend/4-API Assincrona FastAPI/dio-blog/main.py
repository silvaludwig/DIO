from fastapi import FastAPI
from datetime import datetime, UTC


app = FastAPI()


@app.get('/posts/{framework}')
def read_posts(framework: str):
    return {
        "posts": [
            {'title': f'Creating an application using {framework}', 'date': datetime.now(UTC)},
            {'title': f'Internationalizing an application using {framework}', 'date': datetime.now(UTC)},
        ]
    }
