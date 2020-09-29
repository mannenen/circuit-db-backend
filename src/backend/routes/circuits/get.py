from starlette.requests import Request
from starlette.responses import JSONResponse


def all_circuits(request: Request):
    circuit_list = request.app.state.db.get_all_circuits()

    return JSONResponse(content=circuit_list, status_code=200, media_type="application/json")


def circuit_by_cid(request: Request):
    pass


def circuit_provider(request: Request):
    pass


def get_customers(request: Request):
    pass


def a_location(request: Request):
    pass


def z_location(request: Request):
    pass
