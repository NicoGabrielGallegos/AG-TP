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
from pysearch import BagItem, Bag, ExhaustiveSearch

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

items_1 = [BagItem(table_1[i]["weight"],table_1[i]["value"]) for i in range(len(table_1))]
items_2 = [BagItem(table_2[i]["weight"],table_2[i]["value"]) for i in range(len(table_2))]

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↓↓↓ \ Algoritmo Genético \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
def program() -> None:
    pass
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↑↑↑ \ Algoritmo Genético \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↓↓↓ \ Ejecución \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↑↑↑ \ Ejecución \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #

os.system("cls")

bag = Bag(4200)

s = ExhaustiveSearch(bag, items_1, "Results_A")

s.table_header()
s.evaluate_possibilities()

s.table_header("Optimum Candidates")
for o in s.optimum:
    s.print_possibility(o)
