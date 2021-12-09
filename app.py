from logging import debug
from flask import Flask, flash, render_template, request, jsonify
from apps.main_torch import *
from apps.main_cv2 import *
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import io
#import cv2
# opencv-python==4.5.3.56



app = Flask(__name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'jfif'}
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET'])
def hello_world():
    src=""
    return render_template('index.html', aaaa=src)

@app.route('/trilha', methods=['GET'])
def trilha():
    return render_template('home-trail.html')

@app.route('/upload', methods=['GET'])
def enviar():
    return render_template('upload.html')

@app.route('/classificacao', methods=['POST'])
def previsao():
    if request.method == 'POST':
        file = request.files.get('file')
        src = request.form.get('invisivel')  
        # print(src)
        if file is None or file.filename == '':
            return render_template('upload.html', previsao="Sem arquivo.")
            # return jsonify({'error': 'no file'})
        if not allowed_file(file.filename):
            # return jsonify({'error': 'format not supported'})
            return render_template('upload.html', previsao="Formato não suportado.")
        else:
            img_bytes = file.read()
            # print(type(img_bytes))
#             image = Image.open(io.BytesIO(img_bytes)) #imagem PIL
#             # print(type(image))
#             buff = np.fromstring(img_bytes, np.uint8)
#             # print(type(buff))
#             buff = buff.reshape(1, -1)
#             # print(type(buff))
#             img = cv2.imdecode(buff,  cv2.IMREAD_GRAYSCALE )
            # print(type(img))
            # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #imagem cv2 pronta para ser trabalhada
            # print(type(img))

    



            # buff = np.fromstring(img_bytes, np.uint8)
            # buff = buff.reshape(1, -1)
            # img = cv2.imdecode(buff, cv2.IMREAD_COLOR)
            # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #imagem cv2 pronta para ser trabalhada

#             lista_blocos = corta3x3(img)
#             lista_blocos_PIL = cv2_to_PIL(lista_blocos)
#             resultado = quantos_verificou(lista_blocos_PIL)

#             if resultado[0]>0:
#                 fusivel = f'Quantidade de Fusível: {resultado[0]}'
#             else:
#                 fusivel = 0

#             if resultado[1]>0:
#                 rele = f'Quantidade de Relé: {resultado[1]}'
#             else:
#                 rele = 0

#             if resultado[2]>0:
#                 capacitor = f'Quantidade de Capacitor Eletrolítico: {resultado[2]}'
#             else:
#                 capacitor = 0

#             if resultado[3]>0:
#                 led = f'Quantidade de LED: {resultado[3]}'
#             else:
#                 led = 0
            

#             prev = "deu certo por enquanto"


            # fusivel, rele, capacitor, led = 0,0,0,0


            tensor = transform_image(image)
            # img = Image.open(src)
            # plt.imshow(img)
            # return "Imagem transformada em tensor e pronto para a classificação: " + str(tensor)
            prev =  str(tensor)
            return render_template('upload.html', previsao=prev, aaaa=src)


@app.route('/t1', methods=['GET'])
def t1():
    return render_template('trail-content-1.html')

@app.route('/t2', methods=['GET'])
def t2():
    return render_template('trail-content-2.html')

@app.route('/t3', methods=['GET'])
def t3():
    return render_template('trail-content-3.html')

@app.route('/t4', methods=['GET'])
def t4():
    return render_template('trail-content-4.html')

@app.route('/t5', methods=['GET'])
def t5():
    return render_template('trail-content-5.html')

@app.route('/t6', methods=['GET'])
def t6():
    return render_template('trail-content-6.html')

@app.route('/t7', methods=['GET'])
def t7():
    return render_template('trail-content-7.html')

@app.route('/t8', methods=['GET'])
def t8():
    return render_template('trail-content-8.html')

@app.route('/t9', methods=['GET'])
def t9():
    return render_template('trail-content-9.html')

@app.route('/t10', methods=['GET'])
def t10():
    return render_template('trail-content-10.html')

@app.route('/t11', methods=['GET'])
def t11():
    return render_template('trail-content-11.html')

@app.route('/t12', methods=['GET'])
def t12():
    return render_template('trail-content-12.html')

@app.route('/t13', methods=['GET'])
def t13():
    return render_template('trail-content-13.html')

if __name__ == '__main__':
    app.secret_key = 'ItIsASecret'
    app.run( debug=True)
