import pandas as pd
import json

def ler_json(arq_json):
    with open(arq_json, 'r', encoding='utf8') as f:
        return json.load(f)

def ler_materia_no_json(json_data, line):
    materia = json_data[line]['id']
    print(materia)
    return materia

def ler_dado_da_materia_no_json(json_data, line, key):
    dado = json_data[line]['id']
    print(dado)
    return dado

