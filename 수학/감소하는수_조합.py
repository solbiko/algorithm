"""
음이 아닌 정수 X의 자릿수가 가장 큰 자릿수부터 작은 자릿수까지 감소한다면, 그 수를 감소하는 수라고 한다.
예를 들어, 321과 950은 감소하는 수지만, 322와 958은 아니다.
N번째 감소하는 수를 출력하는 프로그램을 작성하시오.
0은 0번째 감소하는 수이고, 1은 1번째 감소하는 수이다. 만약 N번째 감소하는 수가 없다면 -1을 출력한다.
"""
from itertools import combinations

n = int(input())

nums = []
# 반복문을 통해 감소하는 수를 조합
# 최대 감소하는 수는 9876543210
for i in range(1, 11):
    for j in combinations(range(10), i):
        num = sorted(list(j), reverse=True)
        nums.append(int("".join(map(str, num))))

nums.sort() # 감소하는 수 정렬
print(nums[n] if len(nums) > n else -1)  # 감소하는 수가 있을 때와 없는 경우