import streamlit as st
import pandas as pd
import numpy as np
from utils.db_conn import string_connection_postgres
from src.get_data_sql import GetDataSql


query = "SELECT * FROM test"
df = GetDataSql(string_connection_postgres).get_data_sql_to_df(query)
df.Valor = df.Valor.astype(float)

# Título do app
st.title('Análise de Indicadores')

# Seleção do país e do indicador
paises = df['País'].unique()
indicadores = df['Indicador'].unique()

paises_selecionados = st.multiselect('Selecione os Países', paises)
indicador_selecionado = st.selectbox('Selecione o indicador', indicadores)

if paises_selecionados and indicador_selecionado:
    # Filtrar os dados
    dados_filtrados = df[(df['País'].isin(paises_selecionados)) & (df['Indicador'] == indicador_selecionado)]

    # Pivotar os dados para exibir os países em colunas
    dados_pivot = dados_filtrados.pivot(index='Ano', columns='País', values='Valor')

    # Gráfico de Linha - Evolução ao longo dos anos
    st.subheader(f'Evolução do {indicador_selecionado} nos países selecionados ao longo dos anos')
    st.line_chart(dados_pivot)

    # Gráfico de Barras - Comparação entre os anos
    st.subheader(f'Comparação do {indicador_selecionado} nos países selecionados entre os anos')
    st.bar_chart(dados_pivot)