from Bots.Bot import Bot
from abc import ABC, abstractmethod
import random as r

class BotHogRider(Bot):
    def __init__(self, nome):
        comandos = {1, "Qual seu nome?" : "O QUÊÊÊ QUANTAS DEFESAS EU JA DESTRUI? WOW, MUITAS! Obrigado por perguntar, agora vai embora",
                    2, "Qual sua idade?": "Tenho 38 Marretas e 35 porcos HOG RIDAAA, e dai?",
                    3, "Onde eu moro? ": "A partir do Th7, espero que seja a ultima pergunta por que não estou aguentando mais",
                    4, "Qual o dia do seu aniversário? " : "30/02 HOG RIDAAAA",
                    5, "Conte-me uma historia" : "Era uma vez 3 porquinho level 150 e um Th8, o Th8 assustado, pediu socorro, mas nenhum base-builder conseguia salva-lo. Fim da história, agora vai embora. HOG RIDAAAAAA"}
        super().__init__(nome, comandos)

    def apresentacao(self):
        return(f"Olá eu sou o {super().nome} do clash of clans HOG RIDAAAAA, adoro destruir tudo e hoje estou com muita raiva")

    def boas_vindas(self):
        return("Não acredito que me escolheu, em minha terra chamam isso de noobice")

    def despedida(self):
        return("Até que enfim, já não tava aguentando, HOG RIDAAAA")