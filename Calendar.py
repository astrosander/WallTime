import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
from configparser import ConfigParser
from datetime import datetime
import babel.numbers
import ChangeCfg 


def lol(CONF_FILE):

    def get_date():

        date_obj = datetime.strptime(cal.get_date(), '%m/%d/%y')

        ChangeCfg.change_config('Date','day', str(date_obj.day), CONF_FILE)
        ChangeCfg.change_config('Date','month', str(date_obj.month), CONF_FILE)
        ChangeCfg.change_config('Date','year', str(date_obj.year), CONF_FILE)

        root.destroy()


    root = tk.Tk()
    root.geometry("300x300")
    root.title("Calendar")
    
    try:
        root.iconbitmap('icon.ico')
    except:
        pass

    val = ChangeCfg.read_config(CONF_FILE)
    # print(val)

    cal = Calendar(root, selectmode = "day", year = int(val['Date']['year']), month = int(val['Date']['month']), day = int(val['Date']['day']), cursor="hand1")
    cal.pack(pady = 20)

    date_button = ttk.Button(root, text = "Get Date", command = get_date)
    date_button.pack(pady = 10)

    root.mainloop()


# lol(r'C:\Users\256bit.by\AppData\Local\DataWatch\config.ini')