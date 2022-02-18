from fastapi import FastAPI


from app.routes.api import router
from app.database import init_db


def init_application() -> FastAPI:
    app = FastAPI(
        title="myapp",
        description="my application",
        version="1.0",
    )
    app.include_router(router, prefix="/api")
    return app


app = init_application()


@app.on_event("startup")
async def startup_event():
    print("Starting up...")
    init_db()


@app.on_event("shutdown")
def shutdown_event():
    print("Shutting down...")
