# Digit-Recognizer
A complete end-to-end web application that combines web development and machine learning.

Access a live version of the app here: http://digit-recognizer-v1.herokuapp.com/

# About
This app allows the user to interact with a deep neural network (DNN) trained on the MNIST dataset. The user can draw a digit anywhere on the canvas provided. Upon pressing the **Predict** button, the drawn digit will be sent to the Python backend where it is processed and classified by the DNN. The result is then sent back to the frontend for the user to see. Press **Clear** to clear the canvas and draw a new digit.

# How to run this project:
If you would like to dig into the code and make a first run yourself, follow the steps below:

1) Clone the repo
  > https://github.com/Badhreesh/Digit-Recognizer.git
  
2) Create a virtual environment. Use virtualenv to create a virtual environment named **venv** running python3.6, type the following:
  > virtualenv --python=python3.6 venv
  
  Access the virtual environment by:
  > source venv/bin/activate
  
3) Install all dependencies needed to run the app
  > pip install -r requirements.txt
  
  **Note:** The training script requires tensorflow to be installed. It is not in the requirements.txt in order to keep the size of the docker image as small as possible.
  
4) Run the application using:
  > python app.py
  
 5) In a browser, type:
  > localhost:5000
  
  This will load the entire application on screen and you can interact with it.

# File Descriptions

`app.py` serves a Flask web app that loads a trained neural network in ONNX format.

`train_mnist.py` is the script that was used to train the neural network. 

`utils.py` contains all the preprocessing functions necessary to make a good prediction.

`Procfile`, `requirements.txt` and `runtime.txt` are architectural files for Heroku.

`Dockerfile` is the file used to create a docker image of the app.

`templates` contain a html file that serves as the skeleton for the frontend

`static` contains 2 files:
  1) `style.css` which is responsible for styling the frontend
  2) `index.js` which is reponsible for the dynamic behaviors in the app. For example, what happens then you press a button?
  
  `model` contains the ONNX version of the DNN. Using an ONNX model means you don't need tensorflow during inference. This makes the resulting Docker image much smaller and easier to work with.
  

