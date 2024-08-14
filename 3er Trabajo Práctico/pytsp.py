import tkinter as tk
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

CIUDAD_DE_BS_AS = 0
CORDOBA = 1
CORRIENTES = 2
FORMOSA = 3
LA_PLATA = 4
LA_RIOJA = 5
MENDOZA = 6
NEUQUEN = 7
PARANA = 8
POSADAS = 9
RAWSON = 10
RESISTENCIA = 11
RIO_GALLEGOS = 12
SFDVD_CATAMARCA = 13
SM_DE_TUCUMAN = 14
SS_DE_JUJUY = 15
SALTA = 16
SAN_JUAN = 17
SAN_LUIS = 18
SANTA_FE = 19
SANTA_ROSA = 20
SANTIAGO_DEL_ESTERO = 21
USHUAIA = 22
VIEDMA = 23


class Ciudad():
    id = -1
    
    def __init__(self, nombre: str, provincia: str | None, map_x: int, map_y: int) -> None:
        self.id = Ciudad.id = Ciudad.id + 1
        self.nombre = nombre
        self.provincia = provincia
        self.map_x = map_x
        self.map_y = map_y


def distancia(partida: Ciudad, destino: Ciudad) -> int:
    if partida.id == destino.id or partida.id < 0 or partida.id > 23 or destino.id < 0 or destino.id > 23:
        return 0
    
    d = [[ 646], #  1 - Córdoba
         [ 792,  677], #  2 - Corrientes
         [ 933,  824,  157], #  3 - Formosa
         [  53,  698,  830,  968], #  4 - La Plata
         [ 986,  340,  814,  927, 1038], #  5 - La Rioja
         [ 985,  466, 1131, 1269, 1029,  427], #  6 - Mendoza
         [ 989,  907, 1534, 1690, 1005, 1063,  676], #  7 - Neuquén
         [ 375,  348,  500,  656,  427,  659,  790, 1053], #  8 - Paraná
         [ 834,  919,  291,  263,  857, 1098, 1384, 1709,  658], #  9 - Posadas
         [1127, 1321, 1845, 1999, 1116, 1548, 1201,  543, 1345, 1951], # 10 - Rawson
         [ 794,  669,   13,  161,  833,  802, 1121, 1529,  498,  305, 1843], # 11 - Resistencia
         [2082, 2281, 2819, 2974, 2064, 2473, 2081, 1410, 2320, 2914,  975, 2818], # 12 - Río Gallegos
         [ 979,  362,  691,  793, 1030,  149,  569, 1182,  622,  980, 1647,  678, 2587], # 13 - San Fermín del Valle de Catamarca
         [1080,  517,  633,  703, 1132,  330,  756, 1370,  707,  924, 1827,  620, 2773,  189], # 14 - San Miguel de Tucumán
         [1334,  809,  742,  750, 1385,  600, 1023, 1658,  959, 1007, 2120,  729, 3063,  477,  293], # 15 - San Salvador de Jujuy
         [1282,  745,  719,  741, 1333,  533,  957, 1591,  906,  992, 2054,  706, 2997,  410,  228,   67], # 16 - Salta
         [1005,  412, 1039, 1169, 1053,  283,  152,  824,  757, 1306, 1340, 1029, 2231,  430,  612,  874,  808], # 17 - San Juan
         [ 749,  293,  969, 1117,  795,  435,  235,  643,  574, 1200, 1113,  961, 2046,  540,  727, 1017,  950,  284], # 18 - San Luis
         [ 393,  330,  498,  654,  444,  640,  775, 1049,   19,  664, 1349,  495, 2325,  602,  689,  942,  889,  740,  560], # 19 - Santa Fe
         [ 579,  577, 1136, 1293,  602,  834,  586,  422,  642, 1293,  745, 1132, 1712,  915, 1088, 1382, 1316,  686,  412,  641], # 20 - Santa Rosa
         [ 939,  401,  535,  629,  991,  311,  713, 1286,  566,  827, 1721,  523, 2677,  166,  141,  414,  353,  583,  643,  547,  977], # 21 - Santiago del Estero
         [2373, 2618, 3131, 3284, 2350, 2821, 2435, 1762, 2635, 3207, 1300, 3130,  359, 2931, 3116, 3408, 3341, 2585, 2392, 2641, 2044, 3016], # 22 - Ushuaia
         [ 799, 1047, 1527, 1681,  789, 1311, 1019,  479, 1030, 1624,  327, 1526, 1294, 1391, 1562, 1855, 1790, 1141,  882, 1035,  477, 1446, 1605]] # 23 - Viedma
           #0    #1    #2    #3    #4    #5    #6    #7    #8    #9    #10   #11   #12   #13   #14   #15   #16   #17   #18   #19   #20   #21   #22

    if partida.id > destino.id:
        return d[partida.id - 1][destino.id]
    else:
        return d[destino.id - 1][partida.id]

