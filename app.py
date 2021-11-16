from logging import debug
from flask import Flask, flash, render_template, request, jsonify
from apps.main_torch import transform_image

app = Flask(__name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
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
            tensor = transform_image(img_bytes)
            # return "Imagem transformada em tensor e pronto para a classificação: " + str(tensor)
            prev =  str(tensor)
            return render_template('upload.html', previsao=prev, aaaa=src)

if __name__ == '__main__':
    app.secret_key = 'ItIsASecret'
    app.run( debug=True)
