def calcular_fte(salario_hora, tempo_tarefa, repeticao, tempo_bot,
                 custo_mensal_bot=0):
    '''Realiza toda a lógica do cálculo do FTE'''
    if salario_hora <= 0:
        raise ValueError("O salário não pode ser igual ou menor que zero.")
    salario_minuto = salario_hora/60
    
    if tempo_tarefa <= 0:
        raise ValueError("O tempo de realização da tarefa não pode ser igual ou menor que zero.")   
    custo_por_tarefa_humana = tempo_tarefa * salario_minuto
    
    if repeticao <= 0:
        raise ValueError("O número de repetições não pode ser nulo.") 
    custo_diario_humano = custo_por_tarefa_humana * repeticao
    
    custo_semanal_humano = custo_diario_humano * 5 # Segunda a sexta
    custo_mensal_humano = custo_semanal_humano * 4 # 4 semanas

    if custo_mensal_bot < 0:
        raise ValueError("Custo mensal bot inválido.")
    econ_liq_mes = custo_mensal_humano - custo_mensal_bot # Economia liquída do mês

    if tempo_bot <= 0:
        raise ValueError("O tempo de execução de tarefa não pode ser nulo.")
    produtividade_relativa = tempo_tarefa / tempo_bot

    return {
        "salario_minuto" : salario_minuto,
        "custo_por_tarefa_humana" : custo_por_tarefa_humana,
        "custo_diario_humano" : custo_diario_humano,
        "custo_mensal_humano" : custo_mensal_humano,
        "economia_mensal" : econ_liq_mes,
        "produtividade_relativa" : produtividade_relativa
    }

    
