from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.app import App

class prueba(App):
    def build(self):
        contenedor_principal = BoxLayout(orientation = "vertical", spacing = 10, padding = [20, 20, 20, 20])

        grid_layout = GridLayout(
                cols=2,
                rows=2,
                size_hint = (1, 0.7),
                padding=[50, 50, 50, 50],
                spacing=[20, 20]
                )
        label_layout= Label(text="hola que hace", size_hint=(1, 0.3))

        tamaño =200

        grid_layout.add_widget(Button(text="hola1", size=(tamaño, tamaño), size_hint=(None, None)))
        grid_layout.add_widget(Button(text="hola2", size=(tamaño, tamaño), size_hint=(None, None)))
        grid_layout.add_widget(Button(text="hola3", size=(tamaño, tamaño), size_hint=(None, None)))
        grid_layout.add_widget(Button(text="hola4", size=(tamaño, tamaño), size_hint=(None, None)))
        
        contenedor_principal.add_widget(grid_layout)
        contenedor_principal.add_widget(label_layout)
        return contenedor_principal

prueba().run()
