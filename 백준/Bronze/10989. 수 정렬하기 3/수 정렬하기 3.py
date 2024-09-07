N= int(input())

# 카운팅으로 풀어야 풀릴듯
cnt_arr=[0]*(10001)
for _ in range(N): #나오 숫자만큼 카운팅
    cnt_arr[int(input())]+=1
# print(cnt_arr)

for i, a in enumerate(cnt_arr):
    while a:
        print(i)
        a-=1