from fastapi import FastAPI
from backend.app.routers import ask

app = FastAPI()

app.include_router(ask.router)