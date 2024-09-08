def find_ans(n):
    if n%15==0:
        print('FizzBuzz')
    elif n%3==0:
        print('Fizz')
    elif n%5==0:
        print('Buzz')
    else:
        print(n)
def FizzBuzz():
    num=0
    for i in range(1,len(arr)):
        if arr[i] != 'Fizz' and arr[i] !='Buzz' and arr[i] != 'FizzBuzz':
            if i==1:
                num=int(arr[i])+3
            elif i==2:
                num=int(arr[i])+2
            else:
                num=int(arr[i])+1
            break
    find_ans(num)

arr=[0]+[input() for _ in range(3)]
FizzBuzz()