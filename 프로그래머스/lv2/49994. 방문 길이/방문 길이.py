def solution(dirs):
    d={'U':(-1,0),'D':(1,0),'R':(0,1),'L':(0,-1)}
    
    sets = set()

    r=c=0
    for x in dirs:
        nr=r+d[x][0]
        nc=c+d[x][1]
        if -5<=nr<=5 and -5<=nc<=5:
            sets.add(((r, c), (nr, nc)))
            sets.add(((nr, nc), (r, c)))
            r = nr
            c = nc
    
    return len(sets) // 2