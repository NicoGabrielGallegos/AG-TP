# %% [markdown]
# # Problema del viajante (Travelling salesman problem)

# %%
import random
import math
import tkinter as tk
import tkinter.ttk as ttk
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# %% [markdown]
# ### Datos, funciones y procedimientos

# %% [markdown]
# #### Constantes

# %%
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

CANT_CIUDADES = 24

NOMBRES_CIUDADES = ["Ciudad Autónoma de Buenos Aires", "Córdoba", "Corrientes", "Formosa",
                    "La Plata", "La Rioja", "Mendoza", "Neuquén", "Paraná", "Posadas", "Rawson",
                    "Resistencia", "Río Gallegos", "San Fernando del Valle de Catamarca",
                    "San Miguel de Tucumán", "San Salvador de Jujuy", "Salta", "San Juan", "San Luis",
                    "Santa Fe","Santa Rosa", "Santiago del Estero", "Ushuaia", "Viedma"]

DISTANCIAS = [[ 646], #  1 - Córdoba
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

# %% [markdown]
# #### Definición de las ciudades

# %%
class Ciudad():
    id = -1
    
    def __init__(self, nombre: str, provincia: str | None, map_x: int, map_y: int) -> None:
        self.id = Ciudad.id = Ciudad.id + 1
        self.nombre = nombre
        self.provincia = provincia
        self.map_x = map_x
        self.map_y = map_y

CIUDADES = [Ciudad("Ciudad Autónoma de Buenos Aires", None, 779, 1330),                 #  0
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

# %% [markdown]
# #### Utilidades

# %%
def validar_mascara(mascara: list[int] | None, n: int) -> list[int]:
    '''
        Recibe como parámetro una máscara y el tamaño de la lista que enmascara.

        Si el tamaño de la máscara no coincide con el tamaño de la lista,
        crea una nueva máscara de igual tamaño que la lista. Sino, la mascara
        
        Devuelve una máscara de bits corregida
    '''
    if mascara is None or len(mascara) != n:
        mascara = [0 for i in range(n)]
    return mascara

def desplazar_lista(lista: list, n: int) -> None:
    '''
        Recibe como parámetro una lista.

        Desplaza los elementos de la lista una cantidad n de espacios hacia la izquierda.
    '''

    nueva_lista = []
    for i in range(len(lista)):
        nueva_lista.append(lista[(i + n) % len(lista)])
    
    for i in range(len(lista)):
        lista[i] = nueva_lista[i]


#l = [1, 2, 3, 4]
#
#desplazar_lista(l, 3)
#
#print(l)

# %% [markdown]
# #### Funciones de ciudades y recorridos

# %%
def distancia(partida: int, destino: int) -> int:
    '''
        Recibe como parámetros una ciudad de partida y otra de destino.

        Devuelve la distancia en línea recta entre las mismas.
    '''
    if partida == destino or partida < 0 or partida > 23 or destino < 0 or destino > 23:
        return 0

    if partida > destino:
        return DISTANCIAS[partida - 1][destino]
    else:
        return DISTANCIAS[destino - 1][partida]

def ciudad_mas_cercana(partida: int, ciudades: list[int], mascara: list[int] | None = None) -> int | None:
    '''
        Recibe como parámetros una ciudad de partida, una lista de ciudades y una máscara de bits.

        Devuelve la ciudad dentro del conjunto que tenga la menor distancia con la ciudad de partida y esté incluída en la máscara.
    '''
    mascara = validar_mascara(mascara, len(ciudades))

    d_min = float("inf")
    c_min = None
    for i in range(len(ciudades)):
        if mascara[i] == 0 and ciudades[i] != partida:
            d = distancia(partida, ciudades[i])
            if d < d_min:
                d_min = d
                c_min = ciudades[i]
    return c_min

def longitud_recorrido(recorrido: list[int]) -> int:
    '''
        Recibe como parámetro una lista de ciudades.

        Devuelve la distancia total del recorrido que pasa por esas ciudades.
    '''
    l = 0
    for i in range(-1, len(recorrido) - 1):
        l += distancia(recorrido[i], recorrido[i+1])
    return l

# %% [markdown]
# #### Funciones de presentación

# %%
def mostrar_mapa(recorrido: list[Ciudad]) -> None:
    img = mpimg.imread("./republica argentina.png")

    x: list[int] = []
    y: list[int] = []

    for ciudad in recorrido:
        x.append(ciudad.map_x)
        y.append(ciudad.map_y)

    plt.figure(1)
    plt.figure(1).clear()
    plt.imshow(img, extent=[0, 1035, 0, 1968])
    plt.plot(x, y, color="#551ABC")
    plt.plot(x[0], y[0], marker="o", linestyle="none", color="#EFAC5F", mfc="#FFF", ms=8, mew=2)
    x.pop(0)
    x.pop()
    y.pop(0)
    y.pop()
    plt.plot(x, y, marker="o", linestyle="none", color="#551ABC", mfc="#FFF", ms=8, mew=2)
    plt.subplots_adjust(0, 0.001, 1, 1, 0, 0)
    plt.show()

def mostrar_evolucion_poblaciones(mejores_longitudes: list[int], peores_longitudes: list[int], promedios_longitudes: list[int]) -> None:
    plt.figure(2)
    plt.figure(2).clear()
    x_values = [i for i in range(len(mejores_longitudes))]
    plt.plot(x_values, peores_longitudes, color="#E52D37", label="Maximo")
    plt.plot(x_values, promedios_longitudes, color="#064CD8", label="Promedio")
    plt.plot(x_values, mejores_longitudes, color="#1CA533", label="Minimo")
    plt.xlabel("Generación")
    plt.ylabel("Distancia (km)")
    plt.legend()

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
    txt_area.insert(tk.END, f"ID, CIUDAD - DISTANCIA DEL SEGMENTO (DISTANCIA ACUMULADA)\n\n")
    for i in range(len(recorrido)):
        d = distancia(recorrido[i].id, recorrido[i-1].id)
        l = l + d
        txt_area.insert(tk.END, f"{recorrido[i].id}, {recorrido[i].nombre} - {d} ({l})\n")
    txt_area.insert(tk.END, f"\nDistancia total recorrida: {l}")

# %% [markdown]
# #### Funciones Heurísticas

# %%
def recorrido_heuristico(partida: int, ciudades: list[int], mascara: list[int] | None = None) -> list[int]:
    '''
        Recibe como parámetro una ciudad de partida, una lista de ciudades y una máscara de bits.

        Devuelve una lista de ciudades que representa el camino a realizar para que la distancia del recorrido entre dichas ciudades sea mínimo.
    '''
    mascara = validar_mascara(mascara, len(ciudades))

    recorrido = [partida]
    mascara[partida] = 1
    for i in range(mascara.count(0)):
        siguiente_ciudad: int = ciudad_mas_cercana(recorrido[i], ciudades, mascara)
        recorrido.append(siguiente_ciudad)
        mascara[siguiente_ciudad] = 1
    recorrido.append(partida)
    return recorrido

def recorrido_minimo_heuristico(partida: int, ciudades: list[int], mascara: list[int] | None = None) -> list[int]:
    aux = [i for i in mascara]
    recorrido = recorrido_heuristico(partida, ciudades, mascara)
    for i in range(len(aux)):
        if aux[i] == 0:
            mascara = [i for i in aux]
            r_aux = recorrido_heuristico(i, ciudades, mascara)
            if longitud_recorrido(r_aux) < longitud_recorrido(recorrido):
                recorrido = r_aux
    recorrido.pop(-1)
    desplazar_lista(recorrido, recorrido.index(partida))
    recorrido.append(partida)
    return recorrido

# %% [markdown]
# #### Funciones Genéticas

# %%
def generar_cromosoma(ciudades: list[int]) -> list[int]:
    c: list[int] = [i for i in ciudades]
    cromosoma: list[int] = [c.pop(0)]
    for i in range(len(c)):
        r = random.randint(0, len(c) - 1)
        cromosoma.append(c.pop(r))
    return cromosoma

def generar_poblacion(n: int, ciudades: list[int]) -> list[list[int]]:
    poblacion: list[list[int]] = []
    for i in range(n):
        poblacion.append(generar_cromosoma(ciudades))
    return poblacion

def fitness(cromosoma: list[int]) -> float:
    return -longitud_recorrido(cromosoma)

def seleccion(poblacion: list[list[int]], porcentaje_torneo: float) -> list[int]:
    indices_disponibles: list[int] = [i for i in range(len(poblacion))]
    cromosomas_seleccionados: list[int] = []

    for i in range(math.ceil(len(poblacion) * porcentaje_torneo)):
        indice_aleatorio: int = random.randint(0, len(indices_disponibles) - 1)
        cromosomas_seleccionados.append(poblacion[indices_disponibles.pop(indice_aleatorio)])
    
    mejor_cromosoma: int = cromosomas_seleccionados[0]

    for c in cromosomas_seleccionados:
        if fitness(c) > fitness(mejor_cromosoma):
            mejor_cromosoma = c

    return mejor_cromosoma

def crossover_ciclico(padre: list[int], madre: list[int], probabilidad: int = 0.9) -> tuple[list[int], list[int]]:
    if random.random() < probabilidad:
        lista_indices: list[int] = []
        indice_inicial = indice_nuevo = random.randint(1, len(padre) - 1)
        lista_indices.append(indice_inicial)

        while True:
            indice_nuevo = padre.index(madre[indice_nuevo])
            if indice_nuevo == indice_inicial:
                break
            lista_indices.append(indice_nuevo)

        hijo_1 = [i for i in padre]
        hijo_2 = [i for i in madre]

        for i in lista_indices:
            aux = hijo_1[i]
            hijo_1[i] = hijo_2[i]
            hijo_2[i] = aux
    else:
        hijo_1 = [i for i in padre]
        hijo_2 = [i for i in madre]
    return (hijo_1, hijo_2)

def mutacion(cromosoma: list[int], genes: int = 2, probabilidad: int = 0.2) -> None:
    if random.random() < probabilidad:
        indices: list[int] = [(i + 1) for i in range(len(cromosoma) - 1)]
        genes_mezclados: list[int] = []
        for i in range(genes):
            r = random.randint(1, len(indices) - 1)
            genes_mezclados.append(indices.pop(r))
    
        aux = cromosoma[genes_mezclados[0]]
        for i in range(len(genes_mezclados) - 1):
            cromosoma[genes_mezclados[i]] = cromosoma[genes_mezclados[i + 1]]
        cromosoma[genes_mezclados[-1]] = aux

def siguiente_generacion(poblacion: list[list[int]], porcentaje_torneo: float) -> list[list[int]]:
    nueva_poblacion: list[list[int]] = []

    for i in range(int(len(poblacion) / 2)):
        padre = seleccion(poblacion, porcentaje_torneo)
        madre = seleccion(poblacion, porcentaje_torneo)
        hijo_1, hijo_2 = crossover_ciclico(padre, madre)
        mutacion(hijo_1)
        mutacion(hijo_2)
        nueva_poblacion.append(hijo_1)
        nueva_poblacion.append(hijo_2)

    return nueva_poblacion

def recorrido_minimo_genetico(partida: int, ciudades: list[int], mascara: list[int], n: int = 50, m: int = 200, porcentaje_torneo: float = 0.4):

    validar_mascara(mascara, len(ciudades))
    c: list[int]= []
    for i in range(len(mascara)):
        if mascara[i] == 0:
            c.append(ciudades[i])

    poblacion = generar_poblacion(n, c)
    mejores_longitudes: list[int] = [min([longitud_recorrido(i) for i in poblacion])]
    peores_longitudes: list[int] = [max([longitud_recorrido(i) for i in poblacion])]
    promedios_longitudes: list[int] = [sum([longitud_recorrido(i) for i in poblacion]) / len(poblacion)]

    for i in range(m):
        poblacion = siguiente_generacion(poblacion, porcentaje_torneo)
        mejores_longitudes.append(min([longitud_recorrido(c) for c in poblacion]))
        peores_longitudes.append(max([longitud_recorrido(i) for i in poblacion]))
        promedios_longitudes.append(sum([longitud_recorrido(i) for i in poblacion]) / len(poblacion))

    mostrar_evolucion_poblaciones(mejores_longitudes, peores_longitudes, promedios_longitudes)

    recorrido = poblacion[0]
    for cromosoma in poblacion:
        if longitud_recorrido(cromosoma) < longitud_recorrido(recorrido):
            recorrido = cromosoma
            
    desplazar_lista(recorrido, recorrido.index(partida))
    recorrido.append(partida)
    return recorrido

# %% [markdown]
# ### Presentación

# %%
def generar_recorrido(tipo: str = "Heuristico") -> None:
    mascara = []
    for i in range(len(ciudades_incluidas)):
        mascara.append(ciudades_incluidas[i].get())
    mascara[ciudad_partida.get()] = 0

    ciudades = [i for i in range(CANT_CIUDADES)]

    if tipo == "Heuristico":
        r = recorrido_heuristico(ciudad_partida.get(), ciudades, mascara)
    elif tipo == "Minimo":
        r = recorrido_minimo_heuristico(ciudad_partida.get(), ciudades, mascara)
    elif tipo == "Genetico":
        r = recorrido_minimo_genetico(ciudad_partida.get(), ciudades, mascara)
    r = [CIUDADES[i] for i in r]
    mostrar_recorrido_ttk(txt_recorrido, r)
    if chk_map.get() == 1:
        mostrar_mapa(r)

root = tk.Tk()
root.geometry("1020x650")
root.title("Problema del Viajante - República Argentina")

frm = ttk.Frame(root)
frm.grid()

lbl_frm_0 = ttk.Labelframe(frm, text="Ciudad de partida")
lbl_frm_0.grid(column=0, row=0, padx=16, pady=16)

lbl_frm_1 = ttk.Labelframe(frm, text="Ciudades incluidas en el recorrido")
lbl_frm_1.grid(column=1, row=0, padx=16, pady=16)

lbl_frm_2 = ttk.Labelframe(frm, text="Resolver")
lbl_frm_2.grid(column=2, row=0, padx=16, pady=16)


ciudades_incluidas = [tk.IntVar() for i in range(CANT_CIUDADES)]
ciudad_partida = tk.IntVar()

for i in range(CANT_CIUDADES):
    radbtn = ttk.Radiobutton(lbl_frm_0, text=f"{NOMBRES_CIUDADES[i]}", variable=ciudad_partida, value=i)
    chkbtn = ttk.Checkbutton(lbl_frm_1, text=f"{NOMBRES_CIUDADES[i]}", variable=ciudades_incluidas[i], onvalue=0, offvalue=1)

    radbtn.grid(column = 0, row = i+1, padx=2, pady=2, sticky="W")
    chkbtn.grid(column = 1, row = i+1, padx=2, pady=2, sticky="W")

chk_map = tk.IntVar()

ttk.Button(lbl_frm_2, text="Búsqueda Heurística", command=lambda: generar_recorrido("Heuristico")).grid(column=0, row=0, padx=2, pady=2)
ttk.Button(lbl_frm_2, text="Mínimo por búsqueda heurística", command=lambda: generar_recorrido("Minimo")).grid(column=1, row=0, padx=2, pady=2)
ttk.Button(lbl_frm_2, text="Algoritmo Genético", command=lambda: generar_recorrido("Genetico")).grid(column=2, row=0, padx=2, pady=2)
ttk.Checkbutton(lbl_frm_2, text="Mostrar mapa", variable=chk_map, onvalue=1, offvalue=0).grid(column=0, row=1, padx=2, pady=2)
txt_recorrido = tk.Text(lbl_frm_2, height=34, width=58)
txt_recorrido.grid(column=0, row=3, columnspan=3, padx=2, pady=2, sticky="W")
txt_recorrido.insert(tk.END, f"ID, CIUDAD - DISTANCIA DEL SEGMENTO (DISTANCIA ACUMULADA)")

root.mainloop()


# %%



