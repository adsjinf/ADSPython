# importar o App, Builder (Gui)
## Criar o aplicativo
## Criar a função build

import requests
from kivy.app import App
from kivy.lang import Builder

# Carrega a interface do arquivo .kv
GUI = Builder.load_file("Tela.kv")

class MeuAplicativo(App):
    def build(self):
        return GUI

    def on_start(self):
        self.root.ids["moeda1"].text = f"Dólar: R$ {self.pegar_cotacao('USD').replace('.', ',')}"
        self.root.ids["moeda2"].text = f"Libra: R$ {self.pegar_cotacao('GBP').replace('.', ',')}"
        self.root.ids["moeda3"].text = f"Euro: R$ {self.pegar_cotacao('EUR').replace('.', ',')}"
        self.root.ids["moeda4"].text = f"BitCoin: R$ {self.pegar_cotacao('BTC').replace('.', ',')}"

    def pegar_cotacao(self, moeda):
        link = f"https://economia.awesomeapi.com.br/last/{moeda}"
        requisicao = requests.get(link)
        dic_requisicao = requisicao.json()
        cotacao = dic_requisicao[f"{moeda}BRL"]["bid"]
        return cotacao

# Roda o aplicativo
MeuAplicativo().run()
