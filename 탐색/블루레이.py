n,m=map(int,input().split())
a=list(map(int,input().split()))

start=end=0

for i in a:
    if start<i:
        start=i # 레슨 최대값을 시작 인덱스로 저장
    end+=i # 모든 레슨의 총합을 종료 인덱스로 저장

while start<=end:
    mid=int((start+end)/2)

    tmp=0
    cnt=0
    for i in range(n):
        if tmp+a[i]>mid: # 현재 블루레이에 저장 할 수 없어 새로운 블루레이로 교체
            cnt+=1
            tmp=0
        tmp+=a[i]
    if tmp!=0: # 마지막 블루레이가 필요하므로
        cnt+=1
    if cnt>m:
        start=mid+1
    else:
        end=mid-1

print(start)