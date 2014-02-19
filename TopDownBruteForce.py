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


class Die:
    '''
        Below is a drawing of a rolled out die
            [Front]
      [Left][Bottom][Right]
            [Back]
            [Top]

        Dies are represented by an array with the following format
        [front, left, bottom, right, back, top]
    '''
    sides[4] = -1
    front = -1
    left = -1
    bottom = -1
    right = -1
    back = -1
    top = -1


print Colors.red

#hi amber!
