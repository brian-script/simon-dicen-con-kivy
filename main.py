from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.label import Label
from kivy.app import App
import logica

class prueba(App):
    def build(self):
        #cuerpo de la aplicacion
        contenedor_principal = BoxLayout(orientation = "vertical", spacing = 10, padding = [20, 20, 20, 20])
        
        #area principal y el mas grande
        anchor_conte = AnchorLayout(size_hint=(1, 0.7))
        tamaño = 200
        grid_layout = GridLayout(
                cols=2,
                rows=2,
                size_hint = (None, None),
                size = (tamaño * 2 + 10, tamaño * 2 + 10),
                padding=[10, 10],
                spacing=[10, 10]
                )
        grid_layout.bind(size=anchor_conte.setter("size"))
        #area secundaria botones de start y niveles de dificultad
        grid_layout_inferior = GridLayout(
                cols = 4,
                rows = 1,
                padding = [50, 50, 50, 50],
                spacing = [20],
                size_hint = (1, 0.3)
                )     
        
        #inicializando botones del area principal 
       
        boton1 = Button(text = "", background_normal = "", background_color = (0, 0.5, 0, 1), size = (tamaño, tamaño), size_hint = (None, None))
        
        boton2 = Button(text = "", background_normal = "", background_color = (0.5, 0, 0, 1), size = (tamaño, tamaño), size_hint = (None, None))

        boton3 = Button(text = "", background_normal = "", background_color = (0.6, 0.5, 0, 1), size = (tamaño, tamaño), size_hint = (None, None))

        boton4 = Button(text = "", background_normal = "", background_color = (0, 0.3, 0.5, 1), size = (tamaño, tamaño), size_hint = (None, None))

        grid_layout.add_widget(boton1)
        grid_layout.add_widget(boton2)
        grid_layout.add_widget(boton3)
        grid_layout.add_widget(boton4)
        anchor_conte.add_widget(grid_layout) 

        #inicializando botones del area secundria
        boton_iniciar = Button(text="Star")
        boton_iniciar.bind(on_press=self.iniciar)
        grid_layout_inferior.add_widget(boton_iniciar)

        self.botones = [
            ToggleButton(text="Facil", group="Niveles", state="down"),
            ToggleButton(text="Normal", group="Niveles"),
            ToggleButton(text="Dificil", group="Niveles")
        ]
        
        for toggles in self.botones:
            toggles.bind(on_press = self.dificultad)

        for toggles in self.botones:
            grid_layout_inferior.add_widget(toggles)

        contenedor_principal.add_widget(anchor_conte)
        contenedor_principal.add_widget(grid_layout_inferior)
        return contenedor_principal

    def iniciar(self, instance):
        print("hola")

    def dificultad(self, instance):
        if instance.state == "down":
            if instance.text == "Facil":
                print("nivel 1")
            elif instance.text == "Normal":
                print("nivel 2")
            elif instance.text == "Dificil":
                print("nivel 3")

prueba().run()
