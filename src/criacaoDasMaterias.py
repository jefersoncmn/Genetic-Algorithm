from leituraDeArquivo import ler_dado_da_materia_no_json
from materia import Materia

def criacao_de_materia(id, nome, professor, cargahoraria, dependencias):
    materia = Materia(id, nome,professor, cargahoraria, dependencias)
    return materia

def criacao_das_materias(json_data):
    lista_de_materias = []

    for line in range(6):
        lista_de_materias.append(criacao_de_materia(ler_dado_da_materia_no_json(json_data, line, 'id'), ler_dado_da_materia_no_json(json_data, line, 'nome'),ler_dado_da_materia_no_json(json_data, line, 'professor'), ler_dado_da_materia_no_json(json_data, line, 'cargahorariasemanal'),ler_dado_da_materia_no_json(json_data, line, 'dependencias')))
        print("Materia: "+lista_de_materias[line].nome+" criada")

    return lista_de_materias