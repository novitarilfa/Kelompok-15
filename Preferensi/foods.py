import tkinter as tk
import json
import webbrowser
from random import choice


def load_database():
    with open('foods.json') as file:
        data = json.load(file)
    return data


def choose_food():
    food = choice(foods)
    return food


def open_webpage(url):
    webbrowser.open(url)


def show_random_food():
    food = choose_food()
    window = tk.Toplevel(root)
    window.title(food['name'])

    image_url = food['image']
    lbl_image = tk.Label(window)
    lbl_image.pack()
    lbl_image.bind('<Button-1>', lambda event: open_webpage(image_url))

    lbl_name = tk.Label(window, text=food['name'], font=('Arial', 18, 'bold'))
    lbl_name.pack()

    lbl_description = tk.Label(window, text=food['description'], wraplength=300)
    lbl_description.pack()


root = tk.Tk()
root.title("Random Food Generator")

foods = load_database()

btn_generate = tk.Button(root, text="Generate", font=('Arial', 16), command=show_random_food)
btn_generate.pack(pady=20)

root.mainloop()
