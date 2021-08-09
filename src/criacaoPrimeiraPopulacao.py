def criacao_de_primeira_populacao(lista_de_materias):
    for periodo in range(4):
        for horario in range(25):
            lista_de_materias[horario].horarios.append(horario)
            lista_de_materias[horario].periodo = periodo        
    return lista_de_materias