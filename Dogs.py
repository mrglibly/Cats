from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import requests
from io import BytesIO

def get_dog_image():

def show_image():
    img_url = get_dog_image()
    if img_url:
        try:
            response = requests.get(img_url, stream=True)
            response.raise_for_status()
            img_data = BytesIO(response.content)
            img = Image.open(img_data)
            img.thumbnail((300, 300), Image.Resampling.LANCZOS)
            label.config(image=img)
            label.image = img
        except Exception as e:
            print(f"Error occured {e}.")
            return None

        return ImageTk.PhotoImage(img)


window = Tk()
window.title("Dogy Pictures!")
window.geometry("360x420")

label = Label()
label.pack()

button = Button(text='Загрузить фото', command=show_image)
button.pack(pady=10)

# menu_bar = Menu(window)
# window.config(menu=menu_bar)
#
# file_menu = Menu(menu_bar, tearoff=0)
# menu_bar.add_cascade(label="Файл", menu=file_menu)
# file_menu.add_command(label="Загрузить фото", command=open_new_window)
# file_menu.add_separator()
# file_menu.add_command(label="Выход", command=window.destroy)
#
# # Метка "Выбери тег"
# tag_label = Label(window, text="Выбери тег")
# tag_label.pack()
#
# tag_combobox = ttk.Combobox(window, values=ALLOWED_TAGS)
# tag_combobox.pack()
#


window.mainloop()