import streamlit as st

username_postgres = st.secrets['POSTGRES_USERNAME']
password_postgres = st.secrets['POSTGRES_PASSWORD']
host_postgres = st.secrets['POSTGRES_HOST']
port_postgres = st.secrets['POSTGRES_PORT']
dbname_postgres = st.secrets['POSTGRES_DB']

string_connection_postgres = f'postgresql+psycopg2://{username_postgres}:{
    password_postgres}@{host_postgres}:{port_postgres}/{dbname_postgres}'