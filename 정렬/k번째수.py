"""
11004
수 N개 A1, A2, ..., AN이 주어진다. A를 오름차순 정렬했을 때, 앞에서부터 K번째 있는 수를 구하는 프로그램
첫째 줄에 N(1 ≤ N ≤ 5,000,000)과 K (1 ≤ K ≤ N)이 주어진다.
둘째에는 A1, A2, ..., AN이 주어진다. (-109 ≤ Ai ≤ 109)
5 2
4 1 2 3 5
"""
import sys
input=sys.stdin.readline
n,k=map(int,input().split())
a=list(map(int,input().split()))

a.sort()
print(a[k-1])