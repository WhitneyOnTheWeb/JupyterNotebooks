"""
**Author:**   Whitney King / @whitneyontheweb
**Project:**  LRU Cache Task
**Date:**     2/21/2018
**Language:** Python 2.7.13
"""

from functions import Cache
import functions

class Main(object):

    # Create varaibles to hold text file inputs and outputs
    input = open('stdin.txt', 'r')
    inputs = input.readlines()
    output = open('stdout.txt', 'w').close()
    output = open('stdout.txt', 'w')
    

    for i in range(len(inputs) - 1):
        #Trim text formatting from input items
        inputs[i] = inputs[i][:-1]

    # Check to make sure SIZE is specified on the first line of the input
    size = inputs.pop(0)
    if size[0:4] == 'SIZE':
        size = size[5:]
        c = Cache(size)
        output.write('SIZE OK\n')

        for i in range(len(inputs)):
            parse = inputs[i].split(' ')
            if parse[0] == 'GET':
                if len(parse) >= 3:
                    output.write('ERROR\n')
                output.write(c.get(parse[1]))
            elif parse[0] == 'SET':
                output.write(c.set(parse[1], parse[2]))
            elif parse[0] == 'EXIT':
                exit()
            else:
                output.write('ERROR\n')