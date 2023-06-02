"""
Anagram이란 두 문자열이 알파벳의 나열 순서를 다르지만 그 구성이 일치하면 두 단어는 아나그램이라고 합니다.
예를 들면 AbaAeCe 와 baeeACA 는 알파벳을 나열 순서는 다르지만 그 구성을 살펴보면 A(2), a(1), b(1), C(1), e(2)로 알파벳과 그 개수가 모두 일치합니다.
즉 어느 한 단어를 재배열하면 상대편 단어가 될 수 있는 것을 아나그램이라 합니다.
길이가 같은 두 개의 단어가 주어지면 두 단어가 아나그램인지 판별
아나그램 판별시 대소문자가 구분

AbaAeCe
baeeACA
"""
a=input()
b=input()
str1=dict()
str2=dict()

for x in a:
    str1[x]=str1.get(x,0)+1
for x in b:
    str2[x]=str2.get(x,0)+1

for i in str1.keys():
    if i in str2.keys():
        if str1[i]!=str2[i]: # 개수가 같다면
            print("NO")
            break
    else:
        print("NO")
        break

else:
    print("YES")