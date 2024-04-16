class NumberSums():
    '''
    Representa un tablero del juego Number Sums
    '''
    def __init__(self, filas:int = 5, columnas:int|None = None) -> None:
        '''
        Crea un tablero con las propiedades del juego Number Sums.
        * NumberSums(n, m) inicializa un tablero de n x m
        * NumberSums(n) inicializa un tablero de n x n
        '''
        self.cantidad_filas = filas
        self.cantidad_columnas = filas if columnas==None else columnas
        self.encabezados_filas:list[int] = [0 for i in range(self.cantidad_filas)]
        self.encabezados_columnas:list[int] = [0 for i in range(self.cantidad_columnas)]
        self.elementos_interiores:list[list[int]] = [[0 for j in range(self.cantidad_columnas)] for i in range(self.cantidad_filas)]
        self.estados_interiores: list[list[int]] = [[0 for j in range(self.cantidad_columnas)] for i in range(self.cantidad_filas)] # 0: desconocido 1: invalido; 2: valido en fila; 3: valido en columna; 4: valido en fila y columna; 5: necesario
    
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↓↓↓ \ Encabezados \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
    def ingresar_encabezado_fila(self, fila:int, encabezado:int) -> None:
        '''Ingresa el encabezado de la fila indicada (base-0).'''
        if fila >= 0 and fila < self.cantidad_filas:
            self.encabezados_filas[fila] = encabezado

    def ingresar_encabezados_filas(self, encabezados:list[int]) -> None:
        '''Ingresa el encabezado de las filas desde arriba hacia abajo.'''
        if len(encabezados) == self.cantidad_filas:
            self.encabezados_filas = encabezados

    def ingresar_encabezado_columna(self, columna:int, encabezado:int) -> None:
        '''Ingresa el encabezado de la columna indicada (base-0).'''
        if columna >= 0 and columna < self.cantidad_columnas:
            self.encabezados_columnas[columna] = encabezado

    def ingresar_encabezados_columnas(self, encabezados:list[int]) -> None:
        '''Ingresa el encabezado de las columnas de izquierda a derecha.'''
        if len(encabezados) == self.cantidad_columnas:
            self.encabezados_columnas = encabezados

    def ingresar_encabezados(self, encabezados_filas:list[int], encabezados_columnas:list[int]) -> None:
        '''Ingresa todos los encabezados. Toma como parametros los encabezados de las filas y las columnas por separado.'''
        self.ingresar_encabezados_filas(encabezados_filas)
        self.ingresar_encabezados_columnas(encabezados_columnas)
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↑↑↑ \ Encabezados \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↓↓↓ \ Numeros Interiores \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
    def ingresar_elemento(self, elemento:int, fila:int, columna:int) -> None:
        '''Ingresa un numero en la celda de interseccion entre la fila y la columna.'''
        if fila >= 0 and fila < self.cantidad_filas:
            if columna >= 0 and columna < self.cantidad_columnas:
                self.elementos_interiores[fila][columna] = elemento
            
    def ingresar_fila_de_elementos(self, elementos:list[int], fila:int) -> None:
        '''Ingresa todos los numeros de una fila dada de izquierda a derecha.'''
        if fila >= 0 and fila < self.cantidad_filas and len(elementos) == self.cantidad_columnas:
            self.elementos_interiores[fila] = elementos

    def ingresar_columna_de_elementos(self, elementos:list[int], columna:int) -> None:
        '''Ingresa todos los numeros de una columna dada desde arriba hacia abajo.'''
        if columna >= 0 and columna < self.cantidad_columnas and len(elementos) == self.cantidad_filas:
            for fila in range(self.cantidad_filas):
                self.elementos_interiores[fila][columna] = elementos[fila]
    
    def ingresar_elementos(self, elementos:list[list[int]]) -> None:
        '''Ingresa todos los elementos del tablero de izquierda a derecha y desde arriba hacia abajo.'''
        if len(elementos) == self.cantidad_filas:
            for fila in elementos:
                if len(fila) != self.cantidad_columnas:
                    return
            for fila in range(self.cantidad_filas):
                self.elementos_interiores[fila] = elementos[fila]
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↑↑↑ \ Numeros Interiores \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↓↓↓ \ Validaciones, descartes y busquedas \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
    def descartar_numeros_mayores(self) -> None:
        '''Descarta los numeros invalidos por ser mayores que el numero del encabezado'''
        for fila in range(self.cantidad_filas):
            for columna in range(self.cantidad_columnas):
                if self.encabezados_filas[fila] < self.elementos_interiores[fila][columna]:
                    self.estados_interiores[fila][columna] = 1
                elif self.encabezados_columnas[columna] < self.elementos_interiores[fila][columna]:
                    self.estados_interiores[fila][columna] = 1

    def buscar_necesarios_triviales_en_fila(self, fila:int) -> None:
        ''''Busca el numero que es necesario por ser el unico restantes en una fila dada y que no fue seleccionado aún sin haber llegado al objetivo'''
        indices_validos:list[int] = []
        suma:int = 0
        for columna in range(self.cantidad_columnas):
            if self.estados_interiores[fila][columna] == 4:
                indices_validos.append(columna)
                suma += self.elementos_interiores[fila][columna]
        if len(indices_validos) >= 1:
            if suma == self.suma_restante_fila(fila):
                for indice in indices_validos:
                    self.estados_interiores[fila][indice] = 5
            
    def buscar_necesarios_triviales_en_columna(self, columna:int) -> None:
        '''Busca el numero que es necesario por ser el unico restantes en una columna dada y que no fue seleccionado aún sin haber llegado al objetivo'''
        indices_validos: list[int] = []
        suma:int = 0
        for fila in range(self.cantidad_filas):
            if self.estados_interiores[fila][columna] == 4:
                indices_validos.append(fila)
                suma += self.elementos_interiores[fila][columna]
        if len(indices_validos) >= 1:
            if suma == self.suma_restante_columna(columna):
                for indice in indices_validos:
                    self.estados_interiores[indice][columna] = 5

    def buscar_necesarios_triviales(self) -> None:
        '''Busca los numeros que son necesarios por ser los unicos restantes en su fila o columna y que no fueron seleccionados aún sin haber llegado al objetivo'''
        for fila in range(self.cantidad_filas):
            self.buscar_necesarios_triviales_en_fila(fila)
        for columna in range(self.cantidad_columnas):
            self.buscar_necesarios_triviales_en_columna(columna)

    def buscar_necesarios_complejos_en_fila(self, fila:int) -> None:
        conteo_indices_validos:list[int] = [0 for i in range(self.cantidad_columnas)]
        
        #conteo_indices_validos[columna] += 1
        #conteo_indices_validos[self.cantidad_columnas] += 1
        #print(conteo_indices_validos)

    def validar_tablero(self) -> None:
        '''Valida que en principio todas las sumas de filas y columnas sean mayores o iguales al valor del encabezado'''
    
    #def validar_numeros_posibles_en_fila(self, fila:int) -> int:    #Retorna: 0 si debe volver al paso anterior; 1 si 
    #    for columna in range(self.cantidad_columnas):
    #        if self.estados_interiores[fila][columna] != 1:
    #            objetivo:int = self.encabezados_filas - self.elementos_interiores[fila][columna]
    #            if objetivo == 0:
    #                return 0
    #            elif objetivo > 0:
    #                pass
    #            else:
    #                pass 

    def validar_objetivo_en_fila(self, fila:int, objetivo:int=-1, columna_inicial:int=0, indices_validos:list[int]=[]) -> int:
        if objetivo == -1:
            objetivo = self.suma_restante_fila(fila)
        for columna in range(columna_inicial, self.cantidad_columnas):
            nuevos_indices_validos:list[int] = indices_validos.copy()
            if self.estados_interiores[fila][columna] != 1 and self.estados_interiores[fila][columna] != 5:
                nuevo_objetivo:int = objetivo - self.elementos_interiores[fila][columna]
                if nuevo_objetivo == 0:
                    nuevos_indices_validos.append(columna)
                    for i in nuevos_indices_validos:
                        if self.estados_interiores[fila][i] == 3 or self.estados_interiores[fila][i] == 4:
                            self.estados_interiores[fila][i] = 4
                        else:
                            self.estados_interiores[fila][i] = 2
                elif nuevo_objetivo > 0:
                    # Si llega a este punto despues de haber pasado por todos los elementos de la fila, hay un error en otro lado.
                    nuevos_indices_validos.append(columna)
                    for nueva_columna in range(columna+1, self.cantidad_columnas):
                        self.validar_objetivo_en_fila(fila, nuevo_objetivo, nueva_columna, nuevos_indices_validos)
                else:
                    return
                
    def validar_objetivo_en_columna(self, columna:int, objetivo:int=-1, fila_inicial:int=0, indices_validos:list[int]=[]) -> int:
        if objetivo == -1:
            objetivo = self.suma_restante_columna(columna)
        for fila in range(fila_inicial, self.cantidad_filas):
            nuevos_indices_validos:list[int] = indices_validos.copy()
            if self.estados_interiores[fila][columna] != 1 and self.estados_interiores[fila][columna] != 5:
                nuevo_objetivo:int = objetivo - self.elementos_interiores[fila][columna]
                if nuevo_objetivo == 0:
                    nuevos_indices_validos.append(fila)
                    for i in nuevos_indices_validos:
                        if self.estados_interiores[i][columna] == 2 or self.estados_interiores[i][columna] == 4:
                            self.estados_interiores[i][columna] = 4
                        else:
                            self.estados_interiores[i][columna] = 3
                elif nuevo_objetivo > 0:
                    # Si llega a este punto despues de haber pasado por todos los elementos de la fila, hay un error en otro lado.
                    nuevos_indices_validos.append(fila)
                    for nueva_fila in range(fila+1, self.cantidad_filas):
                        self.validar_objetivo_en_columna(columna, nuevo_objetivo, nueva_fila, nuevos_indices_validos)
                else:
                    return

    def revalidar_estados_temporales(self) -> None:
        for fila in range(self.cantidad_filas):
            for columna in range(self.cantidad_columnas):
                if self.estados_interiores[fila][columna] == 3 or self.estados_interiores[fila][columna] == 2:
                    self.estados_interiores[fila][columna] = 1
        self.buscar_necesarios_triviales()
        for fila in range(self.cantidad_filas):
            for columna in range(self.cantidad_columnas):            
                if self.estados_interiores[fila][columna] == 4:
                    self.estados_interiores[fila][columna] = 0

    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↑↑↑ \ Validaciones, descartes y busquedas \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↓↓↓ \ Algebra y aritmetica \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
    def suma_fila_necesarios(self, fila:int) -> int:
        '''Devuelve la suma de todos los elementos marcados como "Necesarios" actualmente de una fila dada'''
        suma:int = 0
        for columna in range(self.cantidad_columnas):
            suma += self.elementos_interiores[fila][columna] if self.estados_interiores[fila][columna] == 5 else 0
        return suma
    
    def suma_columna_necesarios(self, columna:int) -> int:
        '''Devuelve la suma de todos los elementos marcados como "Necesarios" actualmente de una columna dada'''
        suma:int = 0
        for fila in range(self.cantidad_filas):
            suma += self.elementos_interiores[fila][columna] if self.estados_interiores[fila][columna] == 5 else 0
        return suma
    
    def suma_restante_fila(self, fila:int) -> int:
        '''Devuelve el numero del encabezado menos la suma de todos los elementos marcados como "Necesarios"'''
        return self.encabezados_filas[fila] - self.suma_fila_necesarios(fila)
    
    def suma_restante_columna(self, columna:int) -> int:
        '''Devuelve el numero del encabezado menos la suma de todos los elementos marcados como "Necesarios"'''
        return self.encabezados_columnas[columna] - self.suma_columna_necesarios(columna)

    def suma_fila_validos_desde(self, fila:int, columna:int) -> int:
        '''Devuelve la suma de todos los elementos que no estén marcados como "Invalidos" de una fila dada a partir de una columna dada'''
        suma:int = 0
        for columna in range(columna, self.cantidad_columnas):
            suma += 0 if self.estados_interiores[fila][columna] == 1 else self.elementos_interiores[fila][columna]
        return suma
    
    def suma_columna_validos_desde(self, columna:int, fila:int) -> int:
        '''Devuelve la suma de todos los elementos que no estén marcados como "Invalidos" de una columna dada a partir de una fila dada'''
        suma:int = 0
        for fila in range(fila, self.cantidad_filas):
            suma += 0 if self.estados_interiores[fila][columna] == 1 else self.elementos_interiores[fila][columna]
        return suma

    def suma_fila_validos(self, fila:int) -> int:
        '''
        Devuelve la suma de todos los elementos que no estén marcados como "Invalidos" de una fila dada.\n
        Caso especial de suma_parcial_fila_desde_columna():
            suma_parcial_fila_desde_columna(fila, 0)
        '''
        return self.suma_fila_validos_desde(fila, 0)

    def suma_columna_validos(self, columna:int) -> int:
        '''
        Devuelve la suma de todos los elementos que no estén marcados como "Invalidos" de una columna dada.\n
        Caso especial de suma_parcial_columna_desde_fila():
            suma_parcial_columna_desde_fila(columna, 0)
        '''
        return self.suma_columna_validos_desde(columna, 0)

    def suma_especifica_fila(self, fila:int, mascara:list[int]) -> int:
        '''Devuelve la suma de todos los elementos que no estén marcados como "Invalidos" de una fila dada cuyo indice corresponda también con un elemento "1" en la mascara'''
        if len(mascara) == self.cantidad_columnas:
            suma:int = 0
            for columna in range(self.cantidad_columnas):
                suma += self.elementos_interiores[fila][columna] if (mascara[columna] == 1 and self.estados_interiores[fila][columna] != 1) else 0
            return suma
        return 0

    def suma_especifica_columna(self, columna:int, mascara:list[int]) -> int:
        '''Devuelve la suma de todos los elementos que no estén marcados como "Invalidos" de una columna dada cuyo indice corresponda también con un elemento "1" en la mascara'''
        if len(mascara) == self.cantidad_filas:
            suma:int = 0
            for fila in range(self.cantidad_filas):
                suma += self.elementos_interiores[fila][columna] if (mascara[fila] == 1 and self.estados_interiores[fila][columna] != 1) else 0
            return suma
        return 0

    def suma_fila_validos_excepto(self, fila:int, indice:int) -> int:
        '''Devuelve la suma de todos los elementos de una fila dada excepto el de indice especificado'''
        mascara:list[int] = [1 for i in range(self.cantidad_columnas)]
        mascara[indice] = 0
        return self.suma_especifica_fila(fila, mascara)
    
    def suma_columna_validos_excepto(self, columna:int, indice:int) -> int:
        '''Devuelve la suma de todos los elementos de una columna dada excepto el de indice especificado'''
        mascara:list[int] = [1 for i in range(self.cantidad_filas)]
        mascara[indice] = 0
        return self.suma_especifica_columna(columna, mascara)
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↑↑↑ \ Algebra y aritmetica \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↓↓↓ \ Funciones Visuales \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
    def imprimir_tablero(self) -> None:
        print("      ╭───┬───┬───┬───┬───┬───┬───┬───┬───╮\n" +
              "      │   │   │   │   │   │   │   │   │   │\n" +
              "      ╰───┴───┴───┴───┴───┴───┴───┴───┴───╯\n" +
              " ╭───╮╔═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╗\n" +
              " │   │║   │   │   │   │   │   │   │   │   ║\n" +
              " ├───┤╟───┼───┼───┼───┼───┼───┼───┼───┼───╢\n" +
              " │   │║   │   │   │   │   │   │   │   │   ║\n" +
              " ├───┤╟───┼───┼───┼───┼───┼───┼───┼───┼───╢\n" +
              " │   │║   │   │   │   │   │   │   │   │   ║\n" +
              " ├───┤╟───┼───┼───┼───┼───┼───┼───┼───┼───╢\n" +
              " │   │║   │   │   │   │   │   │   │   │   ║\n" +
              " ├───┤╟───┼───┼───┼───┼───┼───┼───┼───┼───╢\n" +
              " │   │║   │   │   │   │   │   │   │   │   ║\n" +
              " ├───┤╟───┼───┼───┼───┼───┼───┼───┼───┼───╢\n" +
              " │   │║   │   │   │   │   │   │   │   │   ║\n" +
              " ├───┤╟───┼───┼───┼───┼───┼───┼───┼───┼───╢\n" +
              " │   │║   │   │   │   │   │   │   │   │   ║\n" +
              " ├───┤╟───┼───┼───┼───┼───┼───┼───┼───┼───╢\n" +
              " │   │║   │   │   │   │   │   │   │   │   ║\n" +
              " ├───┤╟───┼───┼───┼───┼───┼───┼───┼───┼───╢\n" +
              " │   │║   │   │   │   │   │   │   │   │   ║\n" +
              " ╰───╯╚═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══╝\n")
        # Otros tipos de prints
        #                                                               #print("      ╭───┬───┬───┬───┬───┬───┬───┬───┬───╮\n" +            #print("      ┌───╥───╥───╥───╥───╥───╥───╥───╥───┐\n" +
        #print("     ╭───┬───┬───┬───┬───┬───┬───┬───┬───╮\n" +         #      "      │   │   │   │   │   │   │   │   │   │\n" +            #      "      │   ║   ║   ║   ║   ║   ║   ║   ║   │\n" +
        #      "     │   │   │   │   │   │   │   │   │   │\n" +         #      "      ╰───┴───┴───┴───┴───┴───┴───┴───┴───╯\n" +            #      "      └───╨───╨───╨───╨───╨───╨───╨───╨───┘\n" +
        #      " ╭──╴╔═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╗\n" +         #      " ╭───╮╔═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╗\n" +            #      " ┌───┐╔═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╗\n" +
        #      " │   ║   ║   ║   ║   ║   ║   ║   ║   ║   ║\n" +         #      " │   │║   ║   ║   ║   ║   ║   ║   ║   ║   ║\n" +            #      " │   │║   │   │   │   │   │   │   │   │   ║\n" +
        #      " ├──╴╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣\n" +         #      " ├───┤╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣\n" +            #      " ╞═══╡╟───┼───┼───┼───┼───┼───┼───┼───┼───╢\n" +
        #      " │   ║   ║   ║   ║   ║   ║   ║   ║   ║   ║\n" +         #      " │   │║   ║   ║   ║   ║   ║   ║   ║   ║   ║\n" +            #      " │   │║   │   │   │   │   │   │   │   │   ║\n" +
        #      " ├──╴╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣\n" +         #      " ├───┤╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣\n" +            #      " ╞═══╡╟───┼───┼───┼───┼───┼───┼───┼───┼───╢\n" +
        #      " │   ║   ║   ║   ║   ║   ║   ║   ║   ║   ║\n" +         #      " │   │║   ║   ║   ║   ║   ║   ║   ║   ║   ║\n" +            #      " │   │║   │   │   │   │   │   │   │   │   ║\n" +
        #      " ├──╴╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣\n" +         #      " ├───┤╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣\n" +            #      " ╞═══╡╟───┼───┼───┼───┼───┼───┼───┼───┼───╢\n" +
        #      " │   ║   ║   ║   ║   ║   ║   ║   ║   ║   ║\n" +         #      " │   │║   ║   ║   ║   ║   ║   ║   ║   ║   ║\n" +            #      " │   │║   │   │   │   │   │   │   │   │   ║\n" +
        #      " ├──╴╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣\n" +         #      " ├───┤╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣\n" +            #      " ╞═══╡╟───┼───┼───┼───┼───┼───┼───┼───┼───╢\n" +
        #      " │   ║   ║   ║   ║   ║   ║   ║   ║   ║   ║\n" +         #      " │   │║   ║   ║   ║   ║   ║   ║   ║   ║   ║\n" +            #      " │   │║   │   │   │   │   │   │   │   │   ║\n" +
        #      " ├──╴╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣\n" +         #      " ├───┤╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣\n" +            #      " ╞═══╡╟───┼───┼───┼───┼───┼───┼───┼───┼───╢\n" +
        #      " │   ║   ║   ║   ║   ║   ║   ║   ║   ║   ║\n" +         #      " │   │║   ║   ║   ║   ║   ║   ║   ║   ║   ║\n" +            #      " │   │║   │   │   │   │   │   │   │   │   ║\n" +
        #      " ├──╴╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣\n" +         #      " ├───┤╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣\n" +            #      " ╞═══╡╟───┼───┼───┼───┼───┼───┼───┼───┼───╢\n" +
        #      " │   ║   ║   ║   ║   ║   ║   ║   ║   ║   ║\n" +         #      " │   │║   ║   ║   ║   ║   ║   ║   ║   ║   ║\n" +            #      " │   │║   │   │   │   │   │   │   │   │   ║\n" +
        #      " ├──╴╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣\n" +         #      " ├───┤╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣\n" +            #      " ╞═══╡╟───┼───┼───┼───┼───┼───┼───┼───┼───╢\n" +
        #      " │   ║   ║   ║   ║   ║   ║   ║   ║   ║   ║\n" +         #      " │   │║   ║   ║   ║   ║   ║   ║   ║   ║   ║\n" +            #      " │   │║   │   │   │   │   │   │   │   │   ║\n" +
        #      " ├──╴╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣\n" +         #      " ├───┤╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣\n" +            #      " ╞═══╡╟───┼───┼───┼───┼───┼───┼───┼───┼───╢\n" +
        #      " │   ║   ║   ║   ║   ║   ║   ║   ║   ║   ║\n" +         #      " │   │║   ║   ║   ║   ║   ║   ║   ║   ║   ║\n" +            #      " │   │║   │   │   │   │   │   │   │   │   ║\n" +
        #      " ╰──╴╚═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╝\n")          #      " ╰───╯╚═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╝\n")             #      " └───┘╚═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══╝\n")
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↑↑↑ \ Funciones Visuales \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↓↓↓ \ x \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
    
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↑↑↑ \ x \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #