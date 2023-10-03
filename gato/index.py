# Representación del tablero del Gato
def inicializar_tablero():
    tablero = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    tablero[0] = "O"
    tablero[2] = "O"
    tablero[4] = "X"
    tablero[5] = "O"
    tablero[8] = "X"
    return tablero

# Función para imprimir el tablero
def imprimir_tablero(tablero):
    print(tablero[0] + " | " + tablero[1] + " | " + tablero[2])
    print("--+---+--")
    print(tablero[3] + " | " + tablero[4] + " | " + tablero[5])
    print("--+---+--")
    print(tablero[6] + " | " + tablero[7] + " | " + tablero[8])

# Función para verificar si el juego ha terminado
def juego_terminado(tablero):
    # Verificar filas, columnas y diagonales
    lineas_ganadoras = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for linea in lineas_ganadoras:
        if tablero[linea[0]] == tablero[linea[1]] == tablero[linea[2]] != " ":
            return True
    # Verificar empate
    if " " not in tablero:
        return True
    return False

# Función Minimax
def minimax(tablero, profundidad, es_maximizando):
    # Caso base: el juego ha terminado o se alcanza la profundidad máxima
    if juego_terminado(tablero) or profundidad == 0:
        # Calcular la puntuación del tablero
        if juego_terminado(tablero) and es_maximizando:
            return -1
        elif juego_terminado(tablero) and not es_maximizando:
            return 1
        else:
            return 0
    
    # Nodo Max (jugador que maximiza)
    if es_maximizando:
        mejor_valor = float("-inf")
        for i in range(9):
            if tablero[i] == " ":
                tablero[i] = "O"
                valor = minimax(tablero, profundidad - 1, False)
                tablero[i] = " "
                mejor_valor = max(mejor_valor, valor)
        return mejor_valor
    
    # Nodo Min (jugador que minimiza)
    else:
        mejor_valor = float("inf")
        for i in range(9):
            if tablero[i] == " ":
                tablero[i] = "X"
                valor = minimax(tablero, profundidad - 1, True)
                tablero[i] = " "
                mejor_valor = min(mejor_valor, valor)
        return mejor_valor

# Función para realizar la mejor jugada usando Minimax
def mejor_jugada(tablero):
    mejor_valor = float("-inf")
    mejor_movimiento = -1
    for i in range(9):
        if tablero[i] == " ":
            tablero[i] = "O"
            valor = minimax(tablero, 4, False)  # Profundidad de búsqueda
            tablero[i] = " "
            if valor > mejor_valor:
                mejor_valor = valor
                mejor_movimiento = i
    return mejor_movimiento

# Juego principal
tablero = inicializar_tablero()

while not juego_terminado(tablero):
    imprimir_tablero(tablero)
    movimiento_jugador = int(input("Ingrese su movimiento (1-9): ")) - 1
    if tablero[movimiento_jugador] == " ":
        tablero[movimiento_jugador] = "X"
        if not juego_terminado(tablero):
            mejor_movimiento = mejor_jugada(tablero)
            tablero[mejor_movimiento] = "O"
    else:
        print("¡Movimiento inválido! Inténtelo de nuevo.")

# Mostrar el resultado del juego
imprimir_tablero(tablero)
if juego_terminado(tablero) and not (" " in tablero):
    print("¡Empate!")
elif juego_terminado(tablero) and ("X" in tablero):
    print("¡Has ganado!")
else:
    print("¡Has perdido!")