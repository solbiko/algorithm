# M이상 N 이하의 소수를 모두 출력 (1 ~ 1,000,000)
m, n = map(int, input().split())

#시간초과

list = [0] * (n+1)

for i in range(2, n+1):
    list[i] = i

for i in range(2, n+1):
    for j in range(i+1, n+1):
        if j % i == 0:
            list[j] = 0

for i in list:
    if i != 0 and i != 2:
        print(i)
