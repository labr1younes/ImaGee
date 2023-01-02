import cv2 as cv
import os 
import image_processing as imp
from flask import request ,send_from_directory 
from werkzeug.utils import secure_filename


# check if the file type is allowed 
def allowed_file(filename , allowed):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in allowed

# upload Files
def upload_file(requesst,allowed_files,upload_folder):
    if requesst.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            print('++++++++++No file part')
            return False , ''
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            print('++++++++++No selected file')
            return False , ''
        if not allowed_file(file.filename,allowed_files):
            print('++++++++++File Not allowed ')
            return False , ''
        if file and allowed_file(file.filename,allowed_files):
            filename = secure_filename(file.filename)
            img_path =os.path.join(upload_folder, filename)
            file.save(img_path)
            print("++++++++++file uploaded successfully \n path = " + img_path)
            return True , img_path

# dowload files 
def dowload_file(file_path):
    path,name= os.path.split(file_path)
    return send_from_directory(path,name,as_attachment = True)


# convert image to B&W image 
def img_2_bw(img_path):
    img = cv.imread(img_path,1)
    _,file_name= os.path.split(img_path)
    folder_path = os.path.join('static', 'images')
    tmp_img_path =os.path.join(folder_path, "BnW_{}".format(file_name))
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    check = cv.imwrite(tmp_img_path,img_gray)
    if check :
        return tmp_img_path
    return img_path

# extract text from the image
def img_2_text(img_path,lang):
    text = imp.extract_Text(img_path,lang)
    if len(text)==0 :
        return "No text found in the image"
    return text

