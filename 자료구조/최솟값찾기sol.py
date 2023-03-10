# 슬라이딩 윈도우
# dequeue 사용
from collections import deque
N, L = map(int, input().split())
deque = deque()
list = list(map(int, input().split()))



for i in range(N):

    # 덱의 마지막 위치에서부터 현재 값보다 큰 값은 덱에서 제거
    while deque and deque[-1][0] > list[i]:
        deque.pop()

    # 덱의 마지막 위치에 현재 값 저장
    deque.append((list[i],i))

    # 덱의 1번째 위치에서부터 L의 범위를 벗어난 값을 덱에서 제거
    if deque[0][1] <= i - L:
        deque.popleft()

    # 덱의 1번째 데이터 출력
    print(deque[0][0], end=' ')
