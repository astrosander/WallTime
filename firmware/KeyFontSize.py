import keyboard
from pynput.mouse import Listener
import ChangeCfg

def Check(CONF_FILE):
    def on_scroll(x, y, dx, dy):
        if keyboard.is_pressed('ctrl'):
            val = ChangeCfg.read_config(CONF_FILE)['WallpaperConfig']['fontsize']

            ChangeCfg.change_config('WallpaperConfig','fontsize', str(int(val)+dy*5), CONF_FILE)

    with Listener(on_scroll=on_scroll) as listener:
        listener.join()


# lol(r'C:\Users\256bit.by\AppData\Local\DataWatch\config.ini')