# %%
from src import DataTransform, DataExtractor, DataLoader
# from sqlite3 import SQLite

indicadores = "77836|77819"
paises = "AR|BR"

extractor = DataExtractor(indicadores=indicadores, paises=paises)
dados = extractor.get_data()


transform = DataTransform()
json = transform.data_to_json(dados)


df = transform.transform_to_dataframe()
print(df)
# %%
