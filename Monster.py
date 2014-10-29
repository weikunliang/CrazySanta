from Tkinter import *

class Monster(object):
    pass


from Tkinter import *
root = Tk()
canvas = Canvas(root, width=300, height=200)
canvas.pack()
canvas.create_line((0,0),(150,150), (200, 100), smooth = 1, dash= 1, tag = "a")
c = canvas.coords("a")
print c
root.mainloop()
