
n = int(input()) #1000까지
list = [0]*n

for i in range(n):
    list[i] = int(input())

print(list)

# 오름차순
# 버블정렬 n^2
for i in range(n):
    for j in range(n-i-1):
        print(j)
        if list[j] > list[j+1]:
            temp = list[j]
            list[j] = list[j+1]
            list[j+1] = temp
    i += 1
print(list)