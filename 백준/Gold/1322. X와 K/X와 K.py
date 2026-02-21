import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

X, K = map(int, input().split())
X = list(bin(X)[2:])
K = list(bin(K)[2:])

def solution():
    res = ""
    while K:
        if X:
            n = X.pop()
            if n == "1":
                res += "0"
            else:
                res += K.pop()

        else:
            res += K.pop()
    return res

res = solution()
print(int("0b" + res[::-1],2))
