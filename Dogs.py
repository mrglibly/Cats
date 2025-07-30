from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO


def get_dog_image():
    try:
        response = requests.get('https://dog.ceo/api/breeds/image/random')
        response.raise_for_status()
        data = response.json()
        return data['message']
    except Exception as e:
        messagebox.showerror('Error!', f'Image Load Error occurred: {e}.')
        return None


def show_image():
    img_url = get_dog_image()
    if img_url:
        try:
            response = requests.get(img_url, stream=True)
            response.raise_for_status()
            img_data = BytesIO(response.content)
            img = Image.open(img_data)
            img_size = (int(width_spinbox.get()), int(height_spinbox.get()))
            img.thumbnail(img_size, Image.Resampling.LANCZOS)
            img = ImageTk.PhotoImage(img)
            new_window = Toplevel()
            new_window.title('Randon image')
            lb = ttk.Label(new_window, image=img)
            lb.pack()
            lb.image = img
        except Exception as e:
            messagebox.showerror('Error!', f'The Error occurred {e}.')
        progress_b.stop()

def prog():
    progress_b['value'] = 0
    progress_b.start(30)
    window.after(3000, show_image)

window = Tk()
window.title("Dogy Pictures!")
window.geometry("360x420")

label = ttk.Label()
label.pack()

button = ttk.Button(text='Загрузить фото', command=prog)
button.pack(pady=10)

progress_b = ttk.Progressbar(mode='determinate',length=300)
progress_b.pack(pady=10)

width_label = ttk.Label(text='Width')
width_label.pack(side='left', padx=(10,0 ))
width_spinbox = ttk.Spinbox(from_=200, to=500, increment=50, width=5)
width_spinbox.pack(side='left', padx=(0, 10))

height_label = ttk.Label(text='Height')
height_label.pack(side='left', padx=(10,0 ))
height_spinbox = ttk.Spinbox(from_=200, to=500, increment=50, width=5)
height_spinbox.pack(side='left', padx=(0, 10))


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