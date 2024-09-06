from sqlalchemy import create_engine
import pandas as pd


class GetDataSql:

    def __init__(self, db_name):

        self.db_name = db_name

    def get_data_sql_to_df(
        self,
        query):
    

        db = self.db_name
        db_engine = create_engine(f'{db}')
        df = pd.read_sql(query, db_engine)
        return df
