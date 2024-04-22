import copy

class Piezas:
    empty: str = "   "
    red: str = " \33[91m■\33[0m "
    blue: str = " \33[96m■\33[0m "
    empty_selected: str = "\33[93m[\33[91m \33[93m]\33[0m"
    red_selected: str = "\33[93m[\33[91m■\33[93m]\33[0m"
    blue_selected: str = "\33[93m[\33[96m■\33[93m]\33[0m"
    pieza: tuple[str, str, str] = (empty, red, blue, empty_selected, red_selected, blue_selected)

class OhHi():
    '''
    Representa un tablero del juego 0h h1
    '''
    def __init__(self, filas:int = 8,
                 columnas:int | None = None,
                 elementos:list[list[int]] | None = None,
                 indices_rojos:list[int] | None = None,
                 indices_azules:list[int] | None = None) -> None:
        '''
        Crear un tablero con las propiedades del juego 0h h1.
        -----------------------------------------------------
        Parámetros de Dimensiones:
         filas: int = n; determina la cantidad de filas del tablero. (def=8)
         columnas: int = m; determina la cantidad de columnas del tablero. (Si no se especifica, columnas=filas)
        * OhHi(n, m) inicializa un tablero de n x m.
        * OhHi(n) inicializa un tablero de n x n.\n
        Parámetros de elementos:
         elementos: list[list[int]] = [[a1, a2, ..., aj], [b1, b2, ..., bj], ..., [i1, i2, ..., ij]]); determina todos los elementos del tablero. (ij = 0 | 1 | 2)
         indices_rojos: list[int] = [a1, a2, ..., ai]; determina los elementos rojos por índices. (ai = 0 | 1 | 2 | ... | filas * columnas)
         indices_azules: list[int] = [b1, b2, ..., bj]; determina los elementos azules por índices. (bj = 0 | 1 | 2 | ... | filas * columnas)
        * OhHi(n, m, elementos=[[a1, a2, ..., am], [b1, b2, ..., bm], ..., [n1, n2, ..., nm]]) inicializa un tablero n x m con elementos incluidos.
        * OhHi(n, elementos=[[a1, a2, ..., an], [b1, b2, ..., bn], ..., [n1, n2, ..., nn]]) inicializa un tablero n x n con elementos incluidos.
        * OhHi(n, indices_rojos=[a1, a2, ..., ai]) inicializa un tablero n x n con elementos rojos en los índices ai.
        * OhHi(n, m, indices_rojos=[a1, a2, ..., ai]) inicializa un tablero n x m con elementos rojos en los índices ai.
        * OhHi(n, indices_azules=[b1, b2, ..., bj]) inicializa un tablero n x n con elementos azules en los índices bj.
        * OhHi(n, m, indices_azules=[b1, b2, ..., bj]) inicializa un tablero n x m con elementos azules en los índices bj.
        * OhHi(n, indices_rojos=[a1, a2, ..., ai], indices_azules=[b1, b2, ..., bj) inicializa un tablero n x n con elementos rojos en los índices ai y elementos azules en los índices bj.
        * OhHi(n, m, indices_rojos=[a1, a2, ..., ai], indices_azules=[b1, b2, ..., bj]) inicializa un tablero n x m con elementos rojos en los índices ai y elementos azules en los índices bj.
        '''
        self.cantidad_filas = filas
        self.cantidad_columnas = filas if columnas==None else columnas
        if elementos == None:
            self.elementos:list[list[int]] = [[0 for j in range(self.cantidad_columnas)] for i in range(self.cantidad_filas)] #0:vacio; 1:rojo; 2:azul
            if indices_rojos != None:
                self.insertarElementosRojosPorIndices(indices_rojos)
            if indices_azules != None:
                self.insertarElementosAzulesPorIndices(indices_azules)
        else:
            self.insertarElementos(elementos)
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↓↓↓ \ Funciones visuales \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
    def printTablero(self) -> None:
        #elementos_visuales: list[list[str]] = [["   " for j in range(self.cantidad_columnas)] for i in range(self.cantidad_filas)]
        #for fila in range(self.cantidad_filas):
        #    for columna in range(self.cantidad_columnas):
        #        if self.elemento[fila][columna] == 1 or self.elemento[fila][columna] == 2:
        #            elementos_visuales[fila][columna] = Piezas.pieza[self.elemento[fila][columna]]
        borde_superior: str = "═══╤" * (self.cantidad_columnas - 1)
        borde_inferior: str = "═══╧" * (self.cantidad_columnas - 1)
        print("╔" + borde_superior + "═══╗")
        for fila in range(self.cantidad_filas):
            linea_elementos: str = "║"
            borde_separador: str = "───┼" * (self.cantidad_columnas - 1)
            for columna in range(self.cantidad_columnas - 1):
                linea_elementos += Piezas.pieza[self.elementos[fila][columna]] + "│"
            linea_elementos += Piezas.pieza[self.elementos[fila][self.cantidad_columnas - 1]] + "║"
            print(linea_elementos)
            if fila < (self.cantidad_filas - 1):
                print("╟" + borde_separador + "───╢")
            else:
                print("╚" + borde_inferior + "═══╝")
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↑↑↑ \ Funciones visuales \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↓↓↓ \ Inicializaciones \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
    def insertarElementosRojosPorIndices(self, elementos_rojos:list[int] = []) -> None:
        for elemento in elementos_rojos:
            if elemento >= self.cantidad_filas * self.cantidad_columnas:
                return
        for elemento in elementos_rojos:
            fila: int = int(elemento / self.cantidad_columnas)
            columna: int = elemento % self.cantidad_columnas
            self.elementos[fila][columna] = 1
    
    def insertarElementosAzulesPorIndices(self, elementos_azules:list[int] = []) -> None:
        for elemento in elementos_azules:
            if elemento >= self.cantidad_filas * self.cantidad_columnas:
                return
        for elemento in elementos_azules:
            fila: int = int(elemento / self.cantidad_columnas)
            columna: int = elemento % self.cantidad_columnas
            self.elementos[fila][columna] = 2
    
    def insertarElementosPorIndices(self, elementos_rojos:list[int] = [], elementos_azules:list[int] = []) -> None:
        self.insertarElementosRojosPorIndices(elementos_rojos)
        self.insertarElementosAzulesPorIndices(elementos_azules)
    
    def insertarElementos(self, elementos: list[list[int]]) -> None:
        if len(elementos) == self.cantidad_filas:
            for i in range(self.cantidad_filas):
                if len(elementos[i]) == self.cantidad_columnas:
                    pass
                else:
                    return
            self.elementos = elementos.copy()
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↑↑↑ \ Inicializaciones \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↓↓↓ \ Retornos \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
    def getFila(self, fila:int) -> list[int]:
        '''Devuelve una fila dada como cadena de elementos'''
        cadena_elementos:list[int] = self.elementos[fila].copy()
        return cadena_elementos
    
    def getColumna(self, columna:int) -> list[int]:
        '''Devuelve una columna dada como cadena de elementos'''
        cadena_elementos:list[int] = []
        for fila in range(self.cantidad_filas):
            cadena_elementos.append(self.elementos[fila][columna])
        return cadena_elementos
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↑↑↑ \ Retornos \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↓↓↓ \ Validaciones \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
    def condicionCadenaCompleta(self, cadena:list[int]) -> bool:
        '''
        Devuelve
         True: si los únicos elementos de la cadena son los números 1 o 2
         False: si la cadena tiene al menos un elemento distinto de los números 1 y 2
        '''
        for elemento in cadena:
            if elemento != 1 and elemento != 2:
                return False
        return True
    
    def condicionElementosAdyacentes(self, cadena:list[int]) -> bool:
        '''
        Devuelve
         True: si cumple que no hay 3 elementos adyacentes en una misma cadena
         False: si hay 3 elementos adyacentes en la misma cadena
        '''
        for i in range(len(cadena-2)):
            elemento_n1:int = cadena[i]
            elemento_n2:int = cadena[i+1]
            elemento_n3:int = cadena[i+2]
            if elemento_n1 == elemento_n2 and elemento_n2 == elemento_n3:
                return False
        return True
    
    def condicionCantidadElementos(self, cadena:list[int]) -> bool:
        '''
        Devuelve
         True: si la cadena tiene la misma cantidad de números 1 y 2
         False: si la cadena tiene al menos un elemento distinto de los números 1 y 2 o si tiene distinta cantidad de números 1 y 2
        '''
        contador_rojos:int = 0
        contador_azules:int = 0
        for elemento in cadena:
            if elemento == 1:
                contador_rojos += 1
            elif elemento == 2:
                contador_azules += 1
            else:
                return False
        if contador_azules == contador_rojos:
            return True
        else:
            return False
            
    def condicionCadenasDiferentes(self, cadena_a:list[int], cadena_b:list[int]) -> bool:
        '''
        Devuelve
         True: si la cadena a es distinta a la cadena b en al menos un elemento
         False: si la cadena a es igual a la cadena b
        '''
        for i in range(len(cadena_a)):
            if cadena_a[i] != cadena_b[i]:
                return True
        return False
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↑↑↑ \ Validaciones \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↓↓↓ \ Álgebra y aritmética \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
    def numeroElementosFila(self) -> int:
        '''
        Devuelve la cantidad de elementos de cada color que debe haber en cada fila
        '''
        return (int(self.cantidad_columnas/2))
    
    def numeroElementosColumna(self) -> int:
        '''
        Devuelve la cantidad de elementos de cada color que debe haber en cada columna
        '''
        return (int(self.cantidad_filas/2))
    
    def numeroRestanteElementosFila(self, fila:int) -> tuple[int, int]:
        '''
        Devuelve la cantidad de elementos restantes de cada color de una fila
        '''
        restantes_rojos = restantes_azules = self.numeroElementosFila()
        cadena:list[int] = self.getFila(fila)
        for elemento in cadena:
            if elemento == 1:
                restantes_rojos -= 1
            elif elemento == 2:
                restantes_azules -= 1
        return (restantes_rojos, restantes_azules)
    
    def numeroRestanteElementosColumna(self, columna:int) -> tuple[int, int]:
        '''
        Devuelve la cantidad de elementos restantes de cada color de una columna
        '''
        restantes_rojos = restantes_azules = self.numeroElementosColumna()
        cadena:list[int] = self.getColumna(columna)
        for elemento in cadena:
            if elemento == 1:
                restantes_rojos -= 1
            elif elemento == 2:
                restantes_azules -= 1
        return (restantes_rojos, restantes_azules)
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↑↑↑ \ Álgebra y aritmética \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↓↓↓ \ Métodos de inserción individuales\ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
    def criterioAdyacenciaFilas(self, *filas:int) -> None:
        for fila in filas:
            for columna in range(1, self.cantidad_columnas-1):
                elemento_n1:int = self.elementos[fila][columna-1]
                elemento_n2:int = self.elementos[fila][columna]
                elemento_n3:int = self.elementos[fila][columna+1]
                if elemento_n1 != 0 and elemento_n1 == elemento_n2 and elemento_n3 == 0:
                    if elemento_n1 == 1:
                        self.elementos[fila][columna+1] = 2
                    else:
                        self.elementos[fila][columna+1] = 1
                elif elemento_n2 != 0 and elemento_n2 == elemento_n3 and elemento_n1 == 0:
                    if elemento_n2 == 1:
                        self.elementos[fila][columna-1] = 2
                    else:
                        self.elementos[fila][columna-1] = 1
                elif elemento_n3 != 0 and elemento_n3 == elemento_n1 and elemento_n2 == 0:
                    if elemento_n3 == 1:
                        self.elementos[fila][columna] = 2
                    else:
                        self.elementos[fila][columna] = 1

    def criterioAdyacenciaColumnas(self, *columnas:int) -> None:
        for columna in columnas:
            for fila in range(1, self.cantidad_filas-1):
                elemento_n1:int = self.elementos[fila-1][columna]
                elemento_n2:int = self.elementos[fila][columna]
                elemento_n3:int = self.elementos[fila+1][columna]
                if elemento_n1 != 0 and elemento_n1 == elemento_n2 and elemento_n3 == 0:
                    if elemento_n1 == 1:
                        self.elementos[fila+1][columna] = 2
                    else:
                        self.elementos[fila+1][columna] = 1
                elif elemento_n2 != 0 and elemento_n2 == elemento_n3 and elemento_n1 == 0:
                    if elemento_n2 == 1:
                        self.elementos[fila-1][columna] = 2
                    else:
                        self.elementos[fila-1][columna] = 1
                elif elemento_n3 != 0 and elemento_n3 == elemento_n1 and elemento_n2 == 0:
                    if elemento_n3 == 1:
                        self.elementos[fila][columna] = 2
                    else:
                        self.elementos[fila][columna] = 1
    
    def criterioDiferentesFilas(self, *filas:int) -> None:
        for fila in filas:
            restantesFila:tuple[int, int] = self.numeroRestanteElementosFila(fila)
            for filaComparacion in range(self.cantidad_filas):
                if fila == filaComparacion:
                    continue
                restantesFilaComparacion:tuple[int, int] = self.numeroRestanteElementosFila(filaComparacion)
                suma:int = 0
                if restantesFilaComparacion[0] == 0 and restantesFila[0] == 1:
                    for columna in range(self.cantidad_columnas):
                        if self.elementos[fila][columna] == 1 and self.elementos[filaComparacion][columna] == 1:
                            suma += 1
                    if suma == self.numeroElementosFila() - 1:
                        for columna in range(self.cantidad_columnas):
                            if self.elementos[fila][columna] == 0 and self.elementos[filaComparacion][columna] == 1:
                                self.elementos[fila][columna] = 2
                elif restantesFilaComparacion[1] == 0 and restantesFila[1] == 1:
                    for columna in range(self.cantidad_columnas):
                        if self.elementos[fila][columna] == 2 and self.elementos[filaComparacion][columna] == 2:
                            suma += 1
                    if suma == self.numeroElementosFila() - 1:
                        for columna in range(self.cantidad_columnas):
                            if self.elementos[fila][columna] == 0 and self.elementos[filaComparacion][columna] == 2:
                                self.elementos[fila][columna] = 1

    def criterioDiferentesColumnas(self, *columnas:int) -> None:
        for columna in columnas:
            restantesColumna:tuple[int, int] = self.numeroRestanteElementosColumna(columna)
            for columnaComparacion in range(self.cantidad_columnas):
                if columna == columnaComparacion:
                    continue
                restantesColumnaComparacion:tuple[int, int] = self.numeroRestanteElementosColumna(columnaComparacion)
                suma:int = 0
                if restantesColumnaComparacion[0] == 0 and restantesColumna[0] == 1:
                    for fila in range(self.cantidad_filas):
                        if self.elementos[fila][columna] == 1 and self.elementos[fila][columnaComparacion] == 1:
                            suma += 1
                    if suma == self.numeroElementosFila() - 1:
                        for fila in range(self.cantidad_filas):
                            if self.elementos[fila][columna] == 0 and self.elementos[fila][columnaComparacion] == 1:
                                self.elementos[fila][columna] = 2
                elif restantesColumnaComparacion[0] == 0 and restantesColumna[0] == 1:
                    for fila in range(self.cantidad_filas):
                        if self.elementos[fila][columna] == 2 and self.elementos[fila][columnaComparacion] == 2:
                            suma += 1
                    if suma == self.numeroElementosFila() - 1:
                        for fila in range(self.cantidad_filas):
                            if self.elementos[fila][columna] == 0 and self.elementos[fila][columnaComparacion] == 2:
                                self.elementos[fila][columna] = 1
    
    def criterioColorRestanteFilas(self, *filas:int) -> None:
        for fila in filas:
            restantes = self.numeroRestanteElementosFila(fila)
            if restantes[0] == 0 and restantes[1] > 0:
                for columna in range(self.cantidad_columnas):
                    if self.elementos[fila][columna] == 0:
                        self.elementos[fila][columna] = 2
            elif restantes[1] == 0:
                for columna in range(self.cantidad_columnas):
                    if self.elementos[fila][columna] == 0:
                        self.elementos[fila][columna] = 1

    def criterioColorRestanteColumnas(self, *columnas:int) -> None:
        for columna in columnas:
            restantes = self.numeroRestanteElementosColumna(columna)
            if restantes[0] == 0 and restantes[1] > 0:
                for fila in range(self.cantidad_filas):
                    if self.elementos[fila][columna] == 0:
                        self.elementos[fila][columna] = 2
            elif restantes[1] == 0:
                for fila in range(self.cantidad_filas):
                    if self.elementos[fila][columna] == 0:
                        self.elementos[fila][columna] = 1

    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↑↑↑ \ Métodos de inserción individuales\ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↓↓↓ \ Métodos de inserción completos\ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
    def criterioAdyacencia(self) -> None:
        for fila in range(self.cantidad_filas):
            self.criterioAdyacenciaFilas(fila)
        for columna in range(self.cantidad_columnas):
            self.criterioAdyacenciaColumnas(columna)

    def criterioDiferentes(self) -> None:
        for fila in range(self.cantidad_filas):
            self.criterioDiferentesFilas(fila)
        for columna in range(self.cantidad_columnas):
            self.criterioDiferentesColumnas(columna)
    
    def criterioColorRestante(self) -> None:
        for fila in range(self.cantidad_filas):
            self.criterioColorRestanteFilas(fila)
        for columna in range(self.cantidad_columnas):
            self.criterioColorRestanteColumnas(columna)

    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↑↑↑ \ Métodos de inserción completos\ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↓↓↓ \ Guardado y comparación de estados \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
    def copy(self):
        return copy.deepcopy(self)
    
    def equals(self, other) -> bool:
        if self.cantidad_filas == other.cantidad_filas:
            if self.cantidad_columnas == other.cantidad_columnas:
                for fila in range(self.cantidad_filas):
                    for columna in range(self.cantidad_columnas):
                        if self.elementos[fila][columna] != other.elementos[fila][columna]:
                            return False
                return True
            else:
                return False
        else:
            return False
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↑↑↑ \ Guardado y comparación de estados \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #


    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↓↓↓ \ X \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↑↑↑ \ X \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #

