n,k =  map(int, input().split())
list = list(map(int, input().split()))

# 구간합 배열
sumList = [0]

temp = 0
for i in list:
    temp += i
    sumList.append(temp)

print(sumList)


# 줄의 합을 구해야 하는 구간 s,e
for i in range(k):
    s, e = map(int, input().split())
    print(sumList[e]-sumList[s-1])