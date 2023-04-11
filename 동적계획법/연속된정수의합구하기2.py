n = int(input())
list = list(map(int, input().split()))

# 왼쪽부터 최대 연속합
L=[0]*n
L[0]=list[0]
result=L[0]

for i in range(1, n):
    L[i] = max(list[i], L[i-1]+list[i])
    result=max(result, L[i]) # 1개도 삭제하지 않았을 때 최댓값
# print(L)


# 오른쪽부터 최대 연속합
R=[0]*n
R[n-1]=list[n-1]

for i in range(n-2, -1, -1):
    R[i] = max(list[i], R[i+1]+list[i])
# print(R)


# print(result)

# 수열에서 i삭제 시 최대 연속합
for i in range(1, n-1):
    tmp = L[i-1]+R[i+1]
    result=max(result, tmp)

print(result)
