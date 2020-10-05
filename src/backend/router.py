from starlette.routing import Mount

from backend.endpoints import routes


application_routes = [
    Mount('/api/v1', routes=routes)
]
