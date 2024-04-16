import os

os.system("cls")

class Sudoku():
    '''
    Controlador de un juego de Sudoku.

    ...

    Atributos
    ---------
    regiones: list[list[Region]]
        Arreglo 3x3 de elementos Region    

    Metodos de instancia
    -------
    >>> def validar_fila(self, fila:int) -> bool:

    Notas
    -----
    fila: 0 | 1 | 2
    columna: 0 | 1 | 2
    region_x: 0 | 1 | 2
    region_y: 0 | 1 | 2
    '''
    
    def __init__(self) -> None:
        self.regiones: list[list[Region]] = [[Region() for i in range(3)] for j in range(3)]
        self.filas_error: list[int]
        self.columnas_error: list[int]
        self.regiones_error: list[int]
        self.numeros_error: list[int]

    def ingresar_numero(self, numero:str, fila:int, columna:int) -> None:
        # region_y: int = int(fila/3)
        # region_x: int = int(columna/3)
        # fila_relativa: int = fila%3
        # columna_relativa: int = columna%3
        self.regiones[int(fila/3)][int(columna/3)].ingresar_numero(numero=numero, fila=(fila%3), columna=(columna%3))

    def devolver_numero(self, numero:str, fila:int, columna:int) -> None:
        # region_y: int = int(fila/3)
        # region_x: int = int(columna/3)
        # fila_relativa: int = fila%3
        # columna_relativa: int = columna%3
        self.regiones[int(fila/3)][int(columna/3)].devolver_numero(fila=(fila%3), columna=(columna%3))

    def ingresar_fila(self, numeros:str, fila:int) -> None:
        
        region_y: int = int(fila/3)
        fila_relativa: int = fila%3
        for region_x in range(3):
            self.regiones[region_y][region_x].ingresar_fila(numeros=(numeros[region_x*3]+numeros[region_x*3+1]+numeros[region_x*3+2]), fila=fila_relativa)

    def devolver_fila(self, fila:int) -> str:
        cadena:str = ""
        region_y: int = int(fila/3)
        fila_relativa: int = fila%3
        for region_x in range(3):
            cadena += self.regiones[region_y][region_x].devolver_fila(fila=fila_relativa)
        return cadena

    def validar_fila(self, fila:int) -> tuple[bool, bool]:
        cadena: str = self.devolver_fila(fila=fila)
        return self.validar_cadena(cadena)

    def ingresar_columna(self, numeros:str, columna:int) -> None:
        numeros = numeros.ljust(9, " ")
        region_x: int = int(columna/3)
        columna_relativa: int = columna%3
        for region_y in range(3):
            self.regiones[region_y][region_x].ingresar_columna(numeros=(numeros[region_x*3]+numeros[region_x*3+1]+numeros[region_x*3+2]), columna=columna_relativa)

    def devolver_columna(self, columna:int) -> str:
        cadena:str = ""
        region_x: int = int(columna/3)
        columna_relativa: int = columna%3
        for region_y in range(3):
            cadena += self.regiones[region_y][region_x].devolver_columna(fila=columna_relativa)
        return cadena

    def validar_columna(self, columna:int) -> tuple[bool, bool]:
        cadena: str = self.devolver_columna(columna=columna)
        return self.validar_cadena(cadena)
    
    def ingresar_region(self, numeros:str, region_x:int, region_y:int) -> None:
        numeros = numeros.ljust(9, " ")
        self.regiones[region_y][region_x].ingresar_region(numeros=numeros)

    def devolver_region(self, region_x:int, region_y:int) -> str:
        return (self.regiones[region_y][region_x].devolver_region())

    def validar_region(self, region_x:int, region_y:int) -> tuple[bool, bool]:
        cadena: str = self.devolver_region(region_x=region_x, region_y=region_y)
        return self.validar_cadena(cadena)

    def devolver_tablero(self) -> list[str]:
        tablero:list[str] = ["" for i in range(9)]
        for fila in range(9):
            tablero[fila] = self.devolver_fila(fila)
        return tablero

    def validar_cadena(self, cadena:str) -> tuple[bool, bool]:
        cadena = cadena.replace(" ", "")
        cadena_completa: bool = True if len(cadena) == 9 else False
        for e1 in range(len(cadena) - 1):
            for e2 in range(e1 + 1, len(cadena)):
                if cadena[e1] == cadena[e2]:
                    return [False, cadena_completa]
        return [True, cadena_completa]
    
    def validar(self, filtro:str, indice:int) -> tuple[bool, bool]:
        if indice < 0 or indice > 8:
            return [False, False]
        else:
            match(filtro.lower()):
                case "fila":
                    return self.validar_fila(fila=indice)
                case "columna":
                    return self.validar_columna(columna=indice)
                case "region":
                    return self.validar_region(region_x=indice%3, region_y=int(indice/3))
                case _:
                    return [False, False]

    def imprimir_tablero(self) -> None:
        tablero:list[str] = self.devolver_tablero()
        print("╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗")
        for fila in range(9):
            print("║", end="")
            for columna in range(9):
                if columna%3 == 2:
                    print(f" {tablero[fila][columna]} ║", end="")
                else:
                    print(f" {tablero[fila][columna]} │", end="")
            print()
            if fila%3 == 2:
                if fila == 8:
                    print("╚═══╧═══╧═══╩═══╧═══╧═══╩═══╧═══╧═══╝")
                else:
                    print("╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣")
            else:
                    print("╟───┼───┼───╫───┼───┼───╫───┼───┼───╢")
        #print(
        #    "╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗\n" +
        #    f"║ {n[0][0]} │ {n[0][1]} │ {n[0][2]} ║ {n[0][3]} │ {n[0][4]} │ {n[0][5]} ║ {n[0][6]} │ {n[0][7]} │ {n[0][8]} ║\n" +
        #    "╟───┼───┼───╫───┼───┼───╫───┼───┼───╢\n" +
        #    f"║ {n[1][0]} │ {n[1][1]} │ {n[1][2]} ║ {n[1][3]} │ {n[1][4]} │ {n[1][5]} ║ {n[1][6]} │ {n[1][7]} │ {n[1][8]} ║\n" +
        #    "╟───┼───┼───╫───┼───┼───╫───┼───┼───╢\n" +
        #    f"║ {n[2][0]} │ {n[2][1]} │ {n[2][2]} ║ {n[2][3]} │ {n[2][4]} │ {n[2][5]} ║ {n[2][6]} │ {n[2][7]} │ {n[2][8]} ║\n" +
        #    "╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣\n" +
        #    f"║ {n[3][0]} │ {n[3][1]} │ {n[3][2]} ║ {n[3][3]} │ {n[3][4]} │ {n[3][5]} ║ {n[3][6]} │ {n[3][7]} │ {n[3][8]} ║\n" +
        #    "╟───┼───┼───╫───┼───┼───╫───┼───┼───╢\n" +
        #    f"║ {n[4][0]} │ {n[4][1]} │ {n[4][2]} ║ {n[4][3]} │ {n[4][4]} │ {n[4][5]} ║ {n[4][6]} │ {n[4][7]} │ {n[4][8]} ║\n" +
        #    "╟───┼───┼───╫───┼───┼───╫───┼───┼───╢\n" +
        #    f"║ {n[5][0]} │ {n[5][1]} │ {n[5][2]} ║ {n[5][3]} │ {n[5][4]} │ {n[5][5]} ║ {n[5][6]} │ {n[5][7]} │ {n[5][8]} ║\n" +
        #    "╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣\n" +
        #    f"║ {n[6][0]} │ {n[6][1]} │ {n[6][2]} ║ {n[6][3]} │ {n[6][4]} │ {n[6][5]} ║ {n[6][6]} │ {n[6][7]} │ {n[6][8]} ║\n" +
        #    "╟───┼───┼───╫───┼───┼───╫───┼───┼───╢\n" +
        #    f"║ {n[7][0]} │ {n[7][1]} │ {n[7][2]} ║ {n[7][3]} │ {n[7][4]} │ {n[7][5]} ║ {n[7][6]} │ {n[7][7]} │ {n[7][8]} ║\n" +
        #    "╟───┼───┼───╫───┼───┼───╫───┼───┼───╢\n" +
        #    f"║ {n[8][0]} │ {n[8][1]} │ {n[8][2]} ║ {n[8][3]} │ {n[8][4]} │ {n[8][5]} ║ {n[8][6]} │ {n[8][7]} │ {n[8][8]} ║\n" +
        #    "╚═══╧═══╧═══╩═══╧═══╧═══╩═══╧═══╧═══╝\n"
        #)

    
    #def validar_region(self, region_x:int, region_y:int) -> bool

