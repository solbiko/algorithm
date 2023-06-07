"""
어떤 수가 소수의 N제곱(N ≥ 2) 꼴일 때, 그 수를 거의 소수라고 한다.
두 정수 A와 B가 주어지면, A보다 크거나 같고, B보다 작거나 같은 거의 소수가 몇 개인지 출력
1 ≤ A ≤ B ≤ 10^14
5324 894739
183
"""
import math
min,max=map(int, input().split())
a=[0]*(10000001) # 10^7

for i in range(2, len(a)):
    a[i] = i

# 제곱근까지만 수행 : n보다 작은 수 가운데 소수가 아닌 수는 항상 n보다 작은 약수를 가짐
for i in range(2, int(math.sqrt(len(a))+1)):
   if a[i] == 0:
       continue
   for j in range(i+i, len(a), i):
       a[j] = 0


cnt=0
# for i in range(2, len(a)):
#     if a[i] != 0:
#         tmp=a[i]
#         while a[i]*tmp<=max:
#             if min<=a[i]*tmp:
#                 cnt+=1
#             tmp=tmp*a[i]

# 변수 표현 범위를 넘어갈 수 있어 이항 정리로 처리
for i in range(2,10000001):
    if a[i]!=0:
        tmp=a[i]
        while a[i]<=max/tmp:
            if a[i]>=min/tmp:
                cnt+=1
            tmp=tmp*a[i]
print(cnt)


