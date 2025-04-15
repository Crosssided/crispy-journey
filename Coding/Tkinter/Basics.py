import tkinter as tk

window = tk.Tk()
window.geometry("600x400")
window.title("Basics")

window.rowconfigure(5, weight=1, minsize=50)
window.columnconfigure(5, weight=1, minsize=50)

label = tk.Label(window, text="Label", font=("Arial", 20))
# Display methods: pack, grid, place
label.grid(row=0, column=0)

label2 = tk.Label(window, text="Label 2", font=("Arial", 20))
label2.grid(row=0, column=1)

def Buttonfunc():
    print("button function")

button = tk.Button(window, text="Button", width=10, height=5, command=Buttonfunc)
button.grid(row=1, column=0)

# Option 2 for button using lambda

def secondfunc():
    label.config(text="Button clicked")

button2 = tk.Button(window, text="Button2", width=10, height=5, command=secondfunc)
button2.grid(row=3, column=0)


window.mainloop()