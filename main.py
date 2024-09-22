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
        #label_layout= Label(text="hola que hace", size_hint=(1, 0.3))

        
        #inicializando botones del area principal
        grid_layout.add_widget(Button(text="", background_normal = "", background_color = (0, 0.5, 0, 1), size = (tamaño, tamaño), size_hint=(None, None)))
        grid_layout.add_widget(Button(text="", background_normal = "", background_color = (0.5, 0, 0, 1), size = (tamaño, tamaño), size_hint=(None, None)))
        grid_layout.add_widget(Button(text="", background_normal = "", background_color = (0.6, 0.5, 0, 1), size = (tamaño, tamaño), size_hint=(None, None)))
        grid_layout.add_widget(Button(text="", background_normal = "", background_color = (0, 0.3, 0.5, 1), size = (tamaño, tamaño), size_hint=(None, None)))
       
        #inicializando botones del area secundria
        boton_iniciar = Button(text="Star")
        boton_iniciar.bind(on_press=self.iniciar)
        grid_layout_inferior.add_widget(boton_iniciar)
        anchor_conte.add_widget(grid_layout)

        contenedor_principal.add_widget(anchor_conte)
        contenedor_principal.add_widget(grid_layout_inferior)
        return contenedor_principal

    def iniciar(self, instance):
        print("hola")

prueba().run()
