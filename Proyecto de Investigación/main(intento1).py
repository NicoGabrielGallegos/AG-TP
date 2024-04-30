import os, sys, random
import dependencias.pygate as pygate

conexiones: list[str] = []

def generar_compuerta_aleatoria() -> pygate.Gate2:
    match random.randint(0,5):
        case 0:
            return pygate.AND()
        case 1:
            return pygate.NAND()
        case 2:
            return pygate.OR()
        case 3:
            return pygate.NOR()
        case 4:
            return pygate.XOR()
        case 5:
            return pygate.XNOR()
    
def conectar_entradas(entradas: list[pygate.Input], compuerta: pygate.Gate2) -> None:
    indices_validos = [i for i in range(len(entradas))]
    for k in range(len(compuerta.i)):
        if len(indices_validos) - 1 - k > 0:
            indice = random.randint(0, len(indices_validos) - 1 - k)
        else:
            indice = 0
        match random.randint(0, 1):
            case 0:
                compuerta.i[k] = entradas[indices_validos[indice]]
                conexiones.append(f"{entradas[indices_validos[indice]].name} -> {compuerta.name}")
            case 1:
                compuerta_auxiliar = pygate.NOT(entradas[indices_validos[indice]])
                compuerta.i[k] = compuerta_auxiliar
                conexiones.append(f"{entradas[indices_validos[indice]].name} -> {compuerta_auxiliar.name}")
                conexiones.append(f"{compuerta_auxiliar.name} -> {compuerta.name}")
        indices_validos.pop(indice)

def programa() -> None:
    a = pygate.Input(0)
    b = pygate.Input(0)
    compuerta = generar_compuerta_aleatoria()
    conectar_entradas([a, b], compuerta)
    print(f"Compuerta: {type(compuerta)}")
    print(f"Entrada 0: {type(compuerta.i[0])}")
    print(f"Entrada 1: {type(compuerta.i[1])}")
    for conexion in conexiones:
        print(f"{conexion}\n")
    for j in range(4):
        a.set([*format(j, "02b")][0])
        b.set([*format(j, "02b")][1])
        print(f"{j} | {a} {b} |{compuerta.o()}")
    
    print("\n" + compuerta.expresion())


os.system("cls")
programa()