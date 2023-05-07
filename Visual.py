import tkinter as tk
from tkinter import ttk
from tkinter import colorchooser
from configparser import ConfigParser
import Calendar
import customtkinter, tkinter
import math
import Thm
from Thm import Themes 

CONF_FILE = f"D:\\coding\\TimerWallpaper\\config.ini"
config = ConfigParser()


def SetData(sss, f):
    global config
    config.read(CONF_FILE)

    # print(CONF_FILE)
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

def Settings(conf_file):
    global CONF_FILE
    CONF_FILE = conf_file
    # config = customtkinter.ConfigParser()
    config.read(CONF_FILE)

    app = customtkinter.CTk()
    try:
        app.iconbitmap('icon.ico')
    except:
        pass

    fontsize = config['WallpaperConfig']['fontsize']
    label = customtkinter.CTkLabel(master=app, text="Font size:\n"+fontsize, font=("Sans-serif.ttf", 18))

    def slider_event(value):
        val = math.floor(value)
        label.configure(text="Font size:\n"+str(val))
        SetData(str(val), 2)

    def app_destroy():
        app.destroy()

    app.minsize(400, 400)
    app.title("Settings")

    h = 40

    label.place(relx=0.5, rely=0.625, anchor=customtkinter.CENTER)

    button = customtkinter.CTkButton(master=app, text="Color of background", command=Background_color, width=180, height=h, font=("Sans-serif.ttf", 15))
    button.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)

    button1 = customtkinter.CTkButton(master=app, text="Color of text", command=Text_color, width=180, height=h, font=("Sans-serif.ttf", 15))
    button1.place(relx=0.5, rely=0.325, anchor=customtkinter.CENTER)

    button2 = customtkinter.CTkButton(master=app, text="Change purpose date", command=Calend, width=180, height=h, font=("Sans-serif.ttf", 15))
    button2.place(relx=0.5, rely=0.45, anchor=customtkinter.CENTER)

    slider = customtkinter.CTkSlider(master=app, from_=10, to=100, command=slider_event)
    slider.place(relx=0.5, rely=0.725, anchor=customtkinter.CENTER)
    slider.set(int(fontsize))

    def combobox_callback(choice):
        Themes(choice, CONF_FILE)

    combobox = customtkinter.CTkComboBox(master=app, values=list(Thm.dflt.keys()), command=combobox_callback, fg_color="#30a474", button_color="#30a474", border_color = "#30a474")
    combobox.pack(padx=20, pady=10)
    combobox.set("Themes")  # set initial value

    button3 = customtkinter.CTkButton(master=app, text="Ok", command=app_destroy, width=80, height=h, fg_color=("#F44336"))
    button3.place(relx=0.5, rely=0.875, anchor=customtkinter.CENTER)

    app.mainloop()



# Settings(r'C:\Users\256bit.by\AppData\Local\DataWatch\config.ini')



