from tkinter import *
import customtkinter
from tkinter import messagebox
from contextlib import redirect_stdout
import io

def console():
     win = Tk()
     win.geometry("400x300")
     win.title("Python Code Compiler")
     
     try:
          win.iconbitmap('icon.ico')
     except:
          pass

     back = '#b06f2e'

     text= Text(win, width= 50, height= 30, background="#303841",
          foreground="white",font= ('monkai', 14), insertbackground = "#f2a659")

     text.insert(INSERT, "import TimerWallpaper\nprint(TimerWallpaper.CONF_FILE)")
     text.pack(expand= 1, fill= BOTH)

     def helloCallBack():
          try:
               f = io.StringIO()
               with redirect_stdout(f):
                    exec(text.get("1.0",END))

               messagebox.askquestion('Info', f.getvalue())

          except Exception as e:
               messagebox.showerror('Python Error', 'Error: '+str(e))

     button2 = customtkinter.CTkButton(master=win, text="Compile!", command=helloCallBack, width=100, font=("Sans-serif.ttf", 15), corner_radius = 0, border_color = back, hover_color=back, fg_color = back)
     button2.place(relx=0.5, rely=0.78, anchor=customtkinter.CENTER)

     button2 = customtkinter.CTkButton(master=win, text="Exit!", command=win.destroy, width=100, font=("Sans-serif.ttf", 15), corner_radius = 0, border_color = back, hover_color=back, fg_color = back)
     button2.place(relx=0.5, rely=0.9, anchor=customtkinter.CENTER)


     win.mainloop()
