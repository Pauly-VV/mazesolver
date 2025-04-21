from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title("Maze Solver")
        #self.root.geometry(f"{width}x{height}")
        self.root.protocol("WM_DELETE_WINDOW", self.close)

        self.canvas = Canvas(self.root, bg="white", height=height, width=width)
        self.canvas.pack(fill=BOTH, expand=True)

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

    def draw_line(self, line, fill_colour = "black"):
        line.draw(self.canvas, fill_colour)




