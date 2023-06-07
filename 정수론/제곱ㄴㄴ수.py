"""
어떤 정수 X가 1보다 큰 제곱수로 나누어 떨어지지 않을 때, 그 수를 제곱ㄴㄴ수라고 한다.
제곱수는 정수의 제곱이다. min과 max가 주어지면, min보다 크거나 같고, max보다 작거나 같은 제곱ㄴㄴ수가 몇 개 있는지 출력한다.
1 ≤ min ≤ 1,000,000,000,000
min ≤ max ≤ min + 1,000,000
"""
import math
min,max=map(int, input().split())
checkList=[False]*(max-min+1)

for i in range(2, int(math.sqrt(max)+1)):
    pow=i*i  # 제곱수
    startIdx=int(min/pow)
    if min%pow!=0:
        startIdx+=1
    for j in range(startIdx,int(max/pow)+1):
        checkList[int(j*pow-min)]=True

cnt=0
for i in range(0,max-min+1):
    if not checkList[i]:
        cnt+=1
print(cnt)