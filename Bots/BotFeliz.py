from Bots.Bot import Bot

class BotFeliz(Bot):
    def __init__(self,nome):
        super().__init__(nome)
        self.__nome = nome

        self.__respostas = {"1": "Eu te respondo: 'BOM DIA! MAS QUE LINDO DIA!'",
                    "2": "Eu te respondo: 'Normamente me chamam de idiota, burro... Mas meu nome verdadeiro é "+self.nome,
                    "3": "Eu te respondo: 'Pensar positivo nos ajuda a nos mantermos firmes e fortes e seguir nosso caminho!'",
                    "4": "Eu te respondo: 'Até mais, esterei sempre aqui para mais conversas!'"}


    @property
    def respostas(self):
        return self.__respostas
    @property
    def nome(self):
        return self.__nome


    def apresentacao(self):
        print(":) Meu nome é", self.nome, ", seja MUITOOOO BEM VINDOOO! Estou muito feliz!!")

    def mostra_comandos(self):
        super().mostra_comandos()

    def executa_comando(self,cmd):
        if (cmd == '-1'):
           self.despedida()
        print(self.perguntas[cmd])
        print(self.respostas[cmd])

    def boas_vindas(self):
        print(self.nome, "diz: Fico muito feliz que me escolheu, melhor dia de sempre!")

    def despedida(self):
        print(self.nome, "diz: 'Que pena que vai embora, gostei muito de falar com voce!'")
