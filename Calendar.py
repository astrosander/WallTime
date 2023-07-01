import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
from configparser import ConfigParser
from datetime import datetime
import babel.numbers
import ChangeCfg 


def calculate_time_difference(start_date, end_date):
    date_format = "%Y-%m-%d"  # Format of the dates
    time_difference = datetime.strptime(end_date) - datetime.strptime(start_date)
    return time_difference

def lol(CONF_FILE, f):
    

    def get_date():

        date_obj = datetime.strptime(cal.get_date(), '%m/%d/%y')

        ChangeCfg.change_config('Date','day', str(date_obj.day), CONF_FILE)
        ChangeCfg.change_config('Date','month', str(date_obj.month), CONF_FILE)
        ChangeCfg.change_config('Date','year', str(date_obj.year), CONF_FILE)

        date_obj = date_obj - datetime.today()
        ChangeCfg.change_config('Date','base', str(date_obj.days+1), CONF_FILE)

        root.destroy()

    def work1():
        root.destroy()
        lol(CONF_FILE, 1)

    root = tk.Tk()
    root.geometry("300x300")
    root.title("Calendar")
    
    try:
        root.iconbitmap('icon.ico')
    except:
        pass

    val = ChangeCfg.read_config(CONF_FILE)
    # print(val)

    if(f):
        cal = Calendar(root, selectmode = "day", year = int(datetime.today().year), month = int(datetime.today().month), day = int(datetime.today().day), cursor="hand1")
    else:
        cal = Calendar(root, selectmode = "day", year = int(val['Date']['year']), month = int(val['Date']['month']), day = int(val['Date']['day']), cursor="hand1")

    cal.pack(pady = 20)

    current = ttk.Button(root, text = "Current Date", command = work1)
    current.pack(pady = 10)
    current.place(relx=0.4, rely=0.75)

    date_button = ttk.Button(root, text = "Select!", command = get_date)
    date_button.pack(pady = 10)
    date_button.place(relx=0.4, rely=0.85)

    root.mainloop()


# lol(r'C:\Users\256bit.by\AppData\Local\DataWatch\config.ini', 0)