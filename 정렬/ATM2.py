"""
111399
ATM이 1대밖에 없다. 지금 이 ATM앞에 N명의 사람들이 줄을 서있다. 사람은 1번부터 N번까지 번호가 매겨져 있으며, i번 사람이 돈을 인출하는데 걸리는 시간은 Pi분이다.
사람들이 줄을 서는 순서에 따라서, 돈을 인출하는데 필요한 시간의 합이 달라지게 된다.
줄을 서 있는 사람의 수 N과 각 사람이 돈을 인출하는데 걸리는 시간 Pi가 주어졌을 때, 각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값
첫째 줄에 사람의 수 N(1 ≤ N ≤ 1,000)이 주어진다. 둘째 줄에는 각 사람이 돈을 인출하는데 걸리는 시간 Pi가 주어진다. (1 ≤ Pi ≤ 1,000)
5
3 1 4 3 2
"""
n=int(input())
a=list(map(int,input().split()))
s=[0]*n  # 합배열

# 삽입정렬
for i in range(1,n):
    insert_point=i
    insert_value=a[i]
    for j in range(i-1,-1,-1):
        if a[j]<a[i]:
            insert_point=j+1
            break
        if j==0:
            insert_point=0
    for j in range(i, insert_point, -1):
        a[j]=a[j-1]
    a[insert_point]=insert_value

for i in range(n):  # 합배열 만들기
    s[i]=s[i-1]+a[i]

total=0
for i in range(0,n):  # 합배열 총합 구하기
    total+=s[i]
print(total)
