import pgzrun

WIDTH = 500
HEIGHT = 500

width = 400
height = 300

def draw():
    screen.clear()
    rect = Rect((0,0),(width,height))
    rect = 150, 150
    screen.draw.rect(rect,("white"))

pgzrun.go()