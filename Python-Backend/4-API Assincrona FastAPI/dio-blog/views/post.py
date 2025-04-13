from pydantic import BaseModel
from datetime import datetime


class PostOut(BaseModel):
    id: int
    title: str
    content: str
    publised_at: datetime | None = None
    # author: str
    # published: datetime
 