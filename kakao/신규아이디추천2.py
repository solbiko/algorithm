import re
def solution(new_id):
    st = new_id
    st = st.lower()								#1단계
    st = re.sub('[^a-z0-9\-_.]', '', st)					#2단계
    st = re.sub('\.+', '.', st)							#3단계
    st = re.sub('^[.]|[.]$', '', st)						#4단계
    st = 'a' if len(st) == 0 else st[:15]					#5&6단계
    st = re.sub('^[.]|[.]$', '', st)						#6단계
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])#7단계
    return st

print(solution("...!@BaT#*..y.abcdefghijklm"))