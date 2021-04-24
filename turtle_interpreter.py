# Caroline Ninganga
# Project10 
# Version 5
 

#import the turtle package, the random and sys packages
import turtle as t
import sys
import random

#define a TurtleInterpreter
class TurtleInterpreter:
    initialized = False
    #define the init
    def __init__(self, dx = 800, dy = 800):

        #add two fields to the object called style and jitterSigma
        self.style = 'normal'
        self.jitterSigma = 4
        self.dotSize = 1

        #add 
        #This helps the __init__ method to not create another turtle window if it already exists.
        if TurtleInterpreter.initialized:
            return
        TurtleInterpreter.initialized = True
        # call turtle.setup with dx and dy as the arguments
        t.setup( dx, dy )
        # set the turtle tracer to false (optional)
        t.tracer( False )

     #create a mutator . Then create a mutator method def setJitter(self, j) that assigns 
     # the jitterSigma field the value of the parameter j. Write get methods for both parameters 
     # as well.


    # create a method def setStyle(self, s) that assigns the style field the value 
    # of the parameter s
    def setStyle(self, s):
        self.style = s

    # define the setDotSize method
    def setDotSize(self, d):
        self.dotSize = d

    def setJitter(self, j ):
        self.jitterSigma = j

    def getStyle(self):
        return self.setStyle

    def getJitter(self):
        return self.jitterSigma

    def getDotSize(self):
        return self.dotSize

    
    def forward(self, distance):
        # if self.style is equal to 'jitter'
        if self.style == 'jitter':
            # assign to x0 and y0 the result of turtle.position()
            x0, y0 = t.position()
            # pick up the turtle
            t.up()
            # have the turtle go forward by distance
            t.forward( distance )
            # assign to xf and yf the result of turtle.position()
            xf, yf = t.position()
            # assign to curwidth the result of turtle.width()
            curwidth = t.width()

            # assign to jx the result of random.gauss(0, self.jitterSigma)
            jx = random.gauss( 0, self.jitterSigma )
            # assign to jy the result of random.gauss(0, self.jitterSigma)
            jy = random.gauss( 0, self.jitterSigma ) 
            # assign to kx the result of random.gauss(0, self.jitterSigma)
            kx = random.gauss( 0, self.jitterSigma )
            # assign to ky the result of random.gauss(0, self.jitterSigma)
            ky = random.gauss( 0, self.jitterSigma )

            # set the turtle width to (curwidth + random.randint(0, 2))
            t.width(curwidth + random.randint(0, 2))
            # have the turtle go to (x0 + jx, y0 + jy)
            t.goto(x0 + jx, y0 + jy)
            # put the turtle down
            t.down()
            # have the turtle go to (xf + kx, yf + ky)
            t.goto(xf + kx, yf + ky)
            # pick up the turtle
            t.up()
            # have the turtle go to (xf, yf)
            t.goto( xf, yf )
            # set the turtle width to curwidth
            t.width( curwidth )
            # put the turtle down
            t.down()

        elif self.style == 'jitter3':
            # Part 1: Figure out and store the true start point, true end point, and 
              #optionally the current turtle width, heading, and color (if they are modified).
               # assign to x0 and y0 the result of turtle.position()
            x0, y0 = t.position()
            # pick up the turtle
            t.up()
            # have the turtle go forward by distance
            t.forward( distance )
            # assign to xf and yf the result of turtle.position()
            xf, yf = t.position()
            # assign to curwidth the result of turtle.width()
            curwidth = t.width()

            # curheading = t.heading()

            #color = t.color()

            # Part 2: Draw the alternative visual representation.  This might involve 
              #a for loop if, for example, you want to draw three jittered lines.
              #Be sure to generate new random numbers for each separate element/loop.
            for i in range(3):
                # assign to jx the result of random.gauss(0, self.jitterSigma)
                jx = random.gauss( 0, self.jitterSigma )
                # assign to jy the result of random.gauss(0, self.jitterSigma)
                jy = random.gauss( 0, self.jitterSigma ) 
                # assign to kx the result of random.gauss(0, self.jitterSigma)
                kx = random.gauss( 0, self.jitterSigma )
                # assign to ky the result of random.gauss(0, self.jitterSigma)
                ky = random.gauss( 0, self.jitterSigma )
            
                # Part 3: Pick up the pen and go to the true end point, resetting the width, 
                #heading, and color to their original values if they were modified
                # set the turtle width to (curwidth + random.randint(0, 2))
                t.width(curwidth + random.randint(0, 2))
                # have the turtle go to (x0 + jx, y0 + jy)
                t.goto(x0 + jx, y0 + jy)
                # put the turtle down
                t.down()
                # have the turtle go to (xf + kx, yf + ky)
                t.goto(xf + kx, yf + ky)
                # pick up the turtle
                t.up()

            #step3 
            # have the turtle go to (xf, yf)
            t.goto( xf, yf )
            # set the turtle width to curwidth
            t.width( curwidth )
            # put the turtle down
            t.down()


        #Create a 'dotted' style that draws a series of circles separated by spaces. 
        # The circles do not need to be in a straight line or all be the same size.

        #Create a field in the TurtleInterpreter to hold the dotSize 
        # (the suggested radius for the circles). Then write a setDotSize method in 
        # the TurtleInterpreter class and a setDotSize method and associated dotSize field in 
        # the Shape class, similar to the setStyle and setJitter methods in both classes.

        #The number of dots should vary with the distance being drawn. 
        # You are free to decide the dot spacing.

        #However you create your dotted line, make sure the turtle ends up in the 
        # same location and orientation as it would have if it drew just a straight line.
        # create a dotted style
        elif self.style == 'dotted':
            radius = self.dotSize # set the radius 
            spacing = 5 * radius*1

            # step 1: storing the anchor points 
            x0, y0 = t.position()
            t.up()
            t.forward( distance )
            xf, yf = t.position()
            curheading = t.heading()
            # curwidth = t.width()
            # curColor = t.color()
             
            #step 2: setup and loop
            steps = distance / spacing
            t.backward( distance )
            for i in range( int(steps)):
                t.down()
                t.circle( radius )
                t.up()
                t.forward( spacing )
        
                #step 3 restore everything
            t.goto( xf, yf )
            # curwidth = t.width()
            # t.setheading( curheading )
            t.down()
        
        # else
        else:
            # have the turtle go foward by distance
            t.forward( distance )
        return


    def drawString(self, string, distance, angle ):
        """ Interpret the characters in string as a series of turtle commands. Distance specifies the distance
        to travel for each forward command. Angle specifies the angle (in degrees) for each right 
        or left command. The list of turtle supported turtle commands is:
        F : forward
        - : turn right
        + : turn left
        [ : save the turtle's heading and position
        ] : restore the turtle's heading and position 
        """

        modval = None 
        modgrab = False
        # assign to stack the empty list
        stack = []
        #define a color stack
        colorstack = []
        # for each character d in string 
        for c in string :

            # if c is equal to '('
            if c == '(':
                # assign to modval the empty string
                modval = ""
                # assign to modgrab the value True
                modgrab = True
                # continue
                continue
            # else if c is equal to ')'
            elif c == ')':
                # assign to modval the result of casting modval to a float
                modval = float(modval)
                # assign to modgrab False
                modgrab = False
                # continue
                continue
            # else if modgrab (is True)
            elif modgrab == True:
                # add to modval the character c
                modval = modval + c
                # continue
                continue

            # if modval is equal to None
                # call self.forward with the argument distance
            # else
            # call self.forward with the argument distance * modval

            # if d is equal to 'F'
            if c == 'F' :
                if modval == None:
                    self.forward( distance )
                else:
                    self.forward( distance * modval )


            elif c == 'f':
                if modval == None:
                    self.forward( distance )
                else:
                    self.forward( distance * modval )
            # else if c is equal to '-'
            elif c == '-':
                if modval == None:
                    t.right( angle )
                else:
                    t.right( modval )
            # else if d is equal to '+'
            elif c == '+':
                if modval == None:
                    t.left( angle )
                else:
                    t.left( modval )
            #else if c == ! 
            elif c == '!':
                if modval == None:
                    w = t.width()
                    if w > 1:
                        t.width( w-1 )
                else: 
                    t.width( modval )
            # else if d is equal '['
            elif c == '[':
                # append to stack the position of the turtle (position method)
                stack.append(t.position())
                # append to stack the heading of the turtle (heading method)
                stack.append(t.heading())
            # else if c is  equal to ']'
            elif c == ']':
                # tell the turtle to pick up pen 
                t.up()
                # call the setheading method of the turtle and pass it the value popped off stack
                t.setheading( stack.pop())
                # call the goto method of the turtle and pass it the value popped of stack
                t.goto(stack.pop())
                # tell the turtlr to put down pen
                t.down()

            #'<' - the left angle bracket should push the current turtle color onto a color stack
            #this function returns a tuple of colors (two sub-lists of rgb values)
            elif c == '<':
                colorstack.append( t.color()[0] )
            
            #'>' - the right angle bracket should pop the current turtle color off the color stack and set the 
            # turtle's color to that value using the turtle.color function.
            elif c == '>':
                t.color(colorstack.pop())
            elif c == 'g':
                t.color(0.15, 0.5, 0.2)
            elif c == 'y':
                t.color(0.8, 0.8, 0.3)
            elif c == 'r':
                t.color(0.7, 0.2, 0.3)
            elif c == '{':
                t.begin_fill()
            elif c == '}':
                t.end_fill()
            modval = None

            #Add two cases to drawString. For the character '{' call turtle.begin_fill(), and for the character '}' call turtle.end_fill()            

        # call the turtle.update() (not in the for loop)
        t.update()

    def hold(self):
        '''Holds the screen open until user clicks or presses 'q' key'''

        # Hide the turtle cursor and update the screen
        t.hideturtle()
        t.update()

        # Close the window when users presses the 'q' key
        t.onkey(t.bye, 'q')

        # Listen for the q button press event
        t.listen()

        # Have the turtle listen for a click
        t.exitonclick()


    #def place(self, xpos, ypos, angle=None): - the method should pick up the pen, place the turtle at location (xpos, ypos), 
    # orient the turtle if the angle argument is not None, and then put down the pen.
    def place(self, xpos, ypos, angle=None):
        t.up()
        t.goto( xpos, ypos )
        if angle != None:
            self.orient( angle )
        # tell the turtlr to put down pen
        t.down()

    #def orient(self, angle): - the method should use the turtle's setheading function to set turtle's heading to the given angle.
    def orient( self, angle ):
        t.setheading(angle)

    #def goto(self, xpos, ypos): - the method should pick up the turtle, send the turtle to (xpos, ypos), and then put the pen down.
    def goto( self, xpos, ypos ):
        t.up()
        t.goto( xpos, ypos )
        t.down()

    #def setColor(self, c): - the method should call turtle.color() with the argument c to set the turtle's color.
    def setColor( self, c ):
        t.color( c )

    #def setWidth(self, w): - the method should call turtle.width() with the argument w to set the turtle's width.
    def setWidth( self, w ):
        t.width( w )
