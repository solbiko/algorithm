"""
N개의 수로 된 수열 A[1], A[2], ..., A[N] 이 있다.
이 수열의 i번째 수부터 j번째 수까지의 합 A[i]+A[i+1]+...+A[j-1]+A[j]가 M이 되는 경우의 수를 구하는 프로그램을 작성하시오.

첫째 줄에 N(1≤N≤10,000), M(1≤M≤300,000,000)이 주어진다
다음 줄에는 A[1], A[2], ..., A[N]이 공백으로 분리되어 주어진다. 각각의 A[x]는 30,000을 넘지 않는 자연수
8 3
1 2 1 3 1 1 1 2
"""
n,m = map(int, input().split())
a = list(map(int, input().split()))

# 투 포인터
l=0
r=1
cnt=0

sum=a[0]
while True:
    if sum<m:
        if r<n:
            sum+=a[r]
            r+=1
        else: # 작은데 더이상 더할 것이 없음
            break
    elif sum==m:
        cnt+=1
        # 계속 진행해야 하기 때문에
        sum-=a[l]
        l+=1
    else:
        sum-=a[l]
        l+=1
    print(sum)

print(cnt)