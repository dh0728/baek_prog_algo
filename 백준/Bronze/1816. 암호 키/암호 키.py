N = int(input())

for i in range(N):
  num = int(input())
  ans = 0
  for j in range(2,1000001,1):
    if num % j == 0:
      break
    elif j == 1000000:
      ans = 1
  if ans == 1:
    print("YES")
  else:
    print("NO")