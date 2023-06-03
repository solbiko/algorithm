"""
크기가 N인 수열 A = A1, A2, ..., AN이 있다.
수열의 각 원소 Ai에 대해서 오큰수 NGE(i)를 구하려고 한다.
Ai의 오큰수는 오른쪽에 있으면서 Ai보다 큰 수 중에서 가장 왼쪽에 있는 수를 의미한다.
그러한 수가 없는 경우에 오큰수는 -1이다.

A = [3, 5, 2, 7]인 경우 NGE(1) = 5, NGE(2) = 7, NGE(3) = 7, NGE(4) = -1이다.
A = [9, 5, 4, 8]인 경우 NGE(1) = -1, NGE(2) = 8, NGE(3) = 8, NGE(4) = -1이다.

첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000,000)이 주어진다.
둘째 줄에 수열 A의 원소 A1, A2, ..., AN (1 ≤ Ai ≤ 1,000,000)이 주어진다.
총 N개의 수 NGE(1), NGE(2), ..., NGE(N)을 공백으로 구분해 출력한다.

4
3 5 2 7
"""
import sys
n = int(input())
a = list(map(int, input().split()))
stack = []
res = [0]*n # 정답리스트

for i in range(n):
    while stack and a[stack[-1]] < a[i]: # 스택 탑 인덱스가 가르키는 수 < 현재 수
        res[stack.pop()] = a[i] # 정답 리스트에 오큰수를 현재 수로 저장
    stack.append(i)

while stack: # 반복문을 다 돌고 나왔는데 스택이 비어 있지 않다면 빌 때까지
    res[stack.pop()]=-1 #스택에 쌓인 index에 -1을 넣기

for i in range(n):
    sys.stdout.write(str(res[i]) + " ")

"""
새 원소가 크다면 top pop하면서 새원소 수로 오큰수 저장하고 새원소 삽입
새 원소가 작다면 새 원소 삽입 
"""