from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.exceptions import HTTPException
from starlette.endpoints import HTTPEndpoint


class CircuitCollection(HTTPEndpoint):
    async def get(self, request: Request):
        circuit_list = request.app.state.db.get_all_circuits()

        return JSONResponse(content=circuit_list, status_code=200, media_type="application/json")

    async def post(self, request: Request):
        data: dict = await request.json()

        missing = []
        if "cid" not in data.keys():
            missing.append('circuit ID')
        if "provider" not in data.keys():
            missing.append('provider')

        if len(missing) > 0:
            missing_fields = ', '.join(missing)
            raise HTTPException(status_code=400, detail=f"Missing {missing_fields}")

        added = request.app.state.db.add_circuit(data)
        return JSONResponse(content=added, status_code=201)
