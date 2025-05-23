import time
import os
import pyttsx3
import easyocr
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch
from tkinter import Tk, filedialog
from translate import Translator

os.system("title AlfABC")

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_principal():
    limpar_tela()
    print("Bem-vindo ao AlfABC, um app de ajuda para pessoas com dificuldade em leitura")
    engine.say("Bem-vindo ao AlfA A B C, um app de ajuda para pessoas com dificuldade em leitura")
    engine.runAndWait()

    print("Se você deseja: Ouvir um texto - Digite 1.  Ler o texto de uma imagem - Digite 2.  Interpretar uma imagem - Digite 3")
    engine.say("Se você deseja ouvir um texto que não consegue ler, aperte um. Se deseja ouvir o texto de uma imagem que não consegue ler, aperte dois. Se deseja interpretar uma imagem de maneira simples, aperte três.")
    engine.runAndWait()

    escolha = int(input('Digite aqui: '))

    if escolha == 1:
        Escolha_Um()
    elif escolha == 2:
        Escolha_Dois()
    elif escolha == 3:
        Escolha_Tres()
    else:
        print("Opção não identificada... Tente novamente")
        engine.say("Perdão, não entendi o que digitou. Tente novamente.")
        engine.runAndWait()
        return menu_principal()

def Escolha_Um():
    time.sleep(1)
    limpar_tela()
    print("Bem-vindo ao Leitor de Textos!")
    engine.say("Bem-vindo ao Leitor de Textos. Aqui você poderá mandar um texto, que eu irei ler em voz alta para você")
    engine.runAndWait()

    texto = input("Insira o texto abaixo:\n----> ")
    limpar_tela()

    print(texto)
    engine.say(texto)
    engine.runAndWait()

    print("Se deseja ouvir outro texto - Digite 1.  Voltar ao menu inicial - Digite 2")
    engine.say("Se deseja ouvir outro texto, aperte um. Se deseja voltar ao menu inicial, aperte dois.")
    engine.runAndWait()

    try:
        escolha_1 = int(input('Digite aqui: '))
    except ValueError:
        print("Entrada inválida.")
        return Escolha_Um()

    if escolha_1 == 1:
        Escolha_Um()
    elif escolha_1 == 2:
        menu_principal()
    else:
        print("Opção não identificada... Tente novamente.")
        engine.say("Perdão, não entendi. Tente novamente.")
        engine.runAndWait()
        Escolha_Um()

def Escolha_Dois():
    time.sleep(1)
    limpar_tela()

    print("Bem-vindo ao Leitor de Textos de Imagens!")
    engine.say("Bem-vindo ao Leitor de Textos de Imagens. Envie uma imagem com texto e eu lerei para você.")
    engine.runAndWait()

    root = Tk()
    root.withdraw()
    root.call('wm', 'attributes', '.', '-topmost', '1')
    caminho_imagem = filedialog.askopenfilename(title="Escolha uma imagem de texto")
    root.destroy()

    if not caminho_imagem or not os.path.isfile(caminho_imagem):
        print("Imagem não encontrada ou seleção cancelada.")
        engine.say("Imagem não encontrada ou seleção cancelada.")
        engine.runAndWait()
        return menu_principal()

    print("Analisando imagem... Aguarde.")
    engine.say("Analisando imagem. Aguarde.")
    engine.runAndWait()

    reader = easyocr.Reader(['pt'])
    results = reader.readtext(caminho_imagem)
    texto_final = ' '.join([item[1] for item in results])

    print("TEXTO: " + texto_final)
    engine.say(texto_final)
    engine.runAndWait()

    print("Ouvir outra imagem - Digite 1.  Voltar ao menu principal - Digite 2.")
    engine.say("Ouvir outra imagem, digite um. Voltar ao menu principal, digite dois.")
    engine.runAndWait()

    escolha_2 = int(input('Digite aqui: '))

    if escolha_2 == 1:
        Escolha_Dois()
    elif escolha_2 == 2:
        menu_principal()
    else:
        print("Opção não identificada.")
        engine.say("Desculpe, não entendi.")
        engine.runAndWait()
        Escolha_Dois()

def Escolha_Tres():
    time.sleep(1)
    limpar_tela()

    print("Bem-vindo ao Intérprete de Imagens!")
    engine.say("Bem-vindo ao Intérprete de Imagens. Envie uma imagem e eu a descreverei de forma simples.")
    engine.runAndWait()

    root = Tk()
    root.withdraw()
    root.call('wm', 'attributes', '.', '-topmost', '1')
    caminho_imagem = filedialog.askopenfilename(title="Escolha uma imagem para interpretar")
    root.destroy()

    if not caminho_imagem or not os.path.isfile(caminho_imagem):
        print("Imagem não encontrada ou seleção cancelada.")
        engine.say("Imagem não encontrada ou seleção cancelada.")
        engine.runAndWait()
        return menu_principal()

    print("Analisando imagem... Aguarde.")
    engine.say("Analisando imagem. Aguarde.")
    engine.runAndWait()

    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

    img = Image.open(caminho_imagem).convert("RGB")
    inputs = processor(img, return_tensors="pt")
    output = model.generate(**inputs)
    descricao_em_ingles = processor.decode(output[0], skip_special_tokens=True)

    tradutor = Translator(to_lang="pt")
    descricao = tradutor.translate(descricao_em_ingles)

    print("Descrição da imagem:", descricao)
    engine.say(descricao)
    engine.runAndWait()

    print("Interpretar outra imagem - Digite 1.  Voltar ao menu principal - Digite 2.")
    engine.say("Interpretar outra imagem, digite um. Voltar ao menu principal, digite dois.")
    engine.runAndWait()

    try:
        escolha_3 = int(input('Digite aqui: '))
        if escolha_3 == 1:
            Escolha_Tres()
        elif escolha_3 == 2:
            menu_principal()
        else:
            print("Opção não identificada.")
            engine.say("Desculpe, não entendi.")
            engine.runAndWait()
            Escolha_Tres()
    except ValueError:
        print("Entrada inválida.")
        engine.say("Entrada inválida.")
        engine.runAndWait()
        Escolha_Tres()

menu_principal()