def ciudad_mas_cercana(partida: Ciudad, ciudades: list[Ciudad], mascara: list[int]) -> Ciudad | None:
    d_min = float("inf")
    c_min = None
    for i in range(len(ciudades)):
        if mascara[i] == 0 and ciudades[i].id != partida.id:
            d = distancia(partida, ciudades[i])
            if d < d_min:
                d_min = d
                c_min = ciudades[i]
    return c_min

def longitud_recorrido(recorrido: Ciudad) -> int:
    l = 0
    for i in range(len(recorrido) - 1):
        l += distancia(recorrido[i], recorrido[i+1])
    return l

def recorrido_minimo(partida: Ciudad, ciudades: list[Ciudad], mascara: list[int] | None = None) -> list[Ciudad]:
    if mascara is None or len(mascara) != len(ciudades):
        mascara = [0 for i in range(len(ciudades))]
    recorrido = [partida]
    mascara[partida.id] = 1
    for i in range(mascara.count(0)):
        siguiente_ciudad: Ciudad = ciudad_mas_cercana(recorrido[i], ciudades, mascara)
        recorrido.append(siguiente_ciudad)
        mascara[siguiente_ciudad.id] = 1
    recorrido.append(partida)
    return recorrido

def mostrar_mapa(recorrido: list[Ciudad]) -> None:
    img = mpimg.imread("./republica argentina.png")

    x: list[int] = []
    y: list[int] = []

    for ciudad in recorrido:
        x.append(ciudad.map_x)
        y.append(ciudad.map_y)

    plt.imshow(img, extent=[0, 1035, 0, 1968])
    plt.plot(x, y, color="#F6B532")
    plt.plot(x[0], y[0], marker="o", linestyle="none", color="#551ABC", mfc="#FFF", ms=8, mew=2)
    x.pop(0)
    x.pop()
    y.pop(0)
    y.pop()
    plt.plot(x, y, marker="o", linestyle="none", color="#F6B532", mfc="#FFF", ms=8, mew=2)
    plt.subplots_adjust(0, 0.001, 1, 1, 0, 0)
    plt.savefig("foo.pdf")
    plt.show()

def mostrar_recorrido_consola(recorrido: list[Ciudad]) -> None:
    l = 0
    for i in range(len(recorrido)):
        d = distancia(recorrido[i], recorrido[i-1])
        l = l + d
        print(f"{i}. {recorrido[i].nombre}, {recorrido[i].provincia} - Distancia parcial: {d}")
    print(f"Distancia total recorrida: {l}")

def mostrar_recorrido_ttk(txt_area: tk.Text, recorrido: list[Ciudad]) -> None:
    txt_area.delete(1.0, tk.END)
    l = 0
    txt_area.insert(tk.END, f"ID, CIUDAD - DISTANCIA DEL SEGMENTO (DISTANCIA ACUMULADA)\n")
    for i in range(len(recorrido)):
        d = distancia(recorrido[i], recorrido[i-1])
        l = l + d
        txt_area.insert(tk.END, f"{recorrido[i].id}, {recorrido[i].nombre} - {d} ({l})\n")
    txt_area.insert(tk.END, f"\nDistancia total recorrida: {l}")

ciudades = [Ciudad("Ciudad Autónoma de Buenos Aires", None, 779, 1330),                 #  0
            Ciudad("Córdoba", "Córdoba", 535, 1492),                                    #  1
            Ciudad("Corrientes", "Corrientes", 763, 1685),                              #  2
            Ciudad("Formosa", "Formosa", 790, 1746),                                    #  3
            Ciudad("La Plata", "Buenos Aires", 800, 1314),                              #  4
            Ciudad("La Rioja", "La Rioja", 421, 1591),                                  #  5
            Ciudad("Mendoza", "Mendoza", 336, 1418),                                    #  6
            Ciudad("Neuquén", "Neuquén", 370, 1099),                                    #  7
            Ciudad("Paraná", "Entre Ríos", 690, 1476),                                  #  8
            Ciudad("Posadas", "Misiones", 888, 1690),                                   #  9
            Ciudad("Rawson", "Chubut", 495, 853),                                       # 10
            Ciudad("Resistencia", "Chaco", 756, 1686),                                  # 11
            Ciudad("Río Gallegos", "Santa Cruz", 321, 328),                             # 12
            Ciudad("San Fernando del Valle de Catamarca", "Catamarca", 467, 1637),      # 13
            Ciudad("San Miguel de Tucumán", "Tucumán", 491, 1715),                      # 14
            Ciudad("San Salvador de Jujuy", "Jujuy", 487, 1840),                        # 15
            Ciudad("Salta", "Salta", 483, 1812),                                        # 16
            Ciudad("San Juan", "San Juan", 350, 1486),                                  # 17
            Ciudad("San Luis", "San Luis", 443, 1397),                                  # 18
            Ciudad("Santa Fe", "Santa Fe", 683, 1482),                                  # 19
            Ciudad("Santa Rosa", "La Pampa", 530, 1224),                                # 20
            Ciudad("Santiago del Estero", "Santiago del Estero", 531, 1669),            # 21
            Ciudad("Ushuaia", "Tierra del Fuego", 359, 101),                            # 22
            Ciudad("Viedma", "Rio Negro", 585, 996)]                                    # 23