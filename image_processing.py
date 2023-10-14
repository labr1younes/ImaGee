import os

import cv2 as cv
import pytesseract
from dotenv import load_dotenv

load_dotenv()
teseract_path = os.getenv("TESSERACTS_PATH")
upload_path = os.path.join('static', 'images')


# Read Image
def read_Img(path):
    image_original = cv.imread(path)
    return image_original


# Convert image to Gray
def to_gray_Img(img):
    image_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    return image_gray


# Gaussian filtering
def gaussian_Filt(image):
    image_gauss = cv.GaussianBlur(image, (5, 5), 0)
    return image_gauss


# Otsu's thresholding
def otsu_Thresh(image):
    otsu_threshold, image_result = cv.threshold(image, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
    return image_result


# Get Image dimensions
def get_Img_Dim(image):
    dimensions = image.shape
    height = image.shape[0]
    width = image.shape[1]
    print('Image Dimension    : ', dimensions)
    print('Image Height       : ', height)
    print('Image Width        : ', width)


# Save image
def save_Img(image, name, type):
    path = upload_path + name + '.' + type
    isWritten = cv.imwrite(path, image)
    if isWritten: {
        print('Image is successfully saved.\n')}
    return path


# Resize Image 
def resize_Img(img, scale_percent):
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized_img = cv.resize(img, dim, interpolation=cv.INTER_AREA)
    return resized_img


# Extract text from the image  ( ara , eng )
def extract_Text(image, language):
    pytesseract.pytesseract.tesseract_cmd = teseract_path
    text = pytesseract.image_to_string(image, lang=language)
    return text
