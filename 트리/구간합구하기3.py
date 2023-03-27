"""
구간합 구하기3

N개의 수(1~1,000,000)
중간에 수의 변경이 빈번히 일어남, 그 중간에 어떤 부분의 합을 구함

1,2,3,4,5 -> 1,2,6,4,5 변경 -> 2~5번째 합 구하기 => 17
1,2,6,4,5 -> 1,2,6,4,2 변경 -> 3~5번쨰 합 구하기 => 12

N(1~1,000,000) 수의개수
M(1~10,000) 변경이 일어나는 횟수
K(1~10,000) 구간합
2 - N+1줄 : N개의 수
N+2 N+M+K+1줄 : 3개의 정수 a b c
1 b c : b번째 수 c로 변경
2 b c : b번째 수에서 c 번째 수까지 합 출력

"""
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
treeHeight = 0 # 트리 높이
lenth = n # 리프노드 갯수

# 높이 계산 : 리프노드의 개수를 2씩 나누면서
while lenth != 0:
    lenth //= 2
    treeHeight += 1

# 트리 길이 2ᵏ*2
treeSize = pow(2, treeHeight + 1)

# 리프노드 전 인덱스 2ᵏ-1 = 2ᵏ*2/2 -1
leftStartIdx = treeSize // 2 - 1

# 인덱스 트리 저장 리스트
tree = [0] * (treeSize + 1)

# 데이터를 리프노드에 저장
for i in range(leftStartIdx + 1, leftStartIdx + n + 1):
    tree[i] = int(input())


# 인덱스 트리 생성 함수
def setTree(idx):
    # 인덱스가 루트노드가 아닐때까지
    while idx != 1:
        tree[idx // 2] += tree[idx]
        idx -= 1


# 원본데이터 제외하고 1까지
setTree(treeSize - 1)  # 2ᵏ-1부터 2까지


"""
트리 길이, 크기 = 2ᵏ*2
원본데이터 시작 인덱스 = 2ᵏ
부모노드 챙우기 = 2 ~ 2ᵏ-1

leftStartIdx = 2ᵏ-1 = treeSize // 2 - 1 = 2ᵏ*2//2-1
"""


# 값 변경 함수
def changeVal(idx, val):
    diff = val - tree[idx]
    while idx > 0:
        tree[idx] = tree[idx] + diff
        idx //= 2


# 구간합 출력 함수
def getSum(sIdx, eIdx):
    sum = 0
    while sIdx <= eIdx:
        if sIdx % 2 == 1:  # 선택 : 부모노드 대상범위 제거, 독립노드
            sum += tree[sIdx]
            sIdx += 1
        sIdx = sIdx // 2
        if eIdx % 2 == 0:  # 선택 : 부모노드 대상범위 제거, 독립노드
            sum += tree[eIdx]
            eIdx -= 1
        eIdx = eIdx // 2
    return sum


for _ in range(m+k):
    a, b, c = map(int, input().split())
    if a == 1:
        # 변경
        changeVal(leftStartIdx + b, c)
    elif a == 2:
        # 구간합출력
        b = leftStartIdx + b
        c = leftStartIdx + c
        print(getSum(b, c))
