import pandas as pd
from criacaoDasMaterias import criacao_das_materias
from criacaoPrimeiraPopulacao import criacao_de_primeira_populacao, gerar_valores
from leituraDeArquivo import ler_json, ler_materia_no_json, ler_dado_da_materia_no_json

json_data = ler_json("data.JSON")

lista_de_materias = criacao_das_materias(json_data)

criacao_de_primeira_populacao(lista_de_materias)
