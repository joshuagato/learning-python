try:
    import tkinter
except ImportError:  # python 2
    import tkinter as tkinter


def parabola(page, size):
    for x in range(-size, size + 1):
        y = x * x / size
        plot(page, x, -y)
        # plot(page, x, y)


def parabola2(page, size):
    for x in range(-size, size + 1):
        y = 2 * x * x / size
        plot(page, x, -y)


# TODO: PLOT THE GRAPH OF A CIRCLE => LESSON 097


def draw_axes(canvaspage):
    canvaspage.update()
    x_origin = canvaspage.winfo_width() / 2
    y_origin = canvaspage.winfo_height() / 2
    canvaspage.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    canvaspage.create_line(-x_origin, 0, x_origin, 0, fill="black")
    canvaspage.create_line(0, y_origin, 0, -y_origin, fill="black")
    print(locals())


def plot(canvaspage, x, y):
    canvaspage.create_line(x, y, x + 1, y + 1, fill="red")
    # canvaspage.create_line(x, y, x + 1, -y + 1, fill="red")


mainWindow = tkinter.Tk()

mainWindow.title("Parabola")
mainWindow.geometry("640x480")

canvas = tkinter.Canvas(mainWindow, width=320, height=480)
canvas.grid(row=0, column=0)

canvas2 = tkinter.Canvas(mainWindow, width=320, height=480, background="lightblue")
canvas2.grid(row=0, column=1)

print(repr(canvas), repr(canvas2))

draw_axes(canvas)
draw_axes(canvas2)

parabola(canvas, 100)
parabola(canvas, 200)
# parabola2(canvas2, 100)

mainWindow.mainloop()
