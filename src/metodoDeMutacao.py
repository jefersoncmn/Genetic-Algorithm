import random
from avaliacaoDasGeracoes import verificacao_da_geracao, verificar_individuo
from criacaoDasMaterias import criacao_das_materias
from criacaoPrimeiraPopulacao import criacao_de_individuo
from funcoesDeBusca import procurar_materia_por_horario_e_periodo
from leituraDeArquivo import ler_json
from metodoDeSelecao import atribuir_fitness
from modelos.individuo import Individuo
from modelos.materia import Materia
#A mutação implementada consiste em alterar, de forma aleatória, o horário atribuído a
#uma aula (gene) por outro. Da mesma maneira que na geração dos indivíduos da
#população inicial, o novo horário atribuído pertence a lista dos horários disponíveis do
#professor. Portanto, a troca é feita de forma simples: o horário antigo é excluído e o
#novo, obtido aleatoriamente, é alocado a aula. Assim, o algoritmo tem chances de
#explorar novas características e não permanecer em mínimos locais. Se a nova
#característica for ruim, será eliminada nas gerações seguintes, caso contrário,
#permanecerá. A ferramenta possibilita que o usuário defina o valor da taxa de mutação.

def gerar_mutacao(individuo : Individuo, chance : float):
    random.seed()
    valor = random.random()
    if valor < chance:
        #trocar_horarios_do_mesmo_periodo(individuo.lista_de_materias)
        mudar_horarios(individuo)
        #mudar_horarios_com_elitismo(individuo)

def trocar_horarios_do_mesmo_periodo(lista_de_materias : Materia) -> Materia:
    random.seed()
    periodo : int = random.randint(1,4)

    #pega as matérias a serem trocadas os horários
    materia1 : Materia = None
    materia2 : Materia = None

    while (materia1 == None or materia2 == None):
        materia1 = procurar_materia_por_horario_e_periodo(lista_de_materias, random.randint(0,24), periodo)
        materia2 = procurar_materia_por_horario_e_periodo(lista_de_materias, random.randint(0,24), periodo)

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

def mudar_horarios(individuo : Individuo) -> Individuo:
    for materia in range(len(individuo.lista_de_materias)):
        for horario in range(len(individuo.lista_de_materias[materia].horarios)):
            individuo.lista_de_materias[materia].horarios[horario] = random.randint(0,24)

def mudar_horarios_com_elitismo(individuo : Individuo) -> Individuo:
    individuo_aux : Individuo = Individuo(individuo.id,individuo.lista_de_materias) 

    for materia in range(len(individuo_aux.lista_de_materias)):
        for horario in range(len(individuo_aux.lista_de_materias[materia].horarios)):
            individuo_aux.lista_de_materias[materia].horarios[horario] = random.randint(0,24)

    verificar_individuo(individuo_aux)
    atribuir_fitness(individuo_aux)

    if individuo.fitness < individuo_aux.fitness:
        return individuo_aux
    else:
        return individuo  