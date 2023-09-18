import re
from collections import Counter
def solution(s):
    
    s = Counter(re.findall('\d+', s))
    s = sorted(s.items(), key=lambda x: x[1], reverse=True)
    
    return [int(k) for k, v in s]

