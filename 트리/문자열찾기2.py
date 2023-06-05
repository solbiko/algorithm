"""
총 N개의 문자열로 이루어진 집합 S가 주어진다.
입력으로 주어지는 M개의 문자열 중에서 집합 S에 포함되어 있는 것이 총 몇 개인지 구하는 프로그램을 작성하시오.

첫째 줄에 문자열의 개수 N과 M (1 ≤ N ≤ 10,000, 1 ≤ M ≤ 10,000)이 주어진다.
다음 N개의 줄에는 집합 S에 포함되어 있는 문자열들이 주어진다.
다음 M개의 줄에는 검사해야 하는 문자열들이 주어진다.
입력으로 주어지는 문자열은 알파벳 소문자로만 이루어져 있으며, 길이는 500을 넘지 않는다. 집합 S에 같은 문자열이 여러 번 주어지는 경우는 없다.

첫째 줄에 M개의 문자열 중에 총 몇 개가 집합 S에 포함되어 있는지 출력한다.
5 11
baekjoononlinejudge
startlink
codeplus
sundaycoding
codingsh
baekjoon
codeplus
codeminus
startlink
starlink
sundaycoding
codingsh
codinghs
sondaycoding
startrink
icerink
"""
import sys
input=sys.stdin.readline

# 노드 클래스 생성
class Node(object):
    def __init__(self, isEnd):
        self.isEnd=isEnd  # 마지막 문자열 여부
        self.childNode={}  # 자식노드

class Trie(object):
    def __init__(self):
        self.parent=Node(None)  # 부모노드 저장 변수

    # 문자 삽입
    def insert(self, string):
        nowNode=self.parent
        temp_length=0 # 문자길이 체크
        for char in string:
            # 자식 노드들 미생성된 문자열이면 새로 생성
            if char not in nowNode.childNode:
                nowNode.childNode[char]=Node(char)
            nowNode=nowNode.childNode[char]  # 자식노드로 이동
            temp_length+=1
            # 이번 문자열의 마지막 문자라면
            if temp_length==len(string):
                nowNode.isEnd=True

    # 문자열 존재하는지 탐색
    def search(self, string):
        nowNode=self.parent
        temp_length=0
        for char in string:
            if char in nowNode.childNode:
                nowNode=nowNode.childNode[char]
                temp_length+=1
                # 마지막 문자까지 모두 존재하고 마지막 문자에 isEnd가 True인 경우
                if temp_length==len(string) and nowNode.isEnd==True:
                    return True
            else:
                return False
        return False


n,m=map(int,input().split())
myTrie=Trie()  # Trie 생성

# 문자열 삽입
for _ in range(n):
    word=input().strip()
    myTrie.insert(word)   # 단어 삽입

# 문자열 찾기
cnt=0
for _ in range(m):
    word=input().strip()
    if myTrie.search(word):  # 단어찾기
        cnt+=1

print(cnt)
