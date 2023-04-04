n=int(input())
array=list(map(int, input().split()))

#순서를 뒤집어 LIS 문제로 변환
array.reverse()

d=[1]*n

for i in range(1,n):
    for j in range(0, i):
        if array[j]<array[i]:
            # j를 마지막으로 갖는 부분 수열 최대길이 +1와 비교
            d[i]=max(d[i], d[j]+1)

# 열외시켜야하는 병사의 최소 수
print(n-max(d))