from sqlalchemy import create_engine
import pandas as pd

class GetDataSql:
    """
    Classe para obter dados de um banco de dados SQL e convertê-los para um DataFrame do pandas.

    Attributes:
        db_name (str): Nome ou URL de conexão do banco de dados.
    """

    def __init__(self, db_name: str) -> None:
        """
        Inicializa a classe GetDataSql com o nome ou URL do banco de dados.

        Args:
            db_name (str): String contendo o nome ou URL de conexão do banco de dados.
        """
        self.db_name = db_name

    def get_data_sql_to_df(self, query: str) -> pd.DataFrame:
        """
        Executa uma query SQL e retorna os dados em formato de DataFrame do pandas.

        Args:
            query (str): A query SQL a ser executada.

        Returns:
            pd.DataFrame: O resultado da query em formato de DataFrame.
        """
        db = self.db_name
        db_engine = create_engine(f'{db}')
        df = pd.read_sql(query, db_engine)
        return df
