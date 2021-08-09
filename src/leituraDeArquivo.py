import pandas as pd
import json


def ler_json(arq_json):
    with open(arq_json, 'r', encoding='utf8') as f:
        return json.load(f)


def ler_segmento_no_json(json_data, line):
    value = json_data[line].values()
    print(value)
