"""
N개의 컴퓨터를 모두 서로 연결, 각각의 컴퓨터는 랜선으로 연결
기부할 수 있는 랜선의 길이의 최댓값

컴퓨터의 개수 N(1~50)

랜선의 길이
a~z: 1~26, A~Z: 27~52, (i,j)=0: 랜선이 없음
"""
import sys
input = sys.stdin.readline
from queue import PriorityQueue

n=int(input()) #컴퓨터개수
total=0 # 총 랜선 길이

pq = PriorityQueue()

#랜선길이
for i in range(n):
    temp=list(input())
    for j in range(n):
        num=0
        # 문자열 숫자로 변환
        if 'a' <= temp[j] <= 'z': # 소문자
            num = ord(temp[j])-ord('a')+1
        elif 'A' <= temp[j] <= 'Z': # 대문자
            num = ord(temp[j])-ord('A')+27

        total+=num # 총 랜선 길이 저장
        if i!=j and num!=0: # i,j가 다르고 연결되어있다면
            pq.put((num,i,j))   # 랜선 정보를 큐에 저장

# 인덱스 배열 : 대표 노드 저장
arr = [0]*n
for i in range(n):
    arr[i] = i

# 유니온 파인드
def find(a):
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

useEdge = 0 # 사용 에지 수 저장 변수
result = 0 # 정답 변수

# MST
while pq.qsize()>0:
    w,s,e=pq.get()
    if find(s)!=find(e):
        union(s,e)
        result+=w
        useEdge+=1

if useEdge==n-1:
    print(total-result)
else:
    print(-1)