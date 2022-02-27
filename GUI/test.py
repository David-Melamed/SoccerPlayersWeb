from tkinter import *

def asdf():
    print('test')
tk = Tk()
b = Button(tk, text="test", command=asdf)
b.pack()

tk.mainloop()