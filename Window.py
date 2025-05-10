from tkinter import *

class Window():
    def __init__(self, width, height):
        #generate window, title, and activate close button
        self.root = Tk()
        self.root.title("Maze Solver")
        #self.root.geometry(f"{width}x{height}")
        self.root.protocol("WM_DELETE_WINDOW", self.close)

        #create a canvas for the maze
        self.canvas = Canvas(self.root, bg="white", height=height, width=width)
        self.canvas.pack(fill=BOTH, expand=True)

        #create a canvas for buttons
        self.buttons = Canvas(self.root, bg="grey", height = height / 6, width = width / 3)
        self.buttons.pack(side = BOTTOM, expand=False)
        #create buttons
        #creating a proportion for sizing the buttons based on the size of the maze window, note that if the window gets very small, the buttons will have issues
        proportion = int(width / 150)
        #left
        self.left_button = Button(self.buttons, text="LEFT", command = self.press_left, height = proportion, width = proportion * 2)
        self.left_button.pack(side=LEFT, fill = Y)
        #right
        self.right_button = Button(self.buttons, text="RIGHT", command = self.press_right, height = proportion, width = proportion * 2)
        self.right_button.pack(side=RIGHT, fill = Y)
        #up
        self.up_button = Button(self.buttons, text="UP", command = self.press_up, height = int(proportion / 2), width = proportion * 2)
        self.up_button.pack(side=TOP)
        #down
        self.down_button = Button(self.buttons, text="DOWN", command = self.press_down, height = int(proportion / 2), width = proportion * 2)
        self.down_button.pack(side=BOTTOM)


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

    #Button Press Functions
    def press_left(self):
        print("Moving Left")

    def press_right(self):
        print("Moving Right")
    
    def press_up(self):
        print("Moving Up")

    def press_down(self):
        print("Moving Down")




