import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
class Unitatry(App):
    def build(self):
        self.s, self.ok = 0, 0
        b = BoxLayout(orientation="vertical")
        self.t = Label(font_size=40)
        self.e = TextInput(multiline=False, font_size=30)
        b.add_widget(self.t)
        b.add_widget(self.e)
        b.add_widget(Button(text=OK, on_press=self.go))
        self.go(0)
        return b
    def go(self, x):
        if self.s > 0 and self.e.text == str(self.a): self.ok += 1
        self.s += 1
        if self.s > 5: self.t.text = f"{self.ok}/5"; return
        n1, n2 = random.randint(1, 10), random.randint(1, 10)
        self.a, self.t.text, self.e.text = n1 + n2, f"{n1}+{n2}=?"
        
Unitatry().run()
