from oh_hi import OhHi
import solucionador as sl
from pynput.keyboard import Key, Listener
import os

tecla_presionada = ""
listens:bool = False
estado:int = 0
estado_interno:int = 0
actualizar_pantalla:bool = True

def on_press(key):
    global tecla_presionada
    if listens:
        tecla_presionada = '{0}'.format(key)
    if key == Key.esc:
        print("Ctrl + C para salir")
        quit()

def on_release(key):
    if key == Key.esc:
        return False

listener = Listener(on_press=on_press, on_release=on_release, suppress=True)

def cambiar_estado(est:int, est_int:int):
    global estado, estado_interno, actualizar_pantalla
    estado = est
    estado_interno = est_int
    actualizar_pantalla = True

def estado_siguiente():
    global estado, estado_interno, actualizar_pantalla
    estado += 1
    estado_interno = 0
    actualizar_pantalla = True

def estado_anterior():
    global estado, estado_interno, actualizar_pantalla
    estado -= 1
    estado_interno = 0
    actualizar_pantalla = True


def titulo() -> None:
    print("\033[96m  .----. \033[0m,--.       ,--.    \033[91m.---. \n"
          "\033[96m /  ..  \\\033[0m|  |       |  |   \033[91m/_   | \n"
          "\033[96m.  / /|  \033[0m|  |       |  |    \033[91m|   . \n"
          "\033[96m|  |//|  \033[0m|  `---.   |  `---.\033[91m|   | \n"
          "\033[96m'  |/ /  \033[0m|  .-.  |  |  .-.  \033[91m|   ' \n"
          "\033[96m \\  `'  /\033[0m|  | |  |  |  | | \033[91m |   | \n"
          "\033[96m  `----' \033[0m`--' `--'  `--' `--\033[91m`---' \n\033[0m")
    print("   Presione \033[4mEnter\033[0m para comenzar")

