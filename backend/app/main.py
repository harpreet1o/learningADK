from fastapi import FastAPI
from backend.app.routers import ask
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["chrome-extension://jbeggibadikdfjlogpbbbkmgjlijbigf"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ask.router)