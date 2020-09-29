from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware


all = ["*"]
middleware = [
    Middleware(CORSMiddleware, allow_origins=all, allow_methods=all, allow_headers=all),
]
