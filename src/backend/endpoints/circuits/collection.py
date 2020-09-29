from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.endpoints import HTTPEndpoint


class CircuitCollection(HTTPEndpoint):
    async def get(self, request: Request):
        circuit_list = request.app.state.db.get_all_circuits()

        return JSONResponse(content=circuit_list, status_code=200, media_type="application/json")
