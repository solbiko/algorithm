"""
어떤 N개의 수가 주어져 있다. 그런데 중간에 수의 변경이 빈번히 일어나고 그 중간에 어떤 부분의 곱을 구하려 한다.
1, 2, 3, 4, 5 라는 수가 있고, 3번째 수를 6으로 바꾸고 2번째부터 5번째까지 곱을 구하라고 한다면 240을 출력하면 되는 것이다.
그리고 그 상태에서 다섯 번째 수를 2로 바꾸고 3번째부터 5번째까지 곱을 구하라고 한다면 48이 될 것이다.

첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)과 M(1 ≤ M ≤ 10,000), K(1 ≤ K ≤ 10,000) 가 주어진다.
 M은 수의 변경이 일어나는 횟수이고, K는 구간의 곱을 구하는 횟수이다.
둘째 줄부터 N+1번째 줄까지 N개의 수가 주어진다.
N+2번째 줄부터 N+M+K+1 번째 줄까지 세 개의 정수 a,b,c가 주어지는데, a가 1인 경우 b번째 수를 c로 바꾸고 a가 2인 경우에는 b부터 c까지의 곱을 구하여 출력하면 된다.
5 2 2
1
2
3
4
5
1 3 6
2 2 5
1 5 2
2 3 5
입력으로 주어지는 모든 수는 0보다 크거나 같고, 1,000,000보다 작거나 같은 정수이다.

첫째 줄부터 K줄에 걸쳐 구한 구간의 곱을 1,000,000,007로 나눈 나머지를 출력한다.
"""
import sys
input = sys.stdin.readline

n,m,k=map(int, input().split())  # 수의개수, 변경횟수, 구간곱출력횟수
treeHeight=0  # 트리높이
length=n  # 리프노드개수
MOD=1000000007

while length!=0:
    length//=2
    treeHeight+=1

treeSize=pow(2,treeHeight+1)  # 트리길이
leftStartIdx=treeSize//2-1  # 리프노드 전 인덱스
tree = [1]*(treeSize+1)  # 인덱스 트리 저장 리스트

# 데이터를 리프노드에 저장
for i in range(leftStartIdx+1, leftStartIdx+n+1):
    tree[i] = int(input())

# 인덱스 트리 생성 함수
def setTree(idx):
    while idx!=1:  # 인덱스가 루트노드가 아닐때까지
        tree[idx//2]=tree[idx]*tree[idx//2]%MOD
        idx-=1

setTree(treeSize-1)  # 2ᵏ-1부터 2까지
# print(tree)

# 값 변경 함수
def changeVal(idx, val):
    tree[idx]=val
    while idx>1:
        idx=idx//2
        tree[idx]=tree[idx*2]%MOD*tree[idx*2+1]%MOD

# 구간곱 출력 함수
def getMul(sIdx, eIdx):
    mul = 1
    while sIdx <= eIdx:
        if sIdx%2==1:  # 선택 : 부모노드 대상범위 제거, 독립노드
            mul=mul*tree[sIdx]%MOD
            sIdx+=1
        sIdx=sIdx//2
        if eIdx%2==0:  # 선택 : 부모노드 대상범위 제거, 독립노드
            mul=mul*tree[eIdx]%MOD
            eIdx-=1
        eIdx=eIdx//2
    return mul

for _ in range(m+k):
    q,s,e = map(int, input().split())
    if q == 1:  # 변경
        changeVal(leftStartIdx+s, e)
    elif q == 2:  # 출력
        b = leftStartIdx+s
        c = leftStartIdx+e
        print(getMul(b, c))
