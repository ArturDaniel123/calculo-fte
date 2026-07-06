from fastapi import FastAPI
from app.routers.fte import router as fte_router

app = FastAPI()

app.include_router(fte_router, prefix="/fte") # Coloca as rotas dentro da aplicação

  