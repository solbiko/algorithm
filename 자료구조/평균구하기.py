n = input()
score_list = list(map(int, input().split()))

# 최댓값 구하기
max = max(score_list)


# (a/max * 100 + b/max * 100 )/2
# a + b / (max * 100) /2

# score list 합계 구하기
sum = sum(score_list)


# 새로운 평균
print(sum * 100 / max / int(n))