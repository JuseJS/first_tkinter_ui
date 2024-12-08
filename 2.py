import os
import random
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

### Cargar 10 Imagenes aleatorias ###
def select_images():
    all_image_list = []
    selected_imgs = []

    for archivo in os.listdir(str(dirname)):
      if archivo.endswith(".png"):
        all_image_list.append(archivo)

    while len(selected_imgs) < 10:
      img_name = all_image_list[random.randrange(len(all_image_list))]
      if not img_name in selected_imgs:
          selected_imgs.append(img_name)
    return selected_imgs

### Variables ###
dirname = os.path.dirname(__file__) + '/hiragana'
points = 0
actual_img = 0
selected_images = select_images()


### Root ###
root = tk.Tk()
root.title("Hiragama Game")
root.geometry("400x600")

### Main Frame ###
main_frame = tk.Frame(root,bg="#fad5b7")
main_frame.pack(fill="both", expand=True)


### Show Image ###
def show_img(img):
  img_url = dirname + "/" + img
  img = Image.open(img_url)
  img = img.resize((400, 400))
  photo = ImageTk.PhotoImage(img)
  img_label.config(image=photo)
  img_label.image = photo

### Next Image ###
def next_img():
    global actual_img
    actual_img += 1
    if actual_img < len(selected_images):
        show_img(selected_images[actual_img])
    else:
        img_label.config(text="Final")
        next_btn.config(state=tk.DISABLED)
   

### Start Game ###
img_label = tk.Label(main_frame)
img_label.pack()
show_img(selected_images[0])

next_btn = tk.Button(main_frame, text="Comprobar", command=next_img)
next_btn.pack()

   

root.mainloop()