def solution(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        answer.append(str(bin(i|j)[2:]).rjust(n, '0').replace('1', '#').replace('0', ' '))
    return answer

print(solution(5,[9, 20, 28, 18, 11],[30, 1, 21, 17, 28]))
print(solution(6,[46, 33, 33 ,22, 31, 50],[27 ,56, 19, 14, 14, 10]))
