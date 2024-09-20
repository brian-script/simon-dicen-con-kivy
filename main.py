from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.app import App

class prueba(App):
    def build(self):
        layout = GridLayout(cols=2, row_force_default=True, row_default_height=40)
        layout.add_widget (Button(text="hola1", size_hint_y=None, height=40))
        layout.add_widget (Button(text="hola2", size_hint_y=None, height=40))
        layout.add_widget (Button(text="hola2", size_hint_y=None, height=40))
        layout.add_widget (Button(text="hola3", size_hint_y=None, height=40))
        layout.add_widget (Button(text="hola4", size_hint_y=None, height=40))
        return layout

prueba().run()
