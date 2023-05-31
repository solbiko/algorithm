"""
N개의 동전으로 만들 수 없는 양의 정수 금액 중 최솟값 출력
5
3 2 1 1 9
"""
n=int(input())
a=list(map(int, input()))
a.sort()

target=1
for i in a:
    # 만들 수 없는 금액을 찾았을 때 반복종료
    if target<i:
        break
    target+=i

# 만들 수 없는 금액 출력
print(target)
