""""
철수는 계단을 오를 때 한 번에 한 계단 또는 두 계단씩 올라간다.
만약 총 4계단을 오른다면 그 방법의 수는 1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2 로 5가지이다.
그렇다면 총 N계단일 때 올라가는 방법의 수를 출력

계단의 개수인 자연수 N(3≤N≤45)
"""
n = int(input())
d = [0]*(n+1)


def dfs(len):
    if d[len] > 0:
        return d[len]
    if len == 1 or len == 2:
        return len
    else:
        d[len] = dfs(len-1) + dfs(len-2)
        return d[len]

print(dfs(n))