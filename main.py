# Kivy Imports
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

Window.size = (500,600) #Fenster Größe 500x600

class Calculator(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation = "vertical", **kwargs)

        self.result = TextInput(
            font_size = 45,
            size_hint_y = 0.2,
            readonly = True,
            halign = "right",
            multiline = False
        )

        self.add_widget(self.result)
        
        #Buttons der App, jede Reihe = Reihe in der App
        buttons = [
            ["C", "+/-", "%", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2","3", "+"],
            ["0", "00", ".", "="]
        ]

        grid = GridLayout(cols = 4, spacing = 5, padding = 10) #Cols = 4 = 4 Reihen im Grid
        for row in buttons: #Fügt automatisch die Texte aus "buttons" den Buttons der App hinzu
            for item in row: 
                button = Button(
                    text = item,
                    font_size = 32,

                )
                grid.add_widget(button) #Erstellt die Buttons
        
        self.add_widget(grid) #Erstellt das Grid (mit den Buttons)


class CalculatorApp(App):
    def build(self):
        return Calculator()
    

if __name__ == "__main__":
    CalculatorApp().run()


