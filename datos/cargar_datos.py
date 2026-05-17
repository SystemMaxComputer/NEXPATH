import geopandas as gpd

#leer datos
datos = gpd.read_file('datos\calles_de_medellin_con_acoso.csv', encoding='utf-8')
