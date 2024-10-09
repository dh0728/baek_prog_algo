import sys
#sys.stdin=open('input.txt')
input = sys.stdin.readline


col_dict={'black':0,
          'brown':1,
          'red':2,
          'orange':3,
          'yellow':4,
          'green':5,
          'blue':6 ,
          'violet':7,
          'grey':8,
          'white':9}

num=''
result=0
for i in range(3):
    color =input().strip()
    if i !=2:
        num +=str(col_dict[color])
        continue
    result = int(num)*pow(10,col_dict[color])

print(result)
