
# 🧠 OCR e Correção Ortográfica Automática em PDF e Imagens

Este projeto realiza OCR (reconhecimento de texto) a partir de arquivos de imagem e PDF, aplicando correção ortográfica automática em português. Ele converte arquivos PDF em imagens, extrai texto usando pytesseract, corrige ortograficamente e salva os resultados em arquivos .txt.

---

## 📦 Requisitos

- Python 3.7+
- pip

## 📚 Instalação das dependências

No terminal ou prompt de comando, crie um ambiente virtual e instale os pacotes necessários:

```
pip install pillow pytesseract pdf2image pyspellchecker
```

---

## 🛠️ Instalação de bibliotecas externas

O projeto depende de dois programas externos: Poppler (para PDF) e Tesseract (para OCR). Instale conforme abaixo:

### 📄 Poppler (para pdf2image)

1. Acesse: https://github.com/oschwartz10612/poppler-windows/releases
2. Baixe a versão mais recente (ex: poppler-xx.x.x-x64.zip)
3. Extraia em: C:\poppler
4. Adicione ao PATH do sistema:
   - Caminho: C:\poppler\Library\bin

Para adicionar ao PATH:
- Win + R → digite sysdm.cpl → Enter
- Aba Avançado → Variáveis de Ambiente
- Edite a variável Path do sistema e adicione a linha acima
- Clique em OK

---

### 🔠 Tesseract OCR (para pytesseract)

1. Baixe o instalador:
   https://github.com/tesseract-ocr/tesseract/releases/download/5.5.0/tesseract-ocr-w64-setup-5.5.0.20241111.exe

2. Instale o programa (ex: C:\Program Files\Tesseract-OCR)

3. Adicione ao PATH:
   - Caminho: C:\Program Files\Tesseract-OCR

4. No seu código Python, configure o caminho do executável:

```python
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

---

## 📄 Como funciona o código

O script realiza as seguintes etapas:

1. 📁 Cria uma pasta chamada Textos_Corrigidos, se ainda não existir.
2. 🧾 Abre a imagem exemplo_ocr.jpg e extrai o texto usando OCR (pytesseract).
3. 📝 Aplica correção ortográfica nas palavras usando SpellChecker.
4. 💾 Salva o texto corrigido no arquivo Textos_Corrigidos/exemplo_ocr.txt.
5. 📚 Converte o PDF Mussum Ipsum.pdf em imagens (uma por página).
6. 🖼️ Salva cada página como imagem JPG (pagina_0.jpg, pagina_1.jpg...).
7. 🔍 Para cada imagem:
   - Executa OCR
   - Corrige ortografia
   - Salva o texto corrigido em arquivos .txt (um por página)

Exemplo de saída:
- Textos_Corrigidos/exemplo_ocr.txt
- Textos_Corrigidos/pagina_0.txt
- Textos_Corrigidos/pagina_1.txt
- etc.

---

## 🧪 Teste rápido

Garanta que você tenha os seguintes arquivos:
- exemplo_ocr.jpg
- Mussum Ipsum.pdf

Execute o script principal:

```bash
python seu_arquivo.py
```

Você verá os textos extraídos no terminal e os arquivos corrigidos salvos na pasta Textos_Corrigidos.

---

## 📌 Observações

- Para funcionar com português, o Tesseract precisa do idioma por instalado.
- Se estiver faltando, baixe o pacote de idioma ou instale via chocolatey:  
  choco install tesseract --params "/l por"
