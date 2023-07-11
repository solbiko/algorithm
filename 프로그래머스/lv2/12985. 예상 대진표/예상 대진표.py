import math
def solution(n,a,b):
#     def search(x,y,cnt):
#         x2=x/2
#         y2=y/2
#         if x2==y2:
#             return cnt-1
#         else:
#             return search(math.ceil(x2),math.ceil(y2), cnt+1)

#     return search(a,b,1)

    # a, b 를 xor 취하는 과정에서 ab 사이의 거리가 가까우면 상위비트는 차이가 나지않음
    # 거꾸로 ab 사이의 거리가 멀면 상위비트가 차이남
    return ((a-1)^(b-1)).bit_length()

    