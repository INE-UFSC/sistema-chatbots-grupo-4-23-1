from Bots.Bot import Bot

class BotTriste(Bot):
    def __init__(self,nome):
        super().__init__(nome)
        self.__nome = nome

        self.__respostas = {"1": "Eu te respondo: 'Queria eu que fosse um bom dia...'",
                            "2": "Eu te respondo: 'Normamente me chamam de idiota, burro... Mas meu nome verdadeiro é "+self.nome,
                            "3": "Eu te respondo: 'Também estou precisando, mas até agora nada :('",
                            "4": "Eu te respondo: 'Mas um dia sozinho... Estou acostumado"}


    @property
    def respostas(self):
        return self.__respostas
    @property
    def nome(self):
        return self.__nome


    def apresentacao(self):
        print(":( Meu nome é", self.nome, ", seja bem vindo, eu acho... :c")
 
    def mostra_comandos(self):
        super().mostra_comandos()
    
    def executa_comando(self,cmd):
        if (cmd == '-1'):
           self.despedida()
        print(self.perguntas[cmd])
        print(self.respostas[cmd])

    def boas_vindas(self):
        print(self.nome, "diz: Aleluia alguém me escolheu, não aguentava mais essa solidão...")

    def despedida(self):
        print(self.nome, "diz: 'NAAAAAAAAAAAAAO, por favor :c '")
