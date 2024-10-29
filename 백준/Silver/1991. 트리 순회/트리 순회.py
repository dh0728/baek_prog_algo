import sys
#sys.stdin=open('input.txt')
input = sys.stdin.readline

# 전위 순회
def preorder(node):
    if node == 0:
        return
    print(chr(node + 64), end='')
    preorder(left_node[node])
    preorder(right_node[node])

# 중위 순회
def inorder(node):
    if node == 0:
        return
    inorder(left_node[node])
    print(chr(node+64),end='')
    inorder(right_node[node])

# 후위 순회
def postorder(node):
    if node == 0:
        return
    postorder(left_node[node])
    postorder(right_node[node])
    print(chr(node + 64), end='')

N = int(input())

left_node=[0]*(N+1)
right_node=[0]*(N+1)
for _ in range(N):
    node, left, right =input().strip().split()
    if left.isalpha(): # 알파벳이면
        left_node[ord(node) - 64]=ord(left) - 64
    if right.isalpha(): # 알파벳이면 
        right_node[ord(node) - 64]=ord(right) - 64

preorder(1)
print()
inorder(1)
print()
postorder(1)