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


<hr>

### 🛠️ Classificador de Componentes


<p align="center">
  <img src="https://user-images.githubusercontent.com/65060013/153951837-932adc0b-93b7-48a5-947b-2e7befb3290f.gif">
</p>


Ramo que o usuário é capaz de fazer o upload de uma imagem para o classificador agir. O classificador foi treinado para detectar 4 tipos de componentes, são eles:

- Fusível
- Relê
- Capacitor eletrolítico
- LED

## ✍️ Autores



> *Fabrício da Costa Guimarães* 
> - Engenharia da Computação UFAM 
> - <a href="https://www.linkedin.com/in/abriciof/" target="_blank"> LinkedIn </a> 
> - <a href="https://github.com/abriciof/" target="_blank"> GitHub </a>
> 
>
> *João Victor de Carvalho Marques*
> - Engenharia da Computação UFAM 
> - <a href="https://www.linkedin.com/in/jo%C3%A3o-marques-171261134/" target="_blank"> LinkedIn </a>
> - <a href="https://github.com/Battlesides" target="_blank"> GitHub </a>
> 
>
> *Kluiwert Victor Tavares Mota* 
> - Engenharia Elétrica UFAM
> - <a href="https://www.linkedin.com/" target="_blank"> LinkedIn </a>
> - <a href="https://github.com/kluiwert/" target="_blank"> GitHub </a>
>



<p align="center">
  <br>
  <img src="https://user-images.githubusercontent.com/65060013/156955108-35069a93-3c6e-4e07-abf8-dfd5f3a443bb.png" style="width:20%">
    <img src="https://user-images.githubusercontent.com/65060013/156952397-8edfe44c-edfc-406c-bfb0-87f7a5e73e0b.png" style="width:20%">
</p>



