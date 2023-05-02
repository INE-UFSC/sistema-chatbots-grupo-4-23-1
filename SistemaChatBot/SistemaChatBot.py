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
            print(f'{count} - ', end = '')
            bot.apresentacao()
            count += 1
    
    def escolhe_bot(self): 
        escolha = 0
        while True:
            escolha = int(input("Escolha o bot que deseja conversar! (-1 para sair do programa): "))
            print()

            if escolha == -1:
                return '-1'

            if escolha < 1 or escolha > len(self.__lista_bots): 
                print('Erro! Escolha um valor válido.')
            else:
                break

        self.__bot = self.__lista_bots[escolha-1]
        return str(escolha)

    def mostra_comandos_bot(self):
        
        ##mostra os comandos disponíveis no bot escolhido
        self.__bot.mostra_comandos()


    def le_envia_comando(self):
        escolha = input("Digite o comando desejado (ou -1 fechar o sistema sair): ")
        print()
        return escolha
            
                
        
    def inicio(self):
        
        ##mostra mensagem de boas-vindas do sistema
        ##mostra o menu ao usuário
        ##escolha do bot      
        ##mostra mensagens de boas-vindas do bot escolhido
        ##entra no loop de mostrar comandos do bot e escolher comando do bot até o usuário definir a saída
        ##ao sair mostrar a mensagem de despedida do bot
        opcao = None
        while(True):
            if opcao == '-1':
                print('Fim do programa.')
                break
            self.boas_vindas()
            self.mostra_menu()
            opcao = self.escolhe_bot()

            while(opcao != '-1'):
                print()
                self.__bot.boas_vindas()
                self.mostra_comandos_bot()
                opcao = self.le_envia_comando()
                if(opcao == "-1" or opcao == "4"):
                    break
                else:
                    self.__bot.executa_comando(opcao)