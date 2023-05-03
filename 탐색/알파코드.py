"""
알파벳 A에는 1로, B에는 2로 이렇게 해서 Z에는 26을 할당
"BEAN"을 암호화하면 25114
알파벳으로 바꾸면 BEAAD, YAAD, YAN, YKD, BEKD, BEAN ...

암호화된 코드가 주어지면 그것을 알파벳으로 복원하는데 얼마나 많은 방법인 있는지

입력된 코드를 알파벳으로 복원하는데 몇 가지의 방법이 있는지 각 경우를 출력, 그 가지 수도 출력
단어의 출력은 사전순으로 출력
"""
code=list(map(int, input()))
n=len(code) # 종착점
code.insert(n,-1) # 마지막값 <= 2인 경우, idx+1번째 code도 체크하기 때문에
res=[0]*(n+3)
cnt=0

def dfs(idx, p):
    global cnt
    if idx==n:
        for i in range(p):
            print(chr(res[i]+64), end="")
        cnt+=1
        print()

    else:
        for i in range(1,27):
            if code[idx]==i: # 한자리
                res[p]=i
                dfs(idx+1, p+1)
            elif 10<=i and code[idx]==i//10 and code[idx+1]==i%10: # 10자리
                res[p]=i
                dfs(idx+2, p+1)

dfs(0,0)
print(cnt)