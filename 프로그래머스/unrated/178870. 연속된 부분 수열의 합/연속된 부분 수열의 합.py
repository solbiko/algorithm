import sys
def solution(sequence, k):
    answer = []
    
    n=len(sequence)
    sums = 0
    min_val = sys.maxsize
    
    # 투포인터
    end = 0
    for start in range(n):
        
        while end<n and sums<k:
            sums+=sequence[end]
            end += 1
            
        if sums==k and min_val>end-start:
            min_val=end-start
            answer=[start, end-1]

        sums -= sequence[start]
        
    return answer