import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
from configparser import ConfigParser
from datetime import datetime
import babel.numbers


def lol(CONF_FILE):
    config = ConfigParser()
    config.read(CONF_FILE)
    
    def get_date():

        date_obj = datetime.strptime(cal.get_date(), '%m/%d/%y')

        # config.set('WallpaperConfig','date', f"{str(date_obj.year)}, {str(date_obj.month)}")

        config.set('Date','day', str(date_obj.day))
        config.set('Date','month', str(date_obj.month))
        config.set('Date','year', str(date_obj.year))

        with open(CONF_FILE, 'w') as configfile:
            config.write(configfile)

        print(cal.get_date())
        root.destroy()



    root = tk.Tk()
    root.geometry("300x300")
    root.title("Calendar")
    try:
        root.iconbitmap('icon.ico')
    except:
        pass

    cal = Calendar(root, selectmode = "day", year = 2023, month = 5, day = 2, cursor="hand1")
    cal.pack(pady = 20)

    date_button = ttk.Button(root, text = "Get Date", command = get_date)
    date_button.pack(pady = 10)

    # date_label = tk.Label(root, text = "")
    # date_label.pack(pady = 10)

    root.mainloop()


# lol(r'C:\Users\256bit.by\AppData\Local\DataWatch\config.ini')