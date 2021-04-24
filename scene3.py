# Caroline Ninganga
# Project09 
# Version 3 
# 03/29/2021

# import turle_interpreter 
import turtle_interpreter
import shapes


def topOfDoor(x, y, scale):

    c = shapes.circle2()
    c.setDistance(60)
    c.draw(x, y, scale=1, orientation=90)

    return c

def bottomOfDoor(x, y, scale):

    b = shapes.rectangle1()
    b.draw(x, y, scale=1, orientation=90)

    return b

#creates one tile 
def tile( x, y, scale ):
    s = shapes.Hexagon()
    s.setColor( (0.3, 0.6, 0.2 ) )
    star = shapes.Star()
    s.setColor((0.2, 0.2, 0.4))
    s.draw(x, y, scale=0.8, orientation=90)
    star.draw(x+30, y+30, scale=0.3, orientation=90)
    
    return s
 
# define the mosaic funtion that draws a 2D array of tiles Nx by Ny where each tile was the size of the scale by scale.
def mosaic(x, y, scale, Nx, Ny, orientation=45 ):
    for row in range(Nx): # loop through the rows 
        x = x + 100 # increases the distance in order to draw the next tile in the grid 
        y = -100
        for col in range(Ny): # loop though the columns 
            tile(x, y, scale) # draw the tile
            y = y - 110 # draws the tiles downwards in the columns
            
def main():
    # tile(-200, 100, 10)
    # call the mosaic funtion to draw the grid
    mosaic(-450,-300, 2, 3, 3)

    topOfDoor(-350, 100, 2)
    bottomOfDoor(-350, 0, 4)

    # wait
    turtle_interpreter.TurtleInterpreter().hold()

if __name__ == '__main__':
    main()




    