
# Projeto ETL com Visualização usando Streamlit

[Fontes: Indicadores dos paises - ONU/IBGE] (https://servicodados.ibge.gov.br/api/docs/paises)

## Descrição

Este projeto implementa um pipeline ETL (Extração, Transformação e Carga) com visualização de dados em tempo real utilizando o Streamlit. O objetivo é fornecer uma solução completa para a extração de dados de APIs e bancos de dados, transformá-los utilizando Python e Pandas, carregá-los em um Data Warehouse e, finalmente, disponibilizá-los em uma aplicação web interativa usando o Streamlit.

## Arquitetura

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

## Instalação

### Pré-requisitos

- Python 3.8+
- PostgreSQL instalado e configurado
- Pacotes Python necessários (Pandas, Streamlit, psycopg2, requests)

### Passos

1. Clone o repositório:

```bash
git clone https://github.com/seuusuario/etl-streamlit-project.git
cd etl-streamlit-project
```

2. Crie um ambiente virtual e ative-o:

```bash
python -m venv venv
source venv/bin/activate  # No Windows use: venv\Scripts\activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Configure as variáveis de ambiente no arquivo `.env` para suas credenciais do PostgreSQL e da API.

5. Execute o pipeline de ETL:

```bash
python etl_pipeline.py
```

6. Para iniciar a aplicação Streamlit, execute o comando:

```bash
streamlit run app.py
```

## Como Funciona

- O script de ETL (`etl_pipeline.py`) executa a extração dos dados das fontes configuradas, transforma os dados conforme necessário e os carrega no Data Warehouse.
- A aplicação Streamlit (`app.py`) lê os dados do Data Warehouse e os exibe de maneira interativa.

## Contribuição

1. Faça um fork do projeto.
2. Crie sua feature branch (`git checkout -b feature/nova-feature`).
3. Commit suas alterações (`git commit -am 'Adiciona nova feature'`).
4. Envie para o branch (`git push origin feature/nova-feature`).
5. Crie um novo Pull Request.

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.
