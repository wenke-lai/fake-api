from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import code

app = FastAPI()

origins = [
    "http://localhost:5173",  # vite dev
    "http://localhost:5174",  # vite preview
]
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True)


app.include_router(code.router)


@app.get("/ping")
def ping():
    return "pong"
