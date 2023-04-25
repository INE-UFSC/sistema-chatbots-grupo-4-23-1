from SistemaChatBot import SistemaChatBot
from Bots.BotTriste import BotTriste
from Bots.BotFeliz import BotFeliz
from Bots.BotZangado import BotZangado

system = SistemaChatBot('EmpresaTeste', [BotFeliz('Bot Feliz 1'), BotZangado('Bot Zangado 1'), BotTriste('Bot Triste  1')])
system.inicio()