# -*- coding: utf-8 -*-
#
# El programa será capaz de:
# [0%] simular todas las partidas posibles de Truco
# [0%] calcular la posibilidad de ganar envidos
# [0%] calcular la posibilidad de ganar una partida dada una mano inicial dependiendo del orden de tirada de cartas
# [0%] calcular la posibilidad de ganar una partida dada una mano inicial independientemente del orden de tirada de cartas
# [0%] calcular la posibilidad de ganar flor
# [0%] calcular la posibilidad de ganar una partida dada nuestra mano y la del oponente, basado en el orden de tirada de cartas
# El oponente debería poder:
# ... ofrecer, aceptar o rechazar un envido
# ... ofrecer, aceptar o rechazar un truco
# ... intentar adivinar nuestras cartas basadas en el envido y teniendo en cuenta que podemos mentir
# ... pedir mostrar el envido al finalizar la ronda
# El programa deberá tener en cuenta:
# ... cartas actuales del jugador
# ... cartas en mesa del oponente
# ... valores cantados en envidos
# ... trucos cantados por el oponente
#
# Formato actual:
# - Carta - Número entero de dos dígitos en base 10 - Unidad:Número, Decena:Palo - [0, 40)
# - Palo - 0:Oro, 1:Copa, 2:Espada, 3:Basto
# - Número - 0:1, 1:2, 2:3, 3:4, 4:5, 5:6, 6:7, 7:10, 8:11, 9:12
# Formato deseable:
# - Carta - 6 bits - 0bPPNNNN - 
# - P - 0b00:Oro, 0b01:Copa, 0b10:Espada, 0b11:Basto
# - N - 0b0000:1, 0b0001:2, 0b0010:3, 0b0011:4, 0b0100:5, 0b0101:6, 0b0110:7, 0b0111:10, 0b1000:11, 0b1001:12

import os

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↓↓↓ \ Funciones Debug \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↑↑↑ \ Funciones Debug \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↓↓↓ \ Datos iniciales \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↑↑↑ \ Datos iniciales \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↓↓↓ \ Diccionarios \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #

valor_carta: dict[int, int] = {0: 7, 1: 8, 2: 9, 3: 0, 4: 1, 5: 2, 6: 10, 7: 4, 8: 5, 9: 6,             # Oros
                               10: 7, 11: 8, 12: 9, 13: 0, 14: 1, 15: 2, 16: 3, 17: 4, 18: 5, 19: 6,    # Copas
                               20: 13, 21: 8, 22: 9, 23: 0, 24: 1, 25: 2, 26: 11, 27: 4, 28: 5, 29: 6,  # Espadas
                               30: 12, 31: 8, 32: 9, 33: 0, 34: 1, 35: 2, 36: 3, 37: 4, 38: 5, 39: 6}   # Bastos

valor_envido: dict[int, int] = {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 0, 8: 0, 9: 0}   # Solo importa el número, no el palo
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↑↑↑ \ Diccionarios \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↓↓↓ \ Funciones \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↑↑↑ \ Funciones \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↓↓↓ \ Algoritmo \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↑↑↑ \ Algoritmo \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↓↓↓ \ Ejecución \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↑↑↑ \ Ejecución \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #