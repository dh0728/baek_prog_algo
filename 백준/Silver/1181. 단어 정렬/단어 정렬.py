N=int(input())
arr_set=set(input() for _ in range(N))
arr=list(arr_set)
arr.sort() # 사전순으로 일단 정렬
# print(arr)
arr.sort(key=len) # 길이순으로 정렬
for a in arr:
    print(a)