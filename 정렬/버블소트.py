"""
1377

N은 배열의 크기이고, A는 정렬해야 하는 배열이다. 배열은 A[1]부터 사용한다.
버블소트 j for문에서 swap되지 않은 i찾기 : 전부 정렬 되었을 때의 i
N(1~500,000) n^2불가

5
10
1
5
2
3
"""
import sys
input=sys.stdin.readline

n=int(input())
a=[]
for i in range(n):
    a.append((int(input()),i))  # (val,idx)

soredA=sorted(a)
# print(a)
# print(soredA)

max=0
for i in range(n):
    if max<soredA[i][1]-i:
        max=soredA[i][1]-i

print(max+1)  # swap이 일어나지 않는 반복문 한번 더 실행됨으로 +1