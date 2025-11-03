import sys
input=sys.stdin.readline

s=int(input())
l=list(map(int,input().split()))
if(1 not in l):
    l.append(0)
n=int(input())
cnt=0
l.sort()


for i in range(len(l)-1):
    if(n>l[i] and n<l[i+1]):
        tmp=[i for i in range(l[i]+1,l[i+1])]
        #print(tmp)
        for j in range(len(tmp)-1):
            for k in range(j,len(tmp)):
                if(n>=tmp[j] and n<=tmp[k] and tmp[j]!=tmp[k]):
                    #print(tmp[j],tmp[k])
                    cnt+=1
print(cnt)