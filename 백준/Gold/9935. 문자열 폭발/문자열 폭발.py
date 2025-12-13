import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

str = list(input().strip())
bumb = list(input().strip())
blen = len(bumb)

def solution():

    stack = []

    for c in str:
        stack.append(c)
        slen = len(stack)

        if stack[slen - blen:] == bumb:
            for _ in range(blen):
                stack.pop()

    if stack:
        print( "".join(stack))
    else:
        print("FRULA")

if __name__ == "__main__":
    solution()