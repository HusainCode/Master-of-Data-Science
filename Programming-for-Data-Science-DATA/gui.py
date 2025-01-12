# this is the GUI.py

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import cv2
import os
from tkinter import PhotoImage


class SignLanguageInterpreter:
    def __init__(self):

        # # Initialize the Tkinter
        self.root = tk.Tk()

        # Set the GUI size, width and height
        self.root.geometry('1000x800')
        # Set the GUI title
        self.root.title("Sign Language Interpreter")
        # path for sign language images
        # It is stored in my local machine
        # We can also use Kaggle API however I find this more convenient
        self.images_path = (r'E:\Documents\King Of The Software Engineers\ML\DATA 5100 Programming for Data '
                            r'Science\Final Porject\archive\asl_alphabet_train\asl_alphabet_train')

        self.make_widgets()
        # Change the background color
        self.root.configure(bg="lightgreen")
        # Tinker logo
        # Credit  due to https://www.flaticon.com/search?word=Sign%20Language
        self.root.iconphoto(True, PhotoImage(file="sign-language.png"))

    def make_widgets(self):

        self.text_input = tk.Entry(self.root, width=50, font=('Comic Sans MS', 14))
        self.input_label = tk.Label(self.root, text="Translate Text:", font=('Comic Sans MS', 14))

        self.text_input.pack(pady=11)
        self.input_label.pack(pady=11)

        # Translate button, assigning job to the buttons
        self.btn_translate = (tk.Button
            (
            self.root,
            text="Translate",
            command=self.translation,
            font=('Comic Sans MS', 14)
        ))
        self.btn_translate.pack(pady=11)

        self.image_frame = tk.Frame(self.root)
        self.image_frame.pack(pady=22, expand=True, fill='both')

    def translation(self):
        # Clear the cash images
        for widget in self.image_frame.winfo_children():
            widget.destroy()

        text = self.text_input.get().upper()
        row = tk.Frame(self.image_frame)
        row.pack()

        for i, c in enumerate(text):
            if c == c.isspace():

                image_path = os.path.join(self.images_path, 'space')
            elif c.isalpha():

                image_path = os.path.join(self.images_path, c)
            else:
                continue

            # Find the first images
            try:
                image_file = os.listdir(image_path)[0]
                image_path = os.path.join(image_path, image_file)

                # Load the images
                img = Image.open(image_path)
                # adjust for display
                img = img.resize((95, 95))
                img = ImageTk.PhotoImage(img)

                # Make the label then display the images
                lbl = tk.Label(row, image=img)
                lbl.image = img
                lbl.pack(side=tk.LEFT, padx=5)

                # make a new row for every 5 characters
                if (i + 1) % 5 == 0:
                    row = tk.Frame(self.image_frame)
                    row.pack()

            except Exception as e:
                print(f"Failed to load image for the {c}: {e}")

    def start(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = SignLanguageInterpreter()
    app.start()
