"""
어떤 수와 그 수의 숫자 순서를 뒤집은 수가 일치하는 수를 팰린드롬이라 부른다. 예를 들어 79,197과 324,423 등이 팰린드롬 수이다.
어떤 수 N (1 ≤ N ≤ 1,000,000)이 주어졌을 때, N보다 크거나 같고, 소수이면서 팰린드롬인 수 중에서, 가장 작은 수를 구하는 프로그램을 작성하시오.
"""
import math

n=int(input())

# 에라토스테네스 채 소수구하기
a=[0]*10000001
for i in range(2, len(a)):
    a[i] = i

for i in range(2, int(math.sqrt(len(a))+1)):
   if a[i] == 0:
       continue
   for j in range(i+i, len(a), i):
       a[j] = 0

def isPalindrome(num):
    flag = True
    tmp=list(str(num))
    for j in range(len(tmp)//2):
        if tmp[j] != tmp[-1-j]:
            flag = False
    return flag

for i in range(2,len(a)):
    if a[i]!=0 and n<=a[i]:  # N보다 크거나 같고, 소수
        num=a[i]
        if isPalindrome(a[i]):
            print(a[i])
            break
