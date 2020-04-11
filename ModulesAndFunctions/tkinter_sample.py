try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter

print(tkinter.TkVersion)
print(tkinter.TclVersion)

mainWindow = tkinter.Tk()
# tkinter._test()   # makes the window pop up

mainWindow.title("Calculator")
mainWindow.geometry('640x480-8-200')
mainWindow.mainloop()   # makes the window pop up
