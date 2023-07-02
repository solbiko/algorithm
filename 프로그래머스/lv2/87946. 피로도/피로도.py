"""
최소 필요 피로도"는 해당 던전을 탐험하기 위해 가지고 있어야 하는 최소한의 피로도를 나타내며, 
소모 피로도"는 던전을 탐험한 후 소모되는 피로도를 나타냅니다.
"""
from itertools import permutations
def solution(k, dungeons):
    answer = -1

    max_cnt=0
    for x in permutations(dungeons, len(dungeons)):
        hp=k
        cnt=0
        for need,spent in x:
            if need>hp:
                break
            hp-=spent
            cnt+=1
        max_cnt=max(max_cnt, cnt)

    return max_cnt