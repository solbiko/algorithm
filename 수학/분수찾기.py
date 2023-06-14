"""
분수들을 1/1 → 1/2 → 2/1 → 3/1 → 2/2 → … 과 같은 지그재그 순서로 차례대로 1번, 2번, 3번, 4번, 5번, … 분수라고 하자.
1/1 - 1/2 - 2/1 - 3/1 - 2/2 - 1/3 - 1/4 - 2/3 - 3/2 - 4/1 - 5/1 - 4/2 - 3/3 - 2/4
X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오. 1 ≤ X ≤ 10,000,000
"""
x=int(input())
a=[]

j=1
for i in range(4500):
    a.append(i+j)
    j+=i

# print(a)

for i in range(4500):
    if x==a[i]:
        if i%2==0:
            print(str(i + 1) + "/1")
        else:
            print("1/" + str(i + 1))
        break
    elif a[i]<x<a[i+1]:
        temp=x-a[i]
        if i%2==0:
            print(str(i+1-temp)+"/"+str(1+temp))
        else:
            print(str(1+temp)+"/"+str(i+1-temp))
        break
