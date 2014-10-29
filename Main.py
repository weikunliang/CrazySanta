from Tkinter import*
from Mount import*
from MountainRange import*
from Blocks import*
from Santa import*
from Present import*
from Score import*
from Booster import*
from Sock import*
from Poison import*
import sys

# loads the best score for the game
def load(fileName):
    try:
        with open(fileName, 'r') as file:
            text="".join(file.readlines())
    except:
        text=""
    return text

# saves the best score for the game
def save(fileName,text):
    with open(fileName, 'w') as file:
        file.truncate(0)
        file.write(repr(text))
        
def menuButtonsInit(canvas):
    # set up the buttons for the main menu
    canvas.data.startButton = Button(canvas,
                        image = canvas.data.startButtonImage,
                         width = 300, height = 100, bg = "white", bd = 0, 
                         command = lambda: startButtonPressed(canvas))
    canvas.data.exitButton = Button(canvas, image = canvas.data.exitButtonImage,
                        width = 300, height = 100, bg = "white", bd = 0,
                        command = exitButtonPressed)
    canvas.data.instructButton = Button(canvas, image = canvas.data.instruct,
                            width = 230, height = 70, bg = "white", bd = 0, 
                            command = lambda: instructButtonPressed(canvas))
    canvas.data.backButton = Button(canvas, image = canvas.data.back,
                            width = 150, height = 50, bg = "white", bd = 0, 
                            command = lambda: backButtonPressed(canvas))
    canvas.data.nextButton = Button(canvas, image = canvas.data.next,
                            width = 150, height = 50, bg = "white", bd = 0, 
                            command = lambda: nextButtonPressed(canvas))
    canvas.data.mainButton = Button(canvas, image = canvas.data.mainMenu,
                            width = 250, height = 80, 
                            command = lambda: mainMenuButtonPressed(canvas))

def init(canvas):
    # the speed at which the background is moving to the left in
    # the beginning of the game
    canvas.data.initialSpeed = 30
    canvas.data.speed = canvas.data.initialSpeed
    
    # initializes the scores of the two different games and loads
    # the best scores from the files
    canvas.data.score = 0
    canvas.data.scoreArcade = 0
    canvas.data.bestScore = int(load("bestScore.txt"))
    canvas.data.bestScoreArcade = int(load("bestScoreArcade.txt"))
    
    # creates a scoreboard object
    canvas.data.scoreBoard = Score()
    
    canvas.data.game = "MENU"
    canvas.data.isPaused = False
    loadImages(canvas)
    menuButtonsInit(canvas)
    canvas.pack(fill=BOTH, expand=YES)
    drawButton(canvas)

# loads all the images that we need for the game
def loadImages(canvas):
    canvas.data.background = PhotoImage(file="menuBackground.gif")
    canvas.data.gameBack = PhotoImage(file="gameBackground.gif")
    canvas.data.instruct = PhotoImage(file = "instruct.gif")
    canvas.data.startButtonImage = PhotoImage(file="start.gif")
    canvas.data.exitButtonImage = PhotoImage(file="exit.gif")
    canvas.data.back = PhotoImage(file="back.gif")
    canvas.data.normalButtonImage = PhotoImage(file="normal.gif")
    canvas.data.arcadeButtonImage = PhotoImage(file="arcade.gif")
    canvas.data.instructScreen = PhotoImage(file="instructBackground.gif")
    canvas.data.santaPic = PhotoImage(file="santa.gif")
    canvas.data.treePic = PhotoImage(file="tree.gif")
    canvas.data.presentPic = PhotoImage(file="present.gif")
    canvas.data.boosterPic = PhotoImage(file = "rocket.gif")
    canvas.data.scoreBoardPic = PhotoImage(file="scoreBoard.gif")
    canvas.data.playAgain = PhotoImage(file="play.gif")
    canvas.data.mainMenu = PhotoImage(file = "main.gif")
    canvas.data.sockPic = PhotoImage(file = "sock.gif")
    canvas.data.poisonPic = PhotoImage(file = "poison.gif")
    canvas.data.next = PhotoImage(file = "next.gif")

