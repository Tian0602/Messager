from fastapi import FastAPI
from .api.routes import router
from .database import engine
from .database.message_db import Base

Base.metadata.create_all(bind=engine)
app = FastAPI(title="Message Service API")
app.include_router(router)