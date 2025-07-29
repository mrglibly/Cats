from tkinter import *
from requests import request
from PIL import Image, ImageTk
from io import BytesIO


def load_image():
    try:
        response = request.get(url)
        response.raise_for_status()
        image_data = BytesIO(response.content)
        img = Image.open(image_data)
        return ImageTk.PhotoImage(img)

    except Exception as e:
        print(f'Error occured {e}')
        return None


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
