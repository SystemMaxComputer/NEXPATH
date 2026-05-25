"""
Punto de entrada principal del proyecto NEXPATH.
Orquesta la carga de datos, construcción del grafo, ejecución de algoritmos y visualización.
"""

import sys
from typing import Optional

import config
from datos import save_data
from utils import construir_grafo_desde_datos, validar_coordenada
from algoritmos import dijkstra
from visualizacion import visualizar_ruta


def cargar_datos(ruta_csv: Optional[str] = None) -> object:
    """
    Carga los datos del archivo CSV.
    
    Args:
        ruta_csv: Ruta al archivo CSV. Si es None, usa la ruta por defecto.
        
    Returns:
        DataFrame de pandas con los datos cargados
    """
    ruta = ruta_csv or str(config.CSV_PATH)
    print(f"Cargando datos desde: {ruta}")
    return save_data(ruta)


def ejecutar_busqueda_ruta(
    inicio: tuple = None,
    fin: tuple = None,
    alpha: float = None,
    beta: float = None
) -> dict:
    """
    Ejecuta el pipeline completo de búsqueda de ruta óptima.
    
    Args:
        inicio: Coordenadas de inicio (lon, lat). Si es None, usa valor por defecto.
        fin: Coordenadas de destino (lon, lat). Si es None, usa valor por defecto.
        alpha: Peso para distancia. Si es None, usa valor por defecto.
        beta: Peso para riesgo de acoso. Si es None, usa valor por defecto.
        
    Returns:
        Diccionario con el resultado de la búsqueda de ruta
    """
    # Usar valores por defecto de configuración si no se proporcionan
    inicio = inicio or config.DEFAULT_ORIGIN
    fin = fin or config.DEFAULT_DESTINATION
    alpha = alpha or config.DEFAULT_ALPHA
    beta = beta or config.DEFAULT_BETA
    
    # Validar coordenadas
    if not validar_coordenada(inicio):
        raise ValueError(f"Coordenadas de inicio inválidas: {inicio}")
    if not validar_coordenada(fin):
        raise ValueError(f"Coordenadas de destino inválidas: {fin}")
    
    print(f"\n--- Configuración ---")
    print(f"Inicio: {inicio}")
    print(f"Destino: {fin}")
    print(f"Alpha (distancia): {alpha}")
    print(f"Beta (riesgo): {beta}")
    
    # Cargar datos
    print(f"\n--- Carga de Datos ---")
    try:
        datos = cargar_datos()
        print(f"Datos cargados exitosamente: {len(datos)} registros")
    except Exception as e:
        print(f"Error cargando datos: {e}")
        sys.exit(1)
    
    # Construir grafo
    print(f"\n--- Construcción del Grafo ---")
    try:
        grafo = construir_grafo_desde_datos(datos)
        print(f"Grafo construido con {len(list(grafo.obtener_nodos()))} nodos")
    except Exception as e:
        print(f"Error construyendo grafo: {e}")
        sys.exit(1)
    
    # Ejecutar algoritmo
    print(f"\n--- Búsqueda de Ruta Óptima ---")
    try:
        resultado = dijkstra(grafo, inicio, fin, alpha, beta)
        print(f"Ruta encontrada con {len(resultado['ruta'])} nodos")
        print(f"Costo total: {resultado['costos'].get(fin, 'N/A')}")
    except Exception as e:
        print(f"Error ejecutando algoritmo: {e}")
        sys.exit(1)
    
    return resultado


def main():
    """
    Función principal que orquesta todo el pipeline.
    """
    print("=" * 60)
    print("NEXPATH - Rutas Óptimas y Seguras en Medellín")
    print("=" * 60)
    
    try:
        # Ejecutar búsqueda con valores por defecto
        resultado = ejecutar_busqueda_ruta()
        
        # Visualizar resultados
        print(f"\n--- Visualización ---")
        try:
            visualizar_ruta(
                resultado,
                config.DEFAULT_ORIGIN,
                nombre_archivo=str(config.DEFAULT_OUTPUT_FILE)
            )
            print(f"Mapa generado exitosamente: {config.DEFAULT_OUTPUT_FILE}")
        except Exception as e:
            print(f"Error generando visualización: {e}")
            sys.exit(1)
        
        print("\n" + "=" * 60)
        print("Proceso completado exitosamente")
        print("=" * 60)
        
    except KeyboardInterrupt:
        print("\n\nProceso interrumpido por el usuario")
        sys.exit(0)
    except Exception as e:
        print(f"\nError inesperado: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
