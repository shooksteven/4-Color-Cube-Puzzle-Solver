'''
    @uthor: Steven Keith Shook II
    Date: 2/14/2014
    Purpose: Brute force the 4-cube color puzzle from a top down approach.
            The idea is that each cube has two possible axis that can be thought of as rings.
            Each ring comprises of 4 sides.
            Iterating through both axis and all sides of the ring for all cubes should render every possible result of the puzzle.

            The axis are represented by the python deque object. This is very useful because of it's "rotate" function.

'''
__author__ = 'sshook'

from collections import deque
from sets import Set


class Colors:
    blue, green, red, yellow = range(4)

class cube:
    def __init__(self):
        self.axis = []
        pass

    def addAxis(self, side1, side2, side3, side4):
        self.axis.append(deque([side1, side2, side3, side4]))

#initialize the cubes
cubes = []
for i in range(4):
    cubes.append(cube())

cubes[0].addAxis(Colors.green, Colors.yellow, Colors.red, Colors.red)
cubes[0].addAxis(Colors.blue, Colors.yellow, Colors.yellow, Colors.red)

cubes[1].addAxis(Colors.green, Colors.green, Colors.red, Colors.yellow)
cubes[1].addAxis(Colors.blue, Colors.green, Colors.red, Colors.yellow)

cubes[2].addAxis(Colors.red, Colors.green, Colors.blue, Colors.green)
cubes[2].addAxis(Colors.yellow, Colors.green, Colors.blue, Colors.green)

cubes[3].addAxis(Colors.blue, Colors.yellow, Colors.red, Colors.yellow)
cubes[3].addAxis(Colors.blue, Colors.yellow, Colors.yellow, Colors.yellow)


#convert the deque back into a list
#print list(cubes[0].axis[0])

#contains every possible solution for each cube
everyPossible = []

#Generate all possible positions for each cube
for i, cube in enumerate(cubes):

    #this will hold every possible rotation for this cube
    possibleSolutions = []
    #print "\nCube ", (i+1)

    #for each axis (2 of them) rotate the cube to find every possible position
    for k, axis in enumerate(cube.axis):
        #print "\taxis ", (k+1)
        #rotate the appropriate number of times and then add it to the possibleSolutions array
        for j in range(len(axis)):
            #rotate the axis by one
            axis.rotate(1)
            #convert the deque back into a list and print
            #print "\t\t", list(axis)
            possibleSolutions.append(list(axis))
    everyPossible.append(possibleSolutions)

#print out every possible solution for each cube
print "\nNumber of cubes: ", len(everyPossible)
for i, cubeSolutions in enumerate(everyPossible):
    print "\nCube ", (i + 1)
    for k, solution in enumerate(cubeSolutions):
        print "\t", solution


#run every solution against the other cubes
print "\n\nComputing final solution!"

for ring1 in everyPossible[0]:
    #print ring1
    for ring2 in everyPossible[1]:
        #print "\t", ring2
        for ring3 in everyPossible[2]:
            #print "\t\t", ring3
            for ring4 in everyPossible[3]:
                #print"\t\t\t", ring4
                #check to see if this game is valid (no duplicates in the columns)
                #add each column into a set, if all columns are 4 then we have a WINNER!   This is because sets don't allow duplicates
                badFlag = 0
                for idx in range(4):
                    column1 = Set([ring1[0], ring2[0], ring3[0], ring4[0]])
                    column2 = Set([ring1[1], ring2[1], ring3[1], ring4[1]])
                    column3 = Set([ring1[2], ring2[2], ring3[2], ring4[2]])
                    column4 = Set([ring1[3], ring2[3], ring3[3], ring4[3]])

                    if len(column1) == 4 and len(column2) == 4 and len(column3) == 4 and len(column4) == 4:
                        print "WINNER"
                        print ring1
                        print ring2
                        print ring3
                        print ring4
                        exit()







