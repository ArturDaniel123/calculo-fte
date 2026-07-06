from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.exceptions.fte_exceptions import FTEValidationError
from app.routers.fte import router as fte_router

app = FastAPI()

@app.exception_handler(FTEValidationError)
def handle_fte_error(request: Request, exc: FTEValidationError):
    return JSONResponse(
        status_code=400,
        content={
            "error": True,
            "type": "fte_validation_error",
            "message": exc.message
        }
    )



app.include_router(fte_router, prefix="/fte") # Coloca as rotas dentro da aplicação

  