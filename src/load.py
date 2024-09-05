import os

from sqlalchemy import create_engine


class DataBaseSQLite3:

    def __init__(self, db_name):

        self.db_name = db_name

    def send_dataframe_to_database(
        self,
        dataframe,
        table_name='',
    ):

        db = self.db_name
        db_engine = create_engine(f'{db}')

        # Store DataFrame in SQLite
        dataframe.to_sql(
            name=table_name,
            con=db_engine,
            if_exists='replace',
            index=False
        )

        # connection = sqlite3.connect(self.db_name)

        # print(connection.total_changes)
