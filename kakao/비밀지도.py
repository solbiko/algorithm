def solution(n, arr1, arr2):
    answer = []

    a1 = []
    a2 = []
    for i in range(n):
        t1=bin(arr1[i])[2:]
        t1='0'*(n-len(t1))+t1
        a1.append(t1)

        t2=bin(arr2[i])[2:]
        t2='0'*(n-len(t2))+t2
        a2.append(t2)

    for i in range(n):
        temp=['#']*n
        for j in range(n):
            if a1[i][j]==a2[i][j]=='0':
                temp[j]=' '
        answer.append(''.join(temp))

    return answer


print(solution(5,[9, 20, 28, 18, 11],[30, 1, 21, 17, 28]))
print(solution(6,[46, 33, 33 ,22, 31, 50],[27 ,56, 19, 14, 14, 10]))
