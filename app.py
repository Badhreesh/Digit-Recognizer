# General imports
from flask import Flask, render_template, jsonify, request
from flask_cors import CORS, cross_origin
import traceback
import numpy as np
import os
import onnxruntime as rt

# Module imports
from utils import preprocess, data_uri_to_cv2_img

# Setting up the Flask app
app = Flask(__name__)

# Allow Cross-Origin Resource Sharing
cors = CORS(app)

sess_options = rt.SessionOptions()
sess_options.execution_mode = rt.ExecutionMode.ORT_SEQUENTIAL
sess_options.graph_optimization_level = rt.GraphOptimizationLevel.ORT_ENABLE_ALL

session = rt.InferenceSession('model/model.onnx', sess_options=sess_options)
# get the I/O names
input_names = session.get_inputs()[0].name
print(session.get_inputs()[0].type)
output_names = [session.get_outputs()[ii].name for ii in range(len(session.get_outputs()))]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
@cross_origin()
def predict():
    try:
        img = request.form.get('data')
        img = preprocess(data_uri_to_cv2_img(img))
        probabilities = session.run(output_names, {input_names: img.astype(np.float32)})[0]
        prediction = np.argmax(probabilities)
        return 'You drew a {}'.format(prediction)

    except:
        return jsonify({'trace': traceback.format_exc()})

# Start flask app
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
