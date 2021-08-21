import random
from funcoesDeBusca import procurar_materia_por_horario_e_periodo
from materia import Materia
#A mutação implementada consiste em alterar, de forma aleatória, o horário atribuído a
#uma aula (gene) por outro. Da mesma maneira que na geração dos indivíduos da
#população inicial, o novo horário atribuído pertence a lista dos horários disponíveis do
#professor. Portanto, a troca é feita de forma simples: o horário antigo é excluído e o
#novo, obtido aleatoriamente, é alocado a aula. Assim, o algoritmo tem chances de
#explorar novas características e não permanecer em mínimos locais. Se a nova
#característica for ruim, será eliminada nas gerações seguintes, caso contrário,
#permanecerá. A ferramenta possibilita que o usuário defina o valor da taxa de mutação.

def mutacao(lista_de_materias : Materia) -> Materia:
    random.seed()
    periodo : int = random.randint(1,4)
    #pega as matérias a serem trocadas os horários
    materia1 : Materia = procurar_materia_por_horario_e_periodo(lista_de_materias, random.randint(0,25), periodo)
    materia2 : Materia = procurar_materia_por_horario_e_periodo(lista_de_materias, random.randint(0,25), periodo)

    #pega os horarios das matérias a serem trocados
    horario_materia1 : int = random.randint(0,len(materia1.horarios)-1)
    horario_materia2 : int = random.randint(0,len(materia2.horarios)-1)

    #realiza a troca
    horario_auxiliar = materia1.horarios[horario_materia1]
    materia1.horarios[horario_materia1] = materia2.horarios[horario_materia2]
    materia2.horarios[horario_materia2] = horario_auxiliar

    #print("Materias trocadas:")
    #print(materia1.nome+" horario: "+str(horario_materia1))
    #print(materia2.nome+" horario: "+str(horario_materia2))
