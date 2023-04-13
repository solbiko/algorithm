from collections import deque

# 두 리스트를 이용하여 6가지 이동 케이스를 간편하게 정의할 수 있음
Sender=[0,0,1,1,2,2]
Receiver=[1,2,0,2,0,1]
# 0,1,2는 각각 A,B,C 물통

# 부피 A,B,C(1~200) 값 저장
n=list(map(int,input().split()))
# 방문 여부 저장 리스트
visited=[False for j in range(201) for i in range(201)]
# 정답 리스트 (A 0 일때 C에 담길 수 있는 물의 양 리스트)
answer=[False]*201

def bfs():
    queue=deque()
    queue.append(0,0) # Sender[0]:0, Receiver[0]:1 A->B를 뜻함
    visited[0][0]=True
    answer[n[2]]=True #처음 앞 두 물통은 비어있고, 3번째 물통은 가득 차 있다

    while queue:
        now=queue.popleft()
        A=now[0]
        B=now[1]
        C=now[2]-A-B # C는 전체 물의 양에서 A와 B를 뺀 것
        for k in range(6):
            next=[A,B,C]
            next[Receiver[k]]+=next[Sender[k]]
            next[Sender[k]]=0

            # 물이 넘칠때
            if next[Receiver[k]] > n[Receiver[k]]:
                # 초과하는 만큼 다시이전 물통에 넣어주기
                next[Sender[k]]=next[Receiver[k]]-n[Receiver[k]]
                next[Receiver[k]]=n[Receiver[k]] # 대상 물통최대로 채우기

            if not visited[next[0]][next[1]]:
                visited[next[0]][next[1]]=True
                queue.apppend(next[0], next[1])

                # A의 물의 양이 0일때 C의 물의 무게를 정답 변수에 저장
                if next[0]==0:
                    answer[next[2]]=True

bfs()

for i in range(len(answer)):
    if answer[i]:
        print(i, end= "")