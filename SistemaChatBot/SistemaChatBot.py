from Bots.Bot import Bot
from Bots.BotZangado import BotZangado
from Bots.BotTriste import BotTriste
from Bots.BotFeliz import BotFeliz

class SistemaChatBot:
    def __init__(self,nomeEmpresa,lista_bots):
        self.__empresa=nomeEmpresa
        ##verificar se a lista de bots contém apenas bots
        self.__lista_bots=lista_bots
        self.__bot = None
    
    def boas_vindas(self):
        
        return (f"Bem-vindo ao {self.__empresa}!")

    def mostra_menu(self):
        
        print(f"Os chat bots disponíveis para conversa são:")
        count = 1
        for bot in self.__lista_bots:
            print(f"{bot.apresentacao()} - {count}")
            count += 1
    
    def escolhe_bot(self):
        
        escolha = int(input("Escolha o bot que deseja conversar!"))
        self.__bot = self.__lista_bots[escolha-1]

    def mostra_comandos_bot(self):
        
        ##mostra os comandos disponíveis no bot escolhido
        self.__bot.mostra_comandos()


    def le_envia_comando(self):
        escolha = input("Escolha o comando que deseja que o BOT realize: ")
        return escolha
            
                
        
    def inicio(self):
        
        ##mostra mensagem de boas-vindas do sistema
        ##mostra o menu ao usuário
        ##escolha do bot      
        ##mostra mensagens de boas-vindas do bot escolhido
        ##entra no loop de mostrar comandos do bot e escolher comando do bot até o usuário definir a saída
        ##ao sair mostrar a mensagem de despedida do bot
        self.boas_vindas()
        self.mostra_menu()
        self.escolhe_bot()


        self.__bot.boas_vindas()
        while(True):
            print()
            self.mostra_comandos_bot()
            opcao = self.le_envia_comando()
            if(opcao == "-1"):
                break
            else:
                self.__bot.executa_comando(opcao)
