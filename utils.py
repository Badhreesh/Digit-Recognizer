# General imports
import numpy as np
import base64
import cv2
import math
from scipy import ndimage

def data_uri_to_cv2_img(uri):
    """
    Convert a data URL to an OpenCV image
    Credit: https://stackoverflow.com/a/54205640/2415512
    : param uri : data URI representing a BW image
    : returns   : OpenCV image
    """

    encoded_data = uri.split(',')[1]
    nparr = np.fromstring(base64.b64decode(encoded_data), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_GRAYSCALE)
    return img


def preprocess(img):
    """
    Isolate the digit in the canvas and pad it so that you get a 28x28 image
    : param img : OpenCV image of size (280, 280)
    : returns : OpenCV image of size (1, 28, 28, 1)
    """

    # Crop out the black rows from the top
    while np.sum(img[0]) == 0:
        img = img[1:]

    # Delete the black columns from the left
    while np.sum(img[:, 0]) == 0:
        img = np.delete(img, 0, 1)

    # Crop out the black rows from the bottom
    while np.sum(img[-1]) == 0:
        img = img[:-1]

    # Delete the black cols from the right
    while np.sum(img[:, -1]) == 0:
        img = np.delete(img, -1 ,1)

    rows, cols = img.shape

    # Depending on whether rows or cols in greater, set largest dimension to 20
    # and resize the other so that the aspect ratio is maintained

    if rows > cols:
        factor = int(rows/cols)
        # Set rows to 20
        rows = 20
        # calculate corresponding col value that maintains the factor
        cols = int(rows/factor)

    else:
        factor = int(cols/rows)
        # Set cols to 20
        cols = 20
        # calculate corresponding row value that maintains the factor
        rows = int(cols/factor)

    img = cv2.resize(img, (cols, rows))

    # Need to pad the image so that the img is 28x28
    colsPadding = (int(math.ceil((28-cols)/2.0)), int(math.floor((28-cols)/2.0)))
    rowsPadding = (int(math.ceil((28-rows)/2.0)), int(math.floor((28-rows)/2.0)))
    img = np.lib.pad(img, (rowsPadding, colsPadding), 'constant')

    # Shift image so that the digit's center of mass
    # is nicely centered
    shiftx, shifty = getBestShift(img)
    shifted_img = shift(img, shiftx, shifty)

    # Reshape the image to NHWC format
    img = shifted_img.reshape(1, 28, 28, 1)
    return img


def getBestShift(img):
    """
    Calculate how to shift an image of a digit so that its
    center of mass is nicely centered.
    : param img : black and white image of a digit
    : returns   : optimal shifts (x, y)
    """

    # Calculate center of mass
    cy, cx = ndimage.measurements.center_of_mass(img)

    # Calculate difference between center of mass and actual
    # image center to get shifts
    rows, cols = img.shape
    shiftx = np.round(cols/2.0-cx).astype(int)
    shifty = np.round(rows/2.0-cy).astype(int)

    return shiftx, shifty


def shift(img, sx, sy):
    """
    Shift an image by some offsets
    : param img : black and white image
    : param sx  : shift in x-direction
    : param sy  : shift in y-direction
    : returns   : shifted image
    """

    # Generate warping matrix representing translation only (rotation)
    # part is unit matrix
    M = np.float32([[1, 0, sx], [0, 1, sy]])

    # Apply warping matrix
    rows, cols = img.shape
    shifted = cv2.warpAffine(img, M, (cols, rows),
                             borderMode=cv2.BORDER_CONSTANT, borderValue=255)

    return shifted

