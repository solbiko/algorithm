"""
사람수 n, 파티수 m
진실아는 사람정보 1 1
파티정보 m줄 참여자수 참여자번호

거짓말 할 수 있는 파티 개수 최댓값
"""
result=0

#사람수 n, 파티수 m
n,m=map(int,input().split())

# 진실을 아는 사람 정보
p=list(map(int, input().split()))
t=p[0] # 진실을 아는 사람 수
del p[0]

# 파티정보
party=[[] for _ in range(m)]
for i in range(m):
    party[i]=list(map(int,input().split()))
    del party[i][0]

# 대표노드  리스트
arr=[0]*(n+1)
for i in range(1, n+1):
    arr[i]=i


def find(a): # 대표노드 찾기
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

# 각 파티에 참여한 사람들을 1개의 그룹으로 만들기 (같이 있으면 사실/과장 통일)
for i in range(m):
    firstPerson=party[i][0]
    for j in range(1, len(party[i])):
        union(firstPerson, party[i][j])
# print(arr)


# 파티 반복
for i in range(m):
    isPossible=True
    # i번째 파티의 사람 (같이 있으면 사실/과장 통일) → 대표노드
    firstPerson=party[i][0]

    # 진실을 아는 사람들의 수만큼 반복
    for j in range(len(p)):
        # 각 파티의 대표 노드와 진실을 아는 사람들의 대표 노드가 같다면 과장 할 수 없음
        print(find(firstPerson))
        if find(firstPerson)==find(p[j]):
            isPossible=False
            break
    if isPossible:
        result+=1

print(result)
