from starlette.routing import Route

from .get import all_circuits, circuit_by_cid, circuit_provider, get_customers, a_location, z_location
from .post import add_circuit, add_customers, add_a_location, add_z_location
from .put import edit_provider, edit_customers, edit_a_location, edit_z_location
from .delete import delete_circuit


__get_routes__ = [
    Route('/', all_circuits, methods=["GET"]),
    Route('/{cid}', circuit_by_cid, methods=["GET"]),
    Route('/{cid}/provider', circuit_provider, methods=["GET"]),
    Route('/{cid}/customers', get_customers, methods=["GET"]),
    Route('/{cid}/a', a_location, methods=["GET"]),
    Route('/{cid}/z', z_location, methods=["GET"])
]

__post_routes__ = [
    Route('/', add_circuit, methods=["POST"]),
    Route('/{cid}/customers', add_customers, methods=["POST"]),
    Route('/{cid}/a', add_a_location, methods=["POST"]),
    Route('/{cid}/z', add_z_location, methods=["POST"])
]

__put_routes__ = [
    Route('/{cid}/provider', edit_provider, methods=["PUT"]),
    Route('/{cid}/customers', edit_customers, methods=["PUT"]),
    Route('/{cid}/a', edit_a_location, methods=["PUT"]),
    Route('/{cid}/z', edit_z_location, methods=["PUT"])
]

__delete_routes__ = [
    Route('/{cid}', delete_circuit, methods=["DELETE"]),
]

circuit_routes = __get_routes__ + __post_routes__ + __put_routes__ + __delete_routes__
