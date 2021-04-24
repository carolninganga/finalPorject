
# Caroline Ninganga
# final Project Forest scene 
# This scene draws a forest with mountains at the top. I also included a road which I added different 
# shapes to the shapes file to helps me create the scene.
# 04/23/2021


# import the differnt packages shapes and tree
import shapes
import tree

# define scene function 
def scene1():
    
    # call the rectangle shape for the road 
    road = shapes.Rectangle(color="grey") #give it the color grey
    road.setStyle('jitter3') #add jitter3 style
    # s.setColor( (0.3, 0.5, 0.3) )
    road.draw(-100, -550, scale=2, orientation=135)

    # draw a line to paint the marks of the road 
    line = shapes.Line(color="white") # import line from shapes
    line.setStyle('normal') # set the style to jitter 
    line.setWidth(11) # set the width to 11
    line.draw(-100, -400, scale=0.7, orientation=45) # white line
    line.draw(0, -300, scale=0.7, orientation=45) 
    line.draw(100, -200, scale=0.7, orientation=45)
    line.draw(200, -100, scale=0.7, orientation=45)
    line.draw(300, 0, scale=0.7, orientation=45)

    # call triangle shape for the mountains
    t = shapes.Triangle() # import triangle from shapes
    t.setStyle( 'jitter3') #add jitter3 style
    t.setColor( (0.5, 0.4, 0.4) )
    t.draw(-200, 120, scale=2, orientation=180) # draw the mountain
    t.draw(-90, 120, scale=2, orientation=180)
    t.draw(-0, 120, scale=2, orientation=180)
    t.draw(90, 150, scale=2, orientation=180)
    t.draw(180, 120, scale=2, orientation=180)


    # import tree from the Tree file
    tr = tree.Tree( distance=5, angle=25, color='green', iterations=5, filename='systemFL.txt' )
    tr.setStyle( 'jitter' ) # set style to jitter

    # draw trees below the moutains
    tr.draw(-300, -150, scale=0.7, orientation=90) 
    tr.draw(-310, -250, scale=0.5, orientation=90)
    tr.draw(-0, -100, scale=0.5, orientation=90)
    tr.draw(-360, -90, scale=0.7, orientation=90) 
    tr.draw(-50, -90, scale=0.5, orientation=90)
    tr.draw(-40, -200, scale=0.5, orientation=90)
    tr.draw(-300, -210, scale=0.7, orientation=90) 
    tr.draw(-310, -330, scale=0.5, orientation=90)
    tr.draw(-350, -340, scale=0.5, orientation=90)
    tr.draw(-360, -200, scale=0.7, orientation=90) 
    tr.draw(-210, -320, scale=0.5, orientation=90)
    tr.draw(-200, -300, scale=0.5, orientation=90)

    tr.draw(-110, 0, scale=0.5, orientation=90)
    tr.draw(-260, 0, scale=0.7, orientation=90) 
    tr.draw(110, 0, scale=0.5, orientation=90)
    tr.draw(100, 50, scale=0.5, orientation=90)

    # draw trees in different locations on the bottom right corner 
    tr.draw(360, -250, scale=0.7, orientation=90) 
    tr.draw(220, -300, scale=0.5, orientation=90)
    tr.draw(300, -350, scale=0.5, orientation=90)
  
    # wait
    tr.hold()

if __name__ == '__main__':
    scene1()


