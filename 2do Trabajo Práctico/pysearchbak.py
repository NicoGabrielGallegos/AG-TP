import math # Librería para utilizar operaciones matemáticas
import copy # Librería para copiar objetos

class BagItem:
    ''' Item con beneficio/valor "v" y peso/volumen "w"'''
    
    serial_number: int = 1

    def __init__(self, w: float = 1, v: float = 1, name: str | None = None) -> None:
        self.set_name(name)
        self.set_weight(w)
        self.set_value(v)

    def set_name(self, name: str | None) -> None:
        if name is None:
            self.name = f"{BagItem.serial_number}"
            BagItem.serial_number += 1
        else:
            self.name = name
    
    def set_value(self, v: float) -> None:
        self.value: float = v if v >= 0 else 0

    def set_weight(self, w: float) -> None:
        self.weight: float = w if w >= 0 else 0
    
    def get_name(self) -> float:
        return self.name
    
    def get_value(self) -> float:
        return self.value
    
    def get_weight(self) -> float:
        return self.weight
    
    def get_value_weight_ratio(self) -> float:
        return self.value / self.weight

    def __str__(self) -> str:
        return self.get_name()

class Bag:
    ''' Mochila de items con un peso/volumen máximo w_max'''
    def __init__(self, w_max: float = 1) -> None:
        self.items: list[BagItem] = []
        self.set_max_weight(w_max)
    
    def empty_bag(self) -> None:
        self.items: list[BagItem] = []

    def set_max_weight(self, w_max: float) -> None:
        self.w_max: float = w_max
    
    def add_item(self, item: BagItem) -> None:
        self.items.append(item)
    
    def remove_last_item(self) -> None:
        if len(self.items) > 0:
            self.items.pop()

    def get_item(self, index: int) -> BagItem:
        return self.items[index]

    def get_items(self) -> list[BagItem]:
        return self.items
    
    def get_total_value(self) -> float:
        total_value: float = 0
        for item in self.items:
            total_value += item.get_value()
        return total_value

    def get_total_weight(self) -> float:
        total_weight: float = 0
        for item in self.items:
            total_weight += item.get_weight()
        return total_weight

    def is_valid(self) -> bool:
        return False if self.get_total_weight() > self.w_max else True
    
    def __str__(self, colors: bool = True) -> str:
        if colors:
            COLOR_END = "\33[0m"
            if self.is_valid():
                ITEM_COLOR = COLOR_END
                BAG_COLOR = "\33[94m" # Celeste
            else:
                BAG_COLOR = ITEM_COLOR = "\33[90m"
        else :
            COLOR_END = ITEM_COLOR = BAG_COLOR = ""

        s = BAG_COLOR + "Bag("
        if(len(self.items) > 0):
            for i in range(len(self.items) - 1):
                s += ITEM_COLOR + str(self.items[i]) + BAG_COLOR + ", "
            s += ITEM_COLOR + str(self.items[-1])
        s += BAG_COLOR + ")" + COLOR_END
        return s

class Search:
    '''
    Clase base para realizar la implementación de
    algoritmos de búsquedas exhaustivas o herústicas
    '''

    def __init__(self, bag: Bag, items: list[BagItem], file_name: str) -> None:
        self.bag: Bag = bag
        self.items: list[BagItem] = copy.deepcopy(items)
        self.optimum: list[Bag] = []
        self.file_name: str = file_name
        self.init_txt()
    
    def init_txt(self) -> None:
        with open(self.file_name + ".txt", "w") as f:
            f.write(f"Base class' placeholder file")
    
    def set_bag(self, bag: Bag) -> None:
        self.bag: Bag = bag
    
    def get_bag(self) -> Bag:
        return self.bag
    
    def get_bag_value(self) -> float:
        return self.bag.get_total_value()
    
    def get_bag_items(self) -> list[BagItem]:
        return self.bag.get_items()

    def set_items(self, items: list[BagItem]) -> None:
        self.items: list[BagItem] = items

    def get_item(self, index: int) -> BagItem:
        return self.items[index]

    def get_items_quantity(self) -> int:
        return len(self.items)

    def insert_into_txt(self, specific_bag: Bag | None = None) -> None:
        pass

    def table_header(self, text: str = "") -> None:
        pass

