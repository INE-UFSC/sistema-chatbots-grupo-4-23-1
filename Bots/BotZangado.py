from Bots.Bot import Bot

class BotZangado(Bot):
    def __init__(self,nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(nome):
        self.__nome = nome

    def apresentacao(self):
        print(":( Meu nome é", self.nome, ", seja mal vindo GRRRR!")
 
    def mostra_comandos(self):
        super().mostra_comandos()
    
    def executa_comando(self,cmd):
        if (cmd == 1):
            print(self.nome, "diz: voce disse 'Bom Dia'")
            print("Eu te respondo: Bom dia pra quem?")
        elif (cmd == 2):
            print(self.nome, "diz: voce disse 'Qual o seu nome?'")
            print("Eu te respondo: Não te interessa! Mas é", self.nome)
        elif (cmd == 3):
            print(self.nome, "diz: voce disse 'Quero um conselho'")
            print("Eu te respondo: 'Pergunda pro seu pai!")
        elif (cmd == 4):
            print(self.nome, "diz: voce disse 'Adeus'")
            print("Eu te respondo: 'Ainda esta aqui :('")
        elif (cmd == -1):
            self.despedida()

    def boas_vindas(self):
        print(self.nome, "diz: Eu não posso acreditar que me escolheu!, GRRRRRRRRR!")

    def despedida(self):
        print(self.nome, "diz: 'Finalmente, já estava na hora! GRRR'")
