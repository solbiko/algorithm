n = int(input())
list = list(map(int, input().split()))
list.sort()

cnt = 0

# 다른 두 수의 합인 수의 개수
for k in  range(n):
    val = list[k]
    # 2포인터
    i = 0
    j = n-1

    sum = list[i] + list[j]
    print(sum)
    while i < j:
        if sum == val:
            # 자기 자신을 좋은 수 만들기에 포함하면 안됨
            if i != k and j != k:
                cnt = cnt + 1
                break
            elif i == k:
                i += 1
            elif j == k:
                j -= 1
        elif sum > val:
            j -= 1
        else:
            i += 1
print(cnt)