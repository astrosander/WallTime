import tkinter as tk
from tkinter import ttk
from tkinter import colorchooser
from configparser import ConfigParser
import Calendar
import customtkinter, tkinter
import math

CONF_FILE = f"D:\\coding\\TimerWallpaper\\config.ini"
config = ConfigParser()


def SetData(sss, f):
    global config
    config.read(CONF_FILE)

    if f == 1:
        config.set('WallpaperConfig','textcolour', sss)
    elif f == 2:
        config.set('WallpaperConfig','fontsize', sss)
    else: 
        config.set('WallpaperConfig','BackgroundColour', sss)

    with open(CONF_FILE, 'w') as configfile:
        config.write(configfile)

def ColorChooser(f):
    color_code = colorchooser.askcolor(title="Choose text color")

    if(color_code[1] != None):
        SetData(str(color_code[1]), f)


def Background_color(): ColorChooser(0)
def Text_color(): ColorChooser(1)

def Calend():
    Calendar.lol(CONF_FILE)




customtkinter.set_appearance_mode("default")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green


def Settings(CONF1_FILE):

    global CONF_FILE, amount_label
    CONF_FILE=CONF1_FILE

    config.read(CONF_FILE)

    app = customtkinter.CTk()

    try:
        app.iconbitmap('icon.ico')
    except:
        pass

    fontsize = config['WallpaperConfig']['fontsize']

    label = customtkinter.CTkLabel(master=app,text="Font size:\n"+fontsize, font=("Sans-serif.ttf", 18))
   

    def slider_event(value): 
        val = math.floor(value)
        label.configure(text="Font size:\n"+str(val))
        SetData(str(val), 2)

    def AppDestroy():
        app.destroy()
    
    app.minsize(400,400)
    app.title("Settings")

    h = 40

    label.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

    button = customtkinter.CTkButton(master=app, text="Color of background", command=Background_color, width=180, height = h, font=("Sans-serif.ttf", 15))
    button.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)

    button1 = customtkinter.CTkButton(master=app, text="Color of text", command=Text_color, width=180, height = h, font=("Sans-serif.ttf", 15))
    button1.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

    button2 = customtkinter.CTkButton(master=app, text="Change purpose date", command=Calend, width=180, height = h, font=("Sans-serif.ttf", 15))
    button2.place(relx=0.5, rely=0.45, anchor=tkinter.CENTER)

    slider = customtkinter.CTkSlider(master=app, from_=10, to=100, command=slider_event)
    slider.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)
    slider.set(int(fontsize))

    # print(inverse_color("#8c2358"))

    button3 = customtkinter.CTkButton(master=app, text="Ok", command=AppDestroy, width=80, height = h,fg_color=("#8c2358"))
    button3.place(relx=0.5, rely=0.85, anchor=tkinter.CENTER)

    app.mainloop()


# Settings(r'C:\Users\256bit.by\AppData\Local\DataWatch\config.ini')
