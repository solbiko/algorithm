"""
DNA 문자열은 모든 문자열에 등장하는 문자가 {‘A’, ‘C’, ‘G’, ‘T’} 인 문자열을 말한다
임의의 DNA 문자열을 만들고 만들어진 DNA 문자열의 부분문자열을 비밀번호로 사용하기로 마음먹었다.
 큰 문제가 있다는 것을 발견했다. 임의의 DNA 문자열의 부분문자열을 뽑았을 때 “AAAA”와 같이 보안에 취약한 비밀번호가 만들어 질 수 있기 때문이다.
부분문자열에서 등장하는 문자의 개수가 특정 개수 이상이여야 비밀번호로 사용할 수 있다는 규칙을 만들었다.

임의의 DNA문자열이 “AAACCTGCCAA” 이고 민호가 뽑을 부분문자열의 길이를 4라고 하자.
‘A’ 는 1개 이상, ‘C’는 1개 이상, ‘G’는 1개 이상, ‘T’는 0개 이상이 등장해야 비밀번호로 사용가능
“ACCT” 사용불가 ‘G’ 가 1 개 이상 등장
“GCCA” 사용가능


임의로 만든 DNA 문자열 길이 |S|와 비밀번호로 사용할 부분문자열의 길이 |P| (1 ≤ |P| ≤ |S| ≤ 1,000,000)
두번 째 줄에는 민호가 임의로 만든 DNA 문자열
세번 째 줄에는 부분문자열에 포함되어야 할 {‘A’, ‘C’, ‘G’, ‘T’} 의 최소 개수

4 2
GATA
1 0 0 1

만들 수 있는 비밀번호의 종류의 수 출력
"""
s,p= map(int, input().split()) # 문자열길이, 부분문자열길이
seqList=input() # 염기서열 문자열
passCkList=list(map(int, input().split())) # 부분문자열에 포함되어야할 염기 ACGT 최소 개수
passCkStatus=[0]*4
passCkFlag=0

def addSeq(c): # 새로 들어온 문자열 처리
    global passCkList, passCkStatus, passCkFlag

    if c=='A':
        passCkStatus[0]+=1
        if passCkList[0]==passCkStatus[0]:
            passCkFlag+=1
    if c=='C':
        passCkStatus[1]+=1
        if passCkList[1]==passCkStatus[1]:
            passCkFlag+=1
    if c=='G':
        passCkStatus[2]+=1
        if passCkList[2]==passCkStatus[2]:
            passCkFlag+=1
    if c=='T':
        passCkStatus[3]+=1
        if passCkList[3]==passCkStatus[3]:
            passCkFlag+=1


def removeSeq(c) : # 제거되는 문자열 처리
    global passCkList, passCkStatus, passCkFlag

    if c == 'A':
        if passCkList[0] == passCkStatus[0]:
            passCkFlag -= 1
        passCkStatus[0] -= 1
    if c == 'C':
        if passCkList[1] == passCkStatus[1]:
            passCkFlag -= 1
        passCkStatus[1] -= 1
    if c == 'G':
        if passCkList[2] == passCkStatus[2]:
            passCkFlag -= 1
        passCkStatus[2] -= 1
    if c == 'T':
        if passCkList[3] == passCkStatus[3]:
            passCkFlag -= 1
        passCkStatus[3] -= 1

for i in range(4):
    if passCkList[i]==0:
        passCkFlag+=1

resCnt=0 # 만들 수 있는 비밀번호의 종류의 수


for i in range(p): # 초기 p부분 문자열 처리
    addSeq(seqList[i])

if passCkFlag==4: # 유효한 비밀번호
    resCnt+=1


for i in range(p,s): #  초기 p부분 이후 한개씩 밀면서 슬라이딩 윈도우 크기(p)만큼 체크
    addSeq(seqList[i])
    removeSeq(seqList[i-p]) # 앞부분 밀어서 제거
    if passCkFlag==4:
        resCnt+=1

print(resCnt)


