import matplotlib.pyplot as plt
from modelos.individuo import Individuo
import numpy as np

#Função responsável por apresentar os gráficos
def apresentar_graficos(rodadas : int , media_valores_fitness : float, individuos_de_maiores_valores_fitness : Individuo):
    maiores_valores_fitness = []
    for individuo in range(len(individuos_de_maiores_valores_fitness)):
        maiores_valores_fitness.append(individuos_de_maiores_valores_fitness[individuo].fitness)

    plt.title('Geração de grades de horario')
    plt.ylabel('Fitness')
    plt.xlabel('Gerações')
    plt.plot(np.arange(rodadas), media_valores_fitness, c='r', label='Media dos indivíduos')
    plt.plot(np.arange(rodadas), maiores_valores_fitness, c='g', label='Melhores indivíduos')
    plt.legend()
    plt.show()