from math import floor, sqrt, ceil
def solution(r1, r2):
    
    tmp=0
    for x in range(1, r2+1):
        y2= floor(sqrt(pow(r2, 2)-pow(x, 2)))
        y1= ceil(sqrt(r1**2-x**2)) if r1 > x else 0
        tmp+=y2-y1+1
    
    return tmp*4