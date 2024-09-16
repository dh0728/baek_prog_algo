import sys

def add(n):
    S.add(n)

def check(n):
    if n in S:
        return 1
    else:
        return 0

def remove(n):
    S.discard(n)

def toggle(n):
    if n in S:
        S.remove(n)
    else:
        S.add(n)

def all():
    for v in range(1,21):
        S.add(str(v))


N=int(sys.stdin.readline())
S=set()
for _ in range(N):
    word= list(sys.stdin.readline().split())

    if word[0]=='add':
        add(word[1])
    elif word[0]=='remove':
        remove(word[1])
    elif word[0]=='check':
        print(check(word[1]))
    elif word[0]=='toggle':
        toggle(word[1])
    elif word[0]=='all':
        all()
    else:
        S=set()