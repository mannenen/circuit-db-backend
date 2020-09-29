from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.endpoints import HTTPEndpoint


class CIDEndpoint(HTTPEndpoint):
    async def get(self, request: Request):
        cid = request.path_params["cid"]
        circuit = request.app.state.db.get_circuit_by_cid(cid)

        return JSONResponse(content=circuit, status_code=200)
