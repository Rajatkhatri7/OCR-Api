import os
from flask import Flask, json, render_template, request , jsonify
from pathlib import Path
import json

from ocr_core import ocr_core  # ocr function

#global variables
BASE_DIR = Path(__file__).resolve().parent
UPLOAD_FOLDER = str(BASE_DIR) + "/src/uploads/"

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

        # check if the post request has the file part

        if 'file' not in request.files:
            return render_template('upload.html', msg='No file selected')


        file = request.files['file']
        fname = file.filename

        # If the user does not select a file, the browser submits an
        # empty file without a filename.

        if fname == '':
            return render_template('upload.html', msg='No file selected')


        #if file is in file and it is in our allowed files then

        if file and allowed_file(fname):      

            extracted_text = ocr_core(file)
            
            #postprocessing the output
            extracted_text = extracted_text.replace("\n" , " ")
            extracted_text = extracted_text.replace("\f" , "")
            # print(extracted_text)

	    #saving image
            file.save(UPLOAD_FOLDER+fname)
	    
	    #saving output as json
            with open('output.json' ,'w') as f:
                output =  {fname: extracted_text}
                json.dump(output ,f)


            return render_template('upload.html',
                                    msg='Successfully processed',
                                    extracted_text=extracted_text,
                                    img_src=UPLOAD_FOLDER + file.filename)

         #   return jsonify(output)




    elif request.method == 'GET':
        return render_template('upload.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
