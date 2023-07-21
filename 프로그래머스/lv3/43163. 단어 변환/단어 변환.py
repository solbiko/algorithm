from collections import deque
def solution(begin, target, words):
    answer = 0
    
    v=[0]*len(words) # 단어 사용체크 리스트
    
    q = deque()
    q.append([begin, 0])
    
    while q:
        word, cnt = q.popleft()
        
        if word == target:
            answer = cnt
            break        
        
        for i in range(len(words)):
            word2=words[i]
            temp_cnt = 0
            
            if not v[i]: # 사용안한경우
                # 단어 두개 비교
                for j in range(len(word)): 
                    if word[j] != word2[j]:
                        temp_cnt += 1
                if temp_cnt == 1:
                    q.append([word2, cnt+1])
                    v[i] = 1 # 사용처리
                    
    return answer