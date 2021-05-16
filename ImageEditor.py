from main import Main
from tkinter import messagebox as msg

root = Main()

def on_close():
    if msg.askyesno("Quit", "Do You want to Quit?"):
        root.destroy()

root.protocol("WM_DELETE_WINDOW", on_close)
root.mainloop()
