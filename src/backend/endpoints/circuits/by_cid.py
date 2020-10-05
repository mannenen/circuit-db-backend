from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.endpoints import HTTPEndpoint
from starlette.exceptions import HTTPException


class CIDEndpoint(HTTPEndpoint):
    async def get(self, request: Request):
        cid = request.path_params["cid"]
        circuit = request.app.state.db.get_circuit_by_cid(cid)

        if circuit is None:
            raise HTTPException(status_code=404, detail=f"could not find circuit with CID {cid}")

        return JSONResponse(content=circuit, status_code=200)

    async def delete(self, request: Request):
        cid = request.path_params["cid"]

        result = request.app.state.db.delete_circuit_by_cid(cid)

        if not result:
            raise HTTPException(status_code=404, detail=f"could not find circuit with CID {cid}")

        return JSONResponse(content=None, status_code=204)

    async def patch(self, request: Request):
        cid = request.path_params["cid"]
        updates = await request.json()

        if "cid" in updates.keys():
            raise HTTPException(status_code=403, detail="Forbidden to change CID of existing circuit, create a new circuit instead")
        
        updated = request.app.state.db.update_circuit_by_cid(cid, updates)
        if updated is None:
            raise HTTPException(status_code=404, detail=f"could not find circuit with CID {cid}")

        return JSONResponse(content=updated, status_code=200)
