class OhHi():
    '''
    Representa un tablero del juego 0h h1
    '''
    def __init__(self, filas:int = 4, columnas:int|None = None) -> None:
        '''
        Crear un tablero con las propiedades del juego 0h h1.
        * NumberSums(n, m) inicializa un tablero de n x m
        * NumberSums(n) inicializa un tablero de n x n
        '''
        self.cantidad_filas = filas
        self.cantidad_columnas = filas if columnas==None else columnas
        self.elemento:list[list[int]] = [[0 for j in range(self.cantidad_columnas)] for i in range(self.cantidad_filas)] #0:vacio; 1:rojo; 2:azul
    
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↓↓↓ \ Retornos \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
    def getFila(self, fila:int) -> list[int]:
        '''Devuelve una fila dada como cadena de elementos'''
        cadena_elementos:list[int] = self.elemento[fila].copy()
        return cadena_elementos
    
    def getColumna(self, columna:int) -> list[int]:
        '''Devuelve una columna dada como cadena de elementos'''
        cadena_elementos:list[int] = []
        for fila in range(self.cantidad_filas):
            cadena_elementos.append(self.elemento[fila][columna])
        return cadena_elementos
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↑↑↑ \ Retornos \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↓↓↓ \ Validaciones \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
    def condicionCadenaCompleta(self, cadena:list[int]) -> bool:
        '''
        Devuelve
         True: si los únicos elementos de la cadena son los números 1 o 2
         False: si tiene al menos un elemento distinto de los números 1 y 2
        '''
        for elemento in cadena:
            if elemento != 1 and elemento != 2:
                return False
        return True
    
    def condicionElementosAdyacentes(self, cadena:list[int]) -> bool:
        for i in range(len(cadena-2)):
            elemento_n1:int = cadena[i]
            elemento_n2:int = cadena[i+1]
            elemento_n3:int = cadena[i+2]
            if elemento_n1 == elemento_n2 and elemento_n2 == elemento_n3:
                return False
        return True
    
    def condicionMismaCantidadElementos(self, cadena:list[int]) -> bool:
        contador_rojos:int = 0
        contador_azules:int = 0
        for elemento in cadena:
            if elemento == 1:
                contador_rojos += 1
            elif elemento == 2:
                contador_azules += 1
            else:
                return False
            
    def condicionCadenasIguales(self, cadena_a:list[int], cadena_b:list[int]) -> bool:
        for i in range(len(cadena_a)):
            #if
            pass

    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↑↑↑ \ Validaciones \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↓↓↓ \ Álgebra y aritmética \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
    def numeroElementosFila(self) -> int:
        return (self.cantidad_columnas/2)
    
    def numeroElementosColumna(self) -> int:
        return (self.cantidad_filas/2)
    
    def numeroRestanteElementosFila(self, fila:int) -> tuple[int, int]:
        restantes_rojos = restantes_azules = self.numeroElementosFila()
        cadena:list[int] = self.getFila(fila)
        for elemento in cadena:
            if elemento == 1:
                restantes_rojos -= 1
            elif elemento == 2:
                restantes_azules -= 1
        return (restantes_rojos, restantes_azules)
    
    def numeroRestanteElementosColumna(self, columna:int) -> tuple[int, int]:
        restantes_rojos = restantes_azules = self.numeroElementosColumna()
        cadena:list[int] = self.getColumna(columna)
        for elemento in cadena:
            if elemento == 1:
                restantes_rojos -= 1
            elif elemento == 2:
                restantes_azules -= 1
        return (restantes_rojos, restantes_azules)
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↑↑↑ \ Álgebra y aritmética \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #

    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↓↓↓ \ X \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↑↑↑ \ X \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
