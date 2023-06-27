from itertools import combinations_with_replacement
from collections import Counter


def solution(n, info):
    max_diff, max_comb_cnt = 0, {}

    for comb in combinations_with_replacement(range(11), n):  # 조합
        cnt = Counter(comb)  # 각각 몇점짜리 맞췄는지

        # 라이언, 어피치 점수 계산
        r_score, a_score = 0, 0
        for i in range(1, 11):
            if info[10 - i] < cnt[i]:  # 라이언 승
                r_score += i
            elif info[10 - i] > 0:  # 어피치 승
                a_score += i

        diff = r_score - a_score
        if diff > max_diff:  # 최대 최종점수
            max_comb_cnt = cnt
            max_diff = diff

    if max_diff > 0:  # 이겼으면
        answer = [0] * 11  # 10~1점까지
        for n in max_comb_cnt:
            answer[10 - n] = max_comb_cnt[n]
        return answer
    else:
        return [-1]