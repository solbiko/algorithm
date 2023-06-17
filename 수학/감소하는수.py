"""
음이 아닌 정수 X의 자릿수가 가장 큰 자릿수부터 작은 자릿수까지 감소한다면, 그 수를 감소하는 수라고 한다.
예를 들어, 321과 950은 감소하는 수지만, 322와 958은 아니다.
N번째 감소하는 수를 출력하는 프로그램을 작성하시오.
0은 0번째 감소하는 수이고, 1은 1번째 감소하는 수이다. 만약 N번째 감소하는 수가 없다면 -1을 출력한다.
"""
n = int(input())
nums = []

def add(idx, num):  # 자리수에 따라 증가
    if idx == 1:
        nums.append(num)
    else:
        for i in range(num % 10):  # 앞자리보다 작은 숫자들만 이어붙이기
            add(idx-1, num*10 + i)



for i in range(1, 11):
    for j in range(i - 1, 10):
        add(i, j)


print(nums)
if n >= len(nums):  # 감소하는 숫자가 없을 때
    print(-1)
else:
    print(nums[n])