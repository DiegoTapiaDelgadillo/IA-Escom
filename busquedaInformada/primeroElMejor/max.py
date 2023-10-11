grafo = {
    'A': [('B', 6), ('C', 8), ('D', 14)],
    'B': [('E', 6), ('C', 4), ('F', 2)],
    'C': [('J', 3), ('G', 7)],
    'D': [('G', 8), ('H', 8)],
    'E': [('I', 2), ('F', 8)],
    'F': [('I', 9), ('J', 1), ('K', 6)],
    'G': [('B', 5), ('H', 11)],
    'H': [('J', 4), ('L', 2), ('K', 9)],
    'I': [('J', 3), ('L', 9)],
    'J': [('L', 6)],
    'K': [('L', 2)],
    'L': []  # Nodo objetivo
}

def primero_el_mejor(grafo, nodo_actual, nodo_objetivo, visitados):
    if nodo_actual == nodo_objetivo:
        return [nodo_actual]
    if nodo_actual not in visitados:
        visitados.add(nodo_actual)
        vecinos = grafo[nodo_actual]
        if not vecinos:
            return None
        vecinos.sort(key=lambda x: x[1], reverse=True)  # Ordenar vecinos por el costo más alto
        for vecino in vecinos:
            siguiente_nodo = vecino[0]
            camino_restante = primero_el_mejor(grafo, siguiente_nodo, nodo_objetivo, visitados)
            if camino_restante is not None:
                return [nodo_actual] + camino_restante
    return None

nodo_inicial = 'A'
nodo_objetivo = 'J'
visitados = set()
camino = primero_el_mejor(grafo, nodo_inicial, nodo_objetivo, visitados)

if camino:
    print("Camino encontrado:", "->".join(camino))
else:
    print("No se encontró un camino al nodo objetivo.")
