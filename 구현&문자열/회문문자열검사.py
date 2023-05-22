"""
앞에서 읽을 때나 뒤에서 읽을 때나 같은 경우(회문 문자열)이면 YES를 출력하고 회문 문자열이 아니면 NO를 출력
첫 줄에 정수 N(1<=N<=20)이 주어지고, 그 다음 줄부터 N개의 단어가 입력된다. 각 단어의 길이는 100을 넘지 않는다.

5
level
moon
abcba
soon
gooG

#1 YES
#2 NO
#3 YES
#4 NO
#5 YES
"""

n=int(input())
for i in range(n):
    s=input()
    s=s.upper()
    size=len(s)

    for j in range(size//2):
        if s[j]!=s[-1-j]:
            print("#%d NO" %(i+1))
            break
    else:
        print("#%d YES" %(i+1))

