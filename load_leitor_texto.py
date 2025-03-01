import pyttsx3
import os
import time
import subprocess
from tqdm import tqdm

os.system('cls')

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

print("Você selecionou o Leitor de texto.")
engine.say("Você selecionou o Leitor de texto.")
engine.runAndWait()

os.system('cls')

print("CARREGANDO. AGUARDE")
engine.say("Carregando. Aguarde")
engine.runAndWait()

for i in tqdm(range(150)):
  time.sleep(0.1)

print("PRONTO")
engine.say("PRONTO")
engine.runAndWait()
os.system('cls')
subprocess.run (["python", "leitor_texto.py"])
