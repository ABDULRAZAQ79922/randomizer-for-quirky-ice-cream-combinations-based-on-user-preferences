import tkinter as tk
from tkinter import messagebox
import random

myIceCreamFlavors = ['Vanilla', 'Chocolate', 'Strawberry', 'Mint Chip', 'Cookie Dough', 'Coffee']
myToppings = ['Sprinkles', 'Hot Fudge', 'Caramel Sauce', 'Marshmallows', 'Crushed Oreos', 'Gummy Bears']
myMixIns = ['Brownie Bits', 'Cookie Dough Chunks', 'Peanut Butter Cups', 'Rainbow Sprinkles', 'Fruity Pebbles', 'Chopped Nuts']

def generateQuirkyIceCream(flavor_var, topping_var, mix_in_var):
    flavor = random.choice(myIceCreamFlavors) if flavor_var.get() else ''
    topping = random.choice(myToppings) if topping_var.get() else ''
    mix_in = random.choice(myMixIns) if mix_in_var.get() else ''
    
    if flavor or topping or mix_in:
        return f"How about a {flavor} ice cream with {topping} and {mix_in}? 🍦🎉"
    else:
        return "Please select at least one preference."

def saveFavorite():
    favorite_combination = ice_cream_label.cget("text")
    messagebox.showinfo("Saved!", f"Favorite combination saved:\n{favorite_combination}")

def create_gradient_background(canvas, color1, color2):
    width = 500
    height = 300
    for i in range(height):
        ratio = i / height
        color = "#%02x%02x%02x" % (
            int((1 - ratio) * int(color1[1:3], 16) + ratio * int(color2[1:3], 16)),
            int((1 - ratio) * int(color1[3:5], 16) + ratio * int(color2[3:5], 16)),
            int((1 - ratio) * int(color1[5:], 16) + ratio * int(color2[5:], 16))
        )
        canvas.create_line(0, i, width, i, fill=color, width=1)

root = tk.Tk()
root.title("Quirky Ice Cream Randomizer")
root.geometry("500x300")

canvas = tk.Canvas(root, width=500, height=300, highlightthickness=0)
canvas.pack()

create_gradient_background(canvas, "#4e54c8", "#8f94fb")

ice_cream_label = tk.Label(root, text="", font=("Helvetica", 14),  fg="#000000")
ice_cream_label.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

generate_button = tk.Button(root, text="Generate", font=("Helvetica", 12), command=lambda: ice_cream_label.config(text=generateQuirkyIceCream(flavor_var, topping_var, mix_in_var)))
generate_button.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

preferences_label = tk.Label(root, text="Select your preferences:", font=("Helvetica", 12),  fg="#000000")
preferences_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

flavor_var = tk.BooleanVar()
flavor_checkbox = tk.Checkbutton(root, text="Include flavor", variable=flavor_var, font=("Helvetica", 10),  fg="#000000", selectcolor="#4e54c8")
flavor_checkbox.place(relx=0.3, rely=0.55, anchor=tk.CENTER)

topping_var = tk.BooleanVar()
topping_checkbox = tk.Checkbutton(root, text="Include topping", variable=topping_var, font=("Helvetica", 10),  fg="#000000", selectcolor="#4e54c8")
topping_checkbox.place(relx=0.5, rely=0.55, anchor=tk.CENTER)

mix_in_var = tk.BooleanVar()
mix_in_checkbox = tk.Checkbutton(root, text="Include mix-in", variable=mix_in_var, font=("Helvetica", 10), fg="#000000", selectcolor="#4e54c8")
mix_in_checkbox.place(relx=0.7, rely=0.55, anchor=tk.CENTER)

save_button = tk.Button(root, text="Save Favorite", font=("Helvetica", 12), command=saveFavorite)
save_button.place(relx=0.5, rely=0.65, anchor=tk.CENTER)

root.mainloop()
