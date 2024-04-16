# -*- coding: latin-1 -*-
#
# Buscar un máximo de la función:
# coef = 2^30 - 1
# f(x) = x/(coef)^2	,	Dom = [0, 2^30 - 1]
#
# Datos:
# - Prob. Crossover = 0.75
# - Prob. Mutación = 0.05
# - Población Inicial = 10
# - Ciclos = 20
# - Tipo Selección = Ruleta
# - Tipo Crossover = 1 Punto
# - Tipo Mutación = Invertida
#
# Salida por Excel:
# - Cromosoma correspontiente al valor máximo obtenido
# - Gráfica de Suma
# - Gráfica de Máx
# - Gráfica de Mín
# - Gráfica de Promedio

                                # Usado para:
import os                       # Limpiar la consola
from random import randint      # Generar numero entero aleatorio
from random import random       # Generar numero flotante en [0, 1)
from random import getrandbits  # Generar número entero aleatorio bit a bit
import numpy as np              # Seleccion de ruleta basada en probabilidades
from openpyxl import Workbook   # Crear el documento xlsx
import agxl                     # Modulo propio para manipular rapidamente el documento xlsx

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↓↓↓ \ Funciones Debug \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
def debug_poblacion_inicial(poblacion):
    for individuo in poblacion:
        print(str(format(individuo, "010d")) + "\t" + format(individuo, "030b"))

def debug_evaluaciones(evaluaciones):
    sumatoria = 0
    for evaluacion in evaluaciones:
        print(format(evaluacion, ".10f"))
        sumatoria += evaluacion
    print("\nSuma total de las evaluaciones: " + str(sumatoria))

def debug_generacion(poblacion, evaluaciones):
    sumatoria = 0
    print("Individuo | Cromosoma  | Cromosoma (binario)            | Fitness")
    for i in range(cantidad_individuos):
        print("----------+------------+--------------------------------+-------------")
        print(str(format(i, "9d")) + " | " + str(format(poblacion[i], "010d")) + " | " + format(poblacion[i], "030b") + " | " + format(evaluaciones[i], ".10f"))
        sumatoria += evaluaciones[i]
    print("----------+------------+--------------------------------+-------------")
    print("Total".rjust(9) + " |            |                                | " + format(sumatoria, "012.10f"))

def debug_ciclos(ciclo):
    porcentaje = int(100 * (ciclo/ciclos))
    barra = "#" * int(porcentaje/2) + "-" * (50 - int(porcentaje/2))
    print("Simulacion en curso |" + barra + f"| {ciclo}/{ciclos}", end="\r")
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↑↑↑ \ Funciones Debug \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #    
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↓↓↓ \ Datos iniciales \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
# Datos de la función
dominio = [0, pow(2,30)-1]
coef: float = pow(2, 30) - 1   
funcion = lambda x : pow(x/coef, 2)

# Datos del algoritmo
probabilidad_crossover: float = 0.75
probabilidad_mutacion: float = 0.05
cantidad_individuos: int = 10
ciclos: int = 20
generaciones: int = 20
tipo_seleccion: str = "ruleta"
tipo_crossover: str = "1_punto"
tipo_mutacion: str = "invertida"
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↑↑↑ \ Datos iniciales \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #   
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↓↓↓ \ Funciones \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
def generar_poblacion_inicial() -> list[int]:
    poblacion: list[int] = []
    for individuo in range(cantidad_individuos):
        poblacion.append(randint(dominio[0], dominio[1]))                   #| Prueba con randint

        #i: str = ""                                                        #| Prueba con randint bit a bit
        #for j in range(30):                                                #|
        #    i += str(randint(0, 1))                                        #|
        #poblacion.append(int(i, base=2))                                   #|
        
        #poblacion.append(getrandbits(30))                                  #| Prueba con getrandbits

        #i: str = ""                                                        #| Prueba con getrandbits bit a bit
        #for j in range(30):                                                #|
        #    i += str(getrandbits(1))                                       #|
        #poblacion.append(int(i, base=2))                                   #|

        #poblacion.append(np.random.randint(dominio[0], dominio[1] + 1))    #| Prueba con numpy randint

        #i: str = ""                                                        #| Prueba con numpy randint bit a bit
        #for j in range(30):                                                #|
        #    i += str(np.random.randint(2))                                 #|
        #poblacion.append(int(i, base=2))                                   #|

    return poblacion

def evaluacion(poblacion: list[int]) -> list[float]:
    evaluaciones: list[float] = []
    sumatoria = 0
    for individuo in poblacion:
        sumatoria += funcion(individuo)
    for individuo in poblacion:
        evaluaciones.append(funcion(individuo)/sumatoria)
    return evaluaciones

def seleccion(evaluaciones: list[float]) -> list[int]:
    indices = np.random.choice(a=10, size=2, replace=False, p=evaluaciones)
    return (indices[0], indices[1])

def recombinacion(padre: int, madre: int) -> list[int]:
    if random() < probabilidad_crossover:
        hijo_uno: str = ""
        hijo_dos: str = ""
        punto_cruce: int = randint(1, 29)
        cadena_uno: str = [*str(format(padre, "030b"))]
        cadena_dos: str = [*str(format(madre, "030b"))]
        for bit in range(punto_cruce, len(cadena_uno)):
            auxiliar: str = cadena_uno[bit]
            cadena_uno[bit] = cadena_dos[bit]
            cadena_dos[bit] = auxiliar
        for c in range(len(cadena_uno)):
            hijo_uno += cadena_uno[c]
            hijo_dos += cadena_dos[c]
        return (int(hijo_uno, base=2), int(hijo_dos, base=2))
    else:
        return (padre, madre)
    
