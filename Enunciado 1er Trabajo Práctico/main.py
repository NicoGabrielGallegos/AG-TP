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
# Datos del algoritmo
tipo_seleccion: str = "ruleta"
tipo_crossover: str = "1pto"
tipo_mutacion: str = "invertida"
probabilidad_crossover: float = 0.75
probabilidad_mutacion: float = 0.05
cantidad_individuos: int = 10
ciclos: int = 20
generaciones: int = 20

# Datos de la función
dominio: tuple[int, int] = [0, pow(2,30)-1]
coef: float = pow(2, 30) - 1   
funcion = lambda x : pow(x/coef, 2)

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↑↑↑ \ Datos iniciales \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #   
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↓↓↓ \ Archivo XLSX \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
# Definiendo el libro de trabajo (wb: workbook)
wb = Workbook()

# Creando las hojas "Generaciones" y "Ciclos" (ws: worksheet)
wb.active.title = "Generaciones"
wb.create_sheet("Ciclos")
ws_gens = wb["Generaciones"]
ws_cycles = wb["Ciclos"]

# Formateando las hojas "Generaciones" y "Ciclos"
agxl.generaciones_formateo(ws_gens, ciclos)
agxl.ciclos_formateo(ws_cycles, generaciones)

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↑↑↑ \ Archivo XLSX \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #   
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↓↓↓ \ Algoritmo Genético \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
def programa(ciclo: int):
    ag = pygen.AlgoritmoGenetico(tipo_seleccion, tipo_crossover, tipo_mutacion, probabilidad_crossover, probabilidad_mutacion, cantidad_individuos, ciclos, generaciones, dominio, funcion)
    ag.generarPoblacionInicial()
    ag.fitness()

    agxl.generaciones_insertar_tabla(ws_gens, ciclo, 1, ag.poblacion, ag.list_fitness)
    agxl.generaciones_insertar_grafica(ws_gens, ciclo, 1)
    for generacion in range(2, generaciones + 1):
        ag.nuevaGeneracion()
        ag.fitness()
        agxl.generaciones_insertar_tabla(ws_gens, ciclo, generacion, ag.poblacion, ag.list_fitness)
        agxl.generaciones_insertar_grafica(ws_gens, ciclo, generacion)
    agxl.ciclos_insertar_tabla(ws_cycles, ciclo, generaciones, cantidad_individuos)
    agxl.ciclos_insertar_grafica(ws_cycles, ciclo, generaciones)  
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↑↑↑ \ Algoritmo Genético \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↓↓↓ \ Ejecución \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
os.system("cls")
print("Iniciando simulación...")
for ciclo in range(ciclos):
    print(f"Ciclo {ciclo}")
    programa(ciclo)
print("Simulación completada.")
wb.save("prueba.xlsx")
print("Documento creado con éxito")
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↑↑↑ \ Ejecución \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #  
