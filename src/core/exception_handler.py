from fastapi import FastAPI
from starlette.responses import JSONResponse
from src.core.exception import (
    ServerErrorException,
    ResourceNotFoundException,
    UnauthorizedBehaviorException,
)


def add_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(ResourceNotFoundException)
    async def handle_resource_not_found_exception(request, exc):
        return JSONResponse(content={"error": "Resource not found", "detail": str(exc)}, status_code=exc.status_code)

    @app.exception_handler(UnauthorizedBehaviorException)
    async def handle_unauthorized_exception(request, exc):
        return JSONResponse(content={"error": "Unauthorized", "detail": str(exc)}, status_code=exc.status_code)

    @app.exception_handler(ServerErrorException)
    async def handle_server_error_exception(request, exc):
        return JSONResponse(content={"error": "Internal server error", "detail": str(exc)}, status_code=exc.status_code)
    