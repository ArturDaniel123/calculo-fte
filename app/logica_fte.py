# Valor da hora
salario_hora = 20.0

def automacao():
    '''Realiza toda a lógica do cálculo do FTE'''

    # Recebe do usuário o tempo para realizar a tarefa
    tempo_tarefa = int(
        input("Informe o tempo médio para se realizar "
                        "essa tarefa (em minutos): ")
    )

    # Recebe do usuário quantas vezes a atividade é realizada
    repeticao = int(
        input("Quantas vezes você repete essa atividade no dia?: ")
    )

    # Recebe do usuário o tempo que o bot leva pra executar a tarefa
    tempo_bot = int(
        input("Tempo do robô para realizar a atividade: ")
    )

    # Custo mensal do bot, caso houver
    custo_mensal_bot = 0

    
    salario_minuto = salario_hora/60

    custo_por_tarefa_humana = tempo_tarefa * salario_minuto
    custo_diario_humano = custo_por_tarefa_humana * repeticao
    custo_semanal_humano = custo_diario_humano * 5 # Segunda a sexta
    custo_mensal_humano = custo_semanal_humano * 4 # 4 semanas

    # Economia liquída do mês
    econ_liq_mes = custo_mensal_humano - custo_mensal_bot

    produtiv_relativa = tempo_tarefa / tempo_bot

    # F-strings para exibição
    valor_trab = f"Cada execução dessa atividade custa: R$ {custo_por_tarefa_humana:.2f}.\n"
    valor_trab_dia = (
        f"Num dia, essa atividade custa: R$ {custo_diario_humano:.2f}.\n"
    )
    valor_trab_sem = (
        f"Numa semana, essa atividade custa: R$ {custo_semanal_humano:.2f}.\n"
    )
    valor_trab_mes = (
        f"Num mês, essa atividade custa: R$ {custo_mensal_humano:.2f}.\n"
    )
    econ_liq = (
        f"Mensalmente, a economia líquida é de: R$ {econ_liq_mes:.2f}.\n"
    )
    nivel_produtiv = (
        f"O robô é {produtiv_relativa:.1f} vezes mais rápido que o humano!\n"
    )

    print(valor_trab,
          valor_trab_dia,
          valor_trab_sem,
          valor_trab_mes,
          econ_liq,
          nivel_produtiv)

automacao()

    
