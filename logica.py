import random
from kivy.clock import Clock

patron = []

def num_random(dificultad):
    patron.clear()
    for i in range(dificultad):
        patron.append(random.randint(0, 3))
    return patron

def iluminar_patron(prueba_app, patron):
    for i, boton_index in enumerate(patron):
        Clock.schedule_once(lambda dt, idx=boton_index: iluminar(prueba_app, idx), i * 0.5)

def iluminar(prueba_app, boton_index):
    boton = prueba_app.botones0[boton_index]
    original_color = boton.background_color[:]

    boton.background_color = (1, 1, 1, 1)
    Clock.schedule_once(lambda dt: restaurar_color(boton, original_color), 0.3)

def restaurar_color(boton, original_color):
    boton.background_color = original_color

def comparar_aciertos(prueba_app, patron, aciertos):
    if aciertos:
        ultimo_acierto = aciertos[-1]
        if ultimo_acierto == patron[prueba_app.indice]:
            prueba_app.indice += 1
            print("Correcto")

            if prueba_app.indice == len(patron):
                print("¡Juego completado!")
                prueba_app.indice = 0
                patron.clear()
        else:
            print("Perdiste")
            prueba_app.indice = 0
            aciertos.clear()  

#Aun no se como puedo hacer para que a la hora de que acierte correctamente todos los colores vuelva a mostrar otro patron en pantalla
#Lo actualizare cuando tenga una idea de como hacerlo 
