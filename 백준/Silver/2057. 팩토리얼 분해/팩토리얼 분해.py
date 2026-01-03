import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input().strip())
fac = [1,1]
for i in range(2,21):
    fac.append(fac[-1]*i)

def bf(now, i):
    if i == 21:
        return now == N
    a = bf(now + fac[i], i + 1)
    b = bf(now, i+ 1)
    return a or b
    
def solution():

    if N == 0:
        print("NO")
        return
    
    if bf(0,0):
        print("YES")
    else:
        print("NO")
    return
    
if __name__ == "__main__":
    solution()

