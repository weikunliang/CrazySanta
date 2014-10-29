from Tkinter import*

class Santa(object):
    
    # the initial x and y-coordinates of the center of Santa
    x = 180
    y = 160
    
    # the dimensions of Santa
    width = 75
    height = 43
    
    # the acceleration of Santa when it goes down
    aDown = 0.5
    # the initial velocity of Santa
    v = 0.2
    # the maximum value of the speed that Santa could reach
    maxSpeed = 4.0
    
    # an offset that is used when calculating collision, as there might
    # be spaces within the rectangle that the image of Santa is contained
    offset = 5
    
    # draws Santa
    def drawSanta(self, canvas, image):
        canvas.create_image(self.x, self.y, image = image, tag = "santa")
    
    # moves the plane in the direction of the parameter passed
    def moveSanta(self, direction):
        # Santa moves up at a constant velocity
        if(direction == "UP"):
            self.v = 3.8
            self.y -= self.v
        # Santa accelerates downwards
        if(direction == "DOWN"):
            self.y += min(self.v, self.maxSpeed)
            self.v += self.aDown
