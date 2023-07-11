def solution(brown, yellow):
    s = brown+yellow
    for i in range(1,s//2):
        if s%i==0:
            if i<=s//i and i>2:
                if (s//i-2)*(i-2)==yellow:
                    return [s//i,i]
