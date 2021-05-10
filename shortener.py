# importing rewuired modules/libs
from tkinter import *
import pyperclip
import pyshorteners
import tkinter as tk
from tkinter import * 
from tkinter import ttk
from datetime import datetime
from PIL import ImageTk, Image
from tkinter.messagebox import *
import datetime as dt





class shortnr:
    # main window
    __root = Tk()
    __root.geometry("1100x600")
    __root.title("URL Shortener")
    __root.resizable(False,False)
    __background = ImageTk.PhotoImage(Image.open("assets/img/background.png"))
    
    
    def __init__(self):
        self.__txt = StringVar(self.__root,value = "paste url here...")
        self.__short_url = StringVar()
        
        # create canvas
        self.__canvas = Canvas(self.__root, width = 500, height = 500)
        self.__canvas.pack(fill = "both", expand = True)
        self.__canvas.create_image(0,0, image = self.__background, anchor = "nw")
        
        # date
        self.__canvas.create_text(165, 30, text=f'{dt.datetime.now():%a, %d %b %Y}', font=('Cutive Mono',5,'underline'), fill='#FFFFFF')
        
        # ttk themed url entry widget
        self.__url = ttk.Entry(self.__root, width = 30, textvariable = self.__txt, font = ("Cutive Mono", 6))
        self.__url.place(x = 135, y = 180, relheight = 0.12, relwidth = 0.75)
        
        # ttk themed shorten button
        self.__style = ttk.Style()
        self.__style.configure("my.TButton", font = ("Carrois Gothic SC", 4))
        self.__button = ttk.Button(self.__root,text = "shorten", style = "my.TButton", command = self.__shorten_url)
        self.__button.place(x = 827,y = 186, relheight = 0.10)
        
        # configuring ttk themed exit button
        self.__stylebt = ttk.Style()
        self.__style.configure("exit.TButton", font = ("Verdana", 5),foreground = 'red')
        
        # configuring ttk themed info button
        self.__stylebt = ttk.Style()
        self.__style.configure("info.TButton", font = ("Verdana", 5))
  
        # exit and info buttons
        self.__infoButton = ttk.Button(self.__root, text = "!",style = 'info.TButton', command = self.__info).place(x = 930, y = 530, relwidth = 0.05, relheight = 0.09)
        self.__exitButton = ttk.Button(self.__root, text = "X",style = 'exit.TButton', command = self.__Exit).place(x = 1000, y = 530, relwidth = 0.05, relheight = 0.09)
                
    # info function gives functionality to the
    # info button   
    def __info(self):
        showinfo("Info", "\nThis is a simple url shortener program\ndeveloped by RLY0NHEART")
                
      
    # shorten_url function gives functionality to
    # the shorten button        
    def __shorten_url(self):
        try:
            self.__shortener = pyshorteners.Shortener()
            self.__shorturl = self.__shortener.tinyurl.short(self.__txt.get())
            
            # set the global short_url
            self.__short_url.set(self.__shorturl)
            
            # ttk themed output entry widget
            self.__output = ttk.Entry(self.__root, textvariable = self.__short_url, font = ("Cutive Mono", 6))
            self.__output.place(x = 290, y = 350, relwidth = 0.47, relheight = 0.15)
            
            # configuring ttk themed copy url button
            self.__style = ttk.Style()
            self.__style.configure("my.TButton",font = ("Carrois Gothic SC", 4))
            ttk.Button(self.__root, text="copy url", style = "my.TButton", command = self.__copy_url).place(x = 290, y = 443)
        except:
            showerror("Error","\nSomething went wrong, please try again")
    
    
    # copy_url function gives functionality to the
    # copy url button           
    def __copy_url():        
        # copy shortened url to clipboard
        pyperclip.copy(self.__short_url.get())
          
      
    # exit function gives functionality to the exit(X) button          
    def __Exit(self):
        self.__msgBox = askquestion("Exit", "\nAre you sure you want to exit?")
        if self.__msgBox == "yes":
            self.__root.destroy()
            
                                      
    def run(self):
        self.__root.mainloop()
        
program = shortnr()
program.run()