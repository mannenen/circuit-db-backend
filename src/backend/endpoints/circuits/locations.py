from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.endpoints import HTTPEndpoint


class ALocationEndpoint(HTTPEndpoint):
    async def get(self, request: Request):
        pass


class ZLocationEndpoint(HTTPEndpoint):
    async def get(self, request: Request):
        pass
