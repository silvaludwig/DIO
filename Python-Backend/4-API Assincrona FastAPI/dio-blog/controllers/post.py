from typing import Annotated
from fastapi import Cookie, Header, Response, status, APIRouter
from datetime import datetime, UTC
from schemas.post import PostIn
from views.post import PostOut


router = APIRouter(prefix="/posts")

fake_db = [
    {'title': 'Creating an application using Django', 'date': datetime.now(UTC), 'published': True},
    {'title': 'Creating an application using Flask', 'date': datetime.now(UTC), 'published': True},
    {'title': 'Creating an application using FastAPI', 'date': datetime.now(UTC), 'published': True},
    {'title': 'Creating an application using Starlett', 'date': datetime.now(UTC), 'published': False},
]


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=PostOut)
def create_post(post: PostIn):
    fake_db.append(post.model_dump())
    return post


@router.get('/', response_model=list[PostOut])
def read_posts(
    response: Response, 
    published: bool,
    limit: int,
    skip: int = 0,
    ads_id: Annotated[str | None, Cookie()] = None,
    user_agent: Annotated[str | None, Header()] = None,
):
    response.set_cookie(key="user", value="user@email.com")
    print(f"Cookie: {ads_id}")
    print(f"User-Agent: {user_agent}")
    return [post for post in fake_db[skip: skip + limit] if post['published'] is published]


@router.get('/{framework}', response_model=PostOut)
def read_framework_posts(framework: str):
    return {
        "posts": [
            {"title": f"criando uma app com {framework}", "date": datetime.now(UTS)},
            {"title": f"criando uma app com {framework}", "date": datetime.now(UTS)},
        ]
    }
