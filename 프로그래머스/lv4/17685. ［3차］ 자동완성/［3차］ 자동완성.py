# 노드 클래스 생성
class Node(object):
    def __init__(self, wordCnt):
        self.wordCnt=0 # 만들 수 있는 단어수
        self.childNode={}  # 자식노드

class Trie(object):
    def __init__(self):
        self.parent=Node(None)  # 부모노드 저장 변수

    # 문자 삽입
    def insert(self, string):
        nowNode=self.parent
        for char in string:
            nowNode.wordCnt+=1
            if char not in nowNode.childNode:
                nowNode.childNode[char]=Node(char)
            nowNode=nowNode.childNode[char]  # 자식노드로 이동
        nowNode.wordCnt+=1
        
    # 문자열 존재하는지 탐색
    def search(self, string):
        nowNode=self.parent
        for char in string:
            if char in nowNode.childNode:
                nowNode=nowNode.childNode[char]
            else:
                return False
        if nowNode.wordCnt==1:
            return True
        else:
            return False

def solution(words):
    answer = 0

    myTrie=Trie()  # Trie 생성
    for x in words: 
        myTrie.insert(x)   # 단어 삽입
        
    for word in words:
        already_find=False
        for i in range(1, len(word)+1):
            if myTrie.search(word[:i]):
                answer+=len(word[:i])
                already_find=True
                break
                
        if not already_find:
            answer+=len(word)
            
    return answer