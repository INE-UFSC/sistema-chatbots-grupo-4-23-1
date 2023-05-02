from Bots.Bot import Bot

class BotZangado(Bot):
    def __init__(self,nome):
        super().__init__(nome)
        self.__nome = nome

        self.__respostas = {"1": "Eu te respondo: 'Bom dia pra quem?'",
                            "2": "Eu te respondo: 'Não te interessa! Mas é "+ self.nome+"'",
                            "3": "Eu te respondo: 'Pergunda pro seu pai!'",
                            "4": "Eu te respondo: 'Ainda esta aqui :('"}

    @property
    def respostas(self):
        return self.__respostas

    @property
    def nome(self):
        return self.__nome


    def apresentacao(self):
        print(":( Meu nome é", self.nome, ", seja mal vindo GRRRR!")
 
    def mostra_comandos(self):
        super().mostra_comandos()
    
    def executa_comando(self,cmd):
        if (cmd == '-1'):
           self.despedida()
        print(self.perguntas[cmd])
        print(self.respostas[cmd])

    def boas_vindas(self):
        print(self.nome, "diz: Eu não posso acreditar que me escolheu!, GRRRRRRRRR!")

    def despedida(self):
        print(self.nome, "diz: 'Finalmente, já estava na hora! GRRR'")
