arr=input()
#a=97 z=122
ch=[-1]*26
for i ,a in enumerate(arr):
    ch_n=ord(a)-97
    if ch[ch_n]==-1:
        ch[ch_n]=i
print(' '.join(map(str,ch)))