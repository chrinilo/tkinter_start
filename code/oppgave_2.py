""" a """
import tkinter as tk
from tkinter import BOTH

root = tk.Tk()
root.title("label basics")
root.iconbitmap("img/thinking.ico")
root.geometry("400x400")
root.resizable(0, 0)  # type:ignore
root.config(bg="green")

name_label_1 = tk.Label(root, text="hello world 1")
name_label_1.pack()

name_label_2 = tk.Label(root, text="hello world 2", font=("Ariel", 18, "bold"))
name_label_2.pack()

name_label_3 = tk.Label(root, text="hello world 3", font=("Ariel", 18), bg="blue")
name_label_3.pack(padx=20, pady=70)

name_label_4 = tk.Label(
    root, text="hello world 4", font=("Ariel", 18), bg="red", fg="blue"
)
name_label_4.pack(pady=(50, 50), ipadx=50, anchor="w")

name_label_5 = tk.Label(
    root, text="hello world 5", font=("Ariel", 18), bg="blue", fg="#123456"
)
name_label_5.pack(fill=BOTH, expand=True)

tk.mainloop()
