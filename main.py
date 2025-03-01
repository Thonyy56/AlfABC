import pyttsx3
import os
import time
import subprocess

os.system('cls')

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  

print("Bem vindo ao app de ajuda para pessoas com dificuldáde em leitura")
engine.say("Bem vindo ao app de ajuda para pessoas com dificuldáde em leitura")
engine.runAndWait()

print("Se voce deseja ouvir o texto de uma imagem aperte 1. Se deseja Ouvir um texto diferente aperte 2. Se deseja sair aperte 3")
engine.say("Se voce deseja ouvir o texto de uma imagem aperte 1. Se deseja Ouvir um texto diferente aperte 2. Se deseja sair aperte 3.")
engine.runAndWait()

escolha = int(input('Digite aqui: '))

if escolha == 1:
    time.sleep(3)
    os.system('cls')
    subprocess.run (["python", "load_leitor_foto.py"])

elif escolha == 2:
    time.sleep(3)
    os.system('cls')
    subprocess.run (["python", "load_leitor_texto.py"])

elif escolha == 3:
    os.system('cls')

else:
    print("não entendi, poderia repetir")
    engine.say("não entendi, poderia repetir")
    engine.runAndWait()