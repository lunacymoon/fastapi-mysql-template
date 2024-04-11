import uvicorn

from src import create_app
from src.settings import settings
from src.core.exception_handler import add_exception_handlers

app = create_app()
add_exception_handlers(app)


if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host=settings.HOST,
        port=settings.PORT,
        app_dir='app',
    )
