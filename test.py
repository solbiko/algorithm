from bisect import bisect_left, bisect_right

a = [0, 1, 2, 3, 4, 5, 8, 10]
x = 3
y = 7
print(bisect_left(a, x))  # 3
print(bisect_left(a, y))  #