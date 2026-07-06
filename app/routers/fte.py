'''Os endpoints da API'''
from fastapi import APIRouter
from app.schemas.fte import FTERequest, FTEResponse
from app.services.logica_fte import calcular_fte

router = APIRouter()

@router.post("/calcular", response_model=FTEResponse)
def calcular_fte_route(dados: FTERequest):
    
    resultado = calcular_fte(
        salario_hora=dados.salario_hora,
        tempo_tarefa=dados.tempo_tarefa,
        repeticao=dados.repeticao,
        tempo_bot=dados.tempo_bot,
        custo_mensal_bot=dados.custo_mensal_bot
    )

    return resultado