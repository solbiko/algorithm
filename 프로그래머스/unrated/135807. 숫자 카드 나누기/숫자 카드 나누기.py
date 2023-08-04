import sys,math
def solution(arrayA, arrayB):
    
    def find(array): #최대공약수
        GCD = 0
        for i in range(len(array)):
            GCD = math.gcd(GCD, array[i])
        return GCD
    
    def check(array, g): # 다른 배열 나눌 수 있는지 체크
        for x in array:
            if x % g == 0:
                return 0
        return g
    
    gA=find(arrayA)
    gB=find(arrayB)
    
    gA=check(arrayB, gA)
    gB=check(arrayA, gB)

    return max((gA, gB))