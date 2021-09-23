"""
Cronometro by Gabriel Lima
"""
from time import sleep
import pyttsx3

print('Bem-vindo ao cronometro em Python!')


def cronometro():
    entrada_h = int(input('Defina as horas do cronometro: '))
    entrada_m = int(input('Defina os minutos do cronometro: '))
    entrada_s = int(input('Defina os segundos do cronometro: '))
    timer = (entrada_h * 3600) + (entrada_m * 60) + entrada_s
    for contagem in range(0, timer):
        sleep(1)
    esgotado('Tempo esgotado')
    sleep(1)
    esgotado('Tempo esgotado')
    exit()


def esgotado(texto):
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()


cronometro()
