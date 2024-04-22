from oh_hi import OhHi
import os

def getTableroInicial(filas:int, columnas:int = None):
    return OhHi(filas, columnas)

def getTableroSolucionado(t:OhHi) -> OhHi:
    continuar:bool = True
    t_cmp:OhHi = t.copy()
    while continuar:
        t.criterioColorRestante()
        t.criterioAdyacencia()
        t.criterioDiferentes()
        if t.equals(t_cmp):
            continuar = False
        t_cmp = t.copy()
    return t.copy()
