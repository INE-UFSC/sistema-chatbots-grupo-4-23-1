from Bots.Bot import Bot

class SistemaChatBot:
    def __init__(self,nomeEmpresa,lista_bots):
        self.__empresa=nomeEmpresa
        ##verificar se a lista de bots contém apenas bots
        self.__lista_bots=lista_bots
        self.__bot = None
    
    def boas_vindas(self):
        
        return (f"Bem-vindo ao SistemaBot!")

    def mostra_menu(self):
        
        print(f"Os chat bots disponíveis para conversa são:")
        count = 1
        for bot in self.__lista_bots:
            print(f"{bot.apresentacao()} - {count}")
            count += 1
    
    def escolhe_bot(self):
        
        escolha = int(input("Escolha o bot que deseja conversar!"))
        count = 1
        for bot in self.__lista_bots:
            if count == escolha:
                self.__bot = bot
            count += 1

    def mostra_comandos_bot(self):
        
        ##mostra os comandos disponíveis no bot escolhido
        print(f"{self.__bot.boas_vindas()}")
        for key, value in self.__bot.comandos.items():
            print(f"Comando {key} - {value}")


    def le_envia_comando(self):
    
        escolha = int(input("Escolha o comando que deseja que o BOT realize: "))
        for key in self.__bot.comandos.keys():
            if key == escolha
                return key
                
        
    def inicio(self):
        
        ##mostra mensagem de boas-vindas do sistema
        ##mostra o menu ao usuário
        ##escolha do bot      
        ##mostra mensagens de boas-vindas do bot escolhido
        ##entra no loop de mostrar comandos do bot e escolher comando do bot até o usuário definir a saída
        ##ao sair mostrar a mensagem de despedida do bot
        boas_vindas()
        mostra_menu()
        escolhe_bot()
        mostra_comandos_bot()
        le_envia_comando()