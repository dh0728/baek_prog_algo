import sys
#sys.stdin=open('input.txt')
input = sys.stdin.readline

num1, num2 = input().strip().split()
num1_list = list(num1)
num2_list = list(num2)
num1_list.reverse()              
num2_list.reverse()

n1=''
for n in num1_list:
    n1+=n
n2=''
for n in num2_list:
    n2+=n
if int(n1)> int(n2):
    print(n1)
else:
    print(n2)