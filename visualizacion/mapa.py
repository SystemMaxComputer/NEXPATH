import folium
from algoritmos.dijkstra import dijkstra

import folium

def visualizar_ruta(dijkstra_res: dict, inicio: tuple, nombre_archivo="index.html"):
    
    centro_mapa = [inicio[1], inicio[0]]
    m = folium.Map(location=centro_mapa, zoom_start=14)

    ruta_original = dijkstra_res["ruta"]


    ruta_folium = [[coord[1], coord[0]] for coord in ruta_original]


    if ruta_folium:
        folium.Marker(
            location=ruta_folium[0],
            popup="Inicio de la ruta",
            icon=folium.Icon(color="green", icon="play")
        ).add_to(m)
        
        folium.Marker(
            location=ruta_folium[-1],
            popup="Destino final",
            icon=folium.Icon(color="red", icon="stop")
        ).add_to(m)

    folium.PolyLine(
        locations=ruta_folium, 
        tooltip="RUTA ÓPTIMA", 
        color="blue", 
        weight=5, 
        opacity=0.8
    ).add_to(m)

    m.save(nombre_archivo)
    print(f"Mapa guardado exitosamente como '{nombre_archivo}'")
    return m