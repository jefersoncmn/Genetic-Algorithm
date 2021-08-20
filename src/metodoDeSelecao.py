import random
from core import gerar_valores
from materia import Materia
#Na seleção por torneio, três indivíduos são selecionados aleatoriamente e os dois
#com os maiores fitness são selecionados para terem seus genes propagados. Na seleção
#por truncamento, o valor do limiar utilizado foi 0.4, ou seja, apenas os 40% melhores
#indivíduos podem ser selecionados para participarem das próximas etapas.

def selecao_por_truncamento(geracao : Materia, valor_do_limiar : float) -> Materia:
    cromossomos_selecionados : Materia = []
    
    geracao = atribuir_fitness_a_geracao(geracao)
    
    return retornar_maiores_fitness(geracao, regra_de_tres(len(geracao), valor_do_limiar*100))


def selecao_por_torneio(geracao : Materia, quantidade_de_selecionados : int, quantidade_de_genes_propagados : int):
    valores : int = [] #Armazena numeros de aulas selecionadas
    lista_de_aulas_selecionadas : Materia = []
    i : int = 0

    valores = gerar_valores(quantidade_de_selecionados,25) #gera o vetor com valores das aulas selecionadas

    for i in range(0,quantidade_de_selecionados):
        #print("Aula selecionada: "+ geracao[valores[i]].nome + " de valor: "+ str(valores[i]))
        lista_de_aulas_selecionadas.append(geracao[valores[i]])
        atribuir_fitness(lista_de_aulas_selecionadas[i])

    return retornar_maiores_fitness(lista_de_aulas_selecionadas, quantidade_de_genes_propagados)



def retornar_maiores_fitness(lista_de_aulas_selecionadas : Materia, quantidade_a_ser_retornada : int):
    valores : Materia = []
    maior_valor : Materia

    for x in range(quantidade_a_ser_retornada):
        maior_valor = lista_de_aulas_selecionadas[0]
        for y in range(len(lista_de_aulas_selecionadas)):
            #print(lista_de_aulas_selecionadas[y].nome + " com fitness "+str(lista_de_aulas_selecionadas[y].fitness))
            
            if maior_valor.fitness < lista_de_aulas_selecionadas[y].fitness:
                maior_valor = lista_de_aulas_selecionadas[y]
            
        lista_de_aulas_selecionadas.remove(maior_valor)
        valores.append(maior_valor)
        #print(maior_valor.nome + " com fitness "+str(maior_valor.fitness))
    
    return valores


def atribuir_fitness_a_geracao(geracao : Materia):
    for materia in range(len(geracao)):
        atribuir_fitness(geracao[materia])

    return geracao

def atribuir_fitness(materia : Materia):
    materia.fitness = calcular_fitness(materia)


def calcular_fitness(materia : Materia) -> float:
    return 100/(100 + materia.punicao)

def regra_de_tres(quantidade : int, porcentagem : int) -> int:
    return int((quantidade*porcentagem)/100)