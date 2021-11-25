from logging import debug
from flask import Flask, flash, render_template, request, jsonify
from apps.main_torch import *
from PIL import Image
import numpy as np
import cv2



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
            image = Image.open(io.BytesIO(img_bytes))
            # buff = np.fromstring(img_bytes, np.uint8)
            # buff = buff.reshape(1, -1)
            # img = cv2.imdecode(buff, cv2.IMREAD_COLOR)
            # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            
            tensor = verifica_imagem(image)
            # img = Image.open(src)
            # plt.imshow(img)
            # return "Imagem transformada em tensor e pronto para a classificação: " + str(tensor)
            prev =  str(tensor)
            return render_template('upload.html', previsao=prev, aaaa=src)

if __name__ == '__main__':
    app.secret_key = 'ItIsASecret'
    app.run( debug=True)
