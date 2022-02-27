import os
import threading
import time
import tkinter as tk
import webbrowser
from tkinter import *

from PIL import ImageTk

root = Tk()


class buttons:
    def run_server(self):
        os.chdir("../SoccerPlayers/")
        os.system("py .\manage.py makemigrations")
        time.sleep(2)
        os.system("py .\manage.py migrate --run-syncdb")
        time.sleep(2)
        os.system("py .\manage.py runserver")

    def __init__(self, master):
        self.canvas = tk.Canvas(root, height=700, width=100, bg="#202020")
        frame = Frame(master)

        # Define buttons
        self.startAppButton = Button(frame, text="Run Website", fg="blue",
                                     command=threading.Thread(target=self.run_server).start)
        self.startAppButton.grid(column=1, row=1)

        self.loadDataButton = Button(frame, text="Load Data", fg="blue",
                                     command=self.load_data)
        self.loadDataButton.grid(column=2, row=1)

        self.startOpenBrowser = Button(frame, text="Open Browser", fg="blue",
                                       command=self.open_broswer)
        self.startOpenBrowser.grid(column=3, row=1)

        self.startExAppButton = Button(frame, text="Run External Application", fg="blue", command=self.runExtrApp)
        self.startExAppButton.grid(column=4, row=1)

        self.quitApp = Button(frame, text="Quit", fg="blue", command=root.destroy)
        self.quitApp.grid(column=10, row=1)

        label = tk.Label(root, text="Soccer Teams GUI", font="Helvetica 18 bold", fg="blue")
        label.pack(padx=80, pady=80)

        frame.pack()

    def load_data(self):
        os.chdir("../SoccerPlayers/")
        os.system(" .\MySQL_data_insert.py")

    # def kill_process(self):
    #     for proc in process_iter():
    #         for conns in proc.connections(kind='inet'):
    #             if conns.laddr.port == 8080:
    #                 proc.send_signal(SIGTERM)

    def open_broswer(self):
        url = 'http://localhost:8080'
        webbrowser.open_new(url)

    def runExtrApp(self):
        os.chdir("../external_application/")
        os.system("py  .\data_manipulation.py")
        file = ""
        with open("../external_application/external_app_results.txt", "r") as output:
            data = output.readlines()
            for x in data:
                file = file + x
            self.canvas = Canvas(root, width=600, height=200, bg="White", bd=0, highlightthickness=0)
            self.canvas.create_text(0, 0, text=file, fill="black", font=("Purisa", 8), anchor="nw")
            self.canvas.pack()


root.geometry("800x600")
root.tk.call('tk', 'scaling', 2.0)



photo = ImageTk.PhotoImage(file="./assets/GuiMain.jpg")
img_label = tk.Label(root, image=photo)
img_label.image = photo
img_label.place(x=0, y=0, relwidth=1, relheight=1)

my_gui = buttons(root)

root.mainloop()
