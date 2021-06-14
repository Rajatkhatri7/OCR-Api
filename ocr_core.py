try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract  


#pytesseract.pytesseract.tesseract_cmd  = r'/usr/share/tesseract-ocr'


def ocr_core(filename):

	text = pytesseract.image_to_string(Image.open(filename))

	return text


print(ocr_core('src/images/Img_13_1.jpg'))