def initGameMenu(canvas):
    canvas.data.game = "GAMEMENU"
    
    # sets the buttons for the game menu
    normalButton = Button(canvas, image = canvas.data.normalButtonImage,
                          width = 300, height = 100, bg = "white", bd = 0, 
                          command = lambda: normalButtonPressed(canvas))
    arcadeButton = Button(canvas, image = canvas.data.arcadeButtonImage,
                          width = 300, height = 100, bg = "white", bd = 0,
                          command = lambda: arcadeButtonPressed(canvas))
    canvas.data.normalButton = normalButton
    canvas.data.arcadeButton = arcadeButton
    canvas.pack(fill=BOTH, expand=YES)
    drawButton(canvas)

def setDistanceAndSpeed(canvas):
    # sets the distance between each tree according to the mode of
    # game we are in
    if(canvas.data.game == "SIMPLE"):
        canvas.data.distance = 400
        canvas.data.hint = False
    elif(canvas.data.game == "ARCADE"):
        canvas.data.distance = 600
        # initializes the speed
        canvas.data.speed = canvas.data.initialSpeed

def initGame(canvas):
    setDistanceAndSpeed(canvas)
    # sets up all the objects (mountains, block and santa)
    canvas.data.mRange = MountainRange()
    canvas.data.mRange.setMountainList()
    canvas.data.blocks = BlockList(canvas.data.distance)
    canvas.data.blocks.createBlock()
    canvas.data.santa = Santa()
    canvas.data.isGameOver, canvas.data.up = False, False
    if(canvas.data.game == "ARCADE"):
        # sets up the additional objects for the arcade mode
        #(present, booster, sock, poison)
        canvas.data.present = PresentList()
        canvas.data.present.createPresent()
        canvas.data.numPresent = 0
        canvas.data.booster = BoosterList()
        canvas.data.booster.init()
        canvas.data.sock = SockList()
        canvas.data.sock.init()
        canvas.data.poison = PosionList()
        canvas.data.poison.init()
        # canvas.data.fast is a boolean value that represents whether
        # Santa hit a rocket, if it did, this value becomes True and the
        # speed of Santa increases for a certain amount of time
        canvas.data.fast = False
    if(canvas.data.game == "SIMPLE"):
        # sets the initial performance to 100%
        canvas.data.performance = 100
    
def startButtonPressed(canvas):
    # goes to the game menu where the user have to choose between
    # the normal mode and the arcade mode
    canvas.data.game = "GAMEMENU"
    initGameMenu(canvas)
    
def exitButtonPressed():
    # exits the game
    sys.exit()
    
def normalButtonPressed(canvas):
    # this starts the normal mode of the game
    canvas.data.game = "SIMPLE"
    initGame(canvas)
    redrawAll(canvas)

def arcadeButtonPressed(canvas):
    # this starts the arcade mode of the game
    canvas.data.game = "ARCADE"
    initGame(canvas)
    redrawAll(canvas)
    
def backButtonPressed(canvas):
    # this button allows the user to go back to the previous page
    # depending on which page the user is currently on
    if(canvas.data.game == "INSTRUCT3"):
        canvas.data.game = "INSTRUCT2"
        instructButtonPressed(canvas)
    elif(canvas.data.game == "INSTRUCT2"):
        canvas.data.game = "INSTRUCT1"
        instructButtonPressed(canvas)
    else:
        canvas.data.game = "MENU"
        init(canvas)
  
def mainMenuButtonPressed(canvas):
    # this goes back to the main menu
    canvas.data.game = "MENU"
    init(canvas)
    
def nextButtonPressed(canvas):
    # this goes to the next page of the instructions depending on
    # which page the user is currently on
    if(canvas.data.game == "INSTRUCT1"):
        canvas.data.game = "INSTRUCT2"
    elif(canvas.data.game == "INSTRUCT2"):
        canvas.data.game = "INSTRUCT3"
    instructButtonPressed(canvas)

# draws the instructions for the first instructions page
def instruct1(canvas):
    t1 = "Press the upward arrow to go up"
    t2 = "Press 'p' to pause"
    t3 = "Press 'r' to restart"
    t4 = "Don't let Santa bump into a tree or mountain!"
    canvas.create_text(500, 160, text = t1, font = "Verdana 20 bold")
    canvas.create_text(500, 210, text = t2, font = "Verdana 20 bold")
    canvas.create_text(500, 260, text = t3, font = "Verdana 20 bold")
    canvas.create_text(500, 310, text = t4, font = "Verdana 20 bold")

