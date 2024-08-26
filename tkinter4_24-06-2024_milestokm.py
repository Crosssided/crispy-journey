import tkinter as tk
from tkinter import ttk

# Button action convert
def convert_action():
    it = entryInt.get()
    outputstr.set(it*1.6)


# Set up window and geometry
window = tk.Tk()
window.geometry("400x250")

# Label 1
title = ttk.Label(master=window, font="Calibri 24 bold", text="Miles to Km")
title.pack()

# input frame
inputFrame = ttk.Frame(master=window)
entryInt = tk.IntVar()
entry = ttk.Entry(master=inputFrame, textvariable=entryInt)

inputFrame.pack()
entry.pack(side='left')

# Buttons
convert = ttk.Button(master=inputFrame, text="convert", command=convert_action)
convert.pack(side='right')

# Output
output_title = ttk.Label(master=window, text="Output", font="Calibri 18 bold")
output_title.pack()

outputstr = tk.StringVar()
output = ttk.Label(master=window, font="Calibri 16", textvariable=outputstr)
output.pack()
entry.delete(0)

# mainloop
window.mainloop()