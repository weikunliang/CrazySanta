from Tkinter import*

class Score(object):
    
    x = 350   
    y = 250
    
    # draws the board and fills it with information
    def drawBoard(self, canvas, score, best, image, performance, present = ""):
        if(canvas.data.game == "ARCADE"): bonus = present*10
        else: bonus = 0
        canvas.create_image(self.x, self.y, image = image)
        scoreText = "Distance Travelled = " + str(score-bonus) + "m"
        bestScoreText = "Best Score = " + str(best) + "m"
        canvas.create_text(460, 180, text = "Game  Over!",
                           font="Calibri 28 bold", fill = "black")
        canvas.create_text(460, 210, text = scoreText,
                           font="Calibri 14 bold", fill = "black")
        canvas.create_text(460, 230, text = bestScoreText,
                           font="Calibri 14 bold", fill = "black")
        if(canvas.data.game == "SIMPLE" and canvas.data.hint):
            canvas.create_text(460, 270, text = "PERFORMANCE:",
                               font="Calibri 14 bold", fill = "black")
            canvas.create_text(460, 290, text = performance + "%",
                               font="Calibri 14 bold", fill = "black")
        if(canvas.data.game == "ARCADE"):
            presentText = "Collected Present: " + str(present)
            final = "Final Score = " + str(score)
            canvas.create_text(460, 250, text = presentText,
                               font="Calibri 14 bold", fill = "black")
            canvas.create_text(460, 280, text = final, 
                               font="Calibri 14 bold", fill = "black")