grafo = {
    'A': [('B', 6), ('C', 8), ('D', 14)],
    'B': [('E', 6), ('C', 4), ('F', 2)],
    'C': [('J', 3), ('G', 7)],
    'D': [('D', 1), ('G', 8), ('H', 8)],
    'E': [('I', 2), ('F', 8)],
    'F': [('I', 9), ('J', 1), ('K', 6)],
    'G': [('B', 5), ('H', 11)],
    'H': [('J', 4), ('L', 2), ('K', 9)],
    'I': [('J', 3), ('L', 9)],
    'J': [('L', 6)],
    'K': [('L', 2)],
    'L': []  # Nodo objetivo
}
def escalada_simple(grafo, nodo_actual, nodo_objetivo):
    camino = [nodo_actual]
    distancia_total = 0

    while nodo_actual != nodo_objetivo:
        vecinos = grafo[nodo_actual]
        mejor_vecino = None
        mejor_distancia = 0  # Inicializar con 0 para encontrar la ruta más larga

        for vecino, distancia in vecinos:
            if distancia > mejor_distancia and vecino not in camino:
                mejor_vecino = vecino
                mejor_distancia = distancia

        if mejor_vecino is None:
            # No hay vecinos no visitados más lejanos al objetivo
            break

        camino.append(mejor_vecino)
        distancia_total += mejor_distancia
        nodo_actual = mejor_vecino

    if nodo_actual == nodo_objetivo:
        return camino, distancia_total
    else:
        return None, None



# Nodo inicial y objetivo
nodo_inicial = 'A'
nodo_objetivo = 'J'

# Encuentra el camino utilizando el algoritmo de escalada simple
camino, distancia = escalada_simple(grafo, nodo_inicial, nodo_objetivo)

if camino:
    print(f"Camino encontrado: {camino}")
    print(f"Distancia total: {distancia}")
else:
    print("No se encontró un camino al nodo objetivo.")
