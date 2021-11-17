import random
from modelos.individuo import Individuo
from modelos.materia import Materia
#Na seleção por torneio, três indivíduos são selecionados aleatoriamente e os dois
#com os maiores fitness são selecionados para terem seus genes propagados. Na seleção
#por truncamento, o valor do limiar utilizado foi 0.4, ou seja, apenas os 40% melhores
#indivíduos podem ser selecionados para participarem das próximas etapas.

#geracao = lista de todos individuos da geracao

def selecao_por_truncamento(geracao : Individuo, valor_do_limiar : float) -> Individuo:
    valor = regra_de_tres(len(geracao), valor_do_limiar*100)
    #print("valor de itens de acordo com a limiar "+str(valor_do_limiar)+" quantidade: "+str(valor))
    return retornar_maiores_fitness(geracao, valor)


def selecao_por_torneio(geracao : Individuo, quantidade_de_selecionados : int, quantidade_de_genes_propagados : int):
    
    lista_de_individuos_selecionados_no_torneio : Individuo = []

    while len(lista_de_individuos_selecionados_no_torneio) < 300:
        lista_de_individuos_selecionados : Individuo = []
        for individuo in range(len(geracao)):
            random.seed()
            if len(lista_de_individuos_selecionados) <= quantidade_de_selecionados:
                if random.randint(0,1) == 0:
                    lista_de_individuos_selecionados.append(geracao[individuo])
        
        lista_de_individuos_selecionados_no_torneio.extend(retornar_maiores_fitness(lista_de_individuos_selecionados, quantidade_de_genes_propagados))

    return lista_de_individuos_selecionados_no_torneio


def retornar_maiores_fitness(geracao : Individuo, quantidade_a_ser_retornada : int) -> Individuo:
    maiores_valores : Individuo = []
    maior_valor : Individuo

    for x in range(quantidade_a_ser_retornada):
        maior_valor = geracao[0]
        for individuo in range(len(geracao)):
            if maior_valor.fitness < geracao[individuo].fitness:
                maior_valor = geracao[individuo]
        
        maiores_valores.append(maior_valor)
        geracao.remove(maior_valor)
        
    return maiores_valores


def atribuir_fitness_a_geracao(geracao : Individuo):
    for individuo in range(len(geracao)): #Percorre os individuos
        atribuir_fitness(geracao[individuo])
    return geracao

def atribuir_fitness(individuo : Individuo):
    punicoes : int = 0
    for materia in range(len(individuo.lista_de_materias)):
        punicoes += individuo.lista_de_materias[materia].punicao
        #print("materia: "+individuo.lista_de_materias[materia].nome+" tem punicao de: "+ str(individuo.lista_de_materias[materia].punicao))
    individuo.fitness = calcular_fitness(punicoes)
    
def calcular_fitness(punicao : int) -> float:
    return 100/(100 + punicao)

def regra_de_tres(quantidade : int, porcentagem : int) -> int:
    return int((quantidade*porcentagem)/100)