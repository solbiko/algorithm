cnt=0
def solution(numbers, target):
    n=len(numbers)
    
    i=0
    def dfs(i, sums):
        global cnt
        if i==n:
            if sums==target:
                cnt+=1
            return 
        else:
            dfs(i+1, sums+numbers[i])
            dfs(i+1, sums-numbers[i])

    dfs(0,0)
    return cnt