# this draws instructions for the second instructions page  
def instruct2(canvas):
    t5 = "Press 'h' for HINT MODE"
    t6 = "HINT MODE creates a rainbow path that represents"
    t7 = "the best possible path taken"
    t8 = "If the HINT MODE is on, your performance compare to the"
    t9 = "best path will be calculated at the end"
    t10 = "SIMPLE MODE"
    canvas.create_text(500, 150, text = t10, font = "Verdana 22 bold")
    canvas.create_text(500, 200, text = t5, font = "Verdana 20 bold")
    canvas.create_text(500, 240, text = t6, font = "Verdana 20 bold")
    canvas.create_text(500, 270, text = t7, font = "Verdana 20 bold")
    canvas.create_text(500, 310, text = t8, font = "Verdana 20 bold")
    canvas.create_text(500, 340, text = t9, font = "Verdana 20 bold")

# this draws instructions for the third instructions page 
def instruct3(canvas):
    t11 = "ARCADE MODE"
    t12 = "Collect presents for bonus"
    t13 = "Hit rockets to speed up"
    t14 = "Avoid Poisons. If Santa hits a poison, it loses 1 sock."
    t15 = "The game is over when all three socks are lost"
    canvas.create_text(500, 150, text = t11, font = "Verdana 22 bold")
    canvas.create_text(500, 200, text = t12, font = "Verdana 20 bold")
    canvas.create_text(500, 240, text = t13, font = "Verdana 20 bold")
    canvas.create_text(500, 280, text = t14, font = "Verdana 20 bold")
    canvas.create_text(500, 320, text = t15, font = "Verdana 20 bold")

# this controls the instruction button on the main menu and the next
# buttons on the instructions page
def instructButtonPressed(canvas):
    if(canvas.data.game == "MENU"):
        canvas.data.game = "INSTRUCT1"
    drawButton(canvas)
    if(canvas.data.game == "INSTRUCT1"):
        instruct1(canvas)
    elif(canvas.data.game == "INSTRUCT2"):
        instruct2(canvas)
    elif(canvas.data.game == "INSTRUCT3"):
        instruct3(canvas)

# this allows the user to restart the game when the game is over     
def playAgainButtonPressed(canvas):
    initGame(canvas)

# this controls all the key presses for the game
def keyPressed(canvas, event):
    canvas = event.widget.canvas
    if(canvas.data.game == "SIMPLE" or canvas.data.game == "ARCADE"):
        # moves Santa up
        if(event.keysym == "Up"):
            canvas.data.up = True
        # resets the game
        if(event.keysym == "r"):
            gameOver(canvas)
            initGame(canvas)
        # pauses the game
        if(event.keysym == "p"):
            canvas.data.isPaused = not canvas.data.isPaused
        # goes back to the previous screen
        if(event.keysym == "q"):
            canvas.data.game = "GAMEMENU"
            initGameMenu(canvas)
        # activates the hint mode where a hint path will be dispalyed
        if(canvas.data.game == "SIMPLE"):
            if(event.keysym == "h"):
                canvas.data.hint = not canvas.data.hint

# the user keeps on moving up when he/she holds the up key, and goes down
# when this key is released
def keyReleased(canvas, event):
    canvas = event.widget.canvas
    if(canvas.data.game == "SIMPLE" or canvas.data.game == "ARCADE"):
        if(event.keysym == "Up"):
            canvas.data.up = False

def addScore(canvas):
    # continuously adds the score as Santa moves
    if(canvas.data.game == "SIMPLE"):
        canvas.data.score += 1
    if(canvas.data.game == "ARCADE"):
        canvas.data.scoreArcade += 1
        # resets the speed of Santa to its original speed after a
        # certain amount of time after it hit the rocket
        if(canvas.data.fast):
            if(canvas.data.scoreArcade == canvas.data.newScore):
                canvas.data.speed = canvas.data.initialSpeed
                canvas.data.fast = False

# moves the santa up and down depending on the key press
def moveSanta(canvas):
    if(canvas.data.up == False):
        canvas.data.santa.moveSanta("DOWN")
    else:
        canvas.data.santa.moveSanta("UP")

