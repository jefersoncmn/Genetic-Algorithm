import pandas as pd
from avaliacaoDasGeracoes import verificar_dependencias_de_todas_materias
from criacaoDasMaterias import criacao_das_materias
from criacaoPrimeiraPopulacao import criacao_de_primeira_populacao, gerar_valores
from leituraDeArquivo import ler_json, ler_materia_no_json, ler_dado_da_materia_no_json
from metodoDeSelecao import selecao_por_torneio, selecao_por_truncamento

json_data = ler_json("data.JSON")

lista_de_materias = criacao_das_materias(json_data)

primeira_populacao = criacao_de_primeira_populacao(lista_de_materias)

verificar_dependencias_de_todas_materias(primeira_populacao)
#print(verificar_conflitos_de_horarios_de_professor(primeira_populacao,primeira_populacao[0]))

#verificar_conflitos_de_horarios_de_professor_de_todas_materias(primeira_populacao)

#selecionados = selecao_por_torneio(primeira_populacao, 3, 2)

#selecionados = selecao_por_truncamento(primeira_populacao, 0.4)