import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()
root.title("label basics")
root.iconbitmap("img/thinking.ico")
root.geometry("400x400")
root.resizable(True, True)

COLOUR1 = "#31B75B"
COLOUR2 = "#60BB7B"
COLOUR3 = "#6ED182"
COLOUR4 = "#72E276"


def submit_name():
    # TODO make somthing.
    return


inputframe = tk.LabelFrame(root, bg=COLOUR1)
inputframe.pack()

outputframe = tk.LabelFrame(root, bg=COLOUR4)
outputframe.pack()

name = tk.Entry(inputframe)
name.grid(row=0, column=0, padx=10)

submit_button = tk.Button(inputframe, text="submit", command=submit_name)
submit_button.grid(row=0, column=1, padx=(0, 10), pady=5)
img = Image.open("img/cat_icon.png")

datas = img.getdata()

newData = []
for item in datas:
    if item[0] == 255 and item[1] == 255 and item[2] == 255:
        newData.append((1, 0, 0, 0))
    else:
        newData.append(item)

# img = img.putdata(newData)

tkimg1 = ImageTk.PhotoImage(img)

img_lable = tk.Label(outputframe, image=tkimg1)
img_lable.pack(padx=20, pady=20)

root.mainloop()
