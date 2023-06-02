"""
1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써, 하나의 수열을 만들 수 있다. 이때, 스택에 push하는 순서는 반드시 오름차순을 지키도록 한다고 하자.
임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는지 없는지, 있다면 어떤 순서로 push와 pop 연산을 수행해야 하는지를 알아낼 수 있다. 이를 계산하는 프로그램을 작성하라.

첫 줄에 n (1 ≤ n ≤ 100,000)이 주어진다. 둘째 줄부터 n개의 줄에는 수열을 이루는 1이상 n이하의 정수가 하나씩 순서대로 주어진다.
입력된 수열을 만들기 위해 필요한 연산을 한 줄에 한 개씩 출력한다. push연산은 +로, pop 연산은 -로 표현하도록 한다. 불가능한 경우 NO를 출력한다.
"""
n=int(input())
a=[0]*n # 수열 리스트
for i in range(n):
    a[i]=int(input())

stack=[]
idx=1

flag=True
res=''

for i in range(n):
    num=a[i]
    if num>=idx: # 현재 수열값 >= 오름차순 자연수 : 같아질때까지 append
        while num>=idx:
            stack.append(idx)
            idx+=1
            res+='+\n'
        stack.pop()
        res+='-\n'
    else: # 현재 수열값 < 오름차순 자연수 : pop
        nn=stack.pop()
        # 수열의 가장 위의 수가 만드어야하는 수열의 수보다 크면 수열 출력 불가
        if nn>num:
            print("NO")
            flag=False
            break
        else:
            res+='-\n'

if flag:
    print(res)