"""
조건 1: 박스를 트럭에 실으면, 이 박스는 받는 마을에서만 내린다.
조건 2: 트럭은 지나온 마을로 되돌아가지 않는다.
조건 3: 박스들 중 일부만 배송할 수도 있다.
마을의 개수, 트럭의 용량, 박스 정보(보내는 마을번호, 받는 마을번호, 박스 개수)가 주어질 때,
트럭 한 대로 배송할 수 있는 최대 박스 수를 구하는 프로그램을 작성하시오. 단, 받는 마을번호는 보내는 마을번호보다 항상 크다.

입력의 첫 줄은 마을 수 N과 트럭의 용량 C가 빈칸을 사이에 두고 주어진다. N은 2이상 2,000이하 정수이고, C는 1이상 10,000이하 정수이다.
다음 줄에, 보내는 박스 정보의 개수 M이 주어진다. M은 1이상 10,000이하 정수이다
다음 M개의 각 줄에 박스를 보내는 마을번호, 박스를 받는 마을번호, 보내는 박스 개수(1이상 10,000이하 정수)를 나타내는 양의 정수가 빈칸을 사이에 두고 주어진다.

트럭 한 대로 배송할 수 있는 최대 박스 수를 한 줄에 출력
4 40
6
3 4 20
1 2 10
1 3 20
1 4 30
2 3 10
2 4 20
"""
import sys
input=sys.stdin.readline

# 마을수, 트럭용량
N,C=map(int,input().split())
M=int(input())
delList=[]
for i in range(M):
    s,e,w=map(int, input().split())
    delList.append((s,e,w))

# 도착지 기준 정렬
delList.sort(key=lambda x: (x[1]))
# print(delList)

v=[0]*(N+1)  # 현재 트럭에 싣은 양
cnt = 0
for f, t, s in delList:
    box = s
    # 트럭 공간 체크
    for i in range(f, t):
        if v[i] + box >= C:  # 트럭에 다 싣을수 없다면
            box = C-v[i]  # 트럭 여유공간
        print(v)
        print("delList", f, t, s, ", i:", i, ", box:", box)
    for i in range(f, t):
        v[i]+=box
        print(v)

    cnt += box  # 배달 택배양 추가
    print()
print(cnt)