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
import os                                   # Limpiar la consola
from openpyxl import Workbook               # Crear el documento xlsx
import dependencias.agxl as agxl            # Modulo propio para manipular rapidamente el documento xlsx
import dependencias.pygen as pygen          # Modulo propio para implementar el algoritmo genético

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↓↓↓ \ Datos iniciales \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
# Parámetros generales de la simulación
cantidad_individuos: int = 10
ciclos: int = 20
generaciones: int = 20 # Habrá que variar entre 20, 100 y 200

# Datos de la función
dominio: tuple[int, int] = [0, pow(2,30)-1]
coef: float = pow(2, 30) - 1   
funcion = lambda x : pow(x/coef, 2)

# Parámetros de cada inciso
# "Nombre": ['tipo_seleccion', 'tipo_crossover', 'tipo_mutacion', 'prob_crossover', 'prob_mutacion', 'porc_elitismo', 'porc_especial']
configuraciones = {"A": ['ruleta', '1pto', 'invertida', 0.75, 0.05, 0, 0],
                   "B": ['torneo', '1pto', 'invertida', 0.75, 0.05, 0, 0.4],
                   "C": ['ruleta', '1pto', 'invertida', 0.75, 0.05, 0.2, 0]}
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↑↑↑ \ Datos iniciales \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #   
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↓↓↓ \ Archivo XLSX \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
# Creación del libro de trabajo (wb: workbook)
wb = Workbook()

# Creación las hojas "Generaciones" y "Ciclos" (ws: worksheet)
wb.active.title = "Generaciones"
wb.create_sheet("Ciclos")
ws_gens = wb["Generaciones"]
ws_cycles = wb["Ciclos"]

# Formateo las hojas "Generaciones" y "Ciclos"
agxl.generaciones_formateo(ws_gens, ciclos)
agxl.ciclos_formateo(ws_cycles, generaciones)
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↑↑↑ \ Archivo XLSX \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #   
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↓↓↓ \ Algoritmo Genético \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
def programa(ag: pygen.AlgoritmoGenetico, ciclo: int):
    ag.generarPoblacionInicial()
    ag.fitness()
    agxl.generaciones_insertar_tabla(ws_gens, ciclo, 1, ag.poblacion, ag.list_fitness)
    agxl.generaciones_insertar_grafica(ws_gens, ciclo, 1)
    for generacion in range(2, generaciones + 1):
        ag.nuevaGeneracion()
        ag.fitness()
        agxl.generaciones_insertar_tabla(ws_gens, ciclo, generacion, ag.poblacion, ag.list_fitness)
        agxl.generaciones_insertar_grafica(ws_gens, ciclo, generacion)
    agxl.ciclos_insertar_tabla(ws_cycles, ws_gens, ciclo, generaciones, cantidad_individuos)
    agxl.ciclos_insertar_grafica(ws_cycles, ciclo, generaciones)  
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↑↑↑ \ Algoritmo Genético \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↓↓↓ \ Ejecución \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
os.system("cls")
for opcion in ["A", "B", "C"]:
    print(f"Iniciando simulación {opcion}...")
    for ciclo in range(ciclos):
        ag_i = pygen.AlgoritmoGenetico(*configuraciones[opcion], cantidad_individuos, generaciones, dominio, funcion)
        programa(ag_i, ciclo)
    print(f"Simulación {opcion} completada.")
    wb.save(f"Resultados_{opcion}.xlsx")
    print(f"Documento \"Resultados_{opcion}.xlsx\" creado con éxito")
input()
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↑↑↑ \ Ejecución \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #