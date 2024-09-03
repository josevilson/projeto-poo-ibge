import pandas as pd
import json

class DataTransform:
    def __init__(self):
        self.data = None
    
    def data_to_json(self, json_data):
        records = []
        for item in json_data:
            indicador = item['indicador']
            for serie in item['series']:
                pais = serie['pais']['nome']
                for entry in serie['serie']:
                    for ano, valor in entry.items():
                        if valor is not None:
                            records.append({
                                'Indicador': indicador,
                                'País': pais,
                                'Ano': ano,
                                'Valor': valor,
                                })
            self.data = records
        return records

    def transform_to_dataframe(self):
        df = pd.json_normalize(self.data)
        return df
