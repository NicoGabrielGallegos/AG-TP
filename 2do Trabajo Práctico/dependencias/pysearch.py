import copy                         # Para copiar objetos
from openpyxl import Workbook       # Para crear los documentos de excel
import dependencias.searchtoxl as searchtoxl     # Para editar los documentos de excel
from dependencias.knapsack import Bag, BagItem   # Clases necesarias

class Search:
    '''
    Clase base para implementar algoritmos de
    búsquedas exhaustivas o heurísticas
    '''

    def __init__(self, bag: Bag, items: list[BagItem], type: str) -> None:
        self.bag = bag
        self.items: list[BagItem] = items
        self.optimums: list[Bag] = []
        self.type = type
        self.init_xlsx_file(type)
    
    @property
    def bag(self) -> Bag:
        return self._bag

    @bag.setter
    def bag(self, bag: Bag) -> None:
        self._bag = bag

    @property
    def items(self) -> list[BagItem]:
        return self._items

    @items.setter
    def items(self, items: list[BagItem]) -> None:
        self._items = copy.deepcopy(items)
    
    @property
    def item_quantity(self) -> int:
        return len(self._items)

    @property
    def node_value(self) -> float:
        return self._bag.total_value
    
    @property
    def node_items(self) -> float:
        return self._bag.items
    
    @property
    def optimums(self) -> list[Bag]:
        return self._optimums

    @optimums.setter
    def optimums(self, bags: list[Bag]) -> None:
        self._optimums = bags
    
    def __getitem__(self, index: int):
        return self._optimums[index]
    
    def __setitem__(self, index: int, value: BagItem):
        self._optimums[index] = value

    def __len__(self) -> int:
        return len(self._optimums)

    def append(self, bag: Bag):
        self._optimums.append(copy.deepcopy(bag))

    def print_optimums(self, colors: bool = True) -> None:
        if colors:
            COLOR_END = "\33[0m"
            WEIGHT_COLOR = "\33[95m"
            VALUE_COLOR = "\33[92m"
        else:
            COLOR_END = WEIGHT_COLOR = VALUE_COLOR = ""

        for index in range(len(self)):
            print(WEIGHT_COLOR + f"{self[index].total_weight:6}" + COLOR_END, end=" | ")
            print(VALUE_COLOR + f"{self[index].total_value:5}" + COLOR_END, end=" | ")
            print(self[index].__str__(colors))
        self.add_optimum_node_xlsx_file()

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, type: str) -> None:
        self._type = type

    def init_xlsx_file(self, type: str) -> None:
        self.xlsx_file: Workbook = Workbook()
        searchtoxl.format(self.xlsx_file, self._items, type)

    def export_xlsx_file(self, name: str = "Resultado") -> None:
        self.xlsx_file.save(name)

    def add_optimum_node_xlsx_file(self) -> None:
        searchtoxl.add_optimum_node(self.xlsx_file["Soluciones"], self.item_quantity, self._optimums, self._type)

    

class ExhaustiveSearch(Search):
    '''
    Funciones necesarias para resolver un
    problema de optimización combinatoria
    '''

    def __init__(self, bag: Bag, items: list[BagItem]) -> None:
        super().__init__(bag, items, "Exhaustive")
        self.q: int = -1

    def print_node(self, bag: Bag | None = None, colors: bool = True) -> None:
        if colors:
            COLOR_END = "\33[0m"
            if self._bag.is_valid:
                WEIGHT_COLOR = "\33[95m"
                VALUE_COLOR = "\33[92m"
            else:
                WEIGHT_COLOR = VALUE_COLOR = "\33[90m"
        else:
            COLOR_END = WEIGHT_COLOR = VALUE_COLOR = ""

        if bag is None:
            bag = self._bag

        print(WEIGHT_COLOR + f"{bag.total_weight:6}" + COLOR_END, end=" | ")
        print(VALUE_COLOR + f"{bag.total_value:5}" + COLOR_END, end=" | ")
        print(bag.__str__(colors))

    def search(self, from_index: int = 0, to_index: int = -1) -> None:
        self.q += 1

        if to_index == -1 or to_index + 1 > len(self.items):
            to_index = self.item_quantity - 1

        #self.print_node()
        searchtoxl.add_node(self.xlsx_file["Soluciones"], self.q, self.bag)
        
        if self._bag.is_valid:
            if not self._optimums or self._bag.total_value > self[0].total_value:
                self.optimums = [copy.deepcopy(self._bag)]
            elif self._bag.total_value == self[0].total_value:
                self.append(self._bag)
        
        for index in range(from_index, to_index + 1):
            self._bag.append(self._items[index])
            self.search(index + 1, to_index)
        self._bag.pop_last()

class GreedySearch(Search):
    '''
    Funciones necesarias para buscar
    el máximo beneficio en casa paso
    '''

    def __init__(self, bag: Bag, items: list[BagItem]) -> None:
        super().__init__(bag, items, "Greedy")
    
    def order_by_vwr(self) -> None: # vwr = Value-Weight Ratio # Valor/Peso
        for i in range(self.item_quantity - 1):
            for j in range(i, self.item_quantity):
                if self._items[i].value_weight_ratio < self._items[j].value_weight_ratio:
                    aux = self._items[i]
                    self._items[i] = self._items[j]
                    self._items[j] = aux

    def search(self) -> None:
        for index in range(self.item_quantity):
            if self._bag.total_weight + self._items[index].weight <= self._bag.max_weight:
                self._bag.append(self._items[index])
        self.optimums = [copy.deepcopy(self._bag)]

#a = BagItem()
#a.value = 20
#a.weight = 100
#print(a.value_weight_ratio)

#b = Bag()
#b.append(BagItem())
#print(b[0])

#i = [1, 2, 3]
#s = Search(Bag(), i)
#s.items[0] = 4
#print(i)
#print(s.items)


#bag = Bag(7)
#items = [BagItem(4, 4), BagItem(5, 2), BagItem(3, 6)]
#s = ExhaustiveSearch(bag, items)
#s.search()
#print()
#s.print_node(s[0])

#bag = Bag(10)
#print(len(bag))
#print(bag.is_empty)
#bag.append(BagItem())
#print(len(bag))
#print(bag.is_empty)