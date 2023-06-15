""""
N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.
첫째 줄에 N이 주어진다. (0 ≤ N ≤ 500)
"""
import math
n=int(input())

def fac(x):
    if x>1: return x * fac(x - 1)
    else: return 1

m=str(fac(n))
# m=str(math.factorial(n))

cnt=0
for i in range(len(m)):
    if m[-1-i]=='0':
        cnt+=1
    else:
        break
print(cnt)