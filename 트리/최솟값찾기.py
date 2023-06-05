"""
N(1 ≤ N ≤ 100,000)개의 정수들이 있을 때, a번째 정수부터 b번째 정수까지 중에서 제일 작은 정수를 찾는 것은 어려운 일이 아니다.
하지만 이와 같은 a, b의 쌍이 M(1 ≤ M ≤ 100,000)개 주어졌을 때는 어려운 문제가 된다.
여기서 a번째라는 것은 입력되는 순서로 a번째라는 이야기이다. 예를 들어 a=1, b=3이라면 입력된 순서대로 1번, 2번, 3번 정수 중에서 최솟값을 찾아야 한다.
각각의 정수들은 1이상 1,000,000,000이하의 값을 갖는다.

첫째 줄에 N, M이 주어진다. 다음 N개의 줄에는 N개의 정수가 주어진다. 다음 M개의 줄에는 a, b의 쌍이 주어진다.
10 4
75
30
100
38
50
51
52
20
81
5
1 10
3 5
6 9
8 10
"""
import sys
input = sys.stdin.readline

n,m= map(int, input().split())
treeHeight=0 # 트리 높이
lenth=n # 리프노드 갯수

# 높이 계산 : 리프노드의 개수를 2씩 나누면서
while lenth != 0:
    lenth//=2
    treeHeight+=1

# 트리 길이 2ᵏ*2
treeSize=pow(2, treeHeight + 1)

# 리프노드 전 인덱스 2ᵏ-1 = 2ᵏ*2/2 -1
leftStartIdx=treeSize//2-1

# 인덱스 트리 저장 리스트
tree=[sys.maxsize]*(treeSize+1)

# 데이터를 리프노드에 저장
for i in range(leftStartIdx+1, leftStartIdx+n+1):
    tree[i]=int(input())

# 인덱스 트리 생성 함수
def setTree(idx):
    # 인덱스가 루트노드가 아닐때까지
    while idx!=1:
        if tree[idx//2]>tree[idx]:
            tree[idx//2]=tree[idx]
        idx -= 1


# 원본데이터 제외하고 1까지
setTree(treeSize-1)  # 2ᵏ-1부터 2까지
# print(tree)

# 최솟값 출력 함수
def getMul(sIdx, eIdx):
    minVal=sys.maxsize
    while sIdx <= eIdx:
        if sIdx%2==1:  # 선택 : 부모노드 대상범위 제거, 독립노드
            minVal=min(minVal,tree[sIdx])
            sIdx+=1
        sIdx=sIdx//2
        if eIdx%2==0:  # 선택 : 부모노드 대상범위 제거, 독립노드
            minVal=min(minVal,tree[eIdx])
            eIdx-=1
        eIdx=eIdx//2
    return minVal

for _ in range(m):
    s,e=map(int,input().split())
    print(getMul(leftStartIdx+s, leftStartIdx+e))