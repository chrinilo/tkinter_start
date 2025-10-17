""" a """
import tkinter as tk
from tkinter import BOTH

import asyncio
import python_weather


root = tk.Tk()
root.title("label basics")
root.iconbitmap("img/thinking.ico")
root.geometry("400x400")
root.resizable(0, 0)  # type:ignore

def show_tet():
    tk.Label(root,text="hello {name}").grid(row=1,column=0)

async def weather():
    async with python_weather.Client(unit=python_weather.METRIC)as client:
        weather_var = await client.get('Halden')
        tk.Label(root, text= f"det er {weather_var.temperature}℃ ute"). grid(row=5, column=4)
        
def run_weather():
    asyncio.run(weather())


button_1 = tk.Button(root, text="hello world", command=show_tet).grid(row=0,column=0)

button_2 = tk.Button(root, text="weather", command=run_weather).grid(row=4,column= 4)

tk.mainloop()
