import random   # Librería para generar números aleatorios
import math     # Librería para utilizar operaciones matemáticas

class AlgoritmoGenetico:
    '''Algoritmo Genético'''
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↓↓↓ \ Init \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #

    def __init__(
            self,
            tipo_seleccion: str = 'ruleta',
            tipo_crossover: str = '1pto',
            tipo_mutacion: str = 'invertida',
            prob_crossover: float = 1,
            prob_mutacion: float = 0,
            porcentaje_elitismo: float = 0,
            porcentaje_seleccion: float = 0,
            cant_individuos: int = 10,
            cant_generaciones: int = 20,
            dominio: tuple[int, int] = [0, 255],
            funcion_objetivo = lambda x : x
            ) -> None:
        '''
        Inicializa un Algoritmo Genético con las configuraciones dadas.\n
        Parámetros por defecto
        --
        - Tipo Seleccion: Ruleta
        - Tipo Crossover: 1 Punto
        - Tipo Mutacion: Invertida
        - Prob. Crossover: 100%
        - Prob. Mutacion: 0%
        - Cant. Individuos: 20
        - Cant. Ciclos: 20
        - Cant. Generaciones: 20
        - Dominio: [0, 2^8 - 1]
        - Funcion Objetivo: f(x) = x
        - Elitismo: No
        '''
        self.tipo_seleccion: str = tipo_seleccion
        self.tipo_crossover: str = tipo_crossover
        self.tipo_mutacion: str = tipo_mutacion
        self.prob_crossover: float = prob_crossover
        self.prob_mutacion: float = prob_mutacion
        self.porcentaje_elitismo: int = porcentaje_elitismo
        self.porcentaje_seleccion: int = porcentaje_seleccion if self.tipo_seleccion.lower() == "torneo" else 0
        self.cant_individuos: int = cant_individuos
        self.cant_generaciones: int = cant_generaciones
        self.dominio: tuple[int, int] = dominio
        self.poblacion: list[int] = []
        self.poblacion_siguiente: list[int] = []
        self.list_fitness: list[float] = []
        self.funcion_objetivo = funcion_objetivo
        self.generacion_actual: int = 0
      
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↑↑↑ \ Init \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #   
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↓↓↓ \ Setters y Getters \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
    def setTipoSeleccion(self, tipo_seleccion: str) -> None: self.tipo_seleccion = tipo_seleccion
    
    def setTipoCrossover(self, tipo_crossover: str) -> None: self.tipo_crossover = tipo_crossover
    
    def setTipoMutacion(self, tipo_mutacion: str) -> None: self.tipo_mutacion = tipo_mutacion
    
    def setProbCrossover(self, prob_crossover: float) -> None: self.prob_crossover = prob_crossover
    
    def setProbMutacion(self, prob_mutacion: float) -> None: self.prob_mutacion = prob_mutacion   
    
    def setCantIndividuos(self, cant_individuos: int) -> None: self.cant_individuos = cant_individuos             
    
    def setCantGeneraciones(self, cant_generaciones: int) -> None: self.cant_generaciones = cant_generaciones            
    
    def setDominio(self, dominio: tuple[int, int]) -> None: self.dominio = dominio

    def setFuncionObjetivo(self, funcion_objetivo) -> None: self.funcion_objetivo = funcion_objetivo

    def getIndividuo(self, indice: int) -> int: return self.poblacion[indice]
 
    def getSumaIndividuos(self) -> int:
        '''Devuelve la suma de los valores de cada individuo de la población'''
        suma: int = 0
        for individuo in self.poblacion:
            suma += individuo
        return suma

    def getSumaFunciones(self) -> float:
        '''Devuelve la suma de las funciones objetivos de cada individuo de población'''
        suma: float = 0
        for individuo in self.poblacion:
            suma += self.funcion_objetivo(individuo)
        return suma
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↑↑↑ \ Setters y Getters \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #   
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↓↓↓ \ Funciones Debugg \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
    def __str__(self) -> str:
        return(f"<AlgoritmoGenético>\n"
               f"├ Selección: {self.tipo_seleccion.capitalize() if self.tipo_seleccion.capitalize() != "Torneo" else self.tipo_seleccion.capitalize() + " ("+str(int(self.porcentaje_seleccion*100))+"%)"}\n"
               f"├ Crossover: {self.tipo_crossover.capitalize()} ({int(self.prob_crossover*100)}%)\n"
               f"├ Mutación: {self.tipo_mutacion.capitalize()} ({int(self.prob_mutacion*100)}%)\n"
               f"├ Elitismo: {"No" if self.porcentaje_elitismo == 0 else int(self.porcentaje_elitismo*100)}\n"
               f"├ Individuos: {self.cant_individuos}\n"
               f"└ Generaciones: {self.cant_generaciones}")
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↑↑↑ \ Funciones Debugg \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #   
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↓↓↓ \ Funciones Principales \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #   
    def generarPoblacionInicial(self) -> None:
        '''Genera la población inicial del Algoritmo Genético'''
        self.generacion_actual = 1
        poblacion: list[int] = []
        for individuo in range(self.cant_individuos):
            poblacion.append(random.randint(self.dominio[0], self.dominio[1]))
        self.poblacion: list[int] = poblacion.copy()

    def fitness(self) -> None:
        '''Calcula el valor de cada individuo dentro de la población'''
        list_fitness: list[float] = []
        for individuo in self.poblacion:
            list_fitness.append(self.funcion_objetivo(individuo)/self.getSumaFunciones())
        self.list_fitness: list[int] = list_fitness.copy()

    def selection(self) -> int:
        '''Devuelve un individuo utilizando el método de selección del Algoritmo Genético'''
        match self.tipo_seleccion:
            case 'ruleta':
                seleccionado: float = random.random()
                acum: float = 0
                for i in range(self.cant_individuos):
                    acum += self.list_fitness[i]
                    if acum > seleccionado:
                        return self.poblacion[i]
            case 'torneo':
                indices_disponibles: list[int] = [i for i in range(self.cant_individuos)]
                individuos_seleccionados: list[int] = []
                for i in range(math.ceil(self.cant_individuos*self.porcentaje_seleccion)):
                    indice_aleatorio: int = random.randint(0, len(indices_disponibles) - 1)
                    individuos_seleccionados.append(self.poblacion[indices_disponibles[indice_aleatorio]])
                    indices_disponibles.pop(indice_aleatorio)
                mejor_individuo: int = self.devolverMejores(1, *individuos_seleccionados)
                return mejor_individuo[0]
    
    def crossover(self, padre: int, madre: int) -> tuple[int, int]:
        '''Cruza (o no) la información genética de dos individuos y devuelve dos nuevos individuos'''
        if random.random() < self.prob_crossover:
            hijo_uno: str = ""
            hijo_dos: str = ""
            bits_hijo_uno: str = [*format(padre, "030b")]
            bits_hijo_dos: str = [*format(madre, "030b")]
            punto_de_cruce: int = random.randint(1, len(bits_hijo_uno) - 1)
            match self.tipo_crossover:
                case '1pto':
                    for bit in range(punto_de_cruce, len(bits_hijo_uno)):
                        bit_auxiliar: str = bits_hijo_uno[bit]
                        bits_hijo_uno[bit] = bits_hijo_dos[bit]
                        bits_hijo_dos[bit] = bit_auxiliar
                    for bit in range(len(bits_hijo_uno)):
                        hijo_uno += bits_hijo_uno[bit]
                        hijo_dos += bits_hijo_dos[bit]
                    return(int(hijo_uno, base=2), int(hijo_dos, base=2))
        else:
            return (padre, madre)

    def mutation(self, *individuos: int) -> list[int]:
        '''Muta (o no) y devuelve a los individuos de la población pasados como parámetros'''
        individuos_mutados: list[int] = []
        for individuo in individuos:
            if random.random() < self.prob_mutacion:
                match self.tipo_mutacion:
                    case 'invertida':
                        individuo_auxiliar: str = ""
                        bits_individuo: list[str] = [*format(individuo, "030b")]
                        bit_inveritdo: int = random.randint(1, len(bits_individuo) - 1)
                        bits_individuo[bit_inveritdo] = "1" if bits_individuo[bit_inveritdo] == "0" else "0"
                        for bit in range(len(bits_individuo)):
                            individuo_auxiliar += bits_individuo[bit]
                        individuos_mutados.append(int(individuo_auxiliar, base=2))
            else:
                individuos_mutados.append(individuo)
        return individuos_mutados
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↑↑↑ \ Funciones Principales \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #   
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↓↓↓ \ Funciones Adicionales \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #   
    def nuevaGeneracion(self) -> bool:
        '''Avanza hacia la siguiente generación si puede y retorna True. Si no puede, retorna False'''
        if self.generacion_actual < self.cant_generaciones:
            cantidad_por_elitismo:int = math.ceil(self.cant_individuos * self.porcentaje_elitismo)
            for i in range(int((self.cant_individuos - cantidad_por_elitismo) / 2)):
                self.cicloReproductivo()
            if self.porcentaje_elitismo > 0:
                a = self.devolverMejores(cantidad_por_elitismo, *self.poblacion)
                self.poblacion_siguiente.extend(a)
            for individuo in range(self.cant_individuos):
                self.poblacion[individuo] = self.poblacion_siguiente[individuo]
            self.poblacion_siguiente = []
            self.generacion_actual += 1
            return True
        return False
    
    def cicloReproductivo(self) -> None:
        '''Selecciona a dos individuos, intenta realizar el cruce, intenta realizar la mutación y luego inserta a los individuos en la nueva población'''
        padre, madre = self.selection(), self.selection()   # Seleccionar
        hijos = self.crossover(padre, madre)                # Cruzar
        hijos = self.mutation(*hijos)                       # Mutar
        self.poblacion_siguiente.extend(hijos)              # Insertar
    
    def devolverMejores(self, cantidad:int, *individuos_tuple:int) -> list[int]:
        '''Dados una cantidad N y un conjunto de individuos, devuelve los N individuos más valiosos (referido al valor de la función objetivo)'''
        individuos: list[int] = []
        individuos.extend(individuos_tuple)
        for i in range(0, len(individuos) - 1):
            for j in range(i, len(individuos)):
                if self.funcion_objetivo(individuos[i]) < self.funcion_objetivo(individuos[j]):
                    individuo_auxiliar = individuos[i]
                    individuos[i] = individuos[j]
                    individuos[j] = individuo_auxiliar
        mejores_n_individuos: list[int] = []
        for i in range(cantidad):
            mejores_n_individuos.append(individuos[i])
        return mejores_n_individuos
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ↑↑↑ \ Funciones Adicionales \ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
