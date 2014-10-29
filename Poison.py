from Tkinter import*
import random

class Poison(object):
    
    # the dimensions of the poison
    width = 43
    height = 50
    
    # generates a random x and y value that represents the
    # center of the poison
    def __init__(self):
        self.x = random.randint(1000, 2000)
        self.y = random.randint(165, 335)
    
    # draws the poison
    def drawPoison(self, canvas, image):
        canvas.create_image(self.x, self.y, image = image,
                            tag = "poison")
    
    # moves the poison to the left
    def resetPoison(self):
        self.x -= 10
    
class PosionList(object):
    
    poisonList = [ ]
    
    def init(self):
        self.poisonList = [ ]
    
    # adds a new poison to the poisonList
    def addPoison(self):
        self.poisonList += [Poison()]

    # draws all the poisons
    def drawAllPoison(self, canvas, image):
        for poison in self.poisonList:
            poison.drawPoison(canvas, image)
    
    def movePoison(self):
        if(len(self.poisonList) == 0): return
        # moves all the poison to the left
        for poison in self.poisonList:
            poison.resetPoison()
        x = self.poisonList[0].x
        # removes the poison as it disappears off the canvas
        if(x < -50):
            self.poisonList.pop(0)