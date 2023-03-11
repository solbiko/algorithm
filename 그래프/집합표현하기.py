"""
유니온 파인드

{0}, {1} ... {n} 각가 n+1개의 집합
합집합 연산과 두 원소가 같은 집합에 포함돼 있는지 확인

n (1~1,000,000), m : 입력으로 주어지는 연산의 개수

0 a b: a가 포함돼 있는 집함과 b가 포함돼 있는 집합 합침 -> union(a,b)
1 a b: 두 원소가 같은 집합에 포함돼 있는지 확인

7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1

"""
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000) #  재귀의 최대 깊이 설정

n, m = map(int, input().split())

#인덱스 배열
arr = [0] * (n+1)
for i in range(len(arr)):
    arr[i] = i


def find(a): # 대표노드 찾기
    if a == arr[a]:
        return a
    else:
        arr[a] = find(arr[a])
        return arr[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        arr[b] = a


for i in range(m):
    q, a, b = map(int, input().split())
    if q == 0:  # 0 합침
        union(a, b)

    elif q == 1:  # 1 포함 확인
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")

    print(arr)
