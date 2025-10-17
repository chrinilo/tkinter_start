""" a """
import tkinter as tk

root = tk.Tk()
root.title("window basics")
root.iconbitmap("img/shield.png")
root.geometry("250x700")
root.resizable(0, 0)  # type: ignore : ingnorerer erroren som jeg sår på linjen
root.config(bg="blue")

top = tk.Toplevel()
top.title("second window")
top.config(bg="#123456")
top.geometry("200x200+500+50")

tk.mainloop()
