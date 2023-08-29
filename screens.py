from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition

class ScrButton(Button):
    def __init__(self, target_screen, screen_manager, **kwargs):
        super().__init__(**kwargs)
        self.target_screen = target_screen
        self.screen_manager = screen_manager
        self.on_release = self.go_to_screen

    def go_to_screen(self):
        self.screen_manager.transition = SlideTransition(direction='left')
        self.screen_manager.current = self.target_screen

class MyApp(App):
    def build(self):
        sm = ScreenManager()

        for i in range(1, 6):
            screen = Screen(name=f"ВІКНО {i}")
            layout = BoxLayout(orientation='vertical', spacing=10)
            label = Label(text=f"ЦЕ ВІКНО {i}", size_hint=(1, 0.8))
            
            if i < 5:
                button = ScrButton(target_screen=f"ВІКНО {i + 1}", screen_manager=sm, text=f"Перейти до вікна {i + 1}", size_hint=(1, 0.2))
            else:
                button = ScrButton(target_screen="ВІКНО 1", screen_manager=sm, text="Перейти до головного вікна", size_hint=(1, 0.2))

            layout.add_widget(label)
            layout.add_widget(button)
            screen.add_widget(layout)
            sm.add_widget(screen)

        return sm

if __name__ == '__main__':
    MyApp().run()
