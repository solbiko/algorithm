answer = ''
def solution(n):
    
    def DFS(x):
        global answer
        if x == 0:
            return
        else:
            if x%3==0:
                DFS((x-1)//3)
                answer+='4'
            else:
                DFS(x//3)
                answer+=str(x%3)
                
    DFS(n)
    return answer