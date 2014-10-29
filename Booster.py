from Tkinter import*
import random

class Booster(object):
    
    # the dimensions of the booster
    width = 45
    height = 50
    
    # gives the booster a random x and y value
    def __init__(self):
        self.x = random.randint(1000, 2000)
        self.y = random.randint(165, 335)
    
    # draws the booster
    def drawBooster(self, canvas, image):
        canvas.create_image(self.x, self.y, image = image,
                            tag = "booster")
    
    # moves the booster to the left
    def resetBooster(self):
        self.x -= 10
    
class BoosterList(object):
    
    boosterList = [ ]
    
    def init(self):
        self.boosterList = [ ]
    
    # adds a new booster to the boosterList
    def addBooster(self):
        self.boosterList += [Booster()]

    # draws all the boosters
    def drawAllBooster(self, canvas, image):
        for booster in self.boosterList:
            booster.drawBooster(canvas, image)
    
    def moveBooster(self):
        if(len(self.boosterList) == 0): return
        # moves the boosters to the left
        for booster in self.boosterList:
            booster.resetBooster()
        x = self.boosterList[0].x
        # deletes the boosters as they go off the screen
        if(x < -50):
            self.boosterList.pop(0)
