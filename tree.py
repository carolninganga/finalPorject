# Caroline Ninganga
# Project10 
# Version 5
# 04/09/2021

import lsystem as ls
import shapes as shp
import turtle_interpreter as ti

# create a class tree 
class Tree(shp.Shape):

    #define the init method with the specified parameters which are also known as the objects of the field
    def __init__(self, distance=5, angle=22.5, color=(0.5, 0.4, 0.3), iterations=3, filename=None):
        shp.Shape.__init__(self, distance, angle, color) # call the parent shape init method with distance, angle and color
        self.iterations = iterations
        self.ls = ls.Lsystem(filename) 
    
    def setIterations(self, N):
        # given a new number of iterations in N, assign it to the iterations field of the object
        self.iterations = N

    def read(self, filename):
        # use the Lsystem object created and stored in the lsystem field to call the read method
        self.ls.read(filename)

    #use the lsystem draw method
    def draw(self, xpos, ypos, scale=1.0, orientation=90):
        # use the buildstring method to from the lsystem file and asign newStr to method
        newStr = self.ls.buildString(self.iterations)
        self.string = newStr
        shp.Shape.draw(self, xpos, ypos, scale, orientation)

#Test function for the tree shape in 3 different locations. est method should take in an Lsystem filename as a parameter, 
#create a Tree object, and then use the Tree object's draw method to draw at least 3 trees in different locations. 
def test():

    tr = Tree( filename='systemJ.txt') # asign tr to the tree object 
    tr.setColor( (0.5, 0.3, 0.4) )
    tr.draw(-200, -200, scale=2, orientation=90) # call the draw function for the first tree 
    tr.draw(50, 100, scale=2, orientation=90) # call the draw function for the second tree 
    tr.draw(300, -150, scale=2, orientation=90) # call the draw function for the third tree 

     # wait
    ti.TurtleInterpreter().hold()

if __name__ == '__main__':
    test()



