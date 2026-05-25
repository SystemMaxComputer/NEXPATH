"""
Configuración centralizada del proyecto NEXPATH.
"""

from pathlib import Path
from typing import Tuple

# Rutas de archivos
BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "datos"
CSV_PATH = DATA_DIR / "calles_de_medellin_con_acoso.csv"
OUTPUT_DIR = BASE_DIR
DEFAULT_OUTPUT_FILE = OUTPUT_DIR / "index.html"

# Parámetros de algoritmos
DEFAULT_ALPHA = 1.0  # Peso para distancia
DEFAULT_BETA = 1.0   # Peso para riesgo de acoso

# Coordenadas por defecto (Medellín)
DEFAULT_ORIGIN: Tuple[float, float] = (-75.598766, 6.2320727)
DEFAULT_DESTINATION: Tuple[float, float] = (-75.5705202, 6.2106275)

# Configuración de visualización
MAP_ZOOM_START = 14
MARKER_START_COLOR = "green"
MARKER_START_ICON = "play"
MARKER_END_COLOR = "red"
MARKER_END_ICON = "stop"
ROUTE_COLOR = "blue"
ROUTE_DASH_ARRAY = [50, 10]
