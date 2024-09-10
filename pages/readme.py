import streamlit as st

readme = '''
# Projeto ETL com Visualização usando Streamlit

[Link do projeto (Deploy) 🚀](https://onu-paises.streamlit.app/)


[Fontes: Indicadores dos paises - ONU/IBGE](https://servicodados.ibge.gov.br/api/docs/paises)

## Descrição

Este projeto implementa um pipeline ETL (Extração, Transformação e Carga) com visualização de dados em tempo real utilizando o Streamlit. O objetivo é fornecer uma solução completa para a extração de dados de APIs e bancos de dados, transformá-los utilizando Python e Pandas, carregá-los em um Data Warehouse e, finalmente, disponibilizá-los em uma aplicação web interativa usando o Streamlit.

## Arquitetura

![Arquitetura do projeto](https://github.com/josevilson/projeto-poo-ibge/raw/main/img/arquitetura.png)

A arquitetura do projeto segue o processo tradicional de ETL e é dividida em três partes principais:

1. **Extração (Extract)**:
   - Fonte de dados: APIs e Banco de Dados.
   - As informações são coletadas de APIs externas e bases de dados relacionais para serem processadas.
   
2. **Transformação (Transform)**:
   - Ferramentas: Python, Pandas.
   - Os dados extraídos são processados e transformados usando scripts em Python, com apoio da biblioteca Pandas, para realizar a limpeza, agregação, e outras transformações necessárias.
   
3. **Carga (Load)**:
   - Destino: Data Warehouse (ex: PostgreSQL).
   - Os dados transformados são então carregados para um armazém de dados, garantindo a persistência e integridade da informação.

4. **Visualização**:
   - Ferramenta: Streamlit.
   - A aplicação web Streamlit permite a visualização dos dados processados e insights em tempo real, tornando os dados acessíveis de forma interativa para o usuário final.

## Tecnologias Utilizadas

- **Python**: Linguagem principal usada para realizar as transformações de dados.
- **Pandas**: Biblioteca Python para manipulação e análise de dados.
- **PostgreSQL**: Usado como o Data Warehouse para armazenar os dados processados.
- **APIs**: Fontes externas de dados que alimentam o pipeline de extração.
- **Streamlit**: Framework para a criação de aplicações web para visualização de dados em tempo real.


'''

st.markdown(readme)
