from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import requests
import os

os.system("cls")

# Carregar o processador e o modelo pré-treinado
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

def gerar_descricao_imagem(url_imagem):
    # Carregar a imagem
    image = Image.open(requests.get(url_imagem, stream=True).raw)
    
    # Preparar a imagem para o modelo
    inputs = processor(images=image, return_tensors="pt")

    # Gerar a descrição da imagem
    output = model.generate(**inputs)
    descricao = processor.decode(output[0], skip_special_tokens=True)
    
    # Simplificar a descrição para ser entendida por pessoas analfabetas
    descricao_simples = simplificar_descricao(descricao)
    
    return descricao_simples

def simplificar_descricao(descricao):
    # Aqui podemos adicionar lógica para simplificar o texto, 
    # como substituição de palavras complexas por palavras simples.
    # Este é um exemplo básico:
    palavras_complexas = {
        "um": "um",
        "menino": "garoto",
        "cachorro": "cão",
        "correndo": "correndo",
        # Adicionar mais substituições conforme necessário
    }
    
    palavras = descricao.split()
    descricao_simples = " ".join([palavras_complexas.get(palavra, palavra) for palavra in palavras])
    
    return descricao_simples

# Exemplo de uso
url_imagem = "https://www.bing.com/th/id/OIP.bSnTokC_c4OMgm-bm9OfyQHaE2?w=240&h=211&c=8&rs=1&qlt=90&o=6&pid=3.1&rm=2"
print(gerar_descricao_imagem(url_imagem))
