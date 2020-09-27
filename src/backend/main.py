from starlette.applications import Starlette
from starlette.config import Config
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware import Middleware

from backend.router import application_routes


config = Config('.env')
DEBUG = config('DEBUG', cast=bool, default=False)
TESTING = config('TESTING', cast=bool, default=False)
# MONGODB_HOSTNAME = config('MONGODB_HOSTNAME', default="localhost")
# MONGODB_TABLENAME = config('MONGODB_TABLENAME', default="test_data")

all = ["*"]
middleware = [
    Middleware(CORSMiddleware, allow_origins=all, allow_methods=all, allow_headers=all),
]

# if TESTING:
#     middleware.append(Middleware(MongoMiddleware))
# else:
#     middleware.append(Middleware(MongoMiddleware, connection_string=f"mongodb://{MONGODB_HOSTNAME}:27017", table=MONGODB_TABLENAME))

app = Starlette(debug=DEBUG,
                middleware=middleware,
                routes=application_routes)
