import os
from flask import Flask, render_template, request
# from werkzeug.utils import secure_filename
import backend_functions as bf
from dotenv import load_dotenv

UPLOAD_FOLDER = os.path.join('static', 'images')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'jpe', 'webp'}

myapp = Flask(__name__)
myapp.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
myapp.secret_key = os.environ.get("SECRET_KEY")


@myapp.route("/")
@myapp.route("/home")
@myapp.route("/index")
def index():
    return render_template("index.html", pagetitle="Main page")


@myapp.route("/contact")
def contact():
    return render_template("contact.html", pagetitle="Contact page")


@myapp.route("/about")
def about():
    return render_template("about.html", pagetitle="About page")


@myapp.route("/to_Black_White", methods=['GET', 'POST'])
def to_black_white():
    if request.method == 'POST':
        _, img_path = bf.upload_file(request, ALLOWED_EXTENSIONS, myapp.config['UPLOAD_FOLDER'])
        if _:
            img_path2 = bf.img_2_bw(img_path)
            return render_template("bnw_page.html", pagetitle="B&W Image page",
                                   orgnl_image_path=img_path,
                                   bnw_image_path=img_path2)
        else:
            return render_template("bnw_page.html", pagetitle="B&W Image page")
    else:
        return render_template("bnw_page.html", pagetitle="B&W Image page")


@myapp.route("/extract_text", methods=['GET', 'POST'])
def extract_text():
    if request.method == 'POST':
        _, img_path = bf.upload_file(request, ALLOWED_EXTENSIONS, myapp.config['UPLOAD_FOLDER'])
        chosen_language = request.form.get("lang")
        if _:
            extrcted_text = bf.img_2_text(img_path, chosen_language)
            return render_template("extracttext_page.html", pagetitle="Text page",
                                   orgnl_image_path=img_path,
                                   extrt_txt=extrcted_text)
        else:
            return render_template("extracttext_page.html", pagetitle="Text page")
    else:
        return render_template("extracttext_page.html", pagetitle="Text page")


@myapp.route("/download_image", methods=['GET', 'POST'])
def download_image():
    if request.method == 'POST':
        name = request.form.get("bnwtest", "(not working)")
        # img_path = os.path.join(myapp.config['UPLOAD_FOLDER'], name)
        return bf.dowload_file(myapp.config['UPLOAD_FOLDER'], name)


if __name__ == "__main__":
    load_dotenv()
    myapp.run(debug=True)
