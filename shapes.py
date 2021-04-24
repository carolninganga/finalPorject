# Caroline Ninganga
# Project09 
# Version 4 

import turtle_interpreter as ti

# class called shapes 
class Shape:

    def __init__(self, distance = 100, angle = 90, color = (0, 0, 0), istring = '' ):
        
        # create a field of self called distance and assign it distance
        self.distance = distance
        # create a field of self called angle and assign it angle
        self.angle = angle
        # create a field of self called color and assign it color
        self.color = color
        # create a field of self called string and assign it istring
        self.string = istring

        self.style = 'normal'
        self.jitterSigma = 2

        # create a field called dotSize 
        self.dotSize = 2
        self.width = 1

    # def hold(self):
    #     ti.TurtleInterpreter().hold()

    #setColor(self, c) - set the color field to c
    def setColor ( self, c ):
        self.color = c
    #setDistance(self, d) - set the distance field to d
    def setDistance( self, d) :
        self.distance = d
    #setAngle(self, a) - set the angle field to a
    def setAngle( self, a):
        self.angle = a 
    #setString(self, s) - set the string field to s
    def setString( self, s):
        self.string = s

    def setStyle(self, s ):
        self.style = s
    
    def setJitter( self, j ):
        self.jitterSigma = j

    # add setDotSize set method
    def setDotSize( self, d):
        self.dotSize = d

    def setWidth( self, w ):
        self.width = w

    def getJitter(self):
        return self.jitterSigma
    
    # add a getDotSize get method
    def getDotSize(self):
        return self.dotSize

    def getStyle( self):
        return self.setStyle

    def getWidth( self ):
        return self.setWidth


    def draw(self, xpos, ypos, scale=1.0, orientation=0):
        # create a TurtleInterpreter object
        
        #print("color: ", self.color, "string: ", self.string)
        shp = ti.TurtleInterpreter()
        # use the TurtleInterpreter object to place the turtle at (xpos, ypos, orientation)
        shp.place(xpos, ypos, orientation)
        # use the TurtleInterpreter object to set the turtle color to self.color
        shp.setColor( self.color )

        shp.setJitter( self.jitterSigma ) 

        shp.setStyle( self.style )

        shp.setDotSize( self.dotSize )


        shp.setWidth( self.width )
        # use the TurtleInterpreter object draw the string
        shp.drawString( self.string, self.distance*scale, self.angle )
        # Note: use the distance, angle, and string fields of self
        #    Note: multiply the distance by the scale parameter of the method

    # def hold(self):
    #     '''Holds the screen open until user clicks or presses 'q' key'''
    
    def hold(self):


        ti.TurtleInterpreter().hold()


class Line(Shape):
    def __init__(self, distance=100, color=(0,0,0)):
        # call the parent's __init__ method with self, distance, 
        Shape.__init__(self, distance, 90, color,'{F-}')


class Square(Shape):
    def __init__(self, distance=100, color=(0,0,0)):
        # call the parent's __init__ method with self, distance, 
        Shape.__init__(self, distance, 90, color,'{F-F-F-F-}')
        #an angle of 90, color, and the string 'F-F-F-F-'

class Rectangle1(Shape):
    def __init__(self, distance=100, color=(0,0,0)):
        # call the parent's __init__ method with self, distance, 
        Shape.__init__(self, distance, 90, color,'{F-FFF-F-FFF-}')
        # Shape.__init__(self, distance, 90, color,'{F-F}')

        #an angle of 90, color, and the string 'F-F-F-F-'

class Rectangle(Shape):
    def __init__(self, distance=100, color=(0,0,0)):
        # call the parent's __init__ method with self, distance, 
        Shape.__init__(self, distance, 90, color,'{F-FFFFF-F-FFFFF-}')
        #an angle of 90, color, and the string 'F-F-F-F-'

class Triangle(Shape):
    def __init__(self, distance=100, color=(0,0,0)):
        Shape.__init__(self, distance, 120, color, '{F-F-F}')

#created a hexagon which has the curly { } for the beginFill() and endFill() methods
class Hexagon(Shape):
    def __init__(self, distance=70, color=(0,0,0)):
        Shape.__init__(self, distance, 60, color, 'F-F-F-F-F-F')

class Hexagon1(Shape):
    def __init__(self, distance=70, color=(0,0,0)):
        Shape.__init__(self, distance, 60, color, 'F-F-F-F-')

#created a star shape
class Star(Shape):
    def __init__(self, distance=100, color=(0,0,0)):
        Shape.__init__(self, distance, 135, color, 'F-F-F-F-F-F-F-F-F')

#created a circle 
class circle(Shape):
    def __init__(self, distance=50, color=(0,0,0)):
        Shape.__init__(self, distance, 22.5, color, 'F-F-F-F-F-F-F-F-F-F-F-F-F-F-F-F')

#created a circle 
class circle2(Shape):
    def __init__(self, distance=50, color=(0,0,0)):
        Shape.__init__(self, distance, 22.5, color, '{F-F-F-F-F-F-F-F-F-F-F-F-F-F-F-F}')


#define a test method for the new shapes 
def test():

    #create the first shape hexagon
    h = Hexagon()
    h.setColor( (0.6, 0.8, 0.9) )
    h.draw( -300, 0, scale=0.6, orientation=12 )

    #create the first shape hexagon
    h = Star()
    h.setColor( (0.3, 0.9, 0.9) )
    h.draw( 0, 200, scale=1.2, orientation=12 )

     #create the first shape hexagon
    h = circle()
    h.setColor( (0.3, 0.9, 0.9) )
    h.draw( 200, 0, scale=0.6, orientation=12 )

      # wait
    ti.TurtleInterpreter().hold()


if __name__ == '__main__':
    test()