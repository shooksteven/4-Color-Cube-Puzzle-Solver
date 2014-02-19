'''
    @uthor: Steven Keith Shook II
    Date: 2/14/2014
    Purpose: Brute force the 4-cube color puzzle from a top down approach.
                Top down - meaning that all possible ways of positioning the cubes will be generated and then checked to see if they
                satisfy the win condition.

'''
__author__ = 'sshook'


class Colors:
    blue, green, red, yellow = range(4)

'''
class side:
    def __init__(self):

            Below is a drawing of a rolled out die
                [Front]
          [Left][Bottom][Right]
                [Back]
                [Top]

            Dies are represented by an array with the following format
            [front, left, bottom, right, back, top]


        #self.sides[6] = -1
        self.color = -1
        self.top = None
        self.bottom = None
        self.left = None
        self.right = None
'''

class cube:
    def __init__(self, front, left, bottom, right, back, top):
        self.top = top
        self.bottom = bottom
        self.left = left
        self.right = right
        self.front = front
        self.back = back

def printCube(cube):
    print "\t[", cube.front , ", " , cube.left , ", " , cube.bottom , ", " , cube.right , ", " , cube.back , ", " , cube.top , "]"


#initialize the cubes
cubes = []
cubes.append(cube(Colors.red, Colors.green, Colors.blue, Colors.yellow, Colors.green, Colors.red))
cubes.append(cube(Colors.green, Colors.green, Colors.yellow, Colors.red, Colors.yellow, Colors.blue))
cubes.append(cube(Colors.red, Colors.blue, Colors.blue, Colors.yellow, Colors.yellow, Colors.red))
cubes.append(cube(Colors.yellow, Colors.blue, Colors.blue, Colors.green, Colors.green, Colors.green))

print("\nAll cubes")
for cube in cubes:
    printCube(cube)


print("\nIterations of cube 1")
printCube(cubes[0])



