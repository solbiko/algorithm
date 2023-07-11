def solution(brown, yellow):
    s = brown+yellow
    for i in range(1,s//2):
        if s%i==0:
            if i<=s//i and i>2:
                h=i
                w=s//i
                if (w-2)*(h-2)==yellow:
                    return [w,h]
