# %%
from src import DataTransform, DataExtractor, DataLoader

indicadores = "77836|77819"
paises = "AR|BR"

extractor = DataExtractor(indicadores=indicadores, paises=paises)
dados = extractor.get_data()
# %%
