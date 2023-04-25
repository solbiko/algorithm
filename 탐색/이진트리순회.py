"""
이진트리를 전위순회와 후위순회
"""

#전위순회 출력 : 1 2 4 5 3 6 7
def preorder(v):
    if v > 7:
        return
    else:
        print(v, end=' ')
        preorder(v * 2)
        preorder(v * 2 + 1)
preorder(1)
print()

# 중위순회 출력 : 4 2 5 1 6 3 7
def inorder(v):
    if v > 7:
        return
    else:
        inorder(v * 2)
        print(v, end=' ')
        inorder(v * 2 + 1)
inorder(1)
print()

#후위순회 출력 : 4 5 2 6 7 3 1
def postorder(v):
    if v > 7:
        return
    else:
        postorder(v * 2)
        postorder(v * 2 + 1)
        print(v, end=' ')
postorder(1)
print()