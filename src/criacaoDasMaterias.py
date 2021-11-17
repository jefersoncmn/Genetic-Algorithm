from leituraDeArquivo import ler_dado_da_materia_no_json
from modelos.materia import Materia

# Função resposável por criar instancias das matérias
# Entrada -> Informações pra criação da matéria
# Retorno -> Instancia da matéria
def criacao_de_materia(id, nome, professor, cargahoraria, dependencias, periodo):
    materia = Materia(id, nome,professor, cargahoraria, dependencias, periodo)
    return materia

# Função responsável por criar todas as matérias da grade
# Entrada -> Vetor com dados de todas as matérias que foram obtidas do JSON
# Retorno -> lista com todas as matérias instanciadas
def criacao_das_materias(json_data):
    lista_de_materias = []

    for line in range(25):
        lista_de_materias.append(criacao_de_materia(ler_dado_da_materia_no_json(json_data, line, 'id'), ler_dado_da_materia_no_json(json_data, line, 'nome'),ler_dado_da_materia_no_json(json_data, line, 'professor'), ler_dado_da_materia_no_json(json_data, line, 'cargahorariasemanal'),ler_dado_da_materia_no_json(json_data, line, 'dependencias'), ler_dado_da_materia_no_json(json_data, line, 'periodo')))
        #print("Materia: "+lista_de_materias[line].nome+" criada")
        #print(lista_de_materias[line].cargahoraria)

    return lista_de_materias