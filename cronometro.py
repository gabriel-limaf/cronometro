"""
Temporizador by Gabriel Lima
"""
from time import sleep
import pyttsx3
import os

print('Bem-vindo ao temporizador em Python!')


def temporizador():
    m = 0
    h = 0
    s = 0
    entrada_h = int(input('Defina as horas do temporizador: '))
    # h = entrada_h * 3600
    entrada_m = int(input('Defina os minutos do temporizador: '))
    # m = entrada_m * 60
    entrada_s = int(input('Defina os segundos do temporizador: '))
    timer = (entrada_h * 3600) + (entrada_m * 60) + entrada_s
    for contagem in range(0, timer + 1):
        if contagem // 60 == contagem / 60:
            m = m + 1
            s = 0
        if contagem // 60 != contagem / 60:
            s = s + 1
        if contagem // 3600 == contagem / 3600:
            h = h + 1
        if contagem < 60:
            s = contagem
        print(f'{h - 1}:{m - 1}:{s}')
        sleep(1)
        os.system("cls") or None
    esgotado('Tempo esgotado')
    sleep(1)
    esgotado('Tempo esgotado')
    exit()


def esgotado(texto):
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()


temporizador()
