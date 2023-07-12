from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from settings.project import Settings
from user.router import router as user_router


app = FastAPI(
    debug=Settings.DEBUG,
    version="0.0.1",
    title="Test APP",
    description="Test task app with add and get user",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=Settings.CORS_ALLOW_ORIGINS,
    allow_credentials=Settings.CORS_ALLOW_CREDENTIALS,
    allow_methods=Settings.CORS_ALLOW_METHODS,
    allow_headers=Settings.CORS_ALLOW_HEADERS,
)

API_PREFIX = "/api/v1"

app.include_router(user_router, prefix=API_PREFIX)
