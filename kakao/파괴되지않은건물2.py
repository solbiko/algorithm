"""
1 ≤ board의 행의 길이 (= N) ≤ 1,000
1 ≤ board의 열의 길이 (= M) ≤ 1,000
1 ≤ skill의 행의 길이 ≤ 250,000
"""
import numpy as np
def solution(board, skill):
    answer = 0  # 적의 공격 혹은 아군의 회복 스킬이 모두 끝난 뒤 파괴되지 않은 건물의 개수
    n=len(board)
    m=len(board[0])
    temp=[[0 for j in range(m+1)] for i in range(n+1)]

    for t,r1,c1,r2,c2,d in skill:
        tt= -d if t==1 else d
        temp[r1][c1]+=tt
        temp[r1][c2+1]-=tt
        temp[r2+1][c1]-=tt
        temp[r2+1][c2+1]+=tt

    temp = np.cumsum(temp,axis=1)
    temp = np.cumsum(temp,axis=0)
    answer = np.array(board) + temp[:len(board), :len(board[0])]

    return len(np.where(answer > 0)[0])