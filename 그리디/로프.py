"""
k개의 로프를 사용하여 중량이 w인 물체를 들어올릴 때, 각각의 로프에는 모두 고르게 w/k 만큼의 중량이 걸리게 된다.
이 로프들을 이용하여 들어올릴 수 있는 물체의 최대 중량을 구해내는 프로그램
첫째 줄에 정수 N이 주어진다. 다음 N개의 줄에는 각 로프가 버틸 수 있는 최대 중량이 주어진다.
2
10
15
"""
n=int(input())
w=[]
for _ in range(n):
    w.append(int(input()))
w.sort(reverse=True)

answer=[]
for i in range(n):
    answer.append(w[i]*(i+1))

print(max(answer))
