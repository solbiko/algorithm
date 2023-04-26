import sys
input=sys.stdin.readline

N = int(input())
tree = {}

for n in range(N):
    root, left, right = input().split()
    tree[root] = [left, right]


def preorder(r):
    if r != '.':
        print(r, end='')  # root
        preorder(tree[r][0])  # left
        preorder(tree[r][1])  # right


def inorder(r):
    if r != '.':
        inorder(tree[r][0])  # left
        print(r, end='')  # root
        inorder(tree[r][1])  # right


def postorder(r):
    if r != '.':
        postorder(tree[r][0])  # left
        postorder(tree[r][1])  # right
        print(r, end='')  # root


preorder('A')
print()
inorder('A')
print()
postorder('A')
