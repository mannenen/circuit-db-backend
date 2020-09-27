from starlette.middleware.base import BaseHTTPMiddleware

import pymongo


class MongoMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, connection_string="mongomock://localhost:27017/", table="test_data"):
        super().__init__(app)
        client = pymongo.MongoClient(connection_string)
        self.db = client[f'{table}']

    async def dispatch(self, request, call_next):
        request.state.db = self.db

        response = await call_next(request)
        return response


class DatabaseMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response = await call_next(request)
        return response
