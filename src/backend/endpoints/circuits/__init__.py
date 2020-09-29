from starlette.routing import Route

from .collection import CircuitCollection
from .by_cid import CIDEndpoint
from .provider import CircuitProvider
from .customers import CircuitCustomers
from .locations import ALocationEndpoint, ZLocationEndpoint


routes = [
    Route("/", CircuitCollection),
    Route("/{cid}", CIDEndpoint),
    Route("/{cid}/provider", CircuitProvider),
    Route("/{cid}/customers", CircuitCustomers),
    Route("/{cid}/a", ALocationEndpoint),
    Route("/{cid}/z", ZLocationEndpoint),
]
