"""a"""

import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()
root.title("label basics")
root.iconbitmap("img/thinking.ico")
root.geometry("400x400")
root.resizable(True, True)


def img_gen(img: str):
    """makes images compatible with tkinter"""
    return ImageTk.PhotoImage(Image.open(img).resize((300, 300)))


image_list = [
    img_gen("img/filmplakat.png"),
    img_gen("img/Screenshot 2025-04-24 114740.png"),
    img_gen("img/cat_icon.png"),
    img_gen("img/cat.jpg")
]


def show_image(image_index: int = 0):
    """shows image"""
    for w in root.winfo_children():
        if isinstance(w, tk.Button):
            w.destroy()
    try:
        tk.Button(
                root, text="cat", image=image_list[image_index],
                command=lambda: show_image(image_index+1)
            ).pack()
        tk.Button(root, text="back", command=lambda:show_image(image_index-1)).pack()
    except IndexError:
        if image_index <=0:
            show_image(3)
        else:
            show_image(0)
    # if turn:
    #     cat_lable_2 = tk.Button(
    #         root, text="cat", image=your_image, command=lambda: show_image(False)
    #     )
    #     cat_lable_2.pack()
    # if turn is False:
    #     cat_lable = tk.Button(
    #         root, text="cat", image=my_image, command=lambda: show_image(True)
    #     )
    #     cat_lable.pack()


but_1 = tk.Button(root, text="show image", command=show_image)
but_1.pack()

root.mainloop()
