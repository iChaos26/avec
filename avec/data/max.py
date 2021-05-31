
#!/bin/python3

import math
import os
import random
import re
import sys
import numpy as np

#
#Extra implementation with np:

def arrayMax(operations):
    return np.max(operations)
#
# Complete the 'getMax' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY operations as parameter.

# Esse teste possui um erro, pois ao converter o raw input em lista, 
# perde-se a capacidade de usa-lo como index. 
# É melhor usar o n como raw input

def getMax(operations):
    
    stack = [0]
    for i in range(int(input())):
        val = list(map(int, input().split()))
        if val[0] == 1:
            items.append(max(val[1], stack[-1]))
        elif val[0] == 2:
            stack.pop()
        else:
            print(items[-1])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

#    ops = []
#
#    for _ in range(n):
#        ops_item = input()
#        ops.append(ops_item)

    res = getMax(ops)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()

#! Vi essa solução no geeks for geeks e achei interessante, pois mantém um auxiliar no tracking do max element: https://www.geeksforgeeks.org/tracking-current-maximum-element-in-a-stack/
class StackWithMax:
    def __init__(self):
          
        # main stack 
        self.mainStack = [] 
      
        # tack to keep track of
        # max element 
        self.trackStack = []
  
    def push(self, x):
        self.mainStack.append(x) 
        if (len(self.mainStack) == 1):
            self.trackStack.append(x) 
            return
  
        # If current element is greater than 
        # the top element of track stack, 
        # append the current element to track 
        # stack otherwise append the element 
        # at top of track stack again into it. 
        if (x > self.trackStack[-1]): 
            self.trackStack.append(x) 
        else:
            self.trackStack.append(self.trackStack[-1])
  
    def getMax(self):
        return self.trackStack[-1]
  
    def pop(self):
        self.mainStack.pop() 
        self.trackStack.pop()
  
# Driver Code
if __name__ == '__main__':
  
    s = StackWithMax()
    s.push(20) 
    print(s.getMax()) 
    s.push(10) 
    print(s.getMax())
    s.push(50) 
    print(s.getMax())