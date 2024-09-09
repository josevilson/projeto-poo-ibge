# fazer um request nos indicadores: 77836 e  77819
import requests


class DataExtractor:
    """
    Classe para extração de dados de indicadores de países usando a API do IBGE.

    Attributes:
        indicadores (list): Lista de códigos dos indicadores a serem consultados.
        paises (list): Lista de países cujos indicadores serão obtidos.
        url (str): URL gerada para fazer a requisição dos dados.
    """

    def __init__(self, indicadores: list, paises: list) -> None:
        """
        Inicializa o DataExtractor com indicadores e países fornecidos.

        Args:
            indicadores (list): Códigos dos indicadores a serem consultados.
            paises (list): Siglas dos países a serem consultados.
        """
        self.indicadores = indicadores
        self.paises = paises
        self.url = f"https://servicodados.ibge.gov.br/api/v1/paises/{
            self.paises}/indicadores/{self.indicadores}"

    def get_data(self) -> list:
        """
        Faz a requisição dos dados da API e retorna os resultados como uma lista de dicionários.

        Returns:
            list: Dados retornados da API.

        Raises:
            Exception: Se a requisição não for bem-sucedida.
        """
        response = requests.get(self.url)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            raise Exception(f"Falha ao carregar os dados. Código de status: {
                            response.status_code}")
