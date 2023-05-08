import psutil
import win32gui
import win32process

def is_desktop_active():
    hwnd = win32gui.GetForegroundWindow()
    if hwnd == 0:
        # no window is currently active, so assume the desktop is active
        return True
    else:
        process_id = win32process.GetWindowThreadProcessId(hwnd)[1]
        process_name = psutil.Process(process_id).name()
        
        if process_name == 'explorer.exe' or process_name == 'python.exe':
            # the active window belongs to the explorer process, so assume the desktop is active
            return True
    return False