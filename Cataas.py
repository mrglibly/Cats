from tkinter import *
from requests import request
from PIL import Image, ImageTk
from io import BytesIO

window = Tk()
window.title('Cats')
window.geometry('600X480')

label = (Label()
label.pack())

url = 'https://cataas.com/cat'

img = load_image(url)

if img:
    label.config(image = img)
    label.imaage - img

window.mainloop()
