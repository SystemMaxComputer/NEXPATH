"""
Utilidades reutilizables del proyecto NEXPATH.
"""

import pandas as pd
from typing import Tuple
from graph.grafo import Grafo


def coord_a_tupla(coord_str: str) -> Tuple[float, float]:
    """
    Convierte una cadena de coordenadas en formato "(lon, lat)" a una tupla de floats.
    
    Args:
        coord_str: String con coordenadas en formato "(lon, lat)"
        
    Returns:
        Tupla (longitud, latitud) como floats
        
    Raises:
        ValueError: Si el formato es incorrecto
    """
    try:
        coord_str = coord_str.strip("()")
        lon, lat = coord_str.split(",")
        return (float(lon), float(lat))
    except (ValueError, AttributeError) as e:
        raise ValueError(f"Formato de coordenada inválido: {coord_str}") from e


def validar_coordenada(coord: Tuple[float, float]) -> bool:
    """
    Valida que una coordenada esté en rangos geográficos razonables.
    
    Args:
        coord: Tupla (longitud, latitud)
        
    Returns:
        True si la coordenada es válida, False en caso contrario
    """
    lon, lat = coord
    # Rangos aproximados para Medellín y alrededores
    return -76.0 <= lon <= -75.0 and 6.0 <= lat <= 6.5


def construir_grafo_desde_datos(datos: pd.DataFrame) -> Grafo:
    """
    Construye un grafo a partir de un DataFrame con datos de calles.
    
    Args:
        datos: DataFrame de pandas con columnas: name, origin, destination, 
               length, oneway, harassmentRisk, geometry
               
    Returns:
        Instancia de Grafo poblada con los datos
    """
    grafo = Grafo()
    
    for _, fila in datos.iterrows():
        try:
            origen = coord_a_tupla(fila["origin"])
            destino = coord_a_tupla(fila["destination"])
            
            grafo.crear_interseccion(
                name=fila["name"],
                origin=origen,
                destination=destino,
                length=float(fila["length"]),
                oneway=fila["oneway"],
                harassment_risk=float(fila["harassmentRisk"]),
                geometry=fila["geometry"]
            )
        except (ValueError, KeyError) as e:
            print(f"Advertencia: Error procesando fila {_}: {e}")
            continue
    
    return grafo
