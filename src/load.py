from sqlalchemy import create_engine
import pandas as pd

class DataBaseSQLite3:
    """
    Classe para interagir com um banco de dados SQLite3 e enviar um DataFrame para uma tabela.

    Attributes:
        db_name (str): Nome ou caminho do banco de dados SQLite3.
    """

    def __init__(self, db_name: str) -> None:
        """
        Inicializa a classe DataBaseSQLite3 com o nome do banco de dados.

        Args:
            db_name (str): O nome ou caminho do banco de dados SQLite3.
        """
        self.db_name = db_name

    def send_dataframe_to_database(self, dataframe: pd.DataFrame, table_name: str = '') -> None:
        """
        Envia um DataFrame para uma tabela no banco de dados SQLite3.

        Args:
            dataframe (pd.DataFrame): O DataFrame a ser enviado para o banco de dados.
            table_name (str): O nome da tabela onde os dados serão armazenados. Se não for fornecido, uma tabela padrão será usada.

        Returns:
            None
        """
        db = self.db_name
        db_engine = create_engine(f'{db}')
        dataframe.to_sql(name=table_name, con=db_engine, if_exists='replace', index=False)
