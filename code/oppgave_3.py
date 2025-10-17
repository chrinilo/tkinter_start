""" a """
import tkinter as tk

root = tk.Tk()
root.title("frame basics")
root.iconbitmap("img/thinking.ico")
root.geometry("400x400")

PackFrame1 = tk.Frame(root, bg="red")
GridFrame1 = tk.Frame(root, bg="blue")
gridFrame2 = tk.LabelFrame(root, text="frame", borderwidth=5)

tk.Label(GridFrame1, text="hello", bg="blue", fg="white").grid(row=1, column=2)

PackFrame1.pack(fill=tk.BOTH, expand=True)
GridFrame1.pack(fill="y", expand=True)
gridFrame2.pack(fill=tk.BOTH, expand=True)

tk.mainloop()
