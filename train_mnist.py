import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential, model_from_json

from tensorflow.keras.layers import Dense, Dropout, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D

# Hyperparameters

num_classes = 10
batch_size = 128
epochs = 20

# Image Resolution

img_rows, img_cols = 28, 28


# Loading the data.

(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Preprocess the data (these are Numpy arrays)
x_train = x_train.reshape(x_train.shape[0], img_rows, img_cols, 1).astype('float32') / 255
x_test = x_test.reshape(x_test.shape[0], img_rows, img_cols, 1).astype('float32') / 255

input_shape = (img_rows, img_cols, 1)

y_train = y_train.astype('float32')
y_test = y_test.astype('float32')


print('x_train shape:', x_train.shape)
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')

y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

# Creating the Model

model = Sequential()
model.add(Conv2D(30, kernel_size=(5, 5), data_format='channels_last',
    activation='relu', input_shape=(input_shape)))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(15, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.2))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(50, activation='relu'))
model.add(Dense(num_classes, activation='softmax'))

# Complile Model

model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

model.fit(x_train, y_train,
          batch_size=batch_size,
          epochs=epochs,
          verbose=1,
          validation_data=(x_test, y_test))

# Evaluating the Predictions on the Model

score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])

# Saving the model for Future Inferences
model.save('mnist_model.h5')