class Region():
    def __init__(self) -> None:
        self.numeros: list[list[str]] = [[" " for i in range(3)] for j in range(3)]

    def ingresar_numero(self, numero:str, fila:int, columna:int) -> None:
        self.numeros[fila][columna] = numero

    def devolver_numero(self, fila:int, columna:int) -> str:
        return self.numeros[fila][columna]

    def ingresar_fila(self, numeros:str, fila:int) -> None:
        for columna in range(3):
            self.numeros[fila][columna] = numeros[columna]

    def devolver_fila(self, fila:int=0) -> str:
        cadena: str = ""
        for columna in range(3):
            cadena += self.numeros[fila][columna]
        return cadena
    
    def ingresar_columna(self, numeros:str, columna:int) -> None:
        for fila in range(3):
            self.numeros[fila][columna] = numeros[fila]
    
    def devolver_columna(self, columna:int=0) -> str:
        cadena: str = ""
        for fila in range(3):
            cadena += self.numeros[fila][columna]
        return cadena
    
    def ingresar_region(self, numeros:str) -> None:
        for fila in range(3):
            for columna in range(3):
                self.numeros[fila][columna] = numeros[fila*3+columna]

    def devolver_region(self) -> str:
        cadena: str = ""
        for fila in range(3):
            for columna in range(3):
                cadena += self.numeros[fila][columna]
        return cadena


        #sos el amor de mi vida, te amo

