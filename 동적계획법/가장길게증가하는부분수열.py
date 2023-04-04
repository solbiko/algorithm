import sys
input=sys.stdin.readline
n=int(input())
a=list(map(int,input().split()))
a.insert(0,0)

index=0
# 최장증가부분수열 길이
maxLength=1

# 현재 가장 유리한 증가수열 저장 리스트
b=[0]*1000001
b[maxLength]=a[1]
# 0~i까지 i를 포함하는 최장증가수열 길이 저장 리스트
d=[0]*1000001
d[1]=1
# 정답 수열 저장 리스트
res=[0]*1000001

def binarySearch(l,r,now):
    while l<r:
        mid=(l+r)//2
        if b[mid]<now:
            l=mid+1
        else:
            r=mid
    return l

for i in range(2, n+1):
    if b[maxLength]<a[i]: # 가장 마지막 수열보다 현재 수열이 큰경우
        # b리스트 끝에 a[i] 추가
        maxLength+=1
        b[maxLength]=a[i]
        d[i]=maxLength

    else:
        # 바이너리 서치를 이용홰 현재 수열이 들어갈 index 찾기
        index=binarySearch(1,maxLength, a[i])
        b[index]=a[i] # 현재 수열값 저장
        d[i]=index


print(maxLength)

index=maxLength
x=b[maxLength]+1

for i in range(n,0,-1): # 뒤에서부터 담색하면서 정답 수열 저장
    if d[i] == index and a[i] < x:
        res[index]=a[i]
        x = a[i]
        index-=1

for i in range(1, maxLength+1):
        print(res[i], end=' ')

