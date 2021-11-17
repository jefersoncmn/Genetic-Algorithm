import pandas as pd
from apresentacao_grade_materias import Table
from avaliacaoDasGeracoes import verificacao_da_geracao, verificar_conflitos_de_horarios_de_professor_de_todas_materias, verificar_dependencias_de_todas_materias, verificar_sobreposicao_de_materia
from core import apresentar_individuo, apresentar_individuo_sem_materias, apresentar_melhor_individuo_encontrado, maior_valor_fitness_da_geracao, media_fitness_da_geracao
from criacaoDasMaterias import criacao_das_materias
from criacaoPrimeiraPopulacao import criacao_de_individuo
from graficos import apresentar_graficos
from metodoDeMultiplicacao import cruzamento_sequenciado, cruzamento_paralelo
from modelos.individuo import Individuo
from leituraDeArquivo import ler_json
from metodoDeMutacao import gerar_mutacao
from metodoDeSelecao import atribuir_fitness_a_geracao, selecao_por_torneio, selecao_por_truncamento

tamanho_da_populacao: int = 300

individuos_de_maiores_valores_fitness: Individuo = []
media_valores_fitness: float = []

rodadas: int = 800
rodadas_operadas: int = 0

json_data = ler_json("data.JSON")  # Pega informacoes das materias

populacao: Individuo = []

filhos: Individuo = []

# Criação da primeira populaçào
# Define aqui a quantidade de individuos que tera a população
for _individuo in range(tamanho_da_populacao):
    individuo: Individuo = Individuo(_individuo, criacao_de_individuo(
        _individuo, criacao_das_materias(json_data)).lista_de_materias)
    populacao.append(individuo)

for rodada in range(rodadas):
    print("Geracao "+str(rodada))
    rodadas_operadas += 1

    # Verificacao
    verificacao_da_geracao(populacao)
    atribuir_fitness_a_geracao(populacao)

    # Apresentação
    media_valores_fitness.append(media_fitness_da_geracao(populacao))
    individuos_de_maiores_valores_fitness.append(
        maior_valor_fitness_da_geracao(populacao))

    # Condição de parada
    if(individuos_de_maiores_valores_fitness[-1].fitness == 1):
        break

    # Seleção
    #populacao = selecao_por_truncamento(populacao, 0.505)
    populacao = selecao_por_torneio(populacao, 3, 2)

    if len(populacao) <= 1:
        break

    # Multiplicação
    #populacao = cruzamento_sequenciado(populacao, media_valores_fitness[-1], 300)
    populacao = cruzamento_paralelo(populacao, media_valores_fitness[-1])

    # Mutação
    for individuo in range(len(populacao)):
        gerar_mutacao(populacao[individuo], 0.01)

individuo_de_maior_fitness: Individuo = maior_valor_fitness_da_geracao(
    individuos_de_maiores_valores_fitness)

#print("Individuo: "+str(individuo_de_maior_fitness.id)+ " com fitness: "+str(individuo_de_maior_fitness.fitness)+" é o melhor!")
apresentar_graficos(rodadas_operadas, media_valores_fitness,
                    individuos_de_maiores_valores_fitness)

# apresentar_individuo(individuo_de_maior_fitness)

apresentar_melhor_individuo_encontrado(individuo_de_maior_fitness)
