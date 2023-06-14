"""
베르트랑 공준은 임의의 자연수 n에 대하여, n보다 크고, 2n보다 작거나 같은 소수는 적어도 하나 존재한다는 내용을 담고 있다.
10보다 크고, 20보다 작거나 같은 소수는 4개가 있다. (11, 13, 17, 19)
14보다 크고, 28보다 작거나 같은 소수는 3개가 있다. (17,19, 23)
자연수 n이 주어졌을 때, n보다 크고, 2n보다 작거나 같은 소수의 개수를 구하는 프로그램
입력의 마지막에는 0
1 ≤ n ≤ 123,456

1
10
13
100
1000
10000
100000
0
"""
import math

m=123456*2
list = [0] * (m+1)

for i in range(2, m+1):
    list[i] = i

for i in range(2, int(math.sqrt(m))+1):
   if list[i] == 0:
       continue
   for j in range(i+i, m+1, i):
       list[j] = 0

while True:
    n=int(input())
    if n==0:
        break

    cnt=0
    if n<3:
        cnt=1
    else:
        for i in range(n,2*n+1):
            if list[i]!=0 and n!=list[i]:
                cnt+=1
    print(cnt)

