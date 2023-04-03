import sys
input=sys.stdin.readline
sys.setrecursionlimit(10000)

a=list(input())
a.pop()
b=list(input())
b.pop()

# 점화식 테이블
d=[[0 for j in range(len(b)+1)] for i in range(len(a)+1)]

# LCS 저장 리스트
res=[]

for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):
        if a[i-1] == b[j-1]:
            d[i][j]= d[i-1][j-1]+1
        else:
            d[i][j] = max(d[i-1][j],d[i][j-1])

# lcs 길이 출력
print(d[len(a)][len(b)])

# lcs
def lcs(r, c):
    if r==0 or c==0:
        return
    if a[r-1]==b[c-1]:
        res.append(a[r-1])
        lcs(r-1, c-1)
    else:
        if d[r-1][c] > d[r][c-1]:
            lcs(r-1, c)
        else:
            lcs(r, c-1)


lcs(len(a), len(b))

# lcs 문자열 출력
for i in range(len(res)-1, -1, -1):
    print(res.pop(i), end='')



