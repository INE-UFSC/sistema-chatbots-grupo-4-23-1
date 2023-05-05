#encoding: utf-8
from SistemaChatBot import SistemaChatBot as scb
from Bots.BotZangado import BotZangado
from Bots.BotTriste import BotTriste
from Bots.BotFeliz import BotFeliz
from Bots.BotHogRider import BotHogRider
from Bots.BotZiggs import BotZiggs

###construa a lista de bots disponíveis aqui
lista_bots = [BotZangado("Yoda"), BotTriste("Stitch"), BotFeliz("Sun"), BotHogRider("Hog Rider"), BotZiggs("Ziggs")]

sys = scb.SistemaChatBot("CrazyBots",lista_bots)
sys.inicio()
