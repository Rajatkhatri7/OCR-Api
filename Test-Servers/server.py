''' Server for giving post request from command line '''
try:
    from PIL import Image
except ImportError:
    import Image

import pytesseract 
from flask import Flask, json , jsonify , request





app = Flask(__name__)
_VERSION = 1  # API version


@app.route("/v{}/ocr".format(_VERSION) , methods = ["GET","POST"])
def ocr():
    if request.method=='POST':

        if 'file' not in request.files:
            return jsonify({'response': 'No image found please upload image'})

        
        file = request.files['file']   #image receiving in binary format from user
        # file.save(secure_filename(file.filename))
        img = Image.open(file.stream)   #reading img already coming in binary
        # img = Image.open(file.filename)    #reading img in binary



        ext_text = pytesseract.image_to_string(img) #ocr 
        ext_text = ext_text.replace("\n" ,"")
        ext_text = ext_text.replace("\f" , "")

        output = {file.filename:ext_text}

        return jsonify(output)

    elif request.method == "GET":
        return jsonify({"response":"Only POST request allowed on this server"})
    



if __name__ == '__main__':
    app.debug = True
    app.run()



