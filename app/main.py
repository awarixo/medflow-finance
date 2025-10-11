from fastapi import FastAPI
from app import models
from app.database import engine
from app.api import router as api_router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Clinic Financial Backend",
    description="API for managing billing and financial records."
)

app.include_router(api_router)