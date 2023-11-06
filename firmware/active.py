import psutil
import win32gui
import win32process

def is_desktop_active(APP_NAME):
    hwnd = win32gui.GetForegroundWindow()
    if hwnd == 0:
        # no window is currently active, so assume the desktop is active
        return True
    else:
        process_id = win32process.GetWindowThreadProcessId(hwnd)[1]
        process_name = psutil.Process(process_id).name()
        
        # with open('filename.txt', mode='a') as file:
        #     file.write('\n'+process_name + ' ' + APP_NAME)
        # print(process_name + ' ' + APP_NAME)

        if process_name == 'explorer.exe' or process_name.split('.')[0] == APP_NAME or process_name == 'python.exe':
            # the active window belongs to the explorer process, so assume the desktop is active
            return True
    return False

# is_desktop_active()