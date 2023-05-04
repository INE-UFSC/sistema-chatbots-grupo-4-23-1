##implemente as seguintes classes

from abc import ABC, abstractmethod
from Comando import Comando

class Bot(ABC):
    def __init__(self, nome: str, lista_comando: list[Comando]):
        self.__nome = nome

        self.__lista_comandos = lista_comando


    @property
    def lista_comandos(self):
        return self.__lista_comandos

    @property
    def perguntas(self):
        return self.__perguntas

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(nome):
        self.__nome = nome

    def mostra_comandos(self) -> str:
        comandos = ""
        for x in self.lista_comandos:
           comandos += f"{x.cmd} - {x.pergunta} \n" 

        return comandos

    def executa_comando(self, cmd: int) -> str:
        for x in self.lista_comandos:
            if (x.cmd == cmd):
                resposta = f"{self.nome} diz: Voce disse: '{x.pergunta}' \n"
                resposta += f"Eu te respondo: '{x.resposta}'"

                return resposta

    @abstractmethod
    def boas_vindas() -> str:
        pass
    
    @abstractmethod
    def despedida() -> str:
        pass
