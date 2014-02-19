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

'''
#Prints all axis for each cube
for i, cube in enumerate(cubes):
    print "\nCube ", (i+1)
    for axis in cube.axis:
        #convert the deque back into a list
        print list(axis)
'''


for i, cube in enumerate(cubes):
    print "\nCube ", (i+1)
    for axis in cube.axis:
        for i in range(len(axis)):
            #rotate the axis by one
            cubes[0].axis[0].rotate(1)
            #convert the deque back into a list and print
            print list(cubes[0].axis[0])


'''
#rotate the axis
#print list(cubes[0].axis[0])
for i in range(len(cubes[0].axis[0])):
    #rotate the axis by one
    cubes[0].axis[0].rotate(1)
    #convert the deque back into a list and print
    print list(cubes[0].axis[0])
'''