# (ARCADE MODE) continuously bounces the trees between mountains
# (the tree reverses its direction of motion when it hits a mountain)
def moveTrees(canvas):
    for block in canvas.data.blocks.blockList:
        if(hitMountain(canvas, block)):
            changeDirection(block)
        block.shift(block.direction)

def timerFired(canvas):
    if(canvas.data.game == "SIMPLE" or canvas.data.game == "ARCADE"):
        if(canvas.data.isGameOver == False):
            if(canvas.data.isPaused == False):
                # continuously moves the mountains and trees to the left
                canvas.data.mRange.moveMountains()
                canvas.data.blocks.moveBlocks()
                if(canvas.data.game == "ARCADE"):
                    # continuously moves the presents, booster and rockets
                    # to the left
                    canvas.data.present.movePresents()
                    canvas.data.booster.moveBooster()
                    canvas.data.poison.movePoison()
                    # moves the trees between the mountain
                    moveTrees(canvas)
                # moves Santa
                moveSanta(canvas)
            redrawAll(canvas)
            # if we loses all three socks, the game is over
            if(canvas.data.game == "ARCADE" and
               len(canvas.data.sock.sockList) == 0):
                        gameOver(canvas)
            # if we collided with a tree or mountain, the game is over
            if(hasCollided(canvas) == True):
                gameOver(canvas)
    # keeps on adding the score if we are not in the pause mode
    if(canvas.data.isPaused == False): addScore(canvas)
    delay = canvas.data.speed # milliseconds
    canvas.after(delay, lambda: timerFired(canvas))

# (gives a very small probability of generating a rocket and a small but a
# bit higher probability of generating a poison)
def drawArcadeObjects(canvas):
    canvas.data.present.drawAllPresent(canvas, canvas.data.presentPic)
    r = random.randint(0, 600)
    # draws a booster only when the random integer we generates is 1 or 2
    if(r == 1 or r == 2):
        canvas.data.booster.addBooster()
    # draws a poison only when the random integer we generates is divisible
    # by 90. 
    if(r % 90 == 0):
        canvas.data.poison.addPoison()
    canvas.data.booster.drawAllBooster(canvas, canvas.data.boosterPic)
    canvas.data.poison.drawAllPoison(canvas, canvas.data.poisonPic)

# draws all the objects on the screen when the game is over
def drawGameOver(canvas):
    canvas.delete(ALL)
    # draws the background image
    drawBackground(canvas)
    performance = ""
    if(canvas.data.game == "SIMPLE"):
        # draws the score for the simple mode
        if(canvas.data.hint):
            # if hint is on, draws the performance
            performance = str(canvas.data.performance)
        canvas.data.scoreBoard.drawBoard(canvas, canvas.data.score,
                                        canvas.data.bestScore,
                                        canvas.data.scoreBoardPic,
                                        performance)
    elif(canvas.data.game == "ARCADE"):
        # draws the score for the arcade mode
        canvas.data.scoreBoard.drawBoard(canvas, canvas.data.scoreArcade,
                                        canvas.data.bestScoreArcade,
                                         canvas.data.scoreBoardPic,
                                         performance,
                                         canvas.data.numPresent)
    # creates the buttons for the play again and main menu window
    canvas.create_window(800, 180, window = canvas.data.playAgainButton)
    canvas.create_window(800, 320, window = canvas.data.mainButton)

def redrawAll(canvas):
    canvas.delete(ALL)
    drawBackground(canvas)
    # draws the main objects(mountain, tree, and santa)
    canvas.data.mRange.drawAll(canvas)
    canvas.data.blocks.drawAllBlocks(canvas, canvas.data.treePic)
    canvas.data.santa.drawSanta(canvas, canvas.data.santaPic)
    if(canvas.data.game == "ARCADE"):
        drawArcadeObjects(canvas)
    drawScore(canvas)
    if(canvas.data.game == "SIMPLE" and canvas.data.hint == True):
        drawHint(canvas)
        canvas.create_text(50, 25,text = "HINT MODE",
                           font = "Verdana 14 bold", fill = "black")
    if(canvas.data.game == "ARCADE"):
        canvas.data.sock.drawAllSock(canvas, canvas.data.sockPic)
    if(canvas.data.isGameOver):
        drawGameOver(canvas)

