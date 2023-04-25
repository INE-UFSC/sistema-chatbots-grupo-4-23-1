from Bots.Bot import Bot

class BotTriste(Bot):
    def __init__(self,nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(nome):
        self.__nome = nome

    def apresentacao(self):
        print(":( Meu nome é", self.nome, ", seja bem vindo, eu acho... :c")
 
    def mostra_comandos(self):
        super().mostra_comandos()
    
    def executa_comando(self,cmd):
        if (cmd == 1):
            print(self.nome, "diz: voce disse 'Bom Dia'")
            print("Eu te respondo: 'Queria eu que fosse um bom dia...'")
        elif (cmd == 2):
            print(self.nome, "diz: voce disse 'Qual o seu nome?'")
            print("Eu te respondo: 'Normalmente me chamam de idiota, burro... Mas meu nome verdadeiro é ", self.nome)
        elif (cmd == 3):
            print(self.nome, "diz: voce disse 'Quero um conselho'")
            print("Eu te respondo: 'Também estou precisando, mas até agora nada :c'")
        elif (cmd == 4):
            print(self.nome, "diz: voce disse 'Adeus'")
            print("Eu te respondo: 'Mais um dia sozinho... Estou acostumado já :c'")
        elif(cmd == -1):
            print(f"{despedida()}")

    def boas_vindas(self):
        print(self.nome, "diz: Aleluia alguém me escolheu, não aguentava mais essa solidão...")

    def despedida(self):
        print(self.nome, "diz: 'NAAAAAAAAAAAAAO, por favor :c '")
