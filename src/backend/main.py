from starlette.applications import Starlette
from starlette.config import Config

from backend.router import application_routes
from backend.middleware import middleware
from backend.database.mongo import MongoDatabase


config = Config('.env')
DEBUG = config('DEBUG', cast=bool, default=False)

app = Starlette(debug=DEBUG,
                middleware=middleware,
                routes=application_routes)

# we only set this if TESTING == False, otherwise we use a pytest fixture
if not config('TESTING', cast=bool, default=False):
    import pymongo

    MONGODB_HOSTNAME = config('MONGODB_HOSTNAME', default="localhost")
    MONGODB_TABLENAME = config('MONGODB_TABLENAME', default="test_data")

    client = pymongo.MongoClient(host=MONGODB_HOSTNAME, port=27017)
    db = client[MONGODB_TABLENAME]

    app.state.db = MongoDatabase(db)
