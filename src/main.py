import pandas as pd
from leituraDeArquivo import ler_json, ler_segmento_no_json

json_data = ler_json("data.JSON")
ler_segmento_no_json(json_data, 0)
