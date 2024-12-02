import tkinter as tk # for the grafical user GUI
from time import strftime

root = tk.Tk()
root.title("Sandy's Digital Clock")

def time():
    string = strftime("%H:%M:%S %p \n %D")
    label.config(text=string)
    label.after(1000,time)

label = tk.Label(root, font=('clibri', 50, 'bold'), background='blue', foreground='black')
label.pack(anchor='center')

time()

root.mainloop()