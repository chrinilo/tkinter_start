"""
a
"""
import tkinter as tk

root = tk.Tk()
root.title("frame basics")
root.iconbitmap("img/thinking.ico")
root.geometry("400x400")

tekst =tk.StringVar()

def teller(x):
    """a"""
    x+=1
    tk.Label(root, text=x).pack()
    return x


txt_box_1 = tk.Entry(root,show="*", textvariable=tekst)
txt_box_1.pack(padx=(10,10),pady=(50,20))

tk.Label(root, textvariable=tekst).pack()

butt = tk.Button(root, text="hello", command=lambda:teller(3))
butt.pack()

tk.mainloop()
