from starlette.routing import Route

from .collection import CircuitCollection
from .by_cid import CIDEndpoint
from .provider import CircuitProvider
from .customers import CircuitCustomers
from .locations import ALocationEndpoint, ZLocationEndpoint


routes = [
    Route("/circuits", CircuitCollection),
    Route("/circuits/{cid}", CIDEndpoint),
    Route("/circuits/{cid}/provider", CircuitProvider),
    Route("/circuits/{cid}/customers", CircuitCustomers),
    Route("/circuits/{cid}/a", ALocationEndpoint),
    Route("/circuits/{cid}/z", ZLocationEndpoint),
]
