import sys
input=sys.stdin.readline

T=int(input())
for tc in range(1, T+1):

    n=int(input())
    kind_dict={}
    for _ in range(n):
        name, kind=input().split()
        if kind in kind_dict: # 같은 종류의 옷이 있으면
            kind_dict[kind]+=1
        else: # 같은 종류 옷 없으면
            kind_dict[kind]=1

    cnt=1
    for k in kind_dict:
        cnt *= kind_dict[k]+1 # 해당 종류의 옷 개수 + 해당 종류를 안입을 경우(1) 다 곱하기
    print(cnt-1) # 아무것도 안입은 경우 빼주기