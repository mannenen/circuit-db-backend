from starlette.endpoints import HTTPEndpoint
from starlette.responses import JSONResponse
from starlette.requests import Request


class ProviderCollection(HTTPEndpoint):
    async def get(self, request: Request):
        provider_names = request.app.state.db.get_all_providers()

        result = {
            "providers": provider_names
        }

        return JSONResponse(content=result, status_code=200)
