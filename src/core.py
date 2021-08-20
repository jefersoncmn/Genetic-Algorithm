import random

def gerar_valores(quantidade_de_valores, range_de_valores):
    random.seed()
    numeros = random.getstate()
    return random.sample(range(range_de_valores), k=quantidade_de_valores)