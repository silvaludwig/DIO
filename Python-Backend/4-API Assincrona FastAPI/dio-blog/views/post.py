from pydantic import BaseModel
from datetime import datetime


class PostOut(BaseModel):
    title: str
    content: str
    publised_at: datetime | None
    # author: str
    # published: datetime
