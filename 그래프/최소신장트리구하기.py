"""
노드의 개수 V (1~10,000)
에지의 개수 E (1~100,000)
A B C (A번 노드와 B번 노드가 가중치 C인 에지로 연결)
가중치 C (-2,147,483,648 ~ 2,147,483,648)

최소 신장 트리의 가중치 출력
"""
import sys
sys.setrecursionlimit(100000) #  재귀의 최대 깊이 설정
from queue import PriorityQueue

input = sys.stdin.readline

N, E = map(int, input().split())

# 에지 정보를 저장할 우선순위 큐 (우선순위 큐를 사용해 자동 정렬)
q = PriorityQueue()


# 유니온파인드 : 사이클 여부 확인
# 인덱스 배열 : 대표 노드 저장
arr = [0] * (N+1)
for i in range(N+1):
    arr[i] = i

# 에지 리스트
for _ in range(E):
    a, b, c = map(int, input().split())
    q.put((c, a, b))




def find(a):  # 대표노드 찾기
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

# 사용 에지 수 저장 변수
useEdge = 0

# 정답 변수
result = 0

# 사용한 에지 수가 노드 수-1이 될 때 까지
while useEdge < N-1:

    # 큐에서 에지 정보 가져오기
    w, s, e = q.get()

    # 에지 시작점과 끝점의 부모 노드가 다르면 (연결해도 사이클이 생기지 않으면)
    if find(s) != find(e):
        union(s, e)
        result += w
        useEdge += 1

print(result)
