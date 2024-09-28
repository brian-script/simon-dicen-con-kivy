import random

patron = []

def num_random(dificultad):
    patron.clear()
    for i in range(3):
        patron.append(random.randint(0, dificultad))

    print(patron)
