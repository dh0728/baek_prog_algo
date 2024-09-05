arr=[]
while True:
    case=list(map(int,input().split()))
    if case.count(0)==3:
        break
    arr.append(case)

for a in arr:
    a.sort()
    if a[0]**2+a[1]**2==a[2]**2:
        print('right')
    else:
        print('wrong')
