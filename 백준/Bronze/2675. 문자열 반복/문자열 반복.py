T=int(input())
for tc in range(1,T+1):
    R, S= input().split()
    word=''
    for s in S:
        word += s*int(R)
    print(word)