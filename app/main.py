from fastapi import FastAPI

from app.routes.api import router


def init_application() -> None:
    app = FastAPI(
        title="myapp",
        description="my application",
        version="1.0",
    )
    app.include_router(router, prefix="/api")


init_application()
