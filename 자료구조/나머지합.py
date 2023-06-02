"""
수 N개 A1, A2, ..., AN이 주어진다. 이때, 연속된 부분 구간의 합이 M으로 나누어 떨어지는 구간의 개수를 구하는 프로그램을 작성하시오.
즉, Ai + ... + Aj (i ≤ j) 의 합이 M으로 나누어 떨어지는 (i, j) 쌍의 개수를 구해야 한다.

첫째 줄에 N과 M이 주어진다. (1 ≤ N ≤ 106, 2 ≤ M ≤ 103)

둘째 줄에 N개의 수 A1, A2, ..., AN이 주어진다. (0 ≤ Ai ≤ 109)
첫째 줄에 연속된 부분 구간의 합이 M으로 나누어 떨어지는 구간의 개수를 출력한다.

5 3
1 2 3 1 2
"""
import sys
input=sys.stdin.readline

n,m=map(int, input().split())
# 입력 리스트
a=list(map(int, input().split()))

# 합배열
s=[0]*n
s[0]=a[0]
for i in range(1,n):
    s[i]=s[i-1]+a[i]

c=[0]*m # 같은 나머지의 인덱스 카운트
# 합배열의 나머지 값이 같으면 두개 뽑아서 합배열값-합배열값으로 나누어떨어지는 구간 구 할 수 있음

cnt=0
for i in range(n):
    k=s[i]%m # 합배열 값을 m으로 나눈 나머지
    if k==0: # 합배열 값(0~i까지 합)이 m으로 나누어떨어짐
        cnt+=1
    c[k]+=1

for i in range(m):
    if c[i]>1:
        cnt+= (c[i]*(c[i]-1)//2) # iC2 : 2가지를 뽑는 경우의 수를 정답에 더함

print(cnt)

