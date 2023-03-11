"""
+-괄호를 이용해 수식 생성 -> 다시 배치, 괄호 넣어서 최소값
100-40+50+74-30+29-45+43+11
"""

prefix = input()
arr = prefix.split("-")

result = 0

for i in range(len(arr)):
    arr2 = list(map(int, arr[i].split("+")))
    print(arr2)

    if i == 0:
        result += sum(arr2)
    else:
        result -= sum(arr2)

print(result)
