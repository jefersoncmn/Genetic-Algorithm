import random
from tkinter import *
from apresentacao_grade_materias import Table
from modelos.individuo import Individuo
from modelos.materia import Materia

#Função responsável por retornar um vetor de valores aleatórios que não se repetem
#quantidade_de_valores -> Tamanho do vetor a ser retornado
def gerar_valores(quantidade_de_valores, range_de_valores):
    random.seed()
    numeros = random.getstate()
    return random.sample(range(range_de_valores), k=quantidade_de_valores)

#Função responsável por apresentar todas as informações de um indivíduo
def apresentar_individuo(individuo : Individuo):
    print("individuo :"+str(individuo.id))
    apresentar_materias(individuo.lista_de_materias)
    print("Sobreposicao de aulas: "+str(individuo.sobreposicao_de_aulas))
    print("Dependencias desordenadas: "+str(individuo.dependencias_desordenadas))
    print("Conflito de horario de professor: "+str(individuo.conflito_de_horario_de_professor))

def apresentar_individuo_sem_materias(individuo : Individuo):
    print("individuo :"+str(individuo.id))
    print("Sobreposicao de aulas: "+str(individuo.sobreposicao_de_aulas))
    print("Dependencias desordenadas: "+str(individuo.dependencias_desordenadas))
    print("Conflito de horario de professor: "+str(individuo.conflito_de_horario_de_professor))

#Função responsável por percorrer as matérias e printar os horários de cada uma e seu respectivo período
def apresentar_materias(lista_de_materias : Materia):
    for materia in range(len(lista_de_materias)):
        print(lista_de_materias[materia].nome + " \ horarios: "+str(lista_de_materias[materia].horarios) + "\ periodo : "+str(lista_de_materias[materia].periodo))

#Função responsável por retornar a média de fitness da geração
def media_fitness_da_geracao(geracao : Individuo) -> float:
    valores_fitness : float = 0
    for individuo in range(len(geracao)):
        #print("individuo: "+str(geracao[individuo].id)+" e fitness: "+str(geracao[individuo].fitness))
        valores_fitness += geracao[individuo].fitness
    
    media : float = valores_fitness/len(geracao)

    #print("Media fitness da geracao: "+str(media))
    return media

#Função responsável por retornar o indivíduo de maior fitness da geração
def maior_valor_fitness_da_geracao(geracao : Individuo) -> Individuo:
    
    individuo_de_maior_valor_fitness : Individuo = geracao[0]

    for individuo in range(len(geracao)):
        #print("individuo: "+str(geracao[individuo].id)+" e fitness: "+str(geracao[individuo].fitness))
        if geracao[individuo].fitness > individuo_de_maior_valor_fitness.fitness:
            individuo_de_maior_valor_fitness = geracao[individuo]

    #print("individuo de maior fitness: "+str(individuo_de_maior_valor_fitness.id)+" e fitness: "+str(individuo_de_maior_valor_fitness.fitness))
    return individuo_de_maior_valor_fitness

def apresentar_geracao(geracao : Individuo):
    for individuo in range(len(geracao)):
        apresentar_individuo_sem_materias(geracao[individuo])

def apresentar_melhor_individuo_encontrado(individuo_de_maior_fitness : Individuo):
    root = Tk()
    t = Table(root, individuo_de_maior_fitness)
    root.mainloop()