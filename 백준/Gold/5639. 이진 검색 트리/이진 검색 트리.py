import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)


li = []

while True:
    try:
        li.append(int(sys.stdin.readline()))
    except:
        break 

def post_traversal(start, end):
    if start > end:
        return
    mid = end + 1
    for i in range(start + 1, end + 1):
        if li[i] > li[start]:
            mid = i
            break
    #print(f"p({start + 1}, {mid - 1}) - 왼쪽 start = {start}, end = {end}")
    post_traversal(start + 1, mid - 1) # 왼쪽 서브트리

    #print(f"p({mid}, {end}) - 오른쪽 start = {start}, end = {end}")
    post_traversal(mid, end)           # 오른쪽 서브트리
    print(li[start])                   # 루트(후위 순회 마지막)


def solution():
    post_traversal(0, len(li) - 1)



if __name__ == "__main__":
    solution()


