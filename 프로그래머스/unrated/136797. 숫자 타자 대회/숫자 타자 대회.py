import sys, math
sys.setrecursionlimit(200000)
from collections import defaultdict
cache = defaultdict(dict)


W = [
    [1, 7, 6, 7, 5, 4, 5, 3, 2, 3], # 0
    [7, 1, 2, 4, 2, 3, 5, 4, 5, 6], # 1
    [6, 2, 1, 2, 3, 2, 3, 5, 4, 5], # 2
    [7, 4, 2, 1, 5, 3, 2, 6, 5, 4], # 3
    [5, 2, 3, 5, 1, 2, 4, 2, 3, 5], # 4
    [4, 3, 2, 3, 2, 1, 2, 3, 2, 3], # 5
    [5, 5, 3, 2, 4, 2, 1, 5, 3, 2], # 6
    [3, 4, 5, 6, 2, 3, 5, 1, 2, 4], # 7
    [2, 5, 4, 5, 3, 2, 3, 2, 1, 2], # 8
    [3, 6, 5, 4, 5, 3, 2, 4, 2, 1], # 9
] # W[i][j] : i번째 숫자에서 j번째 숫자로 이동하여 누를 때의 가중치

def solution(numbers):

    def solve(i, left, right):

        if i==len(numbers):
            return 0
        
        if (left, right) in cache[i]:
            return cache[i][(left, right)]
    
        w=math.inf
        num=numbers[i]
        if num!=left: # 오른손 이동
            w=min(w, solve(i+1,num,left)+W[right][num])
        if num!=right: # 왼손 이동
            w=min(w, solve(i+1,num,right)+W[left][num])

        cache[i][(left, right)] = w
        
        return w

    numbers = list(int(x) for x in numbers)
    
    return solve(0,4,6)  # 최소한의 시간으로 타이핑을 하는 경우의 가중치 합