#def revisar_filas(n: list[str]) -> list[int]:
#    filas_error: list[int] = []
#    for fila in range(9):
#        for e1 in range(8):
#            for e2 in range(e1, 9):
#                if n[fila][e1] == n[fila][e2]:
#                    filas_error.append(fila)
#    return filas_error

solucion: list[str] = ["534678912",
                       "672195348",
                       "198342567",
                       "859761423",
                       "426853791",
                       "713924856",
                       "961537284",
                       "287419635",
                       "345286179"]

sudoku = Sudoku()
#sudoku.imprimir_tablero()
print(sudoku.regiones[0][0].numeros)

sudoku.regiones[0][0].ingresar_region("534678912")
sudoku.regiones[0][1].ingresar_region("672195348")
sudoku.regiones[0][2].ingresar_region("198342567")
sudoku.regiones[1][0].ingresar_region("859761423")
sudoku.regiones[1][1].ingresar_region("426853791")
sudoku.regiones[1][2].ingresar_region("713924856")
sudoku.regiones[2][0].ingresar_region("961537284")
sudoku.regiones[2][1].ingresar_region("287419635")
sudoku.regiones[2][2].ingresar_region("345286179")

sudoku.imprimir_tablero()

sudoku.ingresar_fila("534672198", 0)
sudoku.ingresar_fila("678195342", 1)
sudoku.ingresar_fila("912348567", 2)
sudoku.ingresar_fila("859426713", 3)
sudoku.ingresar_fila("761853924", 4)
sudoku.ingresar_fila("423791856", 5)
sudoku.ingresar_fila("961287345", 6)
sudoku.ingresar_fila("537419286", 7)
sudoku.ingresar_fila("284635179", 8)

sudoku.imprimir_tablero()