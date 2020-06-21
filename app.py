# General imports
import tensorflow as tf
from flask import Flask, render_template, jsonify, request
from flask_cors import CORS, cross_origin
from tensorflow.keras.models import load_model
import traceback
import numpy as np

# Module imports
from utils import preprocess, data_uri_to_cv2_img

# Setting up the Flask app
app = Flask(__name__)

# Allow Cross-Origin Resource Sharing
cors = CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
@cross_origin()
def predict():
    try:
        #img = request.files['data'].read() ## byte file
        img = request.form.get('data')
        img = preprocess(data_uri_to_cv2_img(img))
        probabilities = model.predict(img)
        prediction = np.argmax(probabilities)
        return f'You drew a {prediction}'

    except:
        return jsonify({'trace': traceback.format_exc()})

if __name__ == '__main__':

    # Load the saved model
    model = load_model('model/mnist_model.h5')

    print('model loaded')
    app.run(debug=True, port=8000)
