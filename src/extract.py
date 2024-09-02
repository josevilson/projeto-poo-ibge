### fazer um request nos indicadores: 77836 e  77819
import requests


class DataExtractor:
    def __init__(self):
        # self.indicadores = indicadores
        self.url = f"https://servicodados.ibge.gov.br/api/v1/paises/AR|BR/indicadores/77836|77819"
    
    def get_data(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            raise Exception(f"Falha ao carregar os dados  {response.status_code}")