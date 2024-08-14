import tkinter as tk
from tkinter import ttk
from pytsp import *

nombres_ciudades = ["Ciudad Autónoma de Buenos Aires", "Córdoba", "Corrientes", "Formosa",
                    "La Plata", "La Rioja", "Mendoza", "Neuquén", "Paraná", "Posadas", "Rawson",
                    "Resistencia", "Río Gallegos", "San Fernando del Valle de Catamarca",
                    "San Miguel de Tucumán", "San Salvador de Jujuy", "Salta", "San Juan", "San Luis",
                    "Santa Fe","Santa Rosa", "Santiago del Estero", "Ushuaia", "Viedma"]

def generar_recorrido() -> None:
    mascara = []
    for i in range(len(ciudades_incluidas)):
        mascara.append(ciudades_incluidas[i].get())
    r = recorrido_minimo(ciudades[ciudad_partida.get()], ciudades, mascara)
    mostrar_recorrido_ttk(txt_recorrido, r)
    if chk_map.get() == 1:
        mostrar_mapa(r)

root = tk.Tk()
root.geometry("1100x700")
root.title("Problema del Viajante - República Argentina")

frm = ttk.Frame(root)
frm.grid()

lbl_frm_0 = ttk.Labelframe(frm, text="Ciudad de partida")
lbl_frm_0.grid(column=0, row=0, padx=16, pady=16, sticky="NW")

lbl_frm_1 = ttk.Labelframe(frm, text="Ciudades incluidas en el recorrido")
lbl_frm_1.grid(column=1, row=0, padx=16, pady=16, sticky="NW")

lbl_frm_2 = ttk.Labelframe(frm, text="Resolver")
lbl_frm_2.grid(column=2, row=0, padx=16, pady=16, sticky="NW")


ciudades_incluidas = [tk.IntVar() for i in range(24)]
ciudad_partida = tk.IntVar()

for i in range(24):
    ttk.Radiobutton(lbl_frm_0, text=f"{nombres_ciudades[i]}", variable=ciudad_partida, value=i).grid(column = 0, row = i+1, padx=2, pady=2, sticky="W")
    ttk.Checkbutton(lbl_frm_1, text=f"{nombres_ciudades[i]}", variable=ciudades_incluidas[i], onvalue=0, offvalue=1).grid(column = 1, row = i+1, padx=2, pady=2, sticky="W")

chk_map = tk.IntVar()

ttk.Button(lbl_frm_2, text="Generar recorrido", command=generar_recorrido).grid(column=0, row=0, padx=2, pady=2, sticky="W")
ttk.Checkbutton(lbl_frm_2, text="Mostrar mapa", variable=chk_map, onvalue=1, offvalue=0).grid(column=1, row=0, padx=2, pady=2, sticky="E")
txt_recorrido = tk.Text(lbl_frm_2, height=35, width=58)
txt_recorrido.grid(column=0, row=1, columnspan=2, padx=2, pady=2, sticky="W")

root.mainloop()
