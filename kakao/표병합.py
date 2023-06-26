"""
UPDATE r c value : (r,c) value 저장
UPDATE value1 value2 : value1값 value2로 변경
MERGE r1 c1 r2 c2 : (r1, c1) 위치의 셀과 (r2, c2) 위치의 셀을 선택하여 병합
UNMERGE r c: 병합을 해제
PRINT r c : (r, c) 위치의 셀 출력

"""
def solution(commands):

    n=50
    board=[[(i,j) for j in range(n)] for i in range(n)] # 좌표 넣고 병합셀이면 좌측좌표 저장
    str_board=[['EMPTY']*n for _ in range(n)] # 값 저장

    answer = []

    for c in commands:
        arr=c.split()

        if arr[0]=='UPDATE':
            if len(arr)==4: # UPDATE r c value
                r,c = int(arr[1])-1,int(arr[2])-1
                x,y = board[r][c]
                str_board[x][y]=arr[3]

            elif len(arr)==3:  #  value1값 value2로 변경
                for i in range(n):
                    for j in range(n):
                        if arr[1]==str_board[i][j]:
                            str_board[i][j]=arr[2]


        elif arr[0]=='MERGE':
            r1,c1,r2,c2=int(arr[1])-1,int(arr[2])-1,int(arr[3])-1,int(arr[4])-1
            x1, y1 = board[r1][c1]
            x2, y2 = board[r2][c2]

            # 값 없는 경우 r2,c2 값 저장
            if str_board[x1][y1]=="EMPTY":
                str_board[x1][y1]=str_board[x2][y2]

            # board[i][j]의 값이 (x, y)인 모든 i, j에 대해 board[i][j]의 값을 변경
            for i in range(50):
                for j in range(50):
                    if board[i][j]==(x2,y2):
                        board[i][j]=(x1,y1)


        elif arr[0]=='UNMERGE':
            r,c = int(arr[1])-1, int(arr[2])-1
            x,y = board[r][c]
            temp = str_board[x][y]  # (r1, c1) 위치의 셀 값

            for i in range(n):
                for j in range(n):
                        if board[i][j]==(x,y): #  병합칸이면
                            board[i][j]=(i,j)  #  실행 초기의 상태로 돌아갑니다.
                            str_board[i][j]='EMPTY' # 병합을 해제하기 전 셀이 값을 가지고 있었을 경우로 돌리고
            str_board[r][c]=temp #  (r, c) 위치의 셀이 그 값을 가지게 됩니다.

        elif arr[0]=='PRINT':
            r,c=int(arr[1])-1, int(arr[2])-1
            x,y=board[r][c]
            answer.append(str_board[x][y])

    return answer

