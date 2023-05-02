from Bots.Bot import Bot

class BotFeliz(Bot):
    def __init__(self,nome):
        super().__init__(nome)
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(nome):
        self.__nome = nome

    def apresentacao(self):
        print(":) Meu nome é", self.nome, ", seja MUITOOOO BEM VINDOOO! Estou muito feliz!!")

    def mostra_comandos(self):
        super().mostra_comandos()

    def executa_comando(self,cmd):
        if (cmd = "-1"):
            self.despedida()
        self.perguntas[cmd]
        self.respostas[cmd]
    def boas_vindas(self):
        print(self.nome, "diz: Fico muito feliz que me escolheu, melhor dia de sempre!")

    def despedida(self):
        print(self.nome, "diz: 'Que pena que vai embora, gostei muito de falar com voce!'")
