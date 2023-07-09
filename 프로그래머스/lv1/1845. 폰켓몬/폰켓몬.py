def solution(nums):

    cnt = len(set(nums))
    print(cnt)
    
    if len(nums) // 2 > cnt:
        return cnt
    else:
        return len(nums) // 2