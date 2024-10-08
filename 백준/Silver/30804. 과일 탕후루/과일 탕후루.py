import sys
#sys.stdin=open('input.txt')
input = sys.stdin.readline
from collections import deque

def find_fruit_cnt(arr):
    fruit_cnt = {}
    left =0
    max_fruits= 0

    for right in range(len(arr)): # 딕셔너리에 종류와 개수 저장
        fruit = arr[right]
        if fruit in fruit_cnt: # 과일 종류와 개수 저장 딕셔너리에 과일이 있으면
            fruit_cnt[fruit] +=1
        else:
            fruit_cnt[fruit] = 1

        # 과일의 종류가 두개가 넘으면 left
        while len(fruit_cnt) > 2:
            left_fruit = arr[left]
            fruit_cnt[left_fruit] -=1
            if fruit_cnt[left_fruit] ==0:
                del fruit_cnt[left_fruit] # 개수가 0이된 과일은 딕셔너리에서 빼기
            left +=1
        max_fruits = max(max_fruits, right - left + 1)
    return max_fruits

N = int(input())
arr = list(map(int,input().strip().split()))

result = find_fruit_cnt(arr)
print(result)