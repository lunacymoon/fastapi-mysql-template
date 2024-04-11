from fastapi import FastAPI
from src.settings import settings
from src.settings.logger import make_logger


def create_app():
    app = FastAPI()
    make_logger(settings.REGION_NAME)

    # List Routers Here!
    from src.routers.home import home_router

    app.include_router(home_router, prefix=f'/{settings.SERVICE_NAME}')

    return app
