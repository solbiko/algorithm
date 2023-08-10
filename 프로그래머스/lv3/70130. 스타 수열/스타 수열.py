from collections import Counter
def solution(a):
    answer = 0

    if len(a) <= 1:
        return 0

    c = {i: v for i, v in Counter(a).most_common()}
    
    for i in c:
        if c[i]*2 <= answer: # i의 등장 횟수가 공통인자 횟수 이하
            continue
        cnt = 0
        idx = 0
        while idx < len(a)-1:
            if (a[idx]!=i and a[idx+1]!=i) or a[idx] == a[idx+1]:
                # 집합에 두 값 모두 i가 아님, 집합에 두 값이 같음 -> 스타수열 X
                idx += 1
                continue
            cnt+=2
            idx+=2

        answer = max(answer, cnt)

    return answer