"""
3구 멀티탭을 쓸 때, 전기용품의 사용 순서가 아래와 같이 주어진다면,

1. 키보드
2. 헤어드라이기
3. 핸드폰 충전기
4. 디지털 카메라 충전기
5. 키보드
6. 헤어드라이기

키보드, 헤어드라이기, 핸드폰 충전기의 플러그를 순서대로 멀티탭에 꽂은 다음 디지털 카메라 충전기 플러그를 꽂기 전에 핸드폰충전기 플러그를 빼는 것이 최적일 것이므로 플러그는 한 번만 빼면 된다.
첫 줄에는 멀티탭 구멍의 개수 N (1 ≤ N ≤ 100)과 전기 용품의 총 사용횟수 K (1 ≤ K ≤ 100)가 정수
두 번째 줄에는 전기용품의 이름이 K 이하의 자연수로 사용 순서대로 주어진다. 각 줄의 모든 정수 사이는 공백문자로 구분되어 있다.
"""
import sys
input = sys.stdin.readline
n,k=map(int, input().split())
s=list(map(int, input().split()))

p=[]  # 플러그
cnt=0
for i in range(k):

    if s[i] in p:
        continue

    if len(p)!=n:
        p.append(s[i])
        continue

    dVal=0  # 뽑을거
    maxDVal=0 # 뽑을거중에 가장 먼거
    for x in p:  # 꽂혀있는거 중에
        if x not in s[i:]:  # 앞으로 쓸거에 없으면
            dVal=x
            break
        elif s[i:].index(x) > maxDVal:
            maxDVal= s[i:].index(x)
            dVal=x

    p[p.index(dVal)]=s[i]  # 뽑고 지금꺼 꽂음
    cnt+=1

print(cnt)