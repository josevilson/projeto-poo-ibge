import streamlit as st
import pandas as pd
import numpy as np
from utils.db_conn import string_connection_postgres
from src.get_data_sql import GetDataSql

query = "SELECT * FROM test"
df = GetDataSql(string_connection_postgres).get_data_sql_to_df(query)
df.Valor = df.Valor.astype(float)

# Título do app
st.title('Exibição DataFrame')

# Seleção do país e do indicador
paises_selecionados = st.selectbox('Selecione os Países', df['País'].unique())
indicador_selecionado = st.multiselect('Selecione o Indicador', df['Indicador'].unique())

if paises_selecionados and indicador_selecionado:

    # Filtrando os dados de acordo com os países e indicador selecionados
    dados_filtrados = df[(df['País'] == paises_selecionados) & (df['Indicador'].isin(indicador_selecionado))]


    # Criar um dataframe pivotado para mostrar os valores por país ao longo dos anos
    dados_filtrados