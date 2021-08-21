import random

from materia import Materia
from metodoDeMutacao import mutacao

def gerar_valores(quantidade_de_valores, range_de_valores):
    random.seed()
    numeros = random.getstate()
    return random.sample(range(range_de_valores), k=quantidade_de_valores)

def apresentar_materias(lista_de_materias : Materia):
    for materia in range(len(lista_de_materias)):
        print(lista_de_materias[materia].nome + " \ horarios: "+str(lista_de_materias[materia].horarios))