def mutacion(hijos: list[int]) -> list[int]:
    individuos: list[int] = []
    for hijo in hijos:
        if random() < probabilidad_mutacion:
            #individuo: str = ""
            #puntos_cruce: int = (randint(1, 29), randint(1, 29))
            #cadena: str = [*str(format(hijo, "030b"))]
            #longitud_intercambiar: int = abs(puntos_cruce[0] - puntos_cruce[1])
            #for desplazamiento in range(int((longitud_intercambiar + 1)/2)):
            #    auxiliar: str = cadena[min(puntos_cruce) + desplazamiento]
            #    cadena[min(puntos_cruce) + desplazamiento] = cadena[max(puntos_cruce) - desplazamiento]
            #    cadena[max(puntos_cruce) - desplazamiento] = auxiliar
            #for c in range(len(cadena)):
            #    individuo += cadena[c]
            #individuos.append(int(individuo, base=2))
            individuo: str = ""
            cadena: list[str] = [*str(format(hijo, "030b"))]
            cromosoma_invertido: int = randint(1, 29)
            if cadena[cromosoma_invertido] == "0":
                cadena[cromosoma_invertido] = "1"
            else:
                cadena[cromosoma_invertido] = "0"
            for c in range(len(cadena)):
                individuo += cadena[c]
            individuos.append(int(individuo, base=2))
        else:
            individuos.append(hijo)
    return individuos
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↑↑↑ \ Funciones \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #   
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↓↓↓ \ Archivo XLSX \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
# Definiendo el libro de trabajo (wb: workbook)
wb = Workbook()

# Creando las hojas "Generaciones" y "Ciclos" (ws: worksheet)
wb.active.title = "Generaciones"
wb.create_sheet("Ciclos")
ws_gens = wb["Generaciones"]
ws_cycles = wb["Ciclos"]

# Formateando la primer fila y la primer columna de las hojas "Generaciones" y "Ciclos"
agxl.generaciones_formateo(ws_gens, ciclos)
agxl.ciclos_formateo(ws_cycles, generaciones)

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↑↑↑ \ Archivo XLSX \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #   
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↓↓↓ \ Algoritmo Genético \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
# Programa
def programa(ciclo: int):
    finalizar: bool = False

    # Generar población inicial
    poblacion: list[int] = generar_poblacion_inicial() ### Para debuggear este apartado, utilice 'debug_poblacion_inicial(poblacion)' debajo de esta línea de código

    # Realizar evaluación de cada individuo
    evaluaciones: list[float] = evaluacion(poblacion) ### Para debuggear este apartado, utilice 'debug_evaluaciones(poblacion)' debajo de esta línea de código

    ### Para visualizar los dos apartados anteriores, utilice 'debug_generacion(poblacion, evaluaciones)' debajo de esta línea de código
    agxl.generaciones_insertar_tabla(ws_gens, ciclo, 1, poblacion, evaluaciones)
    agxl.generaciones_insertar_grafica(ws_gens, ciclo, 1)
    
    # Repetir durante una cierta cantidad de generaciones
    for generacion in range(2, generaciones + 1):
        nueva_poblacion: list[int] = []

        # Repite por cada pareja de individuos de la población
        for reproduccion in range(int(cantidad_individuos/2)):

            # Seleccionar un par para intentar realizar el crossover
            par_seleccionado = seleccion(evaluaciones)

            # Intenta realizar el crossover. Si no tiene éxito, toma a los propios padres como hijos. Luego, agrega a los dos individuos a la lista de la nueva población
            hijos: list[int] = recombinacion(poblacion[par_seleccionado[0]], poblacion[par_seleccionado[1]])

            # Intenta realizar una mutación sobre los descendientes
            hijos = mutacion(hijos)

            # Inserta a los nuevos indiviuos a la nueva generación
            nueva_poblacion.extend(hijos)

        # La nueva generación pasa a ser la población actual
        poblacion = nueva_poblacion

        # Se realiza la evaluación de la nueva
        evaluaciones = evaluacion(poblacion)

        agxl.generaciones_insertar_tabla(ws_gens, ciclo, generacion, poblacion, evaluaciones)
        agxl.generaciones_insertar_grafica(ws_gens, ciclo, generacion)
    agxl.ciclos_insertar_tabla(ws_cycles, ciclo, generaciones, cantidad_individuos)
    agxl.ciclos_insertar_grafica(ws_cycles, ciclo, generaciones)
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↑↑↑ \ Algoritmo Genético \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #  
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↓↓↓ \ Ejecución \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
# Iniciar el programa
os.system("cls")
print("Iniciando simulacion...") 
debug_ciclos(0)   
for ciclo in range(ciclos):
    programa(ciclo)
    debug_ciclos(ciclo + 1)
print(f"Simulacion completada. |##################################################| {ciclos}/{ciclos}\nGenerando documento xlsx...")
wb.save('prueba.xlsx')
print("Documento creado con exito")
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↑↑↑ \ Ejecución \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #  