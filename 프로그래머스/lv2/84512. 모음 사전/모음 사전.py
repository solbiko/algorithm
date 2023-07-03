from itertools import product


def solution(word):
    arr=['A', 'E', 'I', 'O', 'U']
    arr.sort()
    prod=[]
    for i in range(1,6):
        prod+=list(product(arr, repeat=i))

    prod.sort()
    cnt=1
    for x in prod:
        str="".join(x)
        print(str)
        if str==word:
            break
        else:
            cnt+=1

    return cnt