def solution(sizes):
    for x in sizes:
        x.sort()
        
    maxw=0
    maxh=0
    for w,h in sizes:
        maxw=max(maxw,w)
        maxh=max(maxh,h)

    return maxw*maxh


