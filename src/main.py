import pandas as pd
from avaliacaoDasGeracoes import procurar_materia_por_horario_e_periodo, verificar_conflitos_de_horarios_de_professor
from criacaoDasMaterias import criacao_das_materias
from criacaoPrimeiraPopulacao import criacao_de_primeira_populacao, gerar_valores
from leituraDeArquivo import ler_json, ler_materia_no_json, ler_dado_da_materia_no_json

json_data = ler_json("data.JSON")

lista_de_materias = criacao_das_materias(json_data)

primeira_populacao = criacao_de_primeira_populacao(lista_de_materias)

print(verificar_conflitos_de_horarios_de_professor(primeira_populacao))

#materia_encontrada = procurar_materia_por_horario_e_periodo(lista_de_materias, 23, 2)
#print(materia_encontrada.nome)

