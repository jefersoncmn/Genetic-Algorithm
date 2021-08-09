import random

def criacao_de_primeira_populacao(lista_de_materias):
    valorRandomico = gerar_valores(25)
    i = 0

#cria uma fila com valores randomizados
#preencher cada matéria e cada credito com a sequencia da fila
    for materia in range(6):
        lista_de_materias[materia].horarios = []
        for c in range(lista_de_materias[materia].cargahoraria):
            lista_de_materias[materia].horarios.append(valorRandomico.index(i))
            i = i+1
        lista_de_materias[materia].periodo = 1
        #print(lista_de_materias[materia].nome)
        #print(lista_de_materias[materia].horarios)      
    return lista_de_materias

def gerar_valores(quantidade_de_valores):
    random.seed()
    numeros = random.getstate()
    return random.sample(range(quantidade_de_valores), k=quantidade_de_valores)