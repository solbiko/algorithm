from string import ascii_uppercase, ascii_lowercase
a = ascii_uppercase
b = ascii_lowercase

def solution(s, n):
    answer=''
    for x in s:
        if x.islower():
            answer+=b[(b.index(x)+n)%len(b)]
        elif x.isupper():
            answer+=a[(a.index(x)+n)%len(a)]
        else:
            answer += x

    return answer