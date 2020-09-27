from starlette.routing import Mount

from backend.routes.circuits import circuit_routes


application_routes = [
    Mount('/api/v1/circuits', routes=circuit_routes)
]
