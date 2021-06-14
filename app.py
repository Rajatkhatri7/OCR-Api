import os
from flask import Flask, render_template, request


from ocr_core import ocr_core  # ocr function


UPLOAD_FOLDER = 'src/uploads/'

# allowed files
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# @app.route('/')
# def home_page():
#     return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def upload_page():
    if request.method == 'POST':

        # check if there is a file in the request
        if 'file' not in request.files:
            return render_template('upload.html', msg='No file selected')
        file = request.files['file']

        # if no file is selected
        if file.filename == '':
            return render_template('upload.html', msg='No file selected')

        if file and allowed_file(file.filename):

            extracted_text = ocr_core(file)

            return render_template('upload.html',
                                   msg='Successfully processed',
                                   extracted_text=extracted_text,
                                   img_src=UPLOAD_FOLDER + file.filename)


                                   

    elif request.method == 'GET':
        return render_template('upload.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
