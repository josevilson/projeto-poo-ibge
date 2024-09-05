# %%
import os

import streamlit as st

from src.extract import DataExtractor
from src.load import DataBaseSQLite3
from src.transform import DataTransform
from utils.data_api import todos_indicadores, todos_paises
from utils.utils import ajustar_selecao

st.set_page_config(layout="wide")
paises_selecionados = st.multiselect(label="Selecione os paises de interesse.",
                                     placeholder='Selecione os paises',
                                     options=todos_paises,
                                     default=['BR - Brasil'])


username_postgres = os.environ['POSTGRES_USERNAME']
password_postgres = os.environ['POSTGRES_PASSWORD']
host_postgres = os.environ['POSTGRES_HOST']
port_postgres = os.environ['POSTGRES_PORT']
dbname_postgres = os.environ['POSTGRES_DB']

string_connection_postgres = f'postgresql+psycopg2://{username_postgres}:{
    password_postgres}@{host_postgres}:{port_postgres}/{dbname_postgres}'
st.write(string_connection_postgres)


if len(paises_selecionados) >= 1:
    paises_ajustado = ajustar_selecao(paises_selecionados)
    paises_pipe = '|'.join(paises_ajustado)
    st.write(paises_pipe)

indicadores_selecionados = st.multiselect(label="Selecione os indicadores de interesse.",
                                          placeholder='Selecione os indicadores',
                                          options=todos_indicadores)


if len(indicadores_selecionados) >= 1:
    indicadores_ajustado = ajustar_selecao(indicadores_selecionados)
    indicadores_pipe = '|'.join(indicadores_ajustado)


def start():
    extractor = DataExtractor(
        indicadores=indicadores_pipe, paises=paises_pipe)
    dados = extractor.get_data()
    transform = DataTransform()
    json = transform.data_to_json(dados)
    df = transform.transform_to_dataframe()
    df
    return df


# indicadores = "77836|77819"
if paises_selecionados and indicadores_selecionados:
    if st.button("Processar dados 🚀"):
        df = start()

        DataBaseSQLite3(string_connection_postgres).send_dataframe_to_database(
            dataframe=df, table_name='test')

    # # transform

    # # load
    # DataBaseSQLite3('db_ibge.db').send_dataframe_to_database(
    #     dataframe=df, table_name='test')

else:
    st.write("Selecione os dados para continuar.")


# # %%
