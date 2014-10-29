from Tkinter import*
import random

class Sock(object):
    
    # the dimensions of the sock
    width = 20
    height = 50
    
    # x and y represents the center coordinates of the sock
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # draws the sock
    def drawSock(self, canvas, image):
        canvas.create_image(self.x, self.y, image = image)
        
class SockList(object):
    
    # number of socks
    num = 3
    
    # the starting center of the sock
    x = 40
    y = 50
    
    # creates a sock list and add num socks into it
    def init(self):
        self.sockList = [Sock(self.x, self.y)]
        while(len(self.sockList) < self.num):
            self.x += 20
            self.sockList += [Sock(self.x, self.y)]

    # draws all the socks
    def drawAllSock(self, canvas, image):
        for sock in self.sockList:
            sock.drawSock(canvas, image)
    
    # removes the sock     
    def remove(self):
        self.sockList.pop()