from random import randint
from core import gerar_valores
from modelos.individuo import Individuo
from modelos.materia import Materia

# Função responsavel por criar um individuo
# Entrada -> Id, Lista de materias (Só as instancias, horarios zerados)
# Retorno -> Lista de materias com horários preenchidos aleatoriamente
def criacao_de_individuo(id : int, lista_de_materias : Materia) -> Individuo:
    
    i : int = 0
    #print("Criacao do individuo: "+str(id))
    #preencher cada matéria e cada credito com a sequencia da fila
    for periodo in range(1,5):
        #valor_randomico = gerar_valores(25,25)#cria uma fila com valores randomizados que nÃo se repetem
        valor_randomico = [randint(0, 24) for i in range(25)] # Cria uma fila de valores radomizados que se repetem
        #print(str(valor_randomico))
        for materia in range(len(lista_de_materias)):
            if lista_de_materias[materia].periodo == periodo:
                lista_de_materias[materia].horarios = []
                for carga_horaria in range(lista_de_materias[materia].cargahoraria):
                    #lista_de_materias[materia].horarios.append(valor_randomico.index(i))
                    lista_de_materias[materia].horarios.append(valor_randomico[i])
                    i +=1
                #print(lista_de_materias[materia].nome)
                #print(lista_de_materias[materia].horarios)
                #print("Período: "+str(lista_de_materias[materia].periodo))
        i = 0

    return Individuo(id,lista_de_materias)

