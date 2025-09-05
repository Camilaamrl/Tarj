1. Pré-requisitos 

Certifique-se de que você tem o Python 3.13.2 instalado.  

Bash 

python --version 
 

2. Instalação das Bibliotecas 

Abra o terminal e execute o seguinte comando para instalar todas as dependências: 

py -m pip install -r requirements.txt 

 

Para instalar manualmente cada biblioteca: 

 

py -m pip install Flask 

py -m pip install python-docx 

py -m pip install PyMuPDF 

py -m pip install pdf2image 

py -m pip install pytesseract 

py -m pip install Pillow 

py -m pip install fuzzywuzzy 

py -m pip install spacy 
 

 

3. Configuração do Tesseract e Modelo spaCy 

Tesseract 

O pytesseract : Você precisa instalar o executável Tesseract em seu sistema. 

Windows: Baixe o instalador em https://github.com/UB-Mannheim/tesseract/wiki 

macOS: Use Homebrew: brew install tesseract. 

Linux (Debian/Ubuntu): Use apt: sudo apt-get install tesseract-ocr. 

Windows:  

Baixe o arquivo  e execute tesseract-ocr-w64-setup-5.5.0.20241111.exe  

Configurando Pyzbar e o Libzbar 

Abra o link no seu navegador: 

 https://pypi.org/project/pyzbar/#files  

E execute o arquivo para instalar manualmente Pyzbar: 

pyzbar-0.1.9-py2.py3-none-win_amd64.whl  

Caso ocorra algum erro, instale a versão C++ 2013:  

https://www.microsoft.com/en-gb/download/details.aspx?id=40784 

 

Modelo de Idioma spaCy 

O projeto utiliza o modelo de processamento de linguagem natural para português pt_core_news_md. Você precisa baixá-lo separadamente: 

Bash 

python -m spacy download pt_core_news_md 
 

 

4. Estrutura do Projeto 

Certifique-se de que a estrutura dos arquivos está organizada da seguinte forma: 

/seu_projeto/ 
├── historico_utils.py 
├── main.py 
├── regex_patterns.py 
├── views.py 
└── templates/ 
    ├── index.html 
    ├── preview_docx.html 
    ├── preview_ocr.html 
    └── preview_pdf.html 
 

Os arquivos .py e a pasta templates devem estar no mesmo diretório. 

 

5. Execução do Projeto 

Bash 

python main.py 
 

 

Descrição das Bibliotecas 

Flask: Um framework para construir a aplicação web. 

python-docx: Usada para ler, modificar e criar arquivos .docx. 

PyMuPDF (fitz): Uma biblioteca para trabalhar com arquivos PDF, permitindo extrair texto e aplicar tarjas (redactions). 

pytesseract: Uma ferramenta de Reconhecimento Óptico de Caracteres (OCR) que extrai texto de imagens, o que é essencial para processar PDFs escaneados. 

pdf2image: Converte páginas de PDF em objetos de imagem do Pillow para que possam ser processadas pelo pytesseract. 

Pillow (PIL): Uma biblioteca de processamento de imagens, usada para manipular as imagens e desenhar tarjas pretas sobre o texto. 

fuzzywuzzy: Ajuda a encontrar correspondências de texto aproximadas (fuzzy string matching), o que é útil para localizar trechos de texto em documentos com erros de OCR. 

spacy: Usada para processamento de linguagem natural, especificamente para o modelo pt_core_news_md. 

 