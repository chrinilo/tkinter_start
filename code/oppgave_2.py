"""a"""

import tkinter as tk


import asyncio
import python_weather


root = tk.Tk()
root.title("label basics")
root.iconbitmap("img/thinking.ico")
root.geometry("400x400")
root.resizable(0, 0)  # type:ignore

name = tk.StringVar()

def show_tet(_name):
    """a"""
    tk.Label(root, text=f"hello {_name}").grid(row=2, column=0)

async def weather():
    """a"""
    async with python_weather.Client(unit=python_weather.METRIC) as client:
        weather_var = await client.get("Halden")
        tk.Label(root, text=f"det er {weather_var.temperature}℃ ute").grid(
            row=5, column=4
        )

def run_weather():
    """a"""
    asyncio.run(weather())

tk.Entry(root, textvariable=name, bg="#00ff40").grid(row=0, column=0)

tk.Button(root, text="hello world", command=lambda: show_tet(name.get())).grid(
    row=1, column=0
)

tk.Button(
    root, text="weather(fryser programmet litt)", command=lambda: asyncio.run(weather())
).grid(row=4, column=4)

tk.mainloop()
