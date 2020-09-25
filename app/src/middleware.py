from starlette.middleware.base import BaseHTTPMiddleware

import pymongo


class MongoMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, host="mongo", table="test_data"):
        super().__init__(app)
        self.host = host
        self.table = table

    async def dispatch(self, request, call_next):
        client = pymongo.MongoClient(f"mongodb://{self.host}:27017/")
        db = client[f'{self.table}']
        request.state.db = db

        response = await call_next(request)
        return response
