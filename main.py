# Importa bibliotecas necessárias
from PIL import Image                   # Para abrir e manipular imagens
import pytesseract                      # Para realizar OCR (reconhecimento de texto em imagem)
from pdf2image import convert_from_path # Para converter PDF em imagens
from spellchecker import SpellChecker   # Para correção ortográfica automática
import os                               # Para manipular arquivos e diretórios

# Cria uma pasta chamada "Textos_Corrigidos", se não existir
os.makedirs("Textos_Corrigidos", exist_ok=True)

# Inicializa o corretor ortográfico com o idioma português
spell = SpellChecker(language="pt")

# Abre a imagem exemplo_ocr.jpg
imagem = Image.open("exemplo_ocr.jpg")

# Extrai o texto da imagem usando OCR com idioma português
texto = pytesseract.image_to_string(imagem, lang="por")

# Exibe o texto extraído no terminal
print(texto)

# Corrige cada palavra do texto, se tiver erro de ortografia
palavras = texto.split()
correcao = [spell.correction(p) if spell.correction(p) else p for p in palavras]
texto_corrigido = " ".join(correcao)

# Salva o texto corrigido em um arquivo de texto dentro da pasta "Textos_Corrigidos"
with open("Textos_Corrigidos/exemplo_ocr.txt", "w", encoding="utf-8") as f:
    f.write(texto_corrigido)

# Converte o arquivo PDF em uma lista de imagens (uma imagem por página)
imagens = convert_from_path('Mussum Ipsum.pdf')

# Salva cada imagem da lista como arquivo JPG, no caso seriam,  pagina_0.jpg, pagina_1.jpg...)
for i, img in enumerate(imagens):
    img.save(f'pagina_{i}.jpg', 'JPEG')
    print(f'Página {i} salva como imagem.')


# Página 0
imagem1 = Image.open("pagina_0.jpg")                        # Abre a imagem da página 0
texto1 = pytesseract.image_to_string(imagem1, lang="por")   # Extrai texto via OCR
print(texto1)                                               # Mostra o texto extraído
palavras1 = texto1.split()                                  # Divide o texto em palavras
correcao1 = [spell.correction(p) if spell.correction(p) else p for p in palavras1]  # Corrige
texto_corrigido1 = " ".join(correcao1)                      # Junta de novo em string
with open("Textos_Corrigidos/pagina_0.txt", "w", encoding="utf-8") as f:  # Salva o txt corrigido
    f.write(texto_corrigido1)

# Página 1      -Comentários para as demais páginas são iguais ao da Página 0, funções são iguais, apenas os arquivos maniulados são diferentes
imagem2 = Image.open("pagina_1.jpg")
texto2 = pytesseract.image_to_string(imagem2, lang="por")
print(texto2)
palavras2 = texto2.split()
correcao2 = [spell.correction(p) if spell.correction(p) else p for p in palavras2]
texto_corrigido2 = " ".join(correcao2)
with open("Textos_Corrigidos/pagina_1.txt", "w", encoding="utf-8") as f:
    f.write(texto_corrigido2)

# Página 2
imagem3 = Image.open("pagina_2.jpg")
texto3 = pytesseract.image_to_string(imagem3, lang="por")
print(texto3)
palavras3 = texto3.split()
correcao3 = [spell.correction(p) if spell.correction(p) else p for p in palavras3]
texto_corrigido3 = " ".join(correcao3)
with open("Textos_Corrigidos/pagina_2.txt", "w", encoding="utf-8") as f:
    f.write(texto_corrigido3)

# Página 3
imagem4 = Image.open("pagina_3.jpg")
texto4 = pytesseract.image_to_string(imagem4, lang="por")
print(texto4)
palavras4 = texto4.split()
correcao4 = [spell.correction(p) if spell.correction(p) else p for p in palavras4]
texto_corrigido4 = " ".join(correcao4)
with open("Textos_Corrigidos/pagina_3.txt", "w", encoding="utf-8") as f:
    f.write(texto_corrigido4)