import os, sys
import time
import ctypes
import datetime
from PIL import Image, ImageDraw, ImageFont
import PIL.Image
from configparser import ConfigParser
import Create, Visual
import pystray
import threading
import winreg as reg

THIS_FILE = os.path.abspath(__file__)
THIS_FILE_NAME = os.path.basename(THIS_FILE)
USER_PATH = os.path.expanduser('~')
DATAWATCH_PATH = os.path.join(USER_PATH, 'AppData', 'Local', 'DataWatch')
CONF_FILE = os.path.join(DATAWATCH_PATH, 'config.ini')

SPI_SETDESKWALLPAPER = 20
BackgroundColour = '#000000'
TextColour = "#ffffff"
day=23
month=12
year=2040
FONT = ImageFont.truetype('arial.ttf', 36)


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

try:
    img = Image.open(resource_path("icon.png"))
    # img = Image.open("icon.png")
except:
    pass

key = reg.OpenKey(reg. HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Run", 0, reg.KEY_ALL_ACCESS) 
reg.SetValueEx(key, "DateTime01", 0, reg.REG_SZ, sys.argv[0])


if not os.path.exists(DATAWATCH_PATH):
    os.makedirs(DATAWATCH_PATH)

if not os.path.exists(CONF_FILE):

    Create.crt(CONF_FILE)
    Visual.Settings(CONF_FILE)



def UpdateDate():
    config = ConfigParser()
    config.read(CONF_FILE)
    global BackgroundColour, TextColour, day, year, month

    BackgroundColour = config['WallpaperConfig']['BackgroundColour']
    TextColour = config['WallpaperConfig']['TextColour']
    day = int(config['Date']['day'])
    year = int(config['Date']['year'])
    month = int(config['Date']['month'])
    global FONT
    FONT = ImageFont.truetype('arial.ttf', int(config['WallpaperConfig']['fontsize']))



def get_remaining_time():
    target_date = datetime.datetime(year, month, day) # set your aim
    remaining_time = target_date - datetime.datetime.now()

    days = remaining_time.days
    hours, rem = divmod(remaining_time.seconds, 3600)
    minutes, seconds = divmod(rem, 60)

    return f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds"

def create_image():
    # global BackgroundColour, TextColour, day, year, month

    UpdateDate()

    image = Image.new('RGB', (1920, 1080), color=(BackgroundColour))
    draw = ImageDraw.Draw(image)
    text = get_remaining_time()
    text_width, text_height = draw.textsize(text, FONT)
    x = (image.width - text_width) // 2
    y = (image.height - text_height) // 2
    draw.text((x, y), text, fill=(TextColour), font=FONT)
    
    path = f"{DATAWATCH_PATH}/Wallpaper.png"

    image.save(path)
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 0)


def default_function():
    Visual.Settings(CONF_FILE)

f = 1

icon = pystray.Icon(name="Date", icon=img, title="Date", menu=pystray.Menu(
    pystray.MenuItem(text="Settings", action=default_function, default=True),
    pystray.MenuItem("Exit", default_function)
))


def Exit():
    global f
    f = 0
    icon.stop()


icon = pystray.Icon(name="Date", icon=img, title="Date", menu=pystray.Menu(
    pystray.MenuItem(text="Settings", action=default_function, default=True),
    pystray.MenuItem("Exit", Exit)
))



# icon = pystray.Icon(name="Date",icon=img,title="Date",menu=pystray.Menu(
#     pystray.MenuItem(text="Settings",action=default_function,default=True),
#     pystray.MenuItem(text="Exit",action=Exit,default=True)
# ))

from threading import Thread


def process1():
    while f:
        create_image()
        time.sleep(1)

def process2():
    icon.run()


if __name__ =="__main__":
    
    t1 = threading.Thread(target=process1)
    t2 = threading.Thread(target=process2)

    t1.start()
    t2.start()
 
    t1.join()
    t2.join()