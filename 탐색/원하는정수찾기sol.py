# 자연수 N(1~100,000)
n = int(input())
# A[] N개의 정수
a = list(map(int, input().split()))
# 자연수 M(1~100,000)
m = int(input())
# M개의 수
list = list(map(int, input().split()))

a.sort()

for i in range(m):
    find = False
    target = list[i]

    start = 0
    end = len(a) - 1

    while start <= end:
        mid = int((start + end) / 2)
        midVal = a[mid]

        if midVal > target:
            end = mid - 1
        elif midVal < target:
            start = mid + 1
        else:
            find = True
            break

    if find:
        print(1)
    else:
        print(0)