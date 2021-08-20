from core import gerar_valores

def criacao_de_primeira_populacao(lista_de_materias):
    valorRandomico = gerar_valores(25,25)
    i = 0
    periodo = 1

    #cria uma fila com valores randomizados
    #preencher cada matéria e cada credito com a sequencia da fila
    for materia in range(25):
        lista_de_materias[materia].horarios = []
        for c in range(lista_de_materias[materia].cargahoraria):
            lista_de_materias[materia].horarios.append(valorRandomico.index(i))
            i +=1
            if(i == 25):
                i = 0
                periodo += 1
                valorRandomico = gerar_valores(25,25)
        lista_de_materias[materia].periodo = periodo
        #print(lista_de_materias[materia].nome)
        #print(lista_de_materias[materia].horarios) 
        #print(lista_de_materias[materia].periodo)
    return lista_de_materias

