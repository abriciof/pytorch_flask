# Classificação de Componentes Eletrônicos em Placa de Circuito Impresso utilizando Machine Learning




<p align="center">
  <img src="https://user-images.githubusercontent.com/65060013/153782146-1fd45186-119c-47f7-9f10-44bd09e5a0b0.gif">
</p>


## 🪧 Descrição

A aplicação tem como objetivo classificar e quantizar os tipos de componentes de uma placa de circuito impresso.

## 🖥️ Tecnologias

A aplicação web foi desenvolvida com auxílio do framework [Flask](https://flask.palletsprojects.com/en/2.0.x/), juntamente com bibliotecas para o processamento de imagens ([OpenCV](https://opencv.org/)) e para o uso da estruturas de rede neural artificial ([PyTorch](https://pytorch.org/)). Todos essas bibliotecas sendo da [Linguagem Python](https://www.python.org/) versão 3.9.7.

## 🧾 Instalação de dependências

Após clonar esse repositório em seu computador e ter a versão surgerida do Python, é necessário instalar as bibliotecas necessárias para o funcionamento da aplicação. São elas: 

```python
fonttools==4.29.0
itsdangerous==2.0.1
Jinja2==3.0.3
kiwisolver==1.3.2
MarkupSafe==2.0.1
matplotlib==3.5.1
numpy==1.21.4
opencv-python==4.5.3.56
packaging==21.3
Pillow==9.0.0
pyparsing==3.0.7
python-dateutil==2.8.2
six==1.16.0
torch==1.8.0
torchvision==0.9.0
typing_extensions==4.0.1
Werkzeug==2.0.2
```

Instalando via terminal com o comando [pip](https://pypi.org/project/pip/):

```bash
$ pip install -r requirements.txt
```


## 📟 Como usar

Após a instalação de dependências, é preciso que usar o comando de iniciação da aplicação no terminal (ou no servidor web), com o comando:

```python
$ python .\app.py
```

Com isso, é possível visualizar a aplicação diretamente no navegador (ou no servidor web).

## 🌳 Ramos da Aplicação

### 📚 Trilha de Aprendizado

<p align="center">
  <img src="https://user-images.githubusercontent.com/65060013/153949876-bc58cecd-b0a1-4eb5-9977-c5dfbdc431ba.gif">
</p>



Ramo responsável pela introdução de conteúdos, conceitos, definições para o usuário da plataforma.

### 🛠️ Classificador de Componentes

imagem

Ramo que o usuário é capaz de fazer o upload de uma imagem para o classificador agir. O classificador foi treinado para detectar 4 tipos de componentes, são eles:

- Fusível
- Relê
- Capacitor eletrolítico
- LED

