from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.button import Label
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        btn = Button(text="Butt1")
        txt = Label(text="label")
        layout = BoxLayout()
        layout.add_widget(txt)
        layout.add_widget(btn)
        return layout

app = MyApp()
app.run()