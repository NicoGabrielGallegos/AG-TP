import os, sys, random
import dependencias.pygate as pygate

conexiones: list[str] = []

# Parámetros del circuito
input_quantity = 2
output_quantity = 1
max_depth = 2
allowed_gates = [0, 1, 2, 3]

# Parámetros del algoritmo
objective_truth_table = pygate.TruthTable("{00:1;01:0;10:1;11:0;}")
objective_function = lambda x : x

def program():
    #c = pygate.RandomCircuit(input_quantity, output_quantity, max_depth)
    #print(c.o.expresion())
    #for connection in c.connections:
    #    print(connection)
    #
    #t = pygate.TruthTable(c.truth_table_format())
    #print(t)
    #print(objective_truth_table)
    #print(t == objective_truth_table)
    #print(c.gates)

    c = pygate.RandomCircuit(input_quantity, output_quantity, max_depth, allowed_gates)
    t = pygate.TruthTable(c.truth_table_format())
    while(t != objective_truth_table):
        del c
        c = pygate.RandomCircuit(input_quantity, output_quantity, max_depth, allowed_gates)
        t = pygate.TruthTable(c.truth_table_format())
    print(c.o.expresion())
    print(c.depth)
    for connection in c.connections:
        print(connection)
    print(t)
    
    

os.system("cls")
program()