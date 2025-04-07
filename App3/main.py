from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window


# Define fundo branco e remove a barra de título da janela
Window.clearcolor = (1, 1, 1, 1)
Window.borderless = True  # remove a barra de título
Window.size = (500, 190)  # tamanho fixo aproximado para acomodar os elementos

class TelaPrincipal(BoxLayout):
    def fechar_app(self):
        App.get_running_app().stop()


class MeuApp(App):
    def build(self):
        return TelaPrincipal()


if __name__ == '__main__':
    MeuApp().run()
