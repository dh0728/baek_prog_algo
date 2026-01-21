import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

S = int(input().strip())


def solution():

    global S
    i = 0
    cnt = 0

    while True:
        if S > i:
            i +=1
            S -= i
            cnt += 1
        else:
            print(cnt)
            return
 
if __name__ == "__main__":
    solution()