# draws the rainbow line that represents the hint path
def rainbowLine(canvas, pos, pos2, pos3, pos4, pos5, pos6, pos7):
    canvas.create_line(*pos, smooth = True, dash = True,
                        width = 2, fill = "red", tag = "hint")
    canvas.create_line(*pos2, smooth = True, dash = True,
                       width = 2, fill = "orange", tag = "hint")
    canvas.create_line(*pos3, smooth = True, dash = True,
                       width = 2, fill = "yellow", tag = "hint")
    canvas.create_line(*pos4, smooth = True, dash = True,
                       width = 2, fill = "green", tag = "hint")
    canvas.create_line(*pos5, smooth = True, dash = True,
                       width = 2, fill = "blue", tag = "hint")
    canvas.create_line(*pos6, smooth = True, dash = True,
                       width = 1, fill = "#4B0082" , tag = "hint")
    canvas.create_line(*pos7, smooth = True, dash = True,
                       width = 2, fill = "violet", tag = "hint")

# measures the performance of Santa (how much its path differs from the
# hint path) 
def measurePerformance(canvas, pos4):
    # the coordinates of the center of Santa's position
    santaY = canvas.data.santa.y
    santaX = canvas.data.santa.x
    (x1, y1), (x2, y2) = (0, 0), (0, 0)
    # finds which two points of the rainbow curve Santa belongs
    for i in xrange(0, len(pos4) - 3, 2):
        p1, p2 = pos4[i], pos4[i+2]
        # if Santa is between these two points, store the two points
        if(santaX >= p1 and santaX <= p2): 
            (x1, y1) = (p1, pos4[i+1])
            (x2, y2) = (p2, pos4[i+1])
            break
    if(x1 != 0 and x2 != 0 and y1 != 0 and y2 != 0):
        # calculates the slope
        m = float(y2-y1)/(x2-x1)
        # approximates the y-coordinate based on the line segment that
        # joins the two points
        hintY = m*(santaX-x1) + y1
        # calculates the difference in the distance between Santa and the
        # center of the rainbow
        diff = santaY - hintY
        # subtracts amounts from the performance based on how large the
        # difference is
        if(diff > 100 and diff < 180):
            canvas.data.performance -= 0.1
        elif(diff >= 180 and diff < 270):
            canvas.data.performance -= 0.3
        elif(diff >= 270):
            canvas.data.performance -= 0.6

def drawHint(canvas):
    if(canvas.data.hint == True):
        # pos 1 to 7 represents the seven different colors of the rainbow
        pos, pos2, pos3, pos4 = [ ], [ ], [ ], [ ]
        pos5, pos6, pos7 = [ ], [ ], [ ]
        # gets the center coordinates of each block and checks if the distance
        # of it to the top mountain or the bottom mountain is greater. It
        # chooses the greater one and calculates the midpoint of these points
        # and adds this point to the hint path
        for block in canvas.data.blocks.blockList:
            x = block.getcx()
            y = block.getcy()
            # yUp and yDown are the y-coordinates of the top and bottom mountain
            # at a specific x-coordinate
            yUp, yDown = canvas.data.mRange.findY(x)
            if(y-yUp > yDown-y): ymid = yUp
            else: ymid = yDown
            # if the upper distance is greater, get the top of the tree
            if(ymid == yUp): y = block.gety1()
            # if the bottom distance is greater, get the bottom of the tree
            else: y = block.gety1() + block.height
            pos += (x, (y+ymid)/2)
            pos2 += (x, (y+ymid)/2 + 2)
            pos3 += (x, (y+ymid)/2 + 4)
            pos4 += (x, (y+ymid)/2 + 6)
            pos5 += (x, (y+ymid)/2 + 8)
            pos6 += (x, (y+ymid)/2 + 10)
            pos7 += (x, (y+ymid)/2 + 12)
            
        rainbowLine(canvas, pos, pos2, pos3, pos4, pos5, pos6, pos7)
        measurePerformance(canvas, pos4)
        