def vista() -> None:
    global listens, tecla_presionada, estado, estado_interno, actualizar_pantalla
    ejecucion:bool = True
    tipo_tablero:str = "Cuadrado"
    filas_tablero:int = 2
    columnas_tablero:int = 2
    tablero:OhHi|None = None
    tablero_solucionado:OhHi|None = None
    nuevo_tablero:bool = True
    posiciones_tablero:tuple[int,int] = [0, 0]

    listens = True
    while ejecucion:
        tecla_presionada = ""
        match estado:
            case 0:
                os.system("cls")
                titulo()
                actualizar_pantalla = False
                while not actualizar_pantalla:
                    if tecla_presionada == "Key.enter":
                        estado_siguiente()
            case 1:
                os.system("cls")
                print("\033[90m- \033[94mPropiedades del tablero \033[90m-\n")
                flechas_filas_arriba:str = "▲"
                flechas_filas_abajo:str = "▼"
                flechas_columnas_arriba:str = "▲"
                flechas_columnas_abajo:str = "▼"
                if tipo_tablero == "Cuadrado":
                    filas_len = len(str(filas_tablero))
                    flechas_filas_arriba = "▲" + "—" * (2 * filas_len + 1) + "▲"
                    flechas_filas_abajo = "▼" + "—" * (2 * filas_len + 1) + "▼"
                elif tipo_tablero == "Rectangulo":
                    filas_len = len(str(filas_tablero))
                    if filas_len == 2:
                        flechas_filas_arriba = "▲▲"
                        flechas_filas_abajo = "▼▼"
                    elif filas_len > 2:
                        flechas_filas_arriba = "▲" + "—" * (filas_len - 2) + "▲"
                        flechas_filas_abajo = "▼" + "—" * (filas_len - 2) + "▼"
                    columnas_len = len(str(columnas_tablero))
                    if columnas_len == 2:
                        flechas_columnas_arriba = "▲▲"
                        flechas_columnas_abajo = "▼▼"
                    elif columnas_len > 2:
                        flechas_columnas_arriba = "▲" + "—" * (columnas_len - 2) + "▲"
                        flechas_columnas_abajo = "▼" + "—" * (columnas_len - 2) + "▼" 
                match estado_interno:
                    case 0:
                        print(f"\033[91mTablero\033[90m: \033[93m◄\033[0m {tipo_tablero.center(10, " ")} \033[93m►\033[0m")
                        if tipo_tablero == "Cuadrado":
                            print(f"             \033[90m{flechas_filas_arriba}\033[0m")
                            print(f"\033[91mDimensiones\033[90m:\033[0m {filas_tablero} x {filas_tablero}")
                            print(f"             \033[90m{flechas_filas_abajo}\033[0m")
                        elif tipo_tablero == "Rectangulo":
                            print(f"             \033[90m{flechas_filas_arriba}\033[0m   \033[90m{flechas_columnas_arriba}\033[0m")
                            print(f"\033[91mDimensiones\033[90m:\033[0m {filas_tablero} x {columnas_tablero}")
                            print(f"             \033[90m{flechas_filas_abajo}\033[0m   \033[90m{flechas_columnas_abajo}\033[0m")
                    case 1:
                        print(f"\033[91mTablero\033[90m: \033[90m◄\033[0m {tipo_tablero.center(10, " ")} \033[90m►\033[0m")
                        if tipo_tablero == "Cuadrado":
                            print(f"             \033[93m{flechas_filas_arriba}\033[0m")
                            print(f"\033[91mDimensiones\033[90m:\033[0m {filas_tablero} x {filas_tablero}")
                            print(f"             \033[93m{flechas_filas_abajo}\033[0m")
                        elif tipo_tablero == "Rectangulo":
                            print(f"             \033[93m{flechas_filas_arriba}\033[0m   \033[90m{flechas_columnas_arriba}\033[0m")
                            print(f"\033[91mDimensiones\033[90m:\033[0m {filas_tablero} x {columnas_tablero}")
                            print(f"             \033[93m{flechas_filas_abajo}\033[0m   \033[90m{flechas_columnas_abajo}\033[0m")                           
                    case 2:
                        print(f"\033[91mTablero\033[90m: \033[90m◄\033[0m {tipo_tablero.center(10, " ")} \033[90m►\033[0m")
                        print(f"             \033[90m{flechas_filas_arriba}\033[0m   \033[93m{flechas_columnas_arriba}\033[0m")
                        print(f"\033[91mDimensiones\033[90m:\033[0m {filas_tablero} x {columnas_tablero}")
                        print(f"             \033[90m{flechas_filas_abajo}\033[0m   \033[93m{flechas_columnas_abajo}\033[0m")   
                print("\033[92m↑\033[90m/\033[92m↓\033[90m:\033[0m Seleccionar Propiedad \033[90m| \033[92m→\033[90m/\033[92m←\033[90m:\033[0m Cambiar Valor")
                actualizar_pantalla = False
                while not actualizar_pantalla:
                    match estado_interno:
                        case 0:
                            if tecla_presionada == "Key.left" or tecla_presionada == "Key.right":
                                if tipo_tablero == "Cuadrado":
                                    tipo_tablero = "Rectangulo"
                                    actualizar_pantalla = True
                                else:
                                    tipo_tablero = "Cuadrado"
                                    actualizar_pantalla = True
                            elif tecla_presionada == "Key.down":
                                    estado_interno = 1
                                    actualizar_pantalla = True
                        case 1:
                            if tecla_presionada == "Key.right":
                                filas_tablero += 2
                                actualizar_pantalla = True
                            elif tecla_presionada == "Key.left":
                                if filas_tablero > 2:
                                    filas_tablero -= 2
                                    actualizar_pantalla = True
                            elif tecla_presionada == "Key.up":
                                    estado_interno = 0
                                    actualizar_pantalla = True
                            elif tecla_presionada == "Key.down" and tipo_tablero == "Rectangulo":
                                    estado_interno = 2
                                    actualizar_pantalla = True
                        case 2:
                            if tecla_presionada == "Key.right":
                                columnas_tablero += 2
                                actualizar_pantalla = True
                            elif tecla_presionada == "Key.left":
                                if columnas_tablero > 2:
                                    columnas_tablero -= 2
                                    actualizar_pantalla = True
                            if tecla_presionada == "Key.up":
                                    estado_interno = 1
                                    actualizar_pantalla = True
                    if tecla_presionada == "Key.enter":
                        nuevo_tablero = True
                        estado_siguiente()
                    elif tecla_presionada == "Key.backspace":
                        estado_anterior()
            case 2:
                os.system("cls")
                if nuevo_tablero:
                    if tipo_tablero == "Cuadrado":
                        tablero = sl.getTableroInicial(filas_tablero)
                        columnas_tablero = filas_tablero
                    else:
                        tablero = sl.getTableroInicial(filas_tablero, columnas_tablero)
                    nuevo_tablero = False
                print(f"\033[90m- \033[94mTablero \033[0m{filas_tablero} \033[90mx \033[0m{columnas_tablero} \033[90m-\033[0m")
                tablero.elementos[posiciones_tablero[0]][posiciones_tablero[1]] += 3
                tablero.printTablero()
                tablero.elementos[posiciones_tablero[0]][posiciones_tablero[1]] -= 3
                print("\n\033[92m↑\033[90m/\033[92m↓\033[90m/\033[92m→\033[90m/\033[92m←\033[90m:\033[0m Seleccionar posicion")
                print("\033[92m0\033[90m:\033[0m Vacio \33[90m| \033[92m1\033[90m:\033[91m Rojo \033[90m| \033[92m2\033[90m:\033[96m Azul\033[0m")
                actualizar_pantalla = False
                while not actualizar_pantalla:
                    if tecla_presionada == "Key.enter":
                        estado_siguiente()
                    elif tecla_presionada == "Key.backspace":
                        estado_anterior()
                    elif tecla_presionada == "Key.up":
                        if posiciones_tablero[0] > 0:
                            posiciones_tablero[0] -= 1
                        actualizar_pantalla = True
                    elif tecla_presionada == "Key.down":
                        if posiciones_tablero[0] < filas_tablero - 1:
                            posiciones_tablero[0] += 1
                        actualizar_pantalla = True
                    elif tecla_presionada == "Key.right":
                        if posiciones_tablero[1] < columnas_tablero - 1:
                            posiciones_tablero[1] += 1
                        actualizar_pantalla = True
                    elif tecla_presionada == "Key.left":
                        if posiciones_tablero[1] > 0:
                            posiciones_tablero[1] -= 1
                        actualizar_pantalla = True
                    elif tecla_presionada == "'0'":
                        tablero.elementos[posiciones_tablero[0]][posiciones_tablero[1]] = 0
                        actualizar_pantalla = True
                    elif tecla_presionada == "'1'":
                        tablero.elementos[posiciones_tablero[0]][posiciones_tablero[1]] = 1
                        actualizar_pantalla = True
                    elif tecla_presionada == "'2'":
                        tablero.elementos[posiciones_tablero[0]][posiciones_tablero[1]] = 2
                        actualizar_pantalla = True
            case 3:
                os.system("cls")
                print(f"\033[90m- \033[94mTablero \033[0m{filas_tablero} \033[90mx \033[0m{columnas_tablero} \033[90m-\033[0m")
                tablero_solucionado = tablero.copy()
                sl.getTableroSolucionado(tablero_solucionado).printTablero()
                actualizar_pantalla = False
                while not actualizar_pantalla:
                    if tecla_presionada == "Key.enter":
                        ejecucion = False
                        actualizar_pantalla = True
                    elif tecla_presionada == "Key.backspace":
                        estado_anterior()
                        


listener.start()
print('\033[?25l', end="")
vista()
print('\033[?25h', end="")