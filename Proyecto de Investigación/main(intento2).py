import os, sys, random
import dependencias.pygate as pygate

conexiones: list[str] = []

class Circuit:
    '''Representa un circuito de compuertas lógicas'''

    def __init__(self, input_quantity: int, output_quantity: int) -> None:
        self.i: list[pygate.Input] = [pygate.Input(name=i) for i in range(input_quantity)]
        self.o: list[pygate.Output] = [pygate.Output(name=o) for o in range(output_quantity)]
        self.gates: list[pygate.GateN] = []
        self.gate_count = [0, 0, 0, 0, 0, 0, 0] # i: 0=and, 1=nand, 2=or, 3=nor, 4=xor, 5=xnor, 6=not
        self.connections = list[str] = []

    def total_gates(self) -> int:
        count = 0
        for i in range(5):
            count += self.gate_count[i]
        return count
    
    def add_unary_gate(self, gate: pygate.Gate1, input: pygate.GateN | pygate.Input):
        gate.i[0] = input
        self.gates.append(gate)

    def add_binary_gate(self, gate: pygate.Gate2, input_a: pygate.GateN | pygate.Input, input_b: pygate.GateN | pygate.Input) -> None:
        gate.i[0] = input_a
        gate.i[1] = input_b
        self.gates.append(gate)

    def generate_random_gate(self) -> pygate.Gate2:
        match random.randint(0,5):
            case 0:
                aux_gate = pygate.AND(name=self.gate_count[0])
                self.gate_count[0] += 1
            case 1:
                aux_gate = pygate.NAND(name=self.gate_count[1])
                self.gate_count[1] += 1
            case 2:
                aux_gate = pygate.OR(name=self.gate_count[2])
                self.gate_count[2] += 1
            case 3:
                aux_gate = pygate.NOR(name=self.gate_count[3])
                self.gate_count[3] += 1
            case 4:
                aux_gate = pygate.XOR(name=self.gate_count[4])
                self.gate_count[4] += 1
            case 5:
                aux_gate = pygate.XNOR(name=self.gate_count[5])
                self.gate_count[5] += 1
        return aux_gate
    
    def select_random_inputs(self) -> tuple[pygate.Input,pygate.Input]:
        inputs: list[pygate.Gate2 | pygate.Input] = []
        valid_selections = [i for i in range(len(self.i) + len(self.gates))]
        for k in range(2):
            if len(valid_selections) - k > 1:
                index = random.randint(0, len(valid_selections) - 1)
            else:
                index = 0
            selected = valid_selections[index]
            if selected >= len(self.i):
                selected -= len(self.i)
                input = self.gates[selected]
            else:
                input = self.i[selected]
            inputs.append(input)
            valid_selections.pop(index)
        return inputs

    def integrate_random_gate(self) -> None:
        gate = self.generate_random_gate()
        inputs = self.select_random_inputs()
        for k in range(2):
            match random.randint(0, 1):
                case 0:
                    gate.i[k] = inputs[k]
                    self.connections.append(f"{inputs[k].name} -> {gate.name}")
                case 1:
                    aux_gate = pygate.NOT(inputs[k])
                    self.connections.append(f"{inputs[k].name} -> {aux_gate.name}")
                    gate.i[k] = aux_gate
                    self.connections.append(f"{aux_gate.name} -> {gate.name}")
        self.gates.append(gate)