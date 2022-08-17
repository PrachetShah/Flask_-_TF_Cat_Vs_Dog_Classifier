from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
import tensorflow as tf
from tensorflow import keras
import numpy as np

UPLOAD_FOLDER = os.getcwd()+'/static/submitted'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        # Getting image and checking for method
        img = request.files['image']
        if img:
            classifier = tf.keras.models.load_model('models/CatVsDogClassifier.h5')
            img_loc = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(img.filename))
            img.save(img_loc)

            # Loading image and performing preprocessing
            test_image = keras.preprocessing.image.load_img(img_loc, target_size=(64, 64))
            test_image = keras.preprocessing.image.img_to_array(test_image)
            test_image = np.expand_dims(test_image, axis=0) 

            # Predicting Image
            result = classifier.predict(test_image/255.0)
            print(result)
            if result[0][0] > 0.5:
                prediction = 'Dog'
            else:
                prediction = 'Cat'
            print(prediction)
            query = {
                'src': img.filename,
                'prediction': prediction
            }

        return render_template('index.html', var1=query)
    return render_template('index.html')
 
if __name__ == '__main__':
    app.run(debug=True)