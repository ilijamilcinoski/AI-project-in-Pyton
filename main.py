From tkinter import *
from tkinter import ttk 

splash_win =Tk()
splash_win_title("This is a splash screen")
splash_win.geometry("620x350+420+200")
splash_win.config(bg="1a1a1a")

#remove border or splash screen/window
splash_win_overrideredirect(True)

splash_label= Label(splash_win, text="Welcome to the Future of AI") bg="1a1a1a", fg="white",
font=("times new roman",30))) .place(x=0, y=40, relwidth=1) 
splash_label =Label(splash_win, text="Redefining Posibilites...", bg="1a1a1a", fg="#e6e6e6",)
font=("times new roman",15))) .place(x=280, y=100)

def getstarted():
    loading=Label(splash_win, text="Loading...") bg="1a1a1a, fg=#e6e6e6",
    font("verdana",15))).place(x=50, y=270)

    progress= ttk.Progressbar(splash_win, orient=HORIZONTAL, Length=520)
    progress.place(x=50, y=300)
    progress.config(mode="indeterminate")
    progress.start()
    splash_win.after(4000, calling_mainwin)
    BTNGetStarted= Button(splash_win, text="Get Started...", font="vardana",12)
    fg="white" bd=0, command=GetStarted, width=20) .place(x=40, y=210)

    def= calling_mainwin():
     splash_win.destroy()
     import landing_page

     mainloop()
     