import cowsay
from math import sin


def print_cowsay():
    cowsay.stegosaurus("Howdy?")


def count_sinus():
    outputs = []
    inputs = []
    with open('arguments.txt') as f:
        for line in f:
            inputs.append(int(line))
            outputs.append(sin(int(line)))
    
    with open('results.txt', 'w') as f:
        for i in range(len(outputs)):
            f.write(f"sin({inputs[i]}) = {outputs[i]}\n")

count_sinus()
print_cowsay()