from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.endpoints import HTTPEndpoint


class CircuitProvider(HTTPEndpoint):
    async def get(self, request: Request):
        pass