# draws the score depending on which game we are in      
def drawScore(canvas):
    if(canvas.data.game == "SIMPLE"):
        canvas.create_text(90, 480, text = "Distance = "+str(canvas.data.score),
                           font = "Verdana 14 bold", fill = "black")
        canvas.create_text(900, 480,
                           text = "Best = " + str(canvas.data.bestScore),
                           font = "Verdana 14 bold", fill = "black")
    if(canvas.data.game == "ARCADE"):
        canvas.create_text(90, 480,
                           text = "Distance = " + str(canvas.data.scoreArcade),
                           font = "Verdana 14 bold", fill = "black")
        canvas.create_text(900, 480,
                           text = "Best = " +
                           str(canvas.data.bestScoreArcade),
                           font = "Verdana 14 bold", fill = "black")

# draws the background for the game
def drawBackground(canvas):
    canvas.create_image(500, 250, image = canvas.data.gameBack)

# draws the different buttons depending on which menu we are on
def drawButton(canvas):
    canvas.delete(ALL)
    if(canvas.data.game == "MENU" or canvas.data.game == "GAMEMENU"):
        if(canvas.data.game == "MENU"):
            canvas.create_window(750, 250, window = canvas.data.startButton)
            canvas.create_window(750, 400, window = canvas.data.exitButton)
            canvas.create_window(150, 440, window = canvas.data.instructButton)
        elif(canvas.data.game == "GAMEMENU"):
            canvas.create_window(500, 260, window = canvas.data.normalButton)
            canvas.create_window(500, 390, window = canvas.data.arcadeButton)
            canvas.create_window(100, 450, window = canvas.data.backButton)
        canvas.create_image(500, 250, image = canvas.data.background)
    elif(canvas.data.game == "INSTRUCT1" or canvas.data.game == "INSTRUCT2"
         or canvas.data.game == "INSTRUCT3"):
        canvas.create_image(500, 250, image = canvas.data.instructScreen)
        canvas.create_window(100, 450, window = canvas.data.backButton)
        if(canvas.data.game == "INSTRUCT1" or canvas.data.game == "INSTRUCT2"):
            canvas.create_window(900, 450, window = canvas.data.nextButton)
        elif(canvas.data.game == "INSTRUCT3"):
            canvas.create_window(850, 435, window = canvas.data.mainButton)

# displays the text for game over and resets the highscores
def gameOver(canvas):
    canvas.data.isGameOver = True
    canvas.data.isPaused = False
    canvas.data.playAgainButton = Button(canvas, image = canvas.data.playAgain,
                            width = 250, height = 80, 
                            command = lambda: playAgainButtonPressed(canvas))
    redrawAll(canvas)
    # compares the score to the high score and replace it if it is higher
    if(canvas.data.game == "SIMPLE"):
        if(canvas.data.score > canvas.data.bestScore):
            canvas.data.bestScore = canvas.data.score
            save("bestScore.txt", canvas.data.bestScore)
        canvas.data.score = 0
    if(canvas.data.game == "ARCADE"):
        canvas.data.scoreArcade += canvas.data.numPresent*10
        if(canvas.data.scoreArcade > canvas.data.bestScoreArcade):
            canvas.data.bestScoreArcade = canvas.data.scoreArcade
            save("bestScoreArcade.txt", canvas.data.bestScoreArcade)
        canvas.data.scoreArcade = 0

# checks if Santa collided with the present, removes it from the list if
# there is a collision and adds one to the number of presents collected
def presentCollision(canvas, overlapSanta):
    allPresents = canvas.data.present
    presentPos = canvas.find_withtag("present")
    for over in overlapSanta:
        for pos in presentPos:
            if(over == pos):
                # collided!
                canvas.data.count = 1
                # finds which present Santa collided with and removes
                # it from the list
                for i in xrange(len(allPresents.presentList)):
                    present = allPresents.presentList[i]
                    xp1 = present.x - present.width/2
                    yp1 = present.y - present.height/2
                    xp2 = present.x + present.width/2
                    yp2 = present.y + present.height/2
                    coord = xp1, yp1, xp2, yp2
                    overlapPresent = canvas.find_overlapping(*coord)
                    if(len(overlapPresent) > 2):
                        allPresents.presentList.pop(i)
                        canvas.data.numPresent += 1
                        break

