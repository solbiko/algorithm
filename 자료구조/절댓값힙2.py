from queue import PriorityQueue
import sys
input=sys.stdin.readline
print=sys.stdout.write

n=int(input())
q = PriorityQueue()

for i in range(n):
    num=int(input())
    if num==0:
        if q.empty():
            print('0\n')
        else:
            temp=q.get()
            print(str((temp[1]))+'\n')
    else:
        #절대값을 기준으로 정렬하고 같으면 음수 우선 정렬하도록 구성
        q.put((abs(num), num))
