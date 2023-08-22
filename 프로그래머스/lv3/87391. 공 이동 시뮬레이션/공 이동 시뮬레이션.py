"""
n × m개의 가능한 시작점에 대해서 해당 시작점에 공을 두고 queries 내의 쿼리들을 순서대로 시뮬레이션했을 때, x행 y열에 도착하는 시작점의 개수
"""
def solution(n, m, x, y, queries):
    sr,sc,er,ec = x,y,x,y

    # queries 역순으로
    for command, dx in reversed(queries):

        if command == 0: # 좌
            if sc==0:
                ec=min(m-1, ec+dx)
            else: 
                if sc+dx >= m: return 0
                sc = min(m-1, sc+dx)
                ec = min(m-1, ec+dx)

        elif command == 1: # 우
            if ec == m-1:
                sc = max(0, sc-dx)
            else:
                if ec-dx < 0: return 0
                sc = max(0, sc-dx)
                ec = max(0, ec-dx)

        elif command == 2: # 상
            if sr == 0: 
                er = min(n-1, er+dx)
            else: 
                if sr+dx >= n: return 0 
                sr = min(n-1, sr+dx)
                er = min(n-1, er+dx)

        else:  # 하
            if er == n-1:
                sr = max(0, sr-dx)
            else:
                if er+dx < 0: return 0 
                sr = max(0, sr-dx)
                er = max(0, er-dx)

    return (er-sr+1)*(ec-sc+1)
