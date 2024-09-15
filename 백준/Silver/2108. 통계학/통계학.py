import sys
# sys.stdin.readline() 쓰자

def arith_mean(): # 산술평균 구하는 함수
    return round(sum(arr) / N)

def cnt_arr(): # 최빈값 구하기
    max_cnt=max(num_dict.values()) # 최대 빈도수 찾기
    max_num=[] 
    for k,v in num_dict.items():
        if v == max_cnt: # 최대 빈도수인 숫자면
            max_num.append(k) # 리스트에 삽입
    if len(max_num)>1: # 여러개면 두번째 값 넣기
        return max_num[1]
    else:
        return max_num[0]



N=int(sys.stdin.readline())
num_dict={}
arr=[]
for _ in range(N):
    n=int(sys.stdin.readline())
    arr.append(n)

arr.sort()

for a in arr:
    if a in num_dict:
        num_dict[a]+=1
    else:
        num_dict[a] =1

mean=arith_mean()

print(mean) # 산술평균
print(arr[N//2]) # 중앙값
print(cnt_arr()) # 최빈값
print(arr[-1]-arr[0])
