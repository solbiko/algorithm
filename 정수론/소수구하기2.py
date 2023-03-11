import math
# M이상 N 이하의 소수를 모두 출력 (1 ~ 1,000,000)
m, n = map(int, input().split())

# 에라토스테네스 방식 : 배수 지우기
list = [0] * (n+1)

for i in range(2, n+1):
    list[i] = i

# 제곱근까지만 수행 : n보다 작은 수 가운데 소수가 아닌 수는 항상 n보다 작은 약수를 가짐
for i in range(2, int(math.sqrt(n))+1):
   if list[i] == 0:
       continue
   for j in range(i+i, n+1, i):
       list[j] = 0

for i in range(m, n+1):
    if list[i] != 0:
        print(list[i])
