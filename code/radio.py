"""
a
"""

import tkinter as tk

root = tk.Tk()
root.title("radio")
root.iconbitmap("img/radio.ico")
root.geometry("400x400")

v = tk.IntVar()

inputFrame = tk.Frame(root, background="blue")

outputFrame = tk.Frame()

values = {"button1": 0, "button2": 1}

for text, value in values.items():
    tk.Radiobutton(
        inputFrame, text=text, value=value, variable=v, indicatoron=False, bg="blue"
    ).grid(row=0, column=value, padx=20)


def PrintOut():
    if v.get() == 1:
        tk.Label(outputFrame, text="du er myndig").pack()
    else:
        tk.Label(outputFrame, text="du er umyndig").pack()
    print("done")

print_button = tk.Button(inputFrame, text="OK", command=PrintOut)

print_button.grid(row=1, column=0, columnspan=2)


inputFrame.pack(pady=20, expand=True)
outputFrame.pack(fill=tk.BOTH, pady=10, expand=True)

print("settup done")

if __name__ == "__main__":
    tk.mainloop()
