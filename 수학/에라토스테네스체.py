"""
N, K가 주어졌을 때, K번째 지우는 수를 구하는 프로그램을 작성하시오.
"""
n,k = map(int, input().split())

list = [0] * (n+1)
for i in range(2, n+1):
    list[i]=i

cnt=1  # 1 지움
ch=True
for i in range(2, n+1):
    if ch:
        for j in range(i, n+1, i):
            if list[j]!=0:
                if cnt==k:
                    print(j)
                    ch=False
                    break
                cnt += 1
                list[j]=0
