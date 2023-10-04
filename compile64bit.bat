echo off

pyinstaller --onedir --noconfirm --onefile --windowed --icon "icon.ico" --add-data "C:/Users/256bit.by/AppData/Local/Programs/Python/Python310/Lib/site-packages/customtkinter;customtkinter/" --add-data "icon.ico;." --add-data "icon.png;."  "TimerWallpaper.py"

rmdir /s /q __pycache__
rmdir /s /q build

:cmd
pause null