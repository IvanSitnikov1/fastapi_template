from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from core.config import run_config
from core.models.db_helper import db_helper


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await db_helper.dispose()


app = FastAPI(lifespan=lifespan)

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host=run_config.host,
        port=run_config.port,
        reload=True,
    )
