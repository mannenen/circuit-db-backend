from starlette.applications import Starlette
from starlette.config import Config
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware import Middleware

from router import application_routes
from middleware import MongoMiddleware

config = Config('.env')
DEBUG = config('DEBUG', cast=bool, default=False)
MONGODB_HOSTNAME = config('MONGODB_HOSTNAME', default="mongo")
MONGODB_TABLENAME = config('MONGODB_TABLENAME', default="test_data")

all = ["*"]
middleware = [
    Middleware(CORSMiddleware, allow_origins=all, allow_methods=all, allow_headers=all),
    Middleware(MongoMiddleware, host=MONGODB_HOSTNAME, table=MONGODB_TABLENAME)
]

app = Starlette(debug=DEBUG,
                middleware=middleware,
                routes=application_routes)
