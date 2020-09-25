from starlette.routing import Route

from .get import all_circuits, circuit_by_cid, circuit_provider, get_customers, a_location, z_location
from .post import add_circuit, add_customers, add_a_location, add_z_location
from .put import edit_provider, edit_customers, edit_a_location, edit_z_location
from .delete import delete_circuit


__get_routes__ = [
    Route('/circuits', all_circuits, methods=["GET"]),
    Route('/circuits/{cid}', circuit_by_cid, methods=["GET"]),
    Route('/circuits/{cid}/provider', circuit_provider, methods=["GET"]),
    Route('/circuits/{cid}/customers', get_customers, methods=["GET"]),
    Route('/circuits/{cid}/a', a_location, methods=["GET"]),
    Route('/circuits/{cid}/z', z_location, methods=["GET"])
]

__post_routes__ = [
    Route('/circuits', add_circuit, methods=["POST"]),
    Route('/circuits/{cid}/customers', add_customers, methods=["POST"]),
    Route('/circuits/{cid}/a', add_a_location, methods=["POST"]),
    Route('/circuits/{cid}/z', add_z_location, methods=["POST"])
]

__put_routes__ = [
    Route('/circuits/{cid}/provider', edit_provider, methods=["PUT"]),
    Route('/circuits/{cid}/customers', edit_customers, methods=["PUT"]),
    Route('/circuits/{cid}/a', edit_a_location, methods=["PUT"]),
    Route('/circuits/{cid}/z', edit_z_location, methods=["PUT"])
]

__delete_routes__ = [
    Route('/circuits/{cid}', delete_circuit, methods=["DELETE"]),
]

circuit_routes = __get_routes__ + __post_routes__ + __put_routes__ + __delete_routes__
