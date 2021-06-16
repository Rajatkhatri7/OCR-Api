import requests


url = 'http://127.0.0.1:5000/v1/ocr'
my_img = {'file' : open('test.jpg' , 'rb')}


response = requests.post(url , files = my_img)
# response = requests.get(url)

print(response.json())