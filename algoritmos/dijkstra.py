def dijkstra(grafo, inicio, fin, alpha, beta):

    nodos = grafo.obtener_nodos()
    costos = {nodo: float("inf") for nodo in nodos}
    anteriores = {}
    visitados = set()
    costos[inicio] = 0

    while True:
        nodo_actual = None
        menor_distancia = float("inf")

        #nodo mas barato conocido
        for nodo in nodos:
            if nodo not in visitados:
                if costos[nodo] < menor_distancia:
                    menor_distancia = costos[nodo]
                    nodo_actual = nodo

        # no hay nodo barato
        if nodo_actual is None:
            break
        
        #llegó al nodo final
        if nodo_actual == fin:
            break
        
        
        visitados.add(nodo_actual)
        
        #visitar vecinos
        for nodo in grafo.calles[nodo_actual]:
            
            vecino = nodo["para"]
            costo_arista = (alpha * float(nodo["dist"]) + beta * float(nodo["peligro"]))
            nuevo_costo = (costos[nodo_actual] + costo_arista)

            # si el cosoto nuevo, es menor al que ya tenia el vecino anters se actualiza
            if nuevo_costo < costos[vecino]:
                costos[vecino] = nuevo_costo
                anteriores[vecino] = nodo_actual

    ruta = []
    nodo = fin
    
    while nodo in anteriores:
        
        ruta.append(nodo)
        nodo = anteriores[nodo]
    
    ruta.append(inicio)

    ruta.reverse()

    return {
        "ruta": ruta,
        "costos": costos,
        "visitados": visitados
    }