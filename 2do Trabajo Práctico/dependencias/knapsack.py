import copy # Librería para copiar objetos

class BagItem:
    '''Objeto con Peso o Volumen "w" y Valor "v"'''

    serial_number: int = 1

    def __init__(self, w: float = 1, v: float = 1, id: str | None = None) -> None:
        self.id = id
        self.weight = w
        self.value = v

    @property
    def id(self) -> str:
        '''Nombre del objeto'''
        return self._id
    
    @id.setter
    def id(self, id: str | None) -> None:
        if id is None:
            self._id = f"{BagItem.serial_number}"
            BagItem.serial_number += 1
        else:
            self._id = id
    
    @property
    def weight(self) -> float:
        '''Peso o Volumen del objeto'''
        return self._weight
    
    @weight.setter
    def weight(self, w: float) -> None:
        self._weight: float = w if w >= 0 else 0

    @property
    def value(self) -> float:
        '''Valor del objeto'''
        return self._value
    
    @value.setter
    def value(self, v: float) -> None:
        self._value: float = v if v >= 0 else 0

    @property
    def value_weight_ratio(self) -> float:
        '''Beneficio del objeto'''
        return self.value / self.weight
    
    def __str__(self) -> str:
        return self.id

class Bag:
    '''Mochila de objetos con un Peso o Volumen máximo'''
    def __init__(self, max_w: float = 1) -> None:
        self.max_weight: float = max_w
        self.items: list[BagItem] = []

    @property
    def max_weight(self) -> float:
        return self._max_weight
    
    @max_weight.setter
    def max_weight(self, max_w: float) -> None:
        self._max_weight = max_w

    @property
    def items(self) -> list[BagItem]:
        return self._items
    
    @items.setter
    def items(self, items: list[BagItem]) -> None:
        self._items = copy.deepcopy(items)

    def __getitem__(self, index: int):
        return self._items[index]
    
    def __setitem__(self, index: int, value: BagItem):
        self._items[index] = value
    
    def __len__(self) -> int:
        return len(self._items)

    def append(self, item: BagItem):
        self._items.append(item)

    def pop_last(self) -> BagItem | bool:
        if len(self._items) > 0:
            return self._items.pop()
        else:
            return False

    def empty_bag(self) -> None:
        self._items = []

    @property
    def item_quantity(self) -> int:
        return len(self._items)

    @property
    def total_value(self) -> float:
        t_v: float = 0
        for item in self._items:
            t_v += item.value
        return t_v

    @property
    def total_weight(self) -> float:
        t_w: float = 0
        for item in self._items:
            t_w += item.weight
        return t_w

    @property
    def is_valid(self) -> bool:
        return False if self.total_weight > self._max_weight else True
    
    @property
    def is_empty(self) -> bool:
        return True if len(self) == 0 else False
    
    def __str__(self, colors: bool = True) -> str:
        if colors:
            COLOR_END = "\33[0m"
            if self.is_valid:
                ITEM_COLOR = COLOR_END
                BAG_COLOR = "\33[94m" # Celeste
            else:
                BAG_COLOR = ITEM_COLOR = "\33[90m"
        else :
            COLOR_END = ITEM_COLOR = BAG_COLOR = ""

        s = BAG_COLOR + "Mochila("
        if self.item_quantity > 0:
            for index in range(self.item_quantity - 1):
                s += f"{ITEM_COLOR}{self[index]}{BAG_COLOR}, "
            s += f"{ITEM_COLOR}{self[-1]}"
        s += f"{BAG_COLOR}){COLOR_END}"

        return s