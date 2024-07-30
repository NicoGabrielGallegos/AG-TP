# Problema de la mochila.
#
# Resolver los siguientes enunciados utilizando:
# - Búsqueda Exhaustiva
# - Algoritmo Greedy
#
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
#
# 1er problema:
#   Cuáles son los elementos de la lista siguiente que cargaremos en
#   una mochila de 4200 cm3 de manera que su valor en $ sea máximo.
#
#   Datos:
#     +--------+---------+-------+
#     | Objeto | Volumen | Valor |
#     +--------+---------+-------+
#     |    1   |   150   |   20  |
#     |    2   |   325   |   40  |
#     |    3   |   600   |   50  |
#     |    4   |   805   |   36  |
#     |    5   |   430   |   25  |
#     |    6   |  1200   |   64  |
#     |    7   |   770   |   54  |
#     |    8   |    60   |   18  |
#     |    9   |   930   |   46  |
#     |   10   |   353   |   28  |
#     +--------+---------+-------+
#
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
#
# 2do problema:
#   Cuáles son los elementos de la lista siguiente que cargaremos en
#   una mochila de 3000 grs de manera que su valor en $ sea máximo.
#
#   Datos:
#     +--------+------+-------+
#     | Objeto | Peso | Valor |
#     +--------+------+-------+
#     |    1   | 1800 |   72  |
#     |    2   |  600 |   36  |
#     |    3   | 1200 |   60  |
#     +--------+------+-------+
#
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #

                                                    # Usado para:
import os                                           # Limpiar la consola
from dependencias.pysearch import BagItem, Bag, ExhaustiveSearch, GreedySearch

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↓↓↓ \ Datos iniciales \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
# Objetos del 1er problema
table_1 = [{"weight":  150, "value": 20},
           {"weight":  325, "value": 40},
           {"weight":  600, "value": 50},
           {"weight":  805, "value": 36},
           {"weight":  430, "value": 25},
           {"weight": 1200, "value": 64},
           {"weight":  770, "value": 54},
           {"weight":   60, "value": 18},
           {"weight":  930, "value": 46},
           {"weight":  353, "value": 28}]

# Objetos del 2do problema
table_2 = [{"weight": 1800, "value": 72},
           {"weight":  600, "value": 36},
           {"weight": 1200, "value": 60}]

# Listas de Objetos
items_1 = [BagItem(table_1[i]["weight"], table_1[i]["value"], str(i+1)) for i in range(len(table_1))]
items_2 = [BagItem(table_2[i]["weight"], table_2[i]["value"], str(i+1)) for i in range(len(table_2))]

# Mochilas
bag_1 = Bag(4200)
bag_2 = Bag(3000)

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↓↓↓ \ Ejecución \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
# Realizar y mostrar la búsqueda
def exec_search(bag: Bag, items: list[BagItem], type: str = "Exhaustive", name: str = "Resultado") -> None:
    match type:
        case "Exhaustive":
            s = ExhaustiveSearch(bag, items)
        case "Greedy":
            s = GreedySearch(bag, items)
            s.order_by_vwr()
    s.search()
    print(f"\nProblema de la mochila - {name}")
    print("-------+-------+------------")
    print("  Peso | Valor | Contenido")
    print("-------+-------+------------")
    s.print_optimums()
    s.export_xlsx_file(f"Resultados_{name}.xlsx")
    print("-------+-------+------------")
    print(f"Documento \"Resultados_{name}.xlsx\" creado con éxito")

os.system("cls")

exec_search(bag_1, items_1, "Exhaustive", "1A") # Problema 1 - A
exec_search(bag_1, items_1, "Greedy", "1B")     # Problema 1 - B
exec_search(bag_2, items_2, "Exhaustive", "2A") # Problema 2 - A
exec_search(bag_2, items_2, "Greedy", "2B")     # Problema 2 - B
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↑↑↑ \ Ejecución \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #

input()