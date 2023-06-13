"""
현재 고속도로에 휴게소를 N개 가지고 있는데, 휴게소의 위치는 고속도로의 시작으로부터 얼만큼 떨어져 있는지로 주어진다. 다솜이는 지금 휴게소를 M개 더 세우려고 한다.
다솜이는 이 고속도로를 이용할 때, 모든 휴게소를 방문한다. 다솜이는 휴게소를 M개 더 지어서 휴게소가 없는 구간의 길이의 최댓값을 최소로 하려고 한다. (반드시 M개를 모두 지어야 한다.)
고속도로의 길이가 1000이고, 현재 휴게소가 {200, 701, 800}에 있고, 휴게소를 1개 더 세우려고 한다고 해보자.
일단, 지금 이 고속도로를 타고 달릴 때, 휴게소가 없는 구간의 최댓값은 200~701구간인 501이다. 하지만, 새로운 휴게소를 451구간에 짓게 되면, 최대가 251이 되어서 최소가 된다.

첫째 줄에 현재 휴게소의 개수 N, 더 지으려고 하는 휴게소의 개수 M, 고속도로의 길이 L이 주어진다.
둘째 줄에 현재 휴게소의 위치가 공백을 사이에 두고 주어진다. N = 0인 경우 둘째 줄은 빈 줄이다.
0 ≤ N ≤ 50
1 ≤ M ≤ 100
100 ≤ L ≤ 1,000
"""
import sys
input=sys.stdin.readline

n,m,l=map(int,input().split())
arr=list(map(int,input().split()))
arr.insert(0,0)
arr.append(l)
arr.sort()

res = 0

def count(mid):
    cnt=0
    for i in range(1, len(arr)):
        if arr[i]-arr[i-1]>mid:
            cnt+=(arr[i]-arr[i-1]-1)//mid
    return cnt

start=1
end=l-1
while start <= end:
    mid=(start+end)//2
    if count(mid)>m:
        start=mid+1
    else:
        end=mid-1
        res=mid
print(res)