import pandas as pd
from leituraDeArquivo import ler_json, ler_materia_no_json, ler_dado_da_materia_no_json

json_data = ler_json("data.JSON")

ler_dado_da_materia_no_json(json_data, 0, 'id')

