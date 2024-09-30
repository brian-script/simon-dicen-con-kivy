import random
from kivy.clock import Clock

patron = []

def num_random(dificultad):
    patron.clear()
    # Generar un patrón de longitud igual a la dificultad
    for i in range(dificultad):
        patron.append(random.randint(0, 3))  # Asegúrate de que el rango sea correcto
    return patron

def iluminar_patron(self, patron):
    for i, boton_index in enumerate(patron):
        # Utiliza el índice correcto para la iluminación
        Clock.schedule_once(lambda dt, idx=boton_index: iluminar(self, idx), i * 0.5)

def iluminar(self, boton_index):
    boton = self.botones0[boton_index]
    original_color = boton.background_color[:]

    boton.background_color = (1, 1, 1, 1)  # Cambia a blanco
    Clock.schedule_once(lambda dt: restaurar_color(boton, original_color), 0.3)

def restaurar_color(boton, original_color):
    boton.background_color = original_color  # Restaura el color original

