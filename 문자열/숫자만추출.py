"""
문자와 숫자가 섞여있는 문자열(~50)이 주어지면 그 중 숫자만 추출하여 그 순서대로 자연수를 만 듭니다.
만들어진 자연수와 그 자연수의 약수 개수를 출력합니다.

만약 “t0e0a1c2h0er”에서 숫자만 추출하면 0, 0, 1, 2, 0이고 이것을 자연수를 만들면 120
120를 출력하고 다음 줄에 120 의 약수의 개수를 출력

추출하여 만들어지는 자연수는 100,000,000을 넘지 않습니다.
"""

str=input()
disStr=""
for i in str:
    if i.isdecimal():
        disStr+=i

num=int(disStr)
print(num)

cnt=0
for i in range(1, num+1):
    if num%i==0:
        cnt+=1
print(cnt)
