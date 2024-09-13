def pack(n):
    p=1
    while n>0:
        p*=n
        n-=1
    return p
def find_zero(n):
    str_n=str(n)
    cnt=0
    for i in range(len(str_n)-1,-1,-1):
        if str_n[i]=='0':
            cnt+=1
        else:
            break
    return cnt

N=int(input())
num=pack(N)
result=find_zero(num)
print(result)