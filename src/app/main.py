from fastapi import FastAPI
from .api.routes import router

app = FastAPI(title="Message Service API")
app.include_router(router)