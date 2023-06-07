"""
1427
수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬
N이 주어진다. N(1~1,000,000,000) 9
2143
"""
a=list(input())

# 내장함수 풀이
# a.sort(reverse=True)

# 선택정렬 풀이
length=len(a)
for i in range(length):
    maxIdx=i
    for j in range(i+1,length):
        if a[j]>a[maxIdx]:
            maxIdx=j
    if a[i]<a[maxIdx]:  # swap
        temp=a[i]
        a[i]=a[maxIdx]
        a[maxIdx]=temp

for i in range(len(a)):
    print(a[i], end="")