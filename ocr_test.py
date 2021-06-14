try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract  # python wrapper for Tesseract engine , so also install Tesseract engine
import glob

#pytesseract.pytesseract.tesseract_cmd  = r'/usr/share/tesseract-ocr'


def ocr(filename):

	text = pytesseract.image_to_string(Image.open(filename))

	return text



images = [imgName for imgName in glob.glob(r'src/images/*')]
images.sort()
for counter, imgName in enumerate(images):
	
	print("for {} :".format(imgName[10:]))
	result = ocr(imgName)
	print(result)
