import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

arr = list(input().strip())

stack = []
indices = []
res = set()

for i in range(len(arr)):
    if arr[i] == "(":
        stack.append(i)
    elif arr[i] == ")":
        indices.append((stack.pop(),i)) # 쌍을 이루는 괄호의 인덱스 찾아서 indices배열에 삽입

def solution():

    for i in range(1, (1 << len(indices))):
        comb = []
        temp = arr[:]
        for j in range(len(indices)):
            if i & (1 << j):
                comb.append(indices[j])

        for k in comb:
            temp[k[0]] = temp[k[1]] = "" # 괄호 없애기

        res.add("".join(temp))
    


    for item in sorted(list(res)):
        print(item)
    
    return

solution()

