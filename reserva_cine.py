# Tarea Semana 12: Reserva de un asiento en sala de cine
# Objetivo: gestionar la reserva de asientos de una sala de cine de 3 filas x 4 columnas
# 0 = asiento libre, 1 = asiento reservado

FILAS = 3
COLUMNAS = 4

# Crear la matriz de asientos inicializada en 0 (todos libres)
asientos = [[0 for _ in range(COLUMNAS)] for _ in range(FILAS)]

print("SISTEMA DE RESERVA DE ASIENTOS - SALA DE CINE")
print(f"La sala tiene {FILAS} filas (0 a {FILAS - 1}) y {COLUMNAS} columnas (0 a {COLUMNAS - 1})\n")

# Pedir al usuario la fila y la columna del asiento a reservar
fila = int(input(f"Ingrese fila (0 a {FILAS - 1}): "))
columna = int(input(f"Ingrese columna (0 a {COLUMNAS - 1}): "))

# Validar que la fila y la columna estén dentro del rango permitido
if fila < 0 or fila >= FILAS or columna < 0 or columna >= COLUMNAS:
    print("\nError: la fila o la columna ingresada está fuera de rango.")
elif asientos[fila][columna] == 1:
    print(f"\nEl asiento [{fila}][{columna}] ya estaba reservado.")
else:
    # Marcar el asiento como reservado
    asientos[fila][columna] = 1
    print(f"\nAsiento [{fila}][{columna}] reservado con éxito.")

# Mostrar el estado completo de la sala recorriendo la matriz con bucles anidados
print("\nEstado de la sala:")
for i in range(FILAS):
    for j in range(COLUMNAS):
        print(asientos[i][j], end=" ")
    print()
