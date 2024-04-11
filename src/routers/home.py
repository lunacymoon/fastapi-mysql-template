from fastapi import APIRouter

from src.settings.router import APIRoute

home_router = APIRouter(route_class=APIRoute)


@home_router.get('/health')
async def test():
    return {'message': 'hello world'}  # for testing purpose
