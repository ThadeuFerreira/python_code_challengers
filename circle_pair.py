#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'circles' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY circlePairs as parameter.
#

def isConcentric(c1,c2):
    return c1[0] == c2[0] and c1[1] == c2[1]

def calculateDistance(c1,c2):  
    distance = math.sqrt((c1[0]-c2[0])**2 + (c1[1]-c2[1])**2)
    return distance

def circles(circlePairs):
    # Write your code here
    for cp in circlePairs:
        x1 = cp[0]
        y1 = cp[1]
        r1 = cp[2]
        x2 = cp[3]
        y2 = cp[4]
        r2 = cp[5]
        max_r = max(r1,r2)
        min_r = min(r1,r2)
        if isConcentric([x1,y1],[x2,y2]):
            return 'Concentric'
        distance = calculateDistance([x1,y1],[x2,y2])
        if  distance == r1 + r2 or max_r == distance + min_r: 
            return 'Touching'
        if distance > r1 + r2:
            return 'Disjoint-Outside'
        
        if distance > max_r and max_r > distance - min_r:
            return 'Intersecting'
        
        
        