class ExhaustiveSearch(Search):
    '''
    Clase que implementa las funciones necesarias para
    resolver un problema de optimización combinatoria
    '''

    def __init__(self, bag: Bag, items: list[BagItem], file_name: str) -> None:
        super().__init__(bag, items, file_name)

    def init_txt(self) -> None:
        with open(self.file_name + ".txt", "w") as f:
            f.write(f"Exhaustive Search - {self.file_name}:\n\n")
            f.write(f"Searching for: max Value\nCondition: Weight < {self.bag.w_max}\nUsing the following objects:\n")
            f.write(f"-------+--------+------\nObject | Weight | Value\n-------+--------+------\n")
            for item in self.items:
                f.write(f"{item.get_name()}".rjust(6, " ") + " | ")
                f.write(f"{item.get_weight():6} | ")
                f.write(f"{item.get_value():5}\n")
            f.write("-------+--------+------\n\nResults:\n")

    def set_new_optimum(self, bag: Bag) -> None:
        self.optimum = [copy.deepcopy(bag)]

    def append_optimum(self, bag: Bag) -> None:
        self.optimum.append(copy.deepcopy(bag))

    def print_possibility(self, specific_bag: Bag | None = None) -> None:
        COLOR_END = "\33[0m"
        if self.bag.is_valid():
            WEIGHT_COLOR = "\33[95m"
            VALUE_COLOR = "\33[92m"
        else:
            WEIGHT_COLOR = VALUE_COLOR = "\33[90m" # Gris

        bag = self.bag if specific_bag is None else specific_bag

        self.insert_into_txt(specific_bag)

        print(WEIGHT_COLOR + f"{bag.get_total_weight():6}" + COLOR_END, end=" | ")
        print(VALUE_COLOR + f"{bag.get_total_value():5}" + COLOR_END, end=" | ")
        print(bag)
    
    def insert_into_txt(self, specific_bag: Bag | None = None) -> None:
        bag = self.bag if specific_bag is None else specific_bag
        with open(self.file_name + ".txt", "a") as f:
            f.write(f"{bag.get_total_weight():6} | "
                    f"{bag.get_total_value():5} | "
                    f"{bag.__str__(False)}\n")

    def evaluate_possibilities(self, from_index: int = 0, to_index: int = -1) -> None:
        if to_index == -1 or to_index + 1 > len(self.items):
            to_index = len(self.items) - 1
        
        self.print_possibility()

        if self.bag.is_valid():
            if not self.optimum or self.bag.get_total_value() > self.optimum[0].get_total_value():
                self.set_new_optimum(self.bag)
            elif self.bag.get_total_value() == self.optimum[0].get_total_value():
                self.append_optimum(self.bag)

        for index in range(from_index, to_index + 1):
            self.bag.add_item(self.get_item(index))
            self.evaluate_possibilities(index+1, to_index)
        self.bag.remove_last_item()

    
    def table_header(self, text: str = "") -> None:
        if text != "":
            with open(self.file_name + ".txt", "a") as f:
                f.write("-------+-------+--------\n"+f"{text}".center(24, " ") + "\n")
            print("-------+-------+--------")
            print(f"{text}".center(24, " "))

        with open(self.file_name + ".txt", "a") as f:
            f.write("-------+-------+--------\nWeight | Value | Content\n-------+-------+--------\n")
        print("-------+-------+--------")
        print("Weight | Value | Content")
        print("-------+-------+--------")

class GreedySearch(Search):
    '''
    Clase que implementa las funciones necesarias para
    buscar el máximo beneficio en cada paso
    '''

    def __init__(self, bag: Bag, items: list[BagItem], file_name: str) -> None:
        super().__init__(bag, items, file_name)

    def init_txt(self) -> None:
        with open(self.file_name + ".txt", "w") as f:
            f.write(f"Greedy Search - {self.file_name}:\n\n")
            f.write(f"Searching for: max Value-Weight Ratio\nCondition: Weight < {self.bag.w_max}\nUsing the following objects:\n")
            f.write(f"-------+--------+------\nObject | Weight | Value | Value/Weight\n-------+--------+------\n")
    
    def order_by_vwr(self) -> None: # vwr = Value-Weight Ratio
        for i in range(len(self.items) - 1):
            for j in range(i, len(self.items)):
                if self.items[i].get_value_weight_ratio() < self.items[j].get_value_weight_ratio():
                    aux = self.items[i]
                    self.items[i] = self.items[j]
                    self.items[j] = aux

    def set_optimum_bag(self) -> None:
        for i in range(len(self.items)):
            if self.bag.get_total_weight() + self.items[i].get_weight() <= self.bag.w_max:
                self.bag.add_item(self.items[i])
    
    def print_optimum(self) -> None:
        COLOR_END = "\33[0m"
        WEIGHT_COLOR = "\33[95m"
        VALUE_COLOR = "\33[92m"
        print("-------+-------+--------")
        print("Weight | Value | Content")
        print("-------+-------+--------")
        print(WEIGHT_COLOR + f"{self.bag.get_total_weight():6}" + COLOR_END, end=" | ")
        print(VALUE_COLOR + f"{self.bag.get_total_value():5}" + COLOR_END, end=" | ")
        print(self.bag)
    


