n=int(input())
arr=list(map(int, input().split()))
s=sum(arr)

res = [arr[0]]
for i in range(1, n):
    num = arr[i]
    temp = [num]
    for e in res:
        temp += [num+e, abs(num-e)]
    res += temp
res = list(set(res))

if 0 in res:
    res.remove(0)

print(s-len(res))