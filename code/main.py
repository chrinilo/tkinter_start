""" a """
import tkinter as tk

# from icecream import ic # bruk for å printe variabler.

root = tk.Tk()

root.title("hello")
root.geometry('400x400')

lbl = tk.Label(root, text="hello world!")
lbl.grid()
test_img = tk.PhotoImage(file="img/shield.png")
img_label = tk.Label(root, image=test_img)
img_label.grid()
root.config(background="red")

# root.mainloop()
while root:
    root.update()
    # print("fin")
