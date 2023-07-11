import math
def solution(n,a,b):
    answer = 0
    
    def search(x,y,cnt):
        x2=x/2
        y2=y/2
        if x2==y2:
            return cnt-1
        else:
            return search(math.ceil(x2),math.ceil(y2), cnt+1)

    return search(a,b,1)