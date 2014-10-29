from Tkinter import*
import random

class Present(object):
    
    # the dimensions of the present
    width = 40
    height = 40
    
    # x and y represents the center coordinates of the present
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def getx(self):
        return self.x
    
    def gety(self):
        return self.y
    
    # draws the present
    def drawPresent(self, canvas, image):
        canvas.create_image(self.x, self.y, image = image,
                            tag = "present")
    
    # moves the present to the left
    def resetPresent(self):
        self.x -= 10
        
class PresentList(object):
    
    # the initial coordinates of the center of the present
    x = 900
    y = 300
    
    # creates a list of presents
    def createPresent(self):
        self.presentList = [ ]
        p = Present(self.x, self.y)
        self.presentList += [p]
        
        # keeps adding presents until its x-coordinate reaches
        # the end of the canvas plus an offset
        while(self.presentList[-1].getx() < 1500):
            self.addPresent()
    
    # adds a new present to the list by generating random x and y values
    def addPresent(self):
        xPrev = self.presentList[-1].getx()
        xNew = xPrev + random.randint(200, 1000)
        yNew = random.randint(165, 335)
        self.presentList += [Present(xNew, yNew)]

    # draws all the presents
    def drawAllPresent(self, canvas, image):
        for present in self.presentList:
            present.drawPresent(canvas, image)
    
    def movePresents(self):
        # moves all the presents to the left
        for present in self.presentList:
            present.resetPresent()
        x = self.presentList[0].getx()
        # deletes the present if it is outside the view of the canvas
        if(x < -50):
            self.presentList.pop(0)
        # adds new presents as we move
        if(self.presentList[-1].getx() < 1800):
            self.addPresent()
