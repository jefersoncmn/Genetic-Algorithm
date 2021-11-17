# Cruzamento uniforme: ​neste método, os genes dos descendentes são criados a
# partir da cópia dos genes dos pais, que são escolhidos de acordo com uma
# máscara de cruzamento. Esta máscara é uma sequência de zeros e uns gerados de
# forma aleatória. Quando houver o valor 1 na máscara de cruzamento, o gene a
# ser copiado deve ser o do primeiro pai e quando houver o valor 0, o gene a ser
# copiado deve ser o do segundo pai [Lucas 2002].
import random
from modelos.individuo import Individuo
from avaliacaoDasGeracoes import verificacao_da_geracao
from metodoDeSelecao import atribuir_fitness_a_geracao

def cruzamento_sequenciado(geracao : Individuo, media_valor_fitness : float, quantidade_retornada : int):
    filhos : Individuo = []
    for contador in range(len(geracao)-1):
        #if len(filhos) < quantidade_retornada:
        multiplicados = cruzamento_uniforme(geracao[contador],geracao[contador+1], media_valor_fitness)
            
        filhos.extend(multiplicados)
        #else:
        #    break
    
    return filhos

#Cruzamento sem repetir o cruzamento de um individuo que já realizou o cruzamento
#O mesmo valor de entrada é o valor de saída de individuos
def cruzamento_paralelo(geracao : Individuo, media_valor_fitness : float):
    filhos : Individuo = []
    contador : int = 0

    while contador+1 < len(geracao):
        multiplicados = cruzamento_uniforme(geracao[contador],geracao[contador+1], media_valor_fitness)      
        filhos.extend(multiplicados)
        contador+=2
    
    return filhos


def cruzamento_uniforme(individuo1 : Individuo, individuo2 : Individuo, media_valor_fitness : float) -> Individuo:
    #mascara : int = gerador_de_mascara()
    #print(str(mascara))

    i : int = 0
    individuo3 : Individuo = Individuo(individuo1.id,individuo1.lista_de_materias)
    individuo4 : Individuo = Individuo(individuo2.id,individuo2.lista_de_materias)

    for periodo in range(4):
        mascara : int = gerador_de_mascara()
        for materia in range(len(individuo1.lista_de_materias)):
            if individuo1.lista_de_materias[materia].periodo == periodo+1:
                for horario in range(len(individuo1.lista_de_materias[materia].horarios)):
                    if mascara[i] == 0: #Se for 0 ele vai fazer a alteracao
                        aux = individuo3.lista_de_materias[materia].horarios[horario]
                        individuo3.lista_de_materias[materia].horarios[horario] = individuo4.lista_de_materias[materia].horarios[horario]
                        individuo4.lista_de_materias[materia].horarios[horario] = aux
                        #print("Mudança feita do individuo 1 com  o individuo 2 de materia "+ individuo3.lista_de_materias[materia].nome+ " periodo "+ str(individuo3.lista_de_materias[materia].periodo))
                    i += 1
        i = 0

    individuos_filhos : Individuo = [individuo3, individuo4]

    return individuos_filhos

    #return elitismo_global(individuo1, individuo2, individuo3, individuo4, media_valor_fitness)

def elitismo_global(individuo1, individuo2, individuo3, individuo4, media_valor_fitness):
    populacao : Individuo = [individuo3, individuo4]
    verificacao_da_geracao(populacao)
    atribuir_fitness_a_geracao(populacao)
    
    individuos_filhos : Individuo = []

    if(individuo3.fitness > media_valor_fitness and individuo4.fitness > media_valor_fitness):
        individuos_filhos = [individuo3, individuo4]
        return individuos_filhos
    if(individuo3.fitness > media_valor_fitness and individuo4.fitness <= media_valor_fitness):
        individuos_filhos = [individuo3, individuo2]
        return individuos_filhos
    if(individuo3.fitness <= media_valor_fitness and individuo4.fitness > media_valor_fitness):
        individuos_filhos = [individuo1, individuo4]
        return individuos_filhos
    else:
        individuos_filhos = [individuo1, individuo2]
        return individuos_filhos

def gerador_de_mascara() -> int:
    mascara : int = []
    for numeros in range(25):
        random.seed()
        mascara.append(random.randint(0,1))
    
    return mascara