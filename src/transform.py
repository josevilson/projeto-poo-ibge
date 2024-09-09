import json
import pandas as pd

class DataTransform:
    """
    Classe para transformar dados JSON em uma lista de registros ou DataFrame.

    Attributes:
        data (list): Armazena os registros extraídos do JSON.
    """

    def __init__(self):
        """
        Inicializa a classe DataTransform com o atributo 'data' vazio.
        """
        self.data = None

    def data_to_json(self, json_data):
        """
        Converte dados JSON em uma lista de dicionários, organizando informações sobre
        indicadores, países, anos e valores.

        Args:
            json_data (list): Dados JSON a serem transformados.

        Returns:
            list: Lista de registros formatados a partir do JSON.
        """
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
        """
        Transforma os registros armazenados no atributo 'data' em um DataFrame do pandas.

        Returns:
            pd.DataFrame: DataFrame contendo os registros extraídos do JSON.
        """
        df = pd.json_normalize(self.data)
        return df
