'''Aqui estará presente a definição dos modelos de entrada e
saída referentes ao cálculo de FTE'''

from pydantic import BaseModel

class FTERequest(BaseModel):
    salario_hora: float
    tempo_tarefa: int
    repeticao: int
    tempo_bot: int
    custo_mensal_bot: float = 0

class FTEResponse(BaseModel):
    '''Define o formato dos dados que a API devolve ao cliente'''
    salario_minuto: float
    custo_por_tarefa_humana: float
    custo_diario_humano: float
    custo_mensal_humano: float
    economia_mensal: float
    produtividade_relativa: float

