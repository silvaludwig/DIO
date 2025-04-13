from contextlib import asynccontextmanager
from fastapi import FastAPI
from controllers import post
from database import database, engine, metadata

@asynccontextmanager
async def lifespan(app: FastAPI):
    from models.post import posts # noqa

    await database.connect()
    metadata.create_all(engine)
    yield
    await database.disconnect()


app = FastAPI(lifespan=lifespan)
app.include_router(post.router)
