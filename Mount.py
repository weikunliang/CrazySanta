import random
from Tkinter import *

class Mountain(object):
    
    def __init__(self, startx, starty):
        # startx and starty are the coordinates of the bottom left
        # starting point of the triangle
        self.startx = startx
        self.starty = starty
        
        # self.height and self.base are the base and height of the
        # triangle (mountain)
        self.height = random.randint(30, 120)
        self.base = random.randint(80, 300)
        
        # self.top is the x coordinate of the top point of the triangle 
        self.top = self.startx + self.base/2
 
    # returns the lower left coordinates of the triangle
    def getLowerLeft(self): pass
    
    # returns the lower right coordinates of the triangle
    def getLowerRight(self): pass
    
    # returns the top coordinate of the triangle
    def getTop(self): pass
    
    # returns the length of the base of the triangle
    def getBase(self):
        return self.base
    
    # returns the length of the height of the triangle
    def getHeight(self):
        return self.height
    
    # draws the mountain
    def drawMountain(self, canvas):
        canvas.create_polygon(self.getLowerLeft(), self.getLowerRight(),
                              self.getTop(), fill = "white")
    
    # moves the mountain to the left 
    def resetValues(self):
        self.startx -= 10
        self.top = self.startx + self.base/2
    
    # checks whether a x coordinate is in a mountain or not
    def inMountain(self, x):
        left = self.getLowerLeft()[0]
        right = self.getLowerRight()[0]
        return(x > left and x < right)
    
    # given a point's xcoordinate in a mountain, returns the y-coodinate
    # of that point
    def find(self, x):
        # if x is in the left half of the triangle
        if(x < self.startx+self.base/2):
            side = "left"
        # if x is in the right half of the triangle
        elif(x > self.startx+self.base/2):
            side = "right"
        # if x is the top coordinate of the triangle
        else: side = "mid"
        
        if(side == "mid"): return self.getTop()[1]
        elif(side == "left"):
            x1, y1 = self.getLowerLeft() 
            x2, y2 = self.getTop()
        elif(side == "right"):
            x1, y1 = self.getLowerRight()
            x2, y2 = self.getTop()
        # m is the slope of the line that is formed by
        # (x1, x2) and (y1, y2)
        m = float(y2-y1)/(x2-x1)
        # returns the y coordinate of that point
        return m*(x-x1) + y1
        
# the mountains coming out from the bottom of the canvas
class MountainBottom(Mountain):

    def getLowerLeft(self):
        return (self.startx, self.starty)
    
    def getLowerRight(self):
        return (self.startx+self.base, self.starty)

    def getTop(self):
        return (self.top, self.starty-self.height)

# the mountain coming out from the top of the canvas
class MountainTop(Mountain):

    def getLowerLeft(self):
        return (self.startx, self.starty)
    
    def getLowerRight(self):
        return (self.startx+self.base, self.starty)
    
    def getTop(self):
        return (self.top, self.starty+self.height)