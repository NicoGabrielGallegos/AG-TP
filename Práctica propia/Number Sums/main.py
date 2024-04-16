import number_sums as ns
from number_sums import NumberSums
import os

os.system("cls")

tablero:NumberSums = NumberSums(7)

tablero.ingresar_encabezados([12,18,17,24,11,11,11],[10,23,25,11,2,9,24])
tablero.ingresar_elementos([[7,4,9,1,3,8,8],
                            [7,7,1,2,8,3,7],
                            [5,2,9,7,3,6,4],
                            [1,8,9,7,6,9,6],
                            [6,7,5,4,3,9,2],
                            [3,3,1,2,5,7,7],
                            [4,9,9,4,2,6,5]])

print(" ", end="")
print(tablero.encabezados_columnas)
print(tablero.encabezados_filas[0], end=" ")
print(tablero.elementos_interiores[0])
print(tablero.encabezados_filas[1], end=" ")
print(tablero.elementos_interiores[1])
print(tablero.encabezados_filas[2], end=" ")
print(tablero.elementos_interiores[2])
print(tablero.encabezados_filas[3], end=" ")
print(tablero.elementos_interiores[3])
print(tablero.encabezados_filas[4], end=" ")
print(tablero.elementos_interiores[4])
print(tablero.encabezados_filas[5], end=" ")
print(tablero.elementos_interiores[5])
print(tablero.encabezados_filas[6], end=" ")
print(tablero.elementos_interiores[6])
print()

tablero.descartar_numeros_mayores()

for j in range(10):
    for i in range(7):
        tablero.validar_objetivo_en_fila(i)
        tablero.validar_objetivo_en_columna(i)
    tablero.revalidar_estados_temporales()
    tablero.buscar_necesarios_triviales()

    print(f"Iteración {j+1}")
    print("   [0, 1, 2, 3, 4, 5, 6]")
    print(" 0", end="")
    print("\33[96m", tablero.estados_interiores[0], "\33[0m")
    print(" 1", end="")
    print("\33[96m", tablero.estados_interiores[1], "\33[0m")
    print(" 2", end="")
    print("\33[96m", tablero.estados_interiores[2], "\33[0m")
    print(" 3", end="")
    print("\33[96m", tablero.estados_interiores[3], "\33[0m")
    print(" 4", end="")
    print("\33[96m", tablero.estados_interiores[4], "\33[0m")
    print(" 5", end="")
    print("\33[96m", tablero.estados_interiores[5], "\33[0m")
    print(" 6", end="")
    print("\33[96m", tablero.estados_interiores[6], "\33[0m")

#x = tablero.suma_fila_validos_excepto(1, 1)
#print(x)
#x = tablero.suma_fila_necesarios(1)
#print(x)
#x = tablero.suma_fila_validos(1)
#print(x)
#x = tablero.suma_fila_validos_desde(1,3)
#print(x)
#x = tablero.suma_restante_fila(1)
#print(x)
#x = tablero.suma_especifica_fila(1, [0, 0, 1, 0, 0, 0, 1])
#print(x)

#tablero.imprimir_tablero()

#----------------------------------------------------------------

#tablero_peque:NumberSums = NumberSums(3)
#
#tablero_peque.ingresar_encabezados([6,7,11],[10,8,6])
#tablero_peque.ingresar_elementos([[1,5,6],
#                                  [8,3,4],
#                                  [9,7,2]])
#
#print("\n\n ", end="")
#print(tablero_peque.encabezados_columnas)
#print(tablero_peque.encabezados_filas[0], end=" ")
#print(tablero_peque.elementos_interiores[0])
#print(tablero_peque.encabezados_filas[1], end=" ")
#print(tablero_peque.elementos_interiores[1])
#print(tablero_peque.encabezados_filas[2], end="")
#print(tablero_peque.elementos_interiores[2])
#
#tablero_peque.descartar_numeros_mayores()
#
#print()
#print("   [0, 1, 2]")
#print(" 0 ", end="")
#print(tablero_peque.estados_interiores[0])
#print(" 1 ", end="")
#print(tablero_peque.estados_interiores[1])
#print(" 2 ", end="")
#print(tablero_peque.estados_interiores[2])
#
#
#tablero_peque.validar_objetivo_en_fila(0)
#tablero_peque.validar_objetivo_en_fila(1)
#tablero_peque.validar_objetivo_en_fila(2)
#
#tablero_peque.validar_objetivo_en_columna(0)
#tablero_peque.validar_objetivo_en_columna(1)
#tablero_peque.validar_objetivo_en_columna(2)
#
#print()
#print("   [0, 1, 2]")
#print(" 0 ", end="")
#print(tablero_peque.estados_interiores[0])
#print(" 1 ", end="")
#print(tablero_peque.estados_interiores[1])
#print(" 2 ", end="")
#print(tablero_peque.estados_interiores[2])