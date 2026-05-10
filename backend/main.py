from fastapi import FastAPI
from api.routes import router
from db.models import Base
from db.session import engine

app = FastAPI(title="AI Photo Search Assistant")

Base.metadata.create_all(bind=engine)

app.include_router(router)