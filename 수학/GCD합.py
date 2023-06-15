"""
양의 정수 n개가 주어졌을 때, 가능한 모든 쌍의 GCD의 합을 구하는 프로그램을 작성하시오.
첫째 줄에 테스트 케이스의 개수 t (1 ≤ t ≤ 100)이 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있다.
각 테스트 케이스는 수의 개수 n (1 < n ≤ 100)가 주어지고, 다음에는 n개의 수가 주어진다.
입력으로 주어지는 수는 1,000,000을 넘지 않는다.
"""
import sys
input=sys.stdin.readline

import math
import itertools as it

n=int(input())
for _ in range(n):
    arr=list(map(int,input().split()))
    sum=0
    for x,y in it.combinations(arr[1:],2):
        sum+=math.gcd(x,y)
    print(sum)