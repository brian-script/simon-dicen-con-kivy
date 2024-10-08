from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.app import App
import logica

aciertos = []

class prueba(App):
    def __init__(self, **kwargs):
        super(prueba, self).__init__(**kwargs)
        self.botones0 = []
        self.niveles = None
        self.indice = 0 

    def build(self):
        contenedor_principal = BoxLayout(orientation="vertical", spacing=10, padding=[20, 20, 20, 20])
        anchor_conte = AnchorLayout(size_hint=(1, 0.7))
        tamaño = 200
        grid_layout = GridLayout(cols=2, rows=2, size_hint=(None, None), size=(tamaño * 2 + 10, tamaño * 2 + 10), padding=[10, 10], spacing=[10, 10])
        grid_layout.bind(size=anchor_conte.setter("size"))
        
        # Inicializando botones del área principal 
        boton1 = Button(text="", background_normal="", background_color=(0, 0.5, 0, 1), size=(tamaño, tamaño), size_hint=(None, None))
        boton2 = Button(text="", background_normal="", background_color=(0.5, 0, 0, 1), size=(tamaño, tamaño), size_hint=(None, None))
        boton3 = Button(text="", background_normal="", background_color=(0.6, 0.5, 0, 1), size=(tamaño, tamaño), size_hint=(None, None))
        boton4 = Button(text="", background_normal="", background_color=(0, 0.3, 0.5, 1), size=(tamaño, tamaño), size_hint=(None, None))
        
        self.botones0.extend([boton1, boton2, boton3, boton4])
        
        for boton in self.botones0:
            boton.bind(on_press=self.registrar_jugada)
            grid_layout.add_widget(boton)

        anchor_conte.add_widget(grid_layout)

        # Inicializando botones del área secundaria
        grid_layout_inferior = GridLayout(cols=4, rows=1, padding=[50, 50, 50, 50], spacing=[20], size_hint=(1, 0.3))
        boton_iniciar = Button(text="Start")
        boton_iniciar.bind(on_press=self.iniciar)
        grid_layout_inferior.add_widget(boton_iniciar)

        self.botones = [
            ToggleButton(text="Facil", group="Niveles"),
            ToggleButton(text="Normal", group="Niveles"),
            ToggleButton(text="Dificil", group="Niveles")
                    ]

        for toggles in self.botones:
            toggles.bind(on_press=self.dificultad)
            grid_layout_inferior.add_widget(toggles)

        contenedor_principal.add_widget(anchor_conte)
        contenedor_principal.add_widget(grid_layout_inferior)
        return contenedor_principal

    def iniciar(self, instance):
        print("Iniciando juego")
        if self.niveles is not None:
            patron = logica.num_random(self.niveles)
            logica.iluminar_patron(self, patron)
        else:
            print("Selecciona un nivel de dificultad primero.")

    def dificultad(self, instance):
        if instance.state == "down":
            if instance.text == "Facil":
                self.niveles = 3
            elif instance.text == "Normal":
                self.niveles = 5
            elif instance.text == "Dificil":
                self.niveles = 7

    def registrar_jugada(self, instance):
        if instance in self.botones0:
            index = self.botones0.index(instance)
            aciertos.append(index)
            logica.comparar_aciertos(self, logica.patron, aciertos)

prueba().run()
