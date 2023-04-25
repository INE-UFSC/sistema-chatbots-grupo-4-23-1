from Bots.Bot import Bot

class BotFeliz(Bot):
    def __init__(self,nome):
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
        if (cmd == "1"):
            print(self.nome, "diz: voce disse 'Bom Dia'")
            print("Eu te respondo: BOM DIA! MAS QUE LINDO DIA!")
        elif (cmd == "2"):
            print(self.nome, "diz: voce disse 'Qual o seu nome?'")
            print("Eu te respondo: 'Meu nome é", self.nome, ", fico feliz em te conhecer!")
        elif (cmd == "3"):
            print(self.nome, "diz: voce disse 'Quero um conselho'")
            print("Eu te respondo: 'Pensar positivo nos ajuda a nos mantermos firmes e fortes e seguir nosso caminho!'")
        elif (cmd == "4"):
            print(self.nome, "diz: voce disse 'Adeus'")
            print("Eu te respondo: 'Até mais, esterei sempre aqui para mais conversas!'")

    def boas_vindas(self):
        print(self.nome, "diz: Fico muito feliz que me escolheu, melhor dia de sempre!")

    def despedida(self):
        print(self.nome, "diz: 'Que pena que vai embora, gostei muito de falar com voce!'")
