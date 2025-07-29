from tkinter import *
import requests
from PIL import Image, ImageTk
from io import BytesIO


def load_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        image_data = BytesIO(response.content)
        img = Image.open(image_data)
        img.thumbnail((600, 480), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Error occured {e}.")
        return None


def open_new_window():
    tag = tag_entry.get()
    url_tag = f'https://cataas.com/cat/{tag}' if tag else 'https://cataas.com/cat'
    img = load_image(url_tag)

    if img:
        new_window = Toplevel()
        new_window.title('Image with a Cat')
        new_window.geometry('600x480')
        label = Label(new_window, image=img)
        label.pack()
        # label.config(image=img)
        label.image = img


def exit():
    window.destroy()

window = Tk()
window.title('Cats')
window.geometry('400x220')

label = Label()
label.pack()

tag_entry = Entry()
tag_entry.pack()

load_button = Button(text='Загрузить тэг', command=open_new_window)
load_button.pack()

# update_button = Button(text='Обновить', command=set_image)
# update_button.pack()

url = 'https://cataas.com/cat'

menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Файл', menu = file_menu)
file_menu.add_command(label='Загрузить фото', command=open_new_window)
file_menu.add_separator()
file_menu.add_command(label='Выход', command=exit)

open_new_window()

window.mainloop()
