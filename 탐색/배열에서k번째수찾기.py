"""
세준이는 크기가 N×N인 배열 A를 만들었다. 배열에 들어있는 수 A[i][j] = i×j 이다. 이 수를 일차원 배열 B에 넣으면 B의 크기는 N×N이 된다.
B를 오름차순 정렬했을 때, B[k]를 구해보자.(배열 A와 B의 인덱스는 1부터 시작한다.)

첫째 줄에 배열의 크기 N이 주어진다. N은 10^5보다 작거나 같은 자연수이다.
둘째 줄에 k가 주어진다. k는 min(1^9, N^2)보다 작거나 같은 자연수이다.

B[k]를 출력
"""
n=int(input())
k=int(input())

start=1
end=k
res=0

# 이진탐색 수행 => k번째 수 체크 : k보다 작은 수가 몇개인지 체크
while start<=end:
    mid=int((start+end)/2) # 중앙 인덱스
    cnt=0 # 중앙값보다 작은 수

    # 중앙값보다 작은 수 계산
    for i in range(1,n+1):
        cnt+=min(int(mid/i), n) # 중앙인덱스를 i(행번호)로 나눈 값: 중앙값보다 작거나 같은 개수
    if cnt<k: # 현재 중앙값보다 작은 수의 개수가 k보다 작음 => k번째 수 아님
        start=mid+1
    else: # 현재 중앙값보다 작은 수의 개수가 k보다 크거나 같음
        res=mid
        end=mid-1
print(res)