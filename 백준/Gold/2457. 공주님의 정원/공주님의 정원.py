"""
올해는 4, 6, 9, 11월은 30일까지 있고, 1, 3, 5, 7, 8, 10, 12월은 31일까지 있으며, 2월은 28일까지만 있다.

공주가 가장 좋아하는 계절인 3월 1일부터 11월 30일까지 매일 꽃이 한 가지 이상 피어 있도록 한다.
정원이 넓지 않으므로 정원에 심는 꽃들의 수를 가능한 적게 한다.

N개의 꽃들 중에서 위의 두 조건을 만족하는, 즉 3월 1일부터 11월 30일까지 매일 꽃이 한 가지 이상 피어 있도록 꽃들을 선택할 때,
선택한 꽃들의 최소 개수를 출력

첫째 줄에는 꽃들의 총 개수 N (1 ≤ N ≤ 100,000)이 주어진다. 다음 N개의 줄에는 각 꽃이 피는 날짜와 지는 날짜가 주어진다.
하나의 날짜는 월과 일을 나타내는 두 숫자로 표현된다. 예를 들어서, 3 8 7 31은 꽃이 3월 8일에 피어서 7월 31일에 진다는 것을 나타낸다.
4
1 1 5 31
1 1 6 30
5 15 8 31
6 10 12 10
"""
import sys
input=sys.stdin.readline


n = int(input())
f = []
for i in range(n):
    sm,sd,em,ed=map(int, input().split())
    f.append([sm*100+sd, em*100+ed])
f.sort()

target = 301  # 시작날
end=0 # 종료날
cnt=0

while f:
    if target >= 1201 or f[0][0] > target:
        break

    for _ in range(len(f)):  # 시작날~종료날 가장 긴 것을 종료날로 저장
        now=f[0]
        if target >= now[0]:
            if end <= now[1]:
                end = now[1]
            f.remove(f[0])
        else:
            break

    target = end  # 현재 종료날을 다음 시작날과 비교하기 위해 target 저장
    cnt += 1

if target <1201:
    print(0)
else:
    print(cnt)


