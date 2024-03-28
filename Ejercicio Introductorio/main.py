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

import os
from random import randint
from random import random
import numpy as np

# DEBUG
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
        print(str(format(i, "9d")) + " | " + str(format(poblacion[i], "010d")) + " | " + format(poblacion[i], "030b") + " | " + format(evaluaciones[i], "f"))
        sumatoria += evaluaciones[i]
    print("----------+------------+--------------------------------+-------------")
    print("Total".rjust(9) + " |            |                                | " + format(sumatoria, "012.10f"))
    

# Datos de la función
dominio = [0, pow(2,30)-1]
coef: float = pow(2, 30) - 1   
funcion = lambda x : x/pow(coef, 2)

# Datos del algoritmo
probabilidad_crossover: float = 0.75
probabilidad_mutacion: float = 0.05
cantidad_individuos: int = 10
ciclos: int = 20
generaciones: int = 200
tipo_seleccion: str = "ruleta"
tipo_crossover: str = "1_punto"
tipo_mutacion: str = "invertida"

# Funciones y modulos
def generar_poblacion_inicial() -> list[int]:
    poblacion: list[int] = []
    for individuo in range(cantidad_individuos):
        poblacion.append(randint(dominio[0], dominio[1]))
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
            individuo: str = ""
            puntos_cruce: int = (randint(1, 29), randint(1, 29))
            cadena: str = [*str(format(hijo, "030b"))]
            longitud_intercambiar: int = abs(puntos_cruce[0] - puntos_cruce[1])
            for desplazamiento in range(int((longitud_intercambiar + 1)/2)):
                auxiliar: str = cadena[min(puntos_cruce) + desplazamiento]
                cadena[min(puntos_cruce) + desplazamiento] = cadena[max(puntos_cruce) - desplazamiento]
                cadena[max(puntos_cruce) - desplazamiento] = auxiliar
            for c in range(len(cadena)):
                individuo += cadena[c]
            individuos.append(int(individuo, base=2))
        else:
            individuos.append(hijo)
    return individuos

# Programa
def programa():
    finalizar: bool = False

    # Generar población inicial
    poblacion: list[int] = generar_poblacion_inicial() ### Para debuggear este apartado, utilice 'debug_poblacion_inicial(poblacion)' debajo de esta línea de código

    # Realizar evaluación de cada individuo
    evaluaciones: list[float] = evaluacion(poblacion) ### Para debuggear este apartado, utilice 'debug_evaluaciones(poblacion)' debajo de esta línea de código

    ### Para visualizar los dos apartados anteriores, utilice 'debug_generacion(poblacion, evaluaciones)' debajo de esta línea de código
    os.system('cls')
    print("Generacion 1")
    debug_generacion(poblacion, evaluaciones)
    
    # Repetir durante una cierta cantidad de generaciones
    for generacion in range(generaciones):
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

        print(f"\nGeneracion {2+generacion}")
        debug_generacion(poblacion, evaluaciones)
    


# Iniciar el programa
programa()