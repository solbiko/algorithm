"""
두 단어 A와 B가 주어졌을 때, A에 속하는 알파벳의 순서를 바꾸어서 B를 만들 수 있다면, A와 B를 애너그램이라고 한다.
두 단어가 애너그램인지 아닌지 구하는 프로그램을 작성하시오.

bizarre brazier
bizarre & brazier are anagrams.
"""
n=int(input())
for i in range(n):
    a, b = map(str, input().split())

    x = sorted(list(a))
    y = sorted(list(b))

    if x == y:
        print("%s & %s are anagrams." % (a, b))
    else:
        print("%s & %s are NOT anagrams." % (a, b))