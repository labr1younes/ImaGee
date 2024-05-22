# ImaGee (In progress)
ImaGee is a Website built with Python and Flask framework , its main purpose is image processing .

## Features
1. **Black and White Conversion**: Convert images to black and white (grayscale) .
2. **Text Extraction**: Extract text from images (Arabic and English) .
3. **Image Enhancement**: improve the quality of image up to 4 times .(In progress)

## Getting Started

To use the ImaGee , follow these steps:

1. **Clone the Repository**:
`git clone https://github.com/labr1younes/ImaGee.git`
2. Install Tesseract OCR .
3. Step into the project folder: `cd ImaGee`
4. Run this command `pip install -r requirements.txt`
5. Add `.env` file with these values:

        SECRET_KEY="flask app secret key"
        TESSERACTS_PATH="tesseract.exe OCR app instlation path"
        UPLOAD_PATH="image uplodaing path folder"
6. And you are done , you can lunch the flask app. 

## Contribution

If you have any suggestions, improvements, or new project ideas, I welcome contributions from the community. Please feel free to open an issue or submit a pull request with your changes.

## License

This repository is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute the code in this repository for personal or commercial purposes.