def solution(name):
    answer=0 # 조이스틱 조작 횟수
    
    n=len(name)
    
    # 최소 이동 횟수는 길이 - 1
    move = len(name) -1
    
    for i,x in enumerate(name):
        answer+=min(ord(x)-ord('A'), ord('Z')-ord(x)+1) # 알파벳 변경 최솟값

        idxA = i+1 #  x다음 연속된 A 문자열 찾기
        while idxA<n and name[idxA] == 'A':
            idxA += 1
        move = min([move, 2*i+n-idxA, i+2*(n-idxA)]) # 연속된 A의 왼쪽시작, 연속된 A의 오른쪽시작
        
    answer += move # 알파벳 변경(상하이동) 횟수에 좌우이동 횟수 추가
    return answer