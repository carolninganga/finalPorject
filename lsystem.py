# Caroline Ninganga
# Final Project
# 04/21/2021

import sys
import random 

class Lsystem: 

    # wirte a constructor 
    def __init__( self, filename=None):
         # assign to the field base, the empty string
         self.base = " "
         # assign to the field rules, the empty dictionary
         self.rules = {}
         # if the filename variable is not equal to None
         if filename != None:
            # call the read method of self with filename as the argument
            self.read( filename )

    # get the base value of the base field of the object
    def getBase(self):
        return self.base

    #get rule should return the specified rule of self
    def getRule(self, index):
        return self.rules[index]
    #the setBase function should assign to the base field (self.base) the value in b.
    def setBase(self, b):
        self.base = b
    #the addRule function should append newrule to the rules field of self
    def addRule(self, newrule):
        # mydict['F'] = ['FF', 'F+F-F']
        # mydict represents the dictionary object
        # 'F' represents the key
        # ['FF', 'F+F-F'] represents the value
        # rule = [symbol, replacement1, replacment2, ...]
        self.rules[newrule[0]] = newrule[1:] # Key = 0 and Value = [replacement1, replacement2,...]

    # numsRules retruns the number of rules in the rules list 
    def numRules(self):
        return len(self.rules)

    # write a read method
    def read( self, filename ):
        # assign to the rules field of self the empty list
        self.rules = {}
        # assign to a variable (e.g. fp) the file object created with filename in read mode
        fp = open(filename)
        # for each line in fp 
        for line in fp:
            # assign to line the result of calling line.strip()
            line = line.strip()
            # assign to a variable (e.g. words) the result of calling the split() method line
            words = line.split()
            # if the first item in words is equal to the string 'base'
            #print("Words: ", words)
            #words = ['base', base]
            #words = ['rule',[symbol, replacement]]
            if words[0] == 'base':
                # call the setBase method of self with the new base string
                self.setBase(words[1])
            # else if the first item in words is equal to the string 'rule'
            elif words[0] == 'rule':
                # call the addRule method of self with the new rule (the slice of words from index 1
                self.addRule(words[1:])

        # call the close method of the file
        fp.close()



    def replace(self, istring):
        """ Replace all characters in the istring with strings from the
            right-hand side of the appropriate rule. This version handles
            parameterized rules.
        """
        tstring = ''
        parstring = ''
        parval = None
        pargrab = False

        for c in istring:
            if c == '(':
                # put us into number-parsing-mode
                pargrab = True
                parstring = ''
                continue
            # elif the character is )
            elif c == ')':
                # put us out of number-parsing-mode
                pargrab = False
                parval = float(parstring)
                continue
            # elif we are in number-parsing-mode
            elif pargrab:
                # add this character to the number string
                parstring += c
                continue

            if parval != None:
                key = '(x)' + c
                if key in self.rules:
                    replacement = random.choice(self.rules[key])
                    tstring += self.substitute( replacement, parval )
                else:
                    if c in self.rules:
                        replacement = random.choice(self.rules[c])
                        tstring += self.insertmod( replacement, parstring, c )
                    else:
                        tstring += '(' + parstring + ')' + c
                parval = None
            else:
                if c in self.rules:
                    tstring += random.choice(self.rules[c])
                else:
                    tstring += c

        return tstring


    def substitute(self, sequence, value ):
        """ given: a sequence of parameterized symbols using expressions
            of the variable x and a value for x
            substitute the value for x and evaluate the expressions
        """

        expr = ''
        exprgrab = False

        outsequence = ''

        for c in sequence:

            # parameter expression starts
            if c == '(':
                # set the state variable to True (grabbing the expression)
                exprgrab = True
                expr = ''
                continue

            # parameter expression ends
            elif c == ')':
                exprgrab = False
                # create a function out of the expression
                lambdafunc = eval( 'lambda x: ' + expr )
                # execute the function and put the result in a (string)
                newpar = '(' + str( lambdafunc( value ) ) + ')'
                outsequence += newpar

            # grabbing an expression
            elif exprgrab:
                expr += c

            # not grabbing an expression and not a parenthesis
            else:
                outsequence += c 

        return outsequence

    def insertmod(self, sequence, modstring, symbol):
        """ given: a sequence, a parameter string, a symbol 
            inserts the parameter, with parentheses, 
            before each
            instance of the symbol in the sequence
        """
        tstring = ''
        for c in sequence:
            if c == symbol:
                # add the parameter string in parentheses
                tstring += '(' + modstring + ')'
            tstring += c
        return tstring





    def buildString(self, iterations):
        # assign to a local variable (e.g. nstring) the base field of self
        nstring = self.base
        # for the number of iterations
        for i in range(iterations):
            # assign to nstring the result of calling the replace method of self with nstring as the argument
            nstring = self.replace( nstring)
        # return nstring
        return nstring

def main(argv):

    # check the number of arguments entered by the user 
    if len(argv) < 2:
      print('Usage: lsystem.py <filename>')
      exit()

    filename = argv[1]
    iterations = 2

    lsys = Lsystem()

    lsys.read( filename )

    print( lsys )
    print( lsys.getBase() )
    for i in range( lsys.numRules() ):
      rule = lsys.getRule(i)
      print( rule[0] + ' -> ' + rule[1] )

    lstr = lsys.buildString( iterations )
    print( lstr )

    return

if __name__ == "__main__":
    main(sys.argv)
