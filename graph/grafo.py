# Creamos clase grafo, implementado como lista de adyacencia

def _parse_bool(value):
    """
    Convierte varios tipos de entrada a booleano de forma consistente.
    
    Args:
        value: Puede ser bool, str, int, float, o None
        
    Returns:
        bool: True si el valor representa verdad, False si representa falsedad
        
    Raises:
        ValueError: Si el valor no puede ser convertido a booleano
    """
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        return value.lower() in ("true", "1", "yes", "y", "t")
    if isinstance(value, (int, float)):
        return bool(value)
    if value is None:
        return False
    raise ValueError(f"No se puede convertir {value} de tipo {type(value)} a booleano")

class Grafo:
    """
    Construccion del grafo
    
    cada nodo es una coordenada
    y sus vecinos un diccionario 
    """
    def __init__(self):
        self.calles = {}
    
    def insertar_nodo(self, nodo):
        self.calles[nodo] = []
    
    def crear_interseccion(self, name, origin, destination, length, oneway, harassment_risk, geometry):
        oneway = _parse_bool(oneway)
        
        if origin not in self.calles:
            self.calles[origin] = []
            
        if destination not in self.calles:
            self.calles[destination] = []
        
        self.calles[origin].append({"para": destination,
                                    "dist": length, 
                                    "peligro": harassment_risk,
                                    "nombre": name,
                                    "geometria": geometry})
        if oneway is False:
            self.calles[destination].append({"para": origin,
                                    "dist": length, 
                                    "peligro": harassment_risk,
                                    "nombre": name,
                                    "geometria": geometry})
        return None

    def obtener_nodos(self):
        return self.calles.keys()

    def __repr__(self):
        return str(self.calles.keys())