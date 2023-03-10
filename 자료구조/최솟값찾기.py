# n, L(1~5,000,000) 입력
n, L = map(int, input().split())
list = list(map(int, input().split()))
d = [0]*n

# i-L+1 ~ i 중 최솟값 Di
# D에 저장된 수 출력

#12 3
# 1 5 2 3 6 2 3 7 3 5 2 6

for i in range(n):
    e = i if i >= 0 else 0
    s = i-L+1 if i-L+1 >= 0 else 0

    nList = list[s:e+1]
    d[i] = min(nList)

for i in d:
    print(i, end=' ')

# 시간초과