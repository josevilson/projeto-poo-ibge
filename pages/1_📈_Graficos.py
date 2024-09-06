import streamlit as st
import pandas as pd
import numpy as np
from utils.db_conn import string_connection_postgres
from src.get_data_sql import GetDataSql


query = "SELECT * FROM test"
df = GetDataSql(string_connection_postgres).get_data_sql_to_df(query)

# Título do app
st.title('Análise de Indicadores')

# Seleção do país e do indicador
paises = df['País'].unique()
indicadores = df['Indicador'].unique()

pais_selecionado = st.selectbox('Selecione o país', paises)
indicador_selecionado = st.selectbox('Selecione o indicador', indicadores)

# Filtrar os dados
dados_filtrados = df[(df['País'] == pais_selecionado) & (df['Indicador'] == indicador_selecionado)]

# Gráfico de Linha - Evolução ao longo dos anos
st.subheader(f'Evolução do {indicador_selecionado} no {pais_selecionado} ao longo dos anos')
st.line_chart(data=dados_filtrados.set_index('Ano')['Valor'])

# Gráfico de Barras - Comparação entre os anos
st.subheader(f'Comparação do {indicador_selecionado} no {pais_selecionado} entre os anos')
st.bar_chart(data=dados_filtrados.set_index('Ano')['Valor'])