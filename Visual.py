import tkinter as tk
from tkinter import ttk
from tkinter import colorchooser
from configparser import ConfigParser
import Calendar
import customtkinter, tkinter
import math
import Thm
from Thm import Themes
import ChangeCfg 
from tkinter import filedialog

# CONF_FILE = f"D:\\coding\\TimerWallpaper\\config.ini"

customtkinter.set_appearance_mode("default")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green


def Settings(CONF_FILE):

    def ColorChooser(f):
        color_code = colorchooser.askcolor(title="Choose text color")

        if(color_code[1] != None):
            if f == 0:
                ChangeCfg.change_config('WallpaperConfig','BackgroundColour', str(color_code[1]), CONF_FILE)
                ChangeCfg.change_config('WallpaperConfig', 'FolderPath', '-', CONF_FILE)
            else:
                ChangeCfg.change_config('WallpaperConfig','textcolour', str(color_code[1]), CONF_FILE)


    def Background_color(): 
        ColorChooser(0)

    def select_file():
        file_path = filedialog.askopenfilename()
        if file_path:
            ChangeCfg.change_config('WallpaperConfig','FolderPath', file_path, CONF_FILE)
            print(file_path)

    def Text_color(): 
        ColorChooser(1)

    def Calend():
        Calendar.lol(CONF_FILE, 0)


    config = ChangeCfg.read_config(CONF_FILE)
    app = customtkinter.CTk()

    check_var = tkinter.IntVar(value=int(config['Date']['base_argument']))

    try:
        app.iconbitmap('icon.ico')
    except:
        pass

    fontsize = config['WallpaperConfig']['fontsize']
    label = customtkinter.CTkLabel(master=app, text="Font size:\n"+fontsize, font=("Sans-serif.ttf", 18))

    def slider_event(value):
        val = math.floor(value)
        label.configure(text="Font size:\n"+str(val))
        ChangeCfg.change_config('WallpaperConfig','fontsize', str(val), CONF_FILE)

    def combobox_callback(choice):
        Thm.Themes(choice, CONF_FILE)

    def app_destroy():
        app.destroy()

    app.minsize(400, 400)
    app.title("Settings")

    h = 40

    def checkbox_event():
        ChangeCfg.change_config('Date','base_argument', str(check_var.get()), CONF_FILE)
    

    button = customtkinter.CTkButton(master=app, text="Color of background", command=Background_color, width=150, height=h, font=("Sans-serif.ttf", 15))
    button.place(relx=0.45, rely=0.2, anchor=customtkinter.CENTER)
    
    button = customtkinter.CTkButton(master=app, text="📂", command=select_file, width=25, height=h, font=("Sans-serif.ttf", 15))
    button.place(relx=0.7, rely=0.2, anchor=customtkinter.CENTER)

    button1 = customtkinter.CTkButton(master=app, text="Color of text", command=Text_color, width=180, height=h, font=("Sans-serif.ttf", 15))
    button1.place(relx=0.5, rely=0.325, anchor=customtkinter.CENTER)

    label.place(relx=0.5, rely=0.45, anchor=customtkinter.CENTER)#0.6

    slider = customtkinter.CTkSlider(master=app, from_=10, to=100, command=slider_event)
    slider.place(relx=0.5, rely=0.525, anchor=customtkinter.CENTER)#0.675
    slider.set(int(fontsize))

    button2 = customtkinter.CTkButton(master=app, text="Change purpose date", command=Calend, width=180, height=h, font=("Sans-serif.ttf", 15))
    button2.place(relx=0.5, rely=0.675, anchor=customtkinter.CENTER)#0.45

    combobox = customtkinter.CTkComboBox(master=app, values=list(Thm.dflt.keys()), command=combobox_callback, fg_color="#30a474", button_color="#30a474", border_color = "#30a474")
    combobox.pack(padx=20, pady=10)
    combobox.set("Themes")  # set initial value

    button3 = customtkinter.CTkButton(master=app, text="Ok", command=app_destroy, width=80, height=h, fg_color=("#F44336"))
    button3.place(relx=0.5, rely=0.925, anchor=customtkinter.CENTER)

    checkbox = customtkinter.CTkCheckBox(master=app, text="Show pensents", command=checkbox_event,
                                         variable=check_var, onvalue=1, offvalue=0)
    checkbox.pack(padx=20, pady=10)
    checkbox.place(relx=0.5, rely=0.775, anchor=customtkinter.CENTER)

    app.mainloop()



# Settings(r'C:\Users\256bit.by\AppData\Local\DataWatch\config.ini')



