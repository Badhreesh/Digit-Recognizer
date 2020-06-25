# General imports
import tensorflow as tf
from flask import Flask, render_template, jsonify, request
from flask_cors import CORS, cross_origin
from tensorflow.keras.models import load_model
import traceback
import numpy as np
import os

# Module imports
from utils import preprocess, data_uri_to_cv2_img

# Setting up the Flask app
app = Flask(__name__)

# Allow Cross-Origin Resource Sharing
cors = CORS(app)

# Load the saved model
model = load_model('model/mnist_model.h5')


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
        return 'You drew a {}'.format(prediction)

    except:
        return jsonify({'trace': traceback.format_exc()})

# Start flask app
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
