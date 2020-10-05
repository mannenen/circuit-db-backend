from starlette.routing import Route

from .providers import ProviderCollection

from .circuits.collection import CircuitCollection
from .circuits.by_cid import CIDEndpoint
from .circuits.provider import CircuitProvider
from .circuits.customers import CircuitCustomers
from .circuits.locations import ALocationEndpoint, ZLocationEndpoint


circuit_routes = [
    Route("/circuits", CircuitCollection),
    Route("/circuits/{cid}", CIDEndpoint),
    Route("/circuits/{cid}/provider", CircuitProvider),
    Route("/circuits/{cid}/customers", CircuitCustomers),
    Route("/circuits/{cid}/a", ALocationEndpoint),
    Route("/circuits/{cid}/z", ZLocationEndpoint),
]

provider_routes = [
    Route("/providers", ProviderCollection)
]


routes = circuit_routes + provider_routes
