# import turle_interpreter 
import turtle_interpreter
import shapes

# create a spiral
def spiral(x, y, size, angle ):
    if size <= 40:
        return 0

    s = shapes.circle( distance=2, color='grey')
    s.setStyle('jitter3')
    s.setWidth( 1 )
    s.draw(x, y, size, angle )
    spiral( x, y, size* 0.8, angle+22.5 )


def leg(x, y, scale):
    l= shapes.Hexagon1( color='brown')
    l.draw(x, y, scale, orientation=30)
    l.setStyle( 'jitter3' )
    l.setWidth( 3 )

def spiderhead(x, y, scale):
    s = shapes.circle2( color='brown')
    s.draw(x, y, scale, orientation=45)

def spiderbody(x, y, scale):
    s = shapes.circle2( color='brown')
    s.draw(x, y, scale, orientation=45)
    




#creates one tile 
def tile( x, y, scale ):
    s = shapes.Square()
    # s.setColor( (0.3, 0.4, 0.4 ) )
    star = shapes.Star()
    star.setColor((0.7, 0.2, 0.4))

    # s.draw(x, y, scale=0.8, orientation=45)
    star.draw(x+20, y, scale=1, orientation=45)
     
    return s
 
# # define the mosaic funtion that draws a 2D array of tiles Nx by Ny where each tile was the size of the scale by scale.
# def mosaic(x, y, scale, Nx, Ny ):
#     for row in range(Nx): # loop through the rows 
#         x = x + 50 # increases the distance in order to draw the next tile in the grid 
#         y = 50
#         for col in range(Ny): # loop though the columns 
#             tile(x, y, scale) # draw the tile
#             y = y - 110 # draws the tiles downwards in the columns

def spider(x, y, scale):
        spiral(0, 0, 200, 0)
        spiderhead(-150, 300, 0.3)
        spiderbody(-250, 300, 0.5)
        leg( -240,300,1 )
        leg( -230,300,1 )
        leg( -280,300,1 )
        leg( -290,300, 1 )
        leg( -300,300, 1 )
            
def main():
    # tile(-200, 100, 10)
    # call the mosaic funtion to draw the grid
    # tile(0,100, 5)
    # s = shapes.Square()
    # tile(-200,-100, 4)
    # tile(-200,0, 4)
   
    
    spider(-300, 200, 1)
    spider(300, -200, 1)




    



    # mosaic(-400,400, 10, 3, 3)


    # wait
    turtle_interpreter.TurtleInterpreter().hold()

if __name__ == '__main__':
    main()


