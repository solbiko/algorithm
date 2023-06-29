import math
def solution(edges, target):

    n = len(target)  # 노드 수
    # 인접리스트
    a = {i: [] for i in range(1, n + 1)}
    for s, e in edges:
        a[s].append(e)

    # 리프노드
    leaf = {}
    for i in a:
        if len(a[i]) == 0:
            leaf[i] = 0
        a[i].sort()


    # 길(하위노드있으면 0 없으면 1)
    r = {i: -1 for i in range(1, n + 1)}
    for i in a:
        if len(a[i]):
            r[i] = 0

    # 리프노드 가는 순서 찾기
    order = []
    flag = True

    while flag:
        i = 1
        while r[i] != -1: # 리프노드일 때 까지
            temp = i
            i = a[i][r[i]] # 다음 노드 찾기 (하위 노드 인덱스로 변경)

            r[temp]=(r[temp]+1)%len(a[temp])  # 새로운 길 설정 ( 하위노드 길 방향 인덱스 변경)

        order.append(i) # 탐색노드 순서 저장
        leaf[i]+=1 # 리프노드 떨어진 횟수 저장


        # 123 떨어뜨려도 리프노드 target값보다 작으면 한바퀴 더시작
        flag=False
        for j in leaf:
            if leaf[j]*3<target[j-1]: # 123 어떤거 떨어뜨려도 리프노드 떨어진거보다 target이 클때
                flag=True
                break
            elif leaf[j]>target[j-1]:
                return[-1]

    answer = [1 for _ in range(len(order))]

    for i in order:
        target[i-1]-=1

    # 가장 적은 숫자를 사용하며 그중 사전 순으로 가장 빠른 경우
    for i in range(len(order)-1, -1, -1):  # 뒤에서 부터 숫자 추가
        if target[order[i]-1]>=2:
            answer[i]+=2
            target[order[i]-1]-=2
        elif target[order[i]-1] == 1:
            answer[i]+=1
            target[order[i]-1]-=1
        else:
            continue


    return answer