# checks if Santa collided with the rocket, removes it from the list if
# there is a collision and changes the speed of Santa                
def boosterCollision(canvas, overlapSanta):
    allBooster = canvas.data.booster
    boosterPos = canvas.find_withtag("booster")
    for over in overlapSanta:
        for pos in boosterPos:
            if(over == pos):
                # collided!
                canvas.data.count = 1
                # finds which booster Santa collided with and removes
                # it from the list
                for i in xrange(len(allBooster.boosterList)):
                    booster = allBooster.boosterList[i]
                    xb1 = booster.x - booster.width/2
                    yb1 = booster.y - booster.height/2
                    xb2 = booster.x + booster.width/2
                    yb2 = booster.y + booster.height/2
                    coord = xb1, yb1, xb2, yb2
                    overlapBooster = canvas.find_overlapping(*coord)
                    if(len(overlapBooster) > 2):
                        allBooster.boosterList.pop(i)
                        # changes the speed
                        canvas.data.fast = True
                        canvas.data.speed = 18
                        # sets the score at which when reached, changes the
                        # speed back to normal
                        canvas.data.newScore=canvas.data.scoreArcade+120
                        break

# checks if Santa collided with the poison, removes it from the list if
# there is a collision and removes a sock from the sock list     
def poisonCollision(canvas, overlapSanta):
    allPoison = canvas.data.poison
    poisonPos = canvas.find_withtag("poison")
    for over in overlapSanta:
        for pos in poisonPos:
            if(over == pos):
                #collided!
                canvas.data.count = 1
                # finds which poison Santa collided with and removes it from
                # the list
                for i in xrange(len(allPoison.poisonList)):
                    poison = allPoison.poisonList[i]
                    xpo1 = poison.x - poison.width/2
                    ypo1 = poison.y - poison.height/2
                    xpo2 = poison.x + poison.width/2
                    ypo2 = poison.y + poison.height/2
                    coord = xpo1, ypo1, xpo2, ypo2
                    overlapPoison = canvas.find_overlapping(*coord)
                    if(len(overlapPoison) > 2):
                        allPoison.poisonList.pop(i)
                        # removes a sock
                        canvas.data.sock.remove()
                        break

# checks for collision
def hasCollided(canvas):
    # the bounds of santa
    santa = canvas.data.santa
    x1, x2 = santa.x - santa.width/2, santa.x + santa.width/2
    y1 = santa.y - santa.height/2 + santa.offset
    y2 = santa.y + santa.height/2 - santa.offset
    overlapSanta = canvas.find_overlapping(x1, y1, x2, y2)
    # when santa didn't collide with anything
    if(len(overlapSanta) <= 2): return False
    else:
        # sets count to 1 if Santa collided with objects other
        # than the tree or the mountain
        canvas.data.count = 0
        if(canvas.data.game == "SIMPLE"):
            hintLine = canvas.find_withtag("hint")
            for over in overlapSanta:
                for pos in hintLine:
                    if(over == pos):
                        # touches the hint line
                        canvas.data.count = 1
        elif(canvas.data.game == "ARCADE"):
            presentCollision(canvas, overlapSanta)
            boosterCollision(canvas, overlapSanta)
            poisonCollision(canvas, overlapSanta)
        if(canvas.data.count == 0): return True
        else: return False

# changes the direction the tree is moving in the arcade mode   
def changeDirection(block):
    if(block.direction == "UP"):
        block.setDirection("DOWN")
    elif(block.direction == "DOWN"):
        block.setDirection("UP")

# checks if the tree hits a mountain
def hitMountain(canvas, block):
    xb = block.x1 + block.width/2
    yb1 = block.y1
    yb2 = block.y1 + block.height
    ym1 , ym2 = canvas.data.mRange.findY(xb)
    if(block.direction == "UP" and yb1 < ym1): return True
    if(block.direction == "DOWN" and yb2 > ym2): return True
    return False

def run():
    root = Tk()
    root.resizable(width=FALSE, height=FALSE)
    canvas = Canvas(root, width=1000, height=500)
    # Store canvas in root and in canvas itself for callbacks
    root.canvas = canvas.canvas = canvas
    # Set up canvas data and call init
    canvas.data = { }
    class Struct: pass
    canvas.data = Struct()
    init(canvas)
    # set up events
    root.bind("<KeyPress>", lambda event: keyPressed(canvas, event))
    root.bind("<KeyRelease>", lambda event :keyReleased(canvas, event))
    timerFired(canvas)
    # and launch the app
    root.mainloop()
    
run()
