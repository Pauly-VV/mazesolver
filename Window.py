from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.root = Tk()
        self.root.title("Window")
        self.root.geometry(f"{width}x{height}")
        self.root.protocol("WM_DELETE_WINDOW", self.close)

        self.canvas = Canvas(self.root)
        self.canvas.pack()

        self.windowRunning = False

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def waitforclose(self):
        self.windowRunning = True
        while self.windowRunning == True:
            self.redraw()
        
    def close(self):
        self.windowRunning = False



