import kivy
kivy.require("2.3.1")

#   Kivy Imports
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line

#   Andere Imports
from random import random

class PaintWidget(Widget):
    def on_touch_down(self, touch): #   Funktion um etwas bei Berührung/  Klick auszuführen
        color = (random(), random(), random()) #    Variable, die zufällige RGB-Werte hat also zufällige Farben
        with self.canvas:
            Color(*color) # Kurze Schreibweise zum Übertragen der Tupel, aus der "color" Variable
            d = 30. #    d = Durchmesser des Kreises (also die Pinseldicke)
            Ellipse(pos = (touch.x - d / 2, touch.y - d / 2), size = (d, d)) #  Die Position der Berührung / des Klicks mit dem Radius subtrahieren, damit der Kreis mittig um den Klick gezeichnet wird
            touch.ud["line"] = Line(points = (touch.x, touch.y)) # ".ud" zum Speichern der Position des ersten Klicks / der ersten Berührung

    def on_touch_move(self, touch): #   Funktion um etwas beim Bewegen des Fingers über dem Bildschirm / der Maus mit gedrücktem Klick auszuführen
        touch.ud["line"].points += [touch.x, touch.y] # ".ud" nutzt jetzt die gespeicherte Position des ersten Klicks als Startpunkt der zu zeichnenden Linie


class PaintApp(App):
    def build(self):
        parent = Widget()
        self.painter = PaintWidget()
        clearbtn = Button(text = "Clear")
        clearbtn.bind(on_release = self.clear_canvas) # Bindet die "clear_canvas" Funktion an den Button "clearbtn". Wird ausgelöst wenn der Button "losgelassen" wird
        parent.add_widget(self.painter) #   Fügt "self.painter" also "PaintWidget()" zum Parent "Widget()" hinzu
        parent.add_widget(clearbtn) #   Fügt den Button "clearbtn" zum Parent "Widget()" hinzu
        return parent
    
    def clear_canvas(self, obj): #  Funktion um das gezeichnete wieder zu löschen
        self.painter.canvas.clear()
    
if __name__ == "__main__":
    PaintApp().run()

