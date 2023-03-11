# 이진탐색
from bisect import bisect_left, bisect_right

'''
정수범위 -2^31 ~ 2^31
M개의 수가 A안에 존재하는지
5
4 1 5 2 3
5
1 3 7 9 5

틀린 이유
bisect_left 함수는 배열 안에 찾으려는 값이 있으면 그 위치 없으면 배열 길이를 반환하는 함수가 아님
bisect_left(Nlist, m)은 Nlist.insert(i, m)을 했을 때 Nlist가 정렬된 상태를 유지하는 인덱스 i를 반환하는 함수
따라서 bisect_left는 찾고자 하는 값이 배열에 없는데도 len(Nlist)가 아닌 값을 반환할 수 있음
'''

# 자연수 N(1~100,000)
n = int(input())
# A[] N개의 정수
a = list(map(int, input().split()))
# 자연수 M(1~100,000)
m = int(input())
# M개의 수
list = list(map(int, input().split()))

a.sort()
for i in list:

    # 이진탐색
    idx = bisect_left(a, i)
    print("i:", i, " idx: ", idx, " len(list): ", list[idx-1])

    # if idx > len(list)-1:
    #     print(0)
    # else:
    #     print(1)
