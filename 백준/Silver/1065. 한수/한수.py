import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())

def solution():
   
    cnt = 0
   
    for i in range(1,N+1):
        if i < 100:
            cnt += 1
        elif 100 < i < 1000:
            num_list = []
            x = 100
            num = i
            ch = 3
            while ch:
                n = num / x
                num_list.append( int(n))
                num %= x
                x /= 10
                ch -= 1

            if num_list[2] - num_list[1] == num_list[1] - num_list[0]:
                cnt +=1

    print(cnt)
    return 0


if __name__ == "__main__":
    solution()


