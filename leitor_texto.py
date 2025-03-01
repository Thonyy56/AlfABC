import pyttsx3
import os
import time
import subprocess

os.system('cls')

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) 

print("BEM VINDO AO LEITOR DE TEXTOS")
engine.say("Bem vindo ao Leitor de textos.")
engine.runAndWait()

print("Para começar, coloque o texto que você quer ouvir")
engine.say("Para começar, coloque o texto que você quer ouvir.")
engine.runAndWait()

texto = input("----> ")

time.sleep(3)

print(texto)
engine.say(texto)
engine.runAndWait()

print("Se você deseja repetir e ler outro texto, digite 1. Se deseja voltar ao início, digite 2. Se deseja fechar, aperte 3")
engine.say("Se você deseja repetir e ler outro texto, digite 1. Se deseja voltar ao início, digite 2. Se deseja fechar, aperte 3")
engine.runAndWait()

Escolha = int(input('---> '))

if Escolha == 1:
    subprocess.run(["python", "leitor_texto.py"])

elif Escolha == 2:
    subprocess.run(["python", "main.py"])

elif Escolha == 3:
    os.system("cls")