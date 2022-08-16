from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = os.getcwd()+'\static\submitted'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        img = request.files['image']
        if img:
            img_loc = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(img.filename))
            img.save(img_loc)

        return render_template('index.html', var1=img.filename)
    return render_template('index.html')
 
if __name__ == '__main__':
    app.run(debug=True)