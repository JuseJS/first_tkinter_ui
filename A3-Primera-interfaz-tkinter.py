import os
import random
import tkinter as tk
from PIL import ImageTk, Image

# Ruta del directorio actual y subcarpeta de imágenes
dirname = os.path.dirname(__file__)
img_home_dir = os.path.join(dirname, 'hiragana')

# Cargar todas las imágenes del directorio
filelist = [f for f in os.listdir(img_home_dir) if f.endswith(".png")]

# Seleccionar 10 imágenes aleatorias de la carpeta sin repetición
selected_imgs = random.sample(filelist, min(len(filelist), 10))
img_num = 0

# Diccionario con las respuestas correctas (suponiendo que el nombre del archivo corresponde a la respuesta)
answers = {img: os.path.splitext(img)[0] for img in selected_imgs}

# Ventana principal
root = tk.Tk()
root.title("Hiragana Game")
root.geometry('500x600')
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.resizable(width=False, height=False)

# Frame principal
main_frame = tk.Frame(root, bg="#007c77")
main_frame.grid(row=0, column=0, sticky="nsew")
main_frame.grid_rowconfigure(0, weight=1)
main_frame.grid_columnconfigure(0, weight=1)

# Variables globales para el juego
user_response = None
user_input = None
correct_answers = 0  # Contador de respuestas correctas


# Función para mostrar la calificación final
def show_score():
    score = correct_answers
    if score < 5:
        grade = "Suspenso 😢"
    elif score == 5:
        grade = "Suficiente 😐"
    elif score == 6:
        grade = "Bien 🙂"
    elif score in [7, 8]:
        grade = "Notable 😃"
    elif score in [9, 10]:
        grade = "Sobresaliente 🤩"

    # Limpiar el frame principal y mostrar la calificación
    for widget in main_frame.winfo_children():
        widget.destroy()

    result_label = tk.Label(main_frame, text=f"Calificación final: {score}/10\n{grade}",
                            font=('Arial 24'), bg="#007c77", fg="#ffffff", wraplength=450, justify="center")
    result_label.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

    print(f"Calificación final: {score}/10 -> {grade}")


# Función para verificar la respuesta y mostrar la siguiente imagen
def open_img():
    global img_num, correct_answers, user_input
    if img_num < len(selected_imgs):
        # Verificar la respuesta anterior si no es la primera imagen
        if img_num > 0:
            user_answer = user_input.get().strip().lower()
            correct_answer = answers[selected_imgs[img_num - 1]].lower()
            if user_answer == correct_answer:
                correct_answers += 1
                print(f"Respuesta correcta: {user_answer}")
            else:
                print(f"Respuesta incorrecta: {user_answer}. Correcta: {correct_answer}")

        # Limpiar el campo de entrada
        user_input.delete(0, tk.END)

        # Cargar y mostrar la imagen actual
        img_url = os.path.join(img_home_dir, selected_imgs[img_num])
        img = Image.open(img_url)
        img = img.resize((400, 400), Image.LANCZOS)
        img = ImageTk.PhotoImage(img)

        panel = tk.Label(main_frame, image=img)
        panel.image = img
        panel.grid(row=0, column=0, sticky="nsew")

        # Imprimir la respuesta para mis test cuando la estaba haciendo
        correct_answer = answers[selected_imgs[img_num]]
        print(f"Respuesta correcta para la imagen {selected_imgs[img_num]}: {correct_answer}")

        img_num += 1
    else:
        # Verificar la última respuesta
        user_answer = user_input.get().strip().lower()
        correct_answer = answers[selected_imgs[img_num - 1]].lower()
        if user_answer == correct_answer:
            correct_answers += 1
            print(f"Respuesta correcta: {user_answer}")
        else:
            print(f"Respuesta incorrecta: {user_answer}. Correcta: {correct_answer}")

        # Mostrar la calificación final
        show_score()


# Función para iniciar el juego
def start_game():
    global img_num, user_response, user_input, correct_answers
    img_num = 0
    correct_answers = 0
    start_btn.destroy()

    # Crear el campo de entrada
    user_response = tk.StringVar()
    user_input = tk.Entry(main_frame, textvariable=user_response, font=('Arial 24'), fg="#ff3cc7", bg="#4c1a57")
    user_input.grid(row=1, column=0, sticky="nsew")

    # Botón para mostrar la siguiente imagen
    next_btn = tk.Button(main_frame,
                         text="Siguiente",
                         bg="#f0f600",
                         font=('Arial 24'),
                         command=open_img)
    next_btn.grid(row=2, column=0, sticky="nsew")

    open_img()


# Botón para iniciar el juego
start_btn = tk.Button(main_frame,
                      text="Iniciar Juego",
                      bg="#f0f600",
                      font=('Arial 24'),
                      command=start_game)
start_btn.grid(row=0, column=0, sticky="nsew")

root.mainloop()
