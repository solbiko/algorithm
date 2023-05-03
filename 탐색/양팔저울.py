"""
무게가 서로 다른 K(3<=K<=13)개의 추, 모든 추 무게의 합 S

{1, 5, 7}이면 S=13이고, 그릇에 담을 수 있는 물의 무게는 {1, 2, 3, 4, 5, 6, 7, 8, 11, 12, 13}이고,
1부터 S사이에서 무게에서 9와 10에 대응하는 무게의 물을 담을 수 없다.
"""
n=int(input())
arr=list(map(int, input().split()))
s=sum(arr)

res=set()
def dfs(idx, sum):
    global res
    if idx==n:
        if 0<sum<=s:
            res.add(abs(sum))
    else:
        dfs(idx+1, sum+arr[idx]) # 왼쪽에 놓는 경우
        dfs(idx+1, sum-arr[idx]) # 오른쪽에 놓는 경우
        dfs(idx+1, sum) # 사용하지 않는 경우

dfs(0,0)
# print(res)
print(s-len(res))