from itertools import permutations
import math
def solution(numbers):
    answer={}
    
    nums=[]
    for i in range(1,len(numbers)+1):
        nums+=permutations(numbers, i)
    
    for x in nums:
        n=int("".join(x))

        if n<2:
         continue
        
        flag = True
        for j in range(2, int(math.sqrt(int(n)) + 1)):
            if int(n) % j == 0:
                flag = False
                break
       
        if flag:
            answer[n]=1

    return len(answer)