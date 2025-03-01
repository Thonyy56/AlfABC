import pyttsx3
import os
import time
import subprocess

os.system('cls')

engine = pyttsx3.init()
print("BEM VINDO AO LEITOR DE FOTOS")
engine.say("Bem vindo ao Leitor de Fotos.")
engine.runAndWait()