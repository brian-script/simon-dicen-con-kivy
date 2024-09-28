import random

patron = []

def num_random(dificultad):
    patron.clear()
    patron.append(random.randint(0, 3))

    for i in range(dificultad):
        num_random(patron)

    print(patron)
