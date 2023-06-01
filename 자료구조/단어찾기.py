"""
현수는 시를 쓰기 전에 시에 쓰일 단어를 미리 노트에 적어둡니다.
이번에는 N개의 단어를 노트에 적었는데 시에 쓰지 않은 단어가 하나 있다고 합니다. 여러분이 찾아 주세요.

첫 번째 줄에 자연수 N(3<=N<=100)이 주어진다.
두 번째 줄부터 노트에 미리 적어놓은 N개의 단어가 주어지고, 이어 바로 다음 줄부터 시에 쓰인 N-1개의 단어가 주어진다.

첫 번째 줄에 시에 쓰지 않은 한 개의 단어를 출력한다.
5
big
good
sky
blue
mouse
sky
good
mouse
big

blue
"""
import sys
input=sys.stdin.readline

n=int(input())
dict = {}
for _ in range(n):
    dict[input()]=1

for _ in range(n-1):
    dict[input()]=0

for key,val in dict.items():
    if val==1:
        print(key)
        break