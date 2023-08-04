from functools import reduce
from math import gcd


def solution(arrayA, arrayB):
    gA, gB = reduce(gcd, arrayA), reduce(gcd, arrayB)
    
    answer = []
    if all(each % gB for each in arrayA):
        answer.append(gB)
        
    if all(each % gA for each in arrayB):
        answer.append(gA)
        
    return max(answer) if answer else 0