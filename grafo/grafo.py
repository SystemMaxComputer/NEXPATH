# Creamos clase grafo, implementado como lista de adyacencia

class Grafo:
    """
    Construccion del grafo
    
    cada nodo es un coordenada
    y sus vecinos un diccionario 
    """
    def __init__(self):
        self.calles = {}
    
    def insertar_nodo(self, nodo):
        self.calles[nodo] = []
    
    def crear_interseccion(self, origin, destination, length, oneway, harassment_risk, geometry):
        oneway = oneway == "True"
        
        if origin not in self.calles:
            self.calles[origin] = []
            
        if destination not in self.calles:
            self.calles[destination] = []
        
        self.calles[origin].append({"para": destination,
                                    "dist": length, 
                                    "peligro": harassment_risk,
                                    "geometria": geometry})
        if oneway is False:
            self.calles[destination].append({"para": origin,
                                    "dist": length, 
                                    "peligro": harassment_risk,
                                    "geometria": geometry})
        return None

    def obtener_nodos(self):
        return list(self.calles.keys())