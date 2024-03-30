# -*- coding: utf-8 -*-
#
# Descripción del problema:
#   Colocar n reinas en un tablero de ajedrez de tamaño n*n de forma
#   que las reinas no se amenacen según las normas del ajedrez
# Encontrar una o todas las soluciones posibles:
#   La solución debe ser de la forma S=(x1, x2, ..., xn)

import os, sys

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↓↓↓ \ Funciones Debug \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
# Representación visual de las soluciones encontradas
def visualizar_solucion() -> None:
    for solucion in soluciones:
        print("+---" * n + "+")
        for fila in range(n):
            for columna in range(n):
                print(f"| {casilla(solucion, fila, columna)} ", end="")
            print("|")
            print("+---" * n + "+")
        print()
    return

# Determina si la casilla tiene una reina
def casilla(solucion: list[int], fila: int, columna: int) -> str:
    if solucion[columna] == fila:
        return "Q"
    return "·"

# Imprimir soluciones en formato de lista
def imprimir_soluciones() -> None:
    longitud: int = len(str(len(soluciones)))
    for i in range(len(soluciones)):
        cantidad = longitud - len(str(i + 1))
        print("- \33[96mS" + "\33[90m0\33[96m" * cantidad + f"{str(i + 1)}\33[0m = (\33[90m", end="")
        print(*(soluciones[i]), sep="\33[0m, \33[90m", end="")
        print("\33[0m)")

# Calcular las posibilidades a analizar
def cantidad_posibilidades() -> int:
    posibilidades: int = pow(n, n)
    return posibilidades

# Calcular la posibilidad que está siendo analizada
def posibilidad_actual() -> int:
    global nivel, n
    posibilidad: int = 0
    for i in range(nivel + 1):
        posibilidad += pow(n, n - 1 - i) * solucion[i]
    return int(posibilidad)

# Barra de progreso
def debug_progreso() -> None:
    global estado
    porcentaje = int(100 * posibilidad_actual()/posibilidades)
    barra = "\33[93m" + "=" * int(porcentaje/2) + "\33[90m" + "-" * (50 - int(porcentaje/2)) + "\33[0m"
    borrar_linea()
    borrar_linea()
    print(f"\33[93mAnalizando posibilidades...\33[0m | \33[93m{str(porcentaje).rjust(3)}%\33[0m |" + barra + f"| \33[90m{posibilidad_actual()}\33[94m/{posibilidades}\33[0m" + f"\n\33[93mSoluciones encontradas: \33[90m{len(soluciones)}\33[0m")
    return

# Borrar última linea de la consola
def borrar_linea():
    sys.stdout.write('\x1b[1A')
    sys.stdout.write('\x1b[2K')
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↑↑↑ \ Funciones Debug \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #    
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↓↓↓ \ Datos iniciales \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
# Datos del problema
n = 9 # numero de filas y columnas del tablero

# Datos del algoritmo
nivel: int = 0
posibilidades: int = cantidad_posibilidades()
solucion: list[int] = [-1]
soluciones: list[list[int]] = []
finalizar: bool = False

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↑↑↑ \ Datos iniciales \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #    
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↓↓↓ \ Funciones \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
# Avanzar al siguiente valor se la solución
def probar_valor() -> bool:
    global nivel
    if solucion[nivel] < (n - 1):
        solucion[nivel] += 1
        return True
    else:
        return False

# Verificar si el valor es válido
def validar_valor() -> bool:
    global nivel
    for i in range(nivel):
        if solucion[i] == solucion[nivel]:
            return False
        elif i - solucion[i] == nivel - solucion[nivel]:
            return False
        elif i + solucion[i] == nivel + solucion[nivel]:
            return False
    return True

def agregar_solucion() -> None:
    soluciones.append([*solucion])
    return

# Avanzar de nivel
def nivel_siguiente() -> bool:
    global nivel
    if nivel < (n - 1):
        solucion.append(-1)
        nivel = nivel + 1
        return True
    return False

# Retroceder de nivel
def nivel_anterior() -> bool:
    global nivel
    if nivel > 0:
        solucion.pop()
        nivel = nivel - 1
        return True
    return False

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↑↑↑ \ Funciones \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #    
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↓↓↓ \ Algoritmo Exhaustivo \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
# Programa
def program() -> None:                          # Algoritmo Exhaustivo
    global finalizar
    while not finalizar:                        # Ejecutar hasta recorrer todas las soluciones
        if probar_valor():                      # Prueba el siguiente valor (Dentro del rango {0, 1, ..., n})
            debug_progreso()
            if validar_valor():                 # Verifica que se trate de un valor valido (La nueva pieza colocada no debe amenazar al resto)
                if not (nivel_siguiente()):     # Intenta avanzar al siguiente nivel. Si puede, lo hace. Si no puede, la solución está completa
                    agregar_solucion()          # Agrega la solución al conjunto de soluciones
        else:
            if not (nivel_anterior()):          # Intenta retroceder al siguiente nivel. Si puede, lo hace. Si no puede, se analizaron todas las posibilidades
                finalizar = True
    return
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↑↑↑ \ Algoritmo Exhaustivo \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #  
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↓↓↓ \ Ejecución \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
# Iniciar el programa
os.system("cls")
print(f"\33[94mProblema N-Reinas\n\33[91mTablero:\33[90m {n}x{n}\33[0m - \33[91mReinas:\33[90m {n}\33[0m")
print("\n")
program()
borrar_linea()
borrar_linea()
print(f"\33[92mAnalizando posibilidades...\33[0m | \33[92m100%\33[0m |\33[92m==================================================\33[0m| \33[94m{posibilidades}/{posibilidades}\33[0m")
print(f"\33[92mSoluciones encontradas: \33[90m{len(soluciones)}\33[0m")
input("Presione cualquier tecla para ver las soluciones...")
borrar_linea()
imprimir_soluciones()
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↑↑↑ \ Ejecución \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #