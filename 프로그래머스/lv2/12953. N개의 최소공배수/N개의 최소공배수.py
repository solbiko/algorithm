from math import gcd
def solution(arr):
    answer = arr[0]

    for x in arr:
        answer = answer*x // gcd(answer, x)     

    return answer