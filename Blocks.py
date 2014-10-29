from Tkinter import*
import random

class Block(object):
    
    # the dimensions of the block
    width = 20
    height = 70

    def __init__(self, x, direction = "UP"):
        # x is the starting top left point of the tree
        self.x1 = x
        self.y1 = random.randint(125, 305)
        
        # (ARCADE MODE) the direction the tree is moving
        self.direction = direction
    
    # sets the direction the block is moving to direction
    def setDirection(self, direction):
        self.direction = direction
        
    def getx1(self):
        return self.x1
    
    def gety1(self):
        return self.y1
    
    # returns the center x-coordinate of the tree
    def getcx(self):
        return self.x1+self.width/2
    
    # returns the center y-coordinate of the tree
    def getcy(self):
        return self.y1+self.height/2
    
    # draws the tree
    def drawBlock(self, canvas, image):
        canvas.create_image(self.x1+self.width/2,
                            self.y1+self.height/2, image = image, tag = "block")
        
    # moves the tree to the left
    def resetBlock(self):
        self.x1 -= 10
    
    # (ARCADE MODE) moves the tree according to its direction
    def shift(self, direction):
        if(direction == "UP"): self.y1 -= 5
        else: self.y1 += 5

class BlockList(object):
    
    # the initial x coordinate of the top left of the tree
    x = 700
    
    def __init__(self, distance):
        # the distance between each tree
        self.distance = distance
    
    # creates a list of trees and keeps on adding trees to it until
    # it is the reaches the size of the canvas plus an offet
    def createBlock(self):
        self.blockList = [ ]
        b = Block(self.x, "DOWN")
        self.blockList += [b]
        while(self.blockList[-1].getx1() < 1500):
            self.addBlocks()
    
    # adds a new tree to the list
    def addBlocks(self):
        # the x-coordinate of the previous tree
        xPrev = self.blockList[-1].getx1()
        xNew = xPrev + self.distance
        # alternates the directions
        if(self.blockList[-1].direction == "DOWN"): direction = "UP"
        else: direction = "DOWN"
        self.blockList += [Block(xNew, direction)]

    # draws all the trees
    def drawAllBlocks(self, canvas, image):
        for block in self.blockList:
            block.drawBlock(canvas, image)

    def moveBlocks(self):
        # moves the treess to the left
        for block in self.blockList:
            block.resetBlock()
            
        # removes the tree if it is far away from the canvas view
        x = self.blockList[0].getx1()
        if(x < -700):
            self.blockList.pop(0)
        
        # adds new trees while we are moving to the left
        if(self.blockList[-1].getx1() < 1500):
            self.addBlocks()