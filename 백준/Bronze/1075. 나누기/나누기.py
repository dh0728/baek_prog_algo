num = input()
M = int(input())
num = int(num[:-2] + '00')
while True:
    if num % M == 0:
        break
    num += 1
print(str(num)[-2:])