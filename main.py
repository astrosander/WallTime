import keyboard
from pynput.mouse import Listener

def on_scroll(x, y, dx, dy):
    if keyboard.is_pressed('ctrl'):
        print(f"Mouse scrolled at ({x}, {y}) with delta ({dx}, {dy}) while ctrl key is pressed")

with Listener(on_scroll=on_scroll) as listener:
    listener.join()
