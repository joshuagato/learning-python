try:
    import tkinter
except ImportError:  # python 2
    import tkinter as tkinter


def parabola(x):
    y = x * x
    return y


mainWindow = tkinter.Tk()
mainWindow.title("Parabola")
mainWindow.geometry("640x480")
canvas = tkinter.Canvas(mainWindow, width=640, height=480)
canvas.grid(row=0, column=0)


for x in range(-100, 101):
    y = parabola(x)
    print("x:{} ==> y:{}".format(x, y))


mainWindow.mainloop()
