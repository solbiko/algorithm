"""
DVD에는 총 N개의 곡이 들어가는데, DVD에 녹화할 때에는 라이브에서의 순서가 그대로 유지 되어야 한다.
한 노래를 쪼개서 두 개의 DVD에 녹화하면 안된다. M개의 DVD에 모든 동영상을 녹화하기로 하였다.

1. DVD의 크기(녹화 가능한 길이) 최소
2. DVD 같은 크기여야함

곡 수 N(1≤N≤1,000), DVD 개수 M(1≤M≤N)
다음 줄에는 부른 순서대로 부른 곡의 길이(자연수, 분단위)
부른 곡의 길이는 10,000분을 넘지 않는다고 가정하자.

첫 번째 줄부터 DVD의 최소 용량 크기를 출력

9 3
1 2 3 4 5 6 7 8 9

3개의 DVD용량이 17분짜리이면 (1, 2, 3, 4, 5) (6, 7), (8, 9) 이렇게 3개의 DVD로 녹음을 할 수 있다.
17분 용량보다 작은 용량으로는 3개의 DVD에 모든 영상을 녹화할 수 없다.
"""
n,m=map(int,input().split())
a=list(map(int,input().split()))

maxA=max(a)
res=0
l=1
r=sum(a)

def ch(x): # dvd 용량 x일때 녹화 dvd 개수 체크
    cnt=1
    tmp=0
    for i in a: # 동영상 리스트
        if tmp+i>x:
            cnt+=1
            tmp=i
        else:
            tmp+=i
    return cnt


while l<=r:
    mid=(l+r)//2
    if mid>= maxA and ch(mid)<= m: # 가장 긴 노래가 dvd 용량보단 커야함
        res=mid
        r=mid-1
    else:
        l=mid+1

print(res)


