from typing import Callable

from fastapi import Request, Response, status
from fastapi.routing import APIRoute as _APIRoute
from starlette.background import BackgroundTask

from src.settings.logger import log_info


class APIRoute(_APIRoute):
    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:
            response = await original_route_handler(request)
            response.background = BackgroundTask(log_info, request, response)
            if response.status_code == status.HTTP_204_NO_CONTENT:
                return Response(status_code=status.HTTP_204_NO_CONTENT)
            return response

        return custom_route_handler
