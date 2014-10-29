import random
from Tkinter import*
from Mount import*
from Blocks import*

class MountainRange(object):
    # sets the initial starting x-coordinate of the mountain
    startPointx = 0
    
    # sets the initial starting y-coordinates of the top and
    # bottom mountain
    startPointYtop = 0
    startPointYbottom = 500
    
    def setMountainList(self):
        # creates a mountain list for the mountains in the bottom
        # of the canvas and adds a mountain to it
        self.mountainListBottom = [ ]
        mbottom = MountainBottom(self.startPointx, self.startPointYbottom)
        self.mountainListBottom += [mbottom]
        
        # creates a mountain list for the mountains in the top
        # of the canvas and adds a mountain to it
        self.mountainListTop = [ ]
        mtop = MountainTop(self.startPointx, self.startPointYtop)
        self.mountainListTop += [mtop]
        
        # keeps on drawing mountains until we reach the width of 
        # the canvas plus a margin of 500
        while((self.mountainListBottom[-1].getLowerRight())[0] < 1500 or
            (self.mountainListTop[-1].getLowerRight())[0] < 1500):
            self.addMountains()

    # adds new mountains to the list
    def addMountains(self):
        # the mountains on the bottom of the canvas
        # the length of the base of the previous mountain
        baseLengthBottom = self.mountainListBottom[-1].getBase()
        # the x-coordinate of the lower left point of the mountain
        xPrevB = self.mountainListBottom[-1].getLowerLeft()[0]
        # generates a starting x value for the new mountain 
        xNewB = xPrevB + random.randint(baseLengthBottom/4, 3*baseLengthBottom/4)
        self.mountainListBottom += [MountainBottom(xNewB,
                                                   self.startPointYbottom)]
        
        # the mountains on the top of the canvas
        baseLengthTop = self.mountainListTop[-1].getBase()
        xPrevT = self.mountainListTop[-1].getLowerLeft()[0]
        xNewT = xPrevT + random.randint(baseLengthTop/4, 3*baseLengthTop/4)
        self.mountainListTop += [MountainTop(xNewT,
                                             self.startPointYtop)]
    
    # draws all the mountains in the mountain list 
    def drawAll(self, canvas):
        for mountain in self.mountainListBottom:
            mountain.drawMountain(canvas)
        for mountain in self.mountainListTop:
            mountain.drawMountain(canvas)
    
    # moves the mountains to the left by reseting the x values
    # of each mountain
    def moveMountains(self):
        for mountain in self.mountainListBottom:
            mountain.resetValues()
        for mountain in self.mountainListTop:
            mountain.resetValues()
            
        # removes the mountains if they are not in the view of the canvas
        xTopMount = self.mountainListTop[0].getLowerLeft()[0]
        xBottomMount = self.mountainListBottom[0].getLowerLeft()[0]
        if(xTopMount < -300):
            self.mountainListTop.pop(0)
        if(xBottomMount < -300):
            self.mountainListBottom.pop(0)
            
        # adds mountains while we are moving the mountains to the left
        if((self.mountainListBottom[-1].getLowerRight())[0] < 1500 or
            (self.mountainListTop[-1].getLowerRight())[0] < 1500):
            self.addMountains()
    
    # given a x value, search through the mountain list and find the y-value
    # of the top and bottom mountain that it hits
    def findY(self, x):
        bottom = 500
        top = -1
        # finds the smallest y-value in case mountains overlap each other
        for i in xrange(len(self.mountainListBottom)):
            mountain = self.mountainListBottom[i]
            if(mountain.inMountain(x)):
                b = mountain.find(x)
                if(b < bottom): bottom = b
        
        #finds the largest y-value in case mountains overlap each other
        for i in xrange(len(self.mountainListTop)):
            mountain = self.mountainListTop[i]
            if(mountain.inMountain(x)):
                t = mountain.find(x)
                if(t > top): top = t
                
        # top is the y-value of the x value hits the top mountain
        # bottom is the y-value of the x that hits the bottom mountain
        return (top, bottom)
