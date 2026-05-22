# Tenés un grafo dirigido con 5 nodos (A, B, C, D, E) y las siguientes aristas:
# A→B (−1) · A→C (4) · B→C (3) · B→D (2) · B→E (2) · D→B (1) · D→C (5) · E→D (−3)
# Desde el origen A: ¿cuáles son las distancias mínimas a todos los nodos? 
# ¿Hay ciclo negativo? 
# Implementalo en código y verificá.

grafo = [("A","B",-1), ("A","C",4), ("B","C",3), ("B","D",2), ("B","E", 2), ("D","B",1), ("D","C", 5), ("E","D", -3)]
def Bellman_Ford(grafo: list[tuple[str, str, str]], origen: str, destino:str ):
    nodos = set()
    for desde, hasta,_ in grafo:
        nodos.add(desde)
        nodos.add(hasta)
    distancias = {}
    if origen not in nodos:
        return f"No se puede"
    predecesores = {}

    for nodo in nodos:
        predecesores[nodo] = None
        if nodo == origen:
            distancias[nodo] = 0
        else:
            distancias[nodo] = float('inf')
    
    n = len(distancias)

    for _ in range(n - 1):
        viejo = distancias.copy()
        for desde, hasta, peso in grafo:
            if distancias[desde] + peso < distancias[hasta]:
                predecesores[hasta] = desde
                distancias[hasta] = distancias[desde] + peso

        if viejo == distancias:
            return distancias, predecesores
        
    for desde, hasta, peso in grafo:
        if distancias[desde] + peso < distancias[hasta]:
            return False
    
    return distancias, predecesores

def reconstruir_camino(grafo, origen, destino):

    distancias, predecesores = Bellman_Ford(grafo, origen, destino)
    if not distancias:
        return f"Hay ciclo negativo."
    nodo_actual = destino
    camino = ""
    while nodo_actual != None:
        if len(camino) == 0:
            camino = nodo_actual
            nodo_actual = predecesores[nodo_actual] 
        else:

            camino = nodo_actual+"->"+camino
            nodo_actual = predecesores[nodo_actual] 
    return camino, distancias


print(reconstruir_camino(grafo, "A", "D"))