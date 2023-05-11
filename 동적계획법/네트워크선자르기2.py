# Top-Down
n=int(input())
d=[0]*(n+1)
d[1]=1
d[2]=2

def dfs(len):
    if d[len]>0:
        return d[len]

    if len==1 or len==2:
        return len
    else:
        d[len]=dfs(len-1)+dfs(len-2)
        return d[len]

print(dfs(n))