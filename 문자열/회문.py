"""
회문이 아니지만 한 문자를 삭제하여 회문으로 만들 수 있는 문자열이라면 우리는 이런 문자열 : 유사회문

회문인지, 또는 한 문자를 삭제하면 회문이 되는 “유사회문”인지, 아니면 회문이나 유사회문도 아닌 일반 문자열
회문이면 0, 유사회문이면 1, 그 외는 2를 출력
"""


def check2(str, i, j):
    while i < j:
        if str[i] == str[j]:
            i += 1
            j -= 1
        else:
            return False
    return True


def check(str, i, j):
    if str == str[::-1]:  # 바로 화문인 경우
        return 0
    while i < j:
        if str[i] == str[j]:
            # 같으면 한칸씩 이동해서 다음 문자 체크
            i += 1
            j -= 1
        else:
            # 다른 문자가 있을 경우 회문X, 유사회문인지 검사
            iCheck = check2(str, i+1, j)  # 왼쪽 한칸 건너뜀
            jCheck = check2(str, i, j-1)  # 오른쪽 한칸 건너뜀

            if iCheck or jCheck:
                # check2에서 다른 문자 안나왔으면 유사회문
                return 1
            else:  # 다른 문자 나온 경우
                return 2
            
    return 1


t = int(input())

for i in range(t):
    str = input()
    print(check(str, 0, len(str) - 1))