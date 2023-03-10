n = int(input())
list = list(map(int, input().split()))
list.sort()

cnt = 0

# 다른 두 수의 합인 수의 개수
for k in  range(n):
    val = list[k]

    i = 0
    j = n-1
    while i < j:  # 투 포인터 알고리즘
        if list[i] + list[j] == val:
            # 자기 자신을 좋은 수 만들기에 포함하면 안됨
            if i != k and j != k:
                cnt += 1
                break
            elif i == k:
                i += 1
            elif j == k:
                j -= 1
        elif list[i] + list[j] > val:
            j -= 1
        else:
            i += 1
print(cnt)