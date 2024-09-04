T=int(input())
for tc in range(T):
    arr=input()
    cnt=0
    score=0
    for a in arr:
        if a=='O':
            cnt+=1
            score+=cnt
        else:
            cnt=0
    print(score)