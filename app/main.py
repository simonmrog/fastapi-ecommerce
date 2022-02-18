from fastapi import FastAPI

from app.routes.api import router


def init_application() -> FastAPI:
    app = FastAPI(
        title="myapp",
        description="my application",
        version="1.0",
    )
    app.include_router(router, prefix="/api")
    return app


app = init_application()
