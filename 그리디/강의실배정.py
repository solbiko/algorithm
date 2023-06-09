"""
김종혜 선생님한테는 Si에 시작해서 Ti에 끝나는 N개의 수업이 주어지는데, 최소의 강의실을 사용해서 모든 수업을 가능하게 해야 한다.
참고로, 수업이 끝난 직후에 다음 수업을 시작할 수 있다. (즉, Ti ≤ Sj 일 경우 i 수업과 j 수업은 같이 들을 수 있다.)
첫 번째 줄에 N이 주어진다. (1 ≤ N ≤ 200,000)
이후 N개의 줄에 Si, Ti가 주어진다. (0 ≤ Si < Ti ≤ 109)
3
1 3
2 4
3 5
"""
import heapq
import sys
input=sys.stdin.readline

n=int(input())
a=[]
q=[]  # 우선순위큐
for _ in range(n):
    s,t=map(int,input().split())
    a.append((s,t))
a.sort(key=lambda x: (x[0], x[1]))

# 처음 수업 (끝나는 시간) 삽입
heapq.heappush(q, a[0][1])

# 다음 수업부터 반복
for i in range(1,n):
    if a[i][0] >= q[0]:
        heapq.heappop(q)
    heapq.heappush(q, a[i][1])

print(q)
print